import express from "express";
import cors from "cors";
import fs from "fs";
import {
  createAuthenticatedClient,
  OpenPaymentsClientError,
  isFinalizedGrant,
} from "@interledger/open-payments";

const app = express();
app.use(cors());
app.use(express.json());

// Guardar temporalmente la info del pago para continuar
let pendingPayments = {};
let ultimoMontoTransferido = null; 
app.post("/start-payment", async (req, res) => {
  try {
    const { destinatario, monto, description } = req.body;
    if (!destinatario || !monto || !description)
      return res.status(400).json({ error: "Faltan parámetros" });
    let montoFinal = Number(monto) * 100;

    const normalizeUrl = (url) =>
      url.startsWith("$") ? `https://${url.slice(1)}` : url;

    const receivingWalletUrl = normalizeUrl(destinatario);

      const client = await createAuthenticatedClient({//wallet que siemrpe recibe
        walletAddressUrl: "https://ilp.interledger-test.dev/cmov",
        privateKey: fs.readFileSync("private.key", "utf8"),
        keyId: "b66b9b81-e448-46ba-8416-6705bc1017c5",
      });

      const sendingWalletAddress = await client.walletAddress.get({
        url:receivingWalletUrl,
      });

      const receivingWalletAddress = await client.walletAddress.get({
        url:    "https://ilp.interledger-test.dev/cmov",
      });
    // console.log(sendingWalletAddress);
    // console.log("------------------------------------------------------------------------------------");
    // console.log(receivingWalletAddress);

    // Step 1: grant incoming payment
    const incomingPaymentGrant = await client.grant.request(
      { url: receivingWalletAddress.authServer },
      { access_token: { access: [{ type: "incoming-payment", actions: ["read","complete","create"] }] } }
    );

    const incomingPayment = await client.incomingPayment.create(
      {
        url: receivingWalletAddress.resourceServer,
        accessToken: incomingPaymentGrant.access_token.value,
      },
      {
        walletAddress: receivingWalletAddress.id,
        incomingAmount: {
          assetCode: receivingWalletAddress.assetCode,
          assetScale: receivingWalletAddress.assetScale,
          value: montoFinal.toString(),
        },
      }
    );

      // Step 2: quote grant y quote
      const quoteGrant = await client.grant.request(
        { url: sendingWalletAddress.authServer },
        { access_token: { access: [{ type: "quote", actions: ["create", "read"] }] } }
      );

      const quote = await client.quote.create(
        {
          url: sendingWalletAddress.resourceServer,
          accessToken: quoteGrant.access_token.value,
        },
        {
          walletAddress: sendingWalletAddress.id,
          receiver: incomingPayment.id,
          method: "ilp",
        }
      );
      // Guardamos el monto final estimado
      ultimoMontoTransferido = quote.debitAmount.value;
    // Step 3: outgoing payment grant interactivo
    const outgoingPaymentGrant = await client.grant.request(
      { url: sendingWalletAddress.authServer },
      {
        access_token: {
          access: [
            {
              type: "outgoing-payment",
              actions: ["read","create"],
              limits: {
                debitAmount: {
                  assetCode: quote.debitAmount.assetCode,
                  assetScale: quote.debitAmount.assetScale,
                  value: quote.debitAmount.value,
                },
              },
              identifier: sendingWalletAddress.id,
            },
          ],
        },
        interact: { start: ["redirect"] },
      }
    );

    // Guardar info para continuar después
    pendingPayments[incomingPayment.id] = {
      client,
      sendingWalletAddress,
      outgoingPaymentGrant,
      quoteId: quote.id,
    };

    res.json({ url: outgoingPaymentGrant.interact.redirect, incomingPaymentId: incomingPayment.id });
  } catch (err) {
    console.error(err);
    if (err instanceof OpenPaymentsClientError)
      return res.status(500).json({ error: err.description || err.message });
    res.status(500).json({ error: err.message });
  }
});

// Endpoint para continuar después de aceptar el pago
app.post("/continue-payment", async (req, res) => {
  try {
    console.log("tu putisima madre")
    const { incomingPaymentId } = req.body;
    if (!incomingPaymentId || !pendingPayments[incomingPaymentId])
      return res.status(400).json({ error: "Pago no encontrado" });

    const { client, sendingWalletAddress, outgoingPaymentGrant, quoteId } = pendingPayments[incomingPaymentId];

    // Continuar grant
    const finalizedGrant = await client.grant.continue({
      url: outgoingPaymentGrant.continue.uri,
      accessToken: outgoingPaymentGrant.continue.access_token.value,
    });

    if (!isFinalizedGrant(finalizedGrant))
      return res.status(500).json({ error: "Grant no finalizado" });

    // Crear outgoing payment
    const outgoingPayment = await client.outgoingPayment.create(
      {
        url: sendingWalletAddress.resourceServer,
        accessToken: finalizedGrant.access_token.value,
      },
      { walletAddress: sendingWalletAddress.id, quoteId }
    );

    // Borrar de pending
    delete pendingPayments[incomingPaymentId];


await fetch("https://7z1qwqzz-4000.usw3.devtunnels.ms/card/recharge", {
    method: 'POST',
    headers: {
        'Content-Type': 'application/json'
    },
    body: JSON.stringify({cardId:"5232373", amount : ultimoMontoTransferido/100}),
});
    res.json({ success: true, outgoingPayment });
  } 
  catch (err) {
    console.error(err);
    res.status(500).json({ error: err.message });
  }


});

app.listen(3000, () => console.log("🚀 Server escuchando en http://localhost:3000"));
