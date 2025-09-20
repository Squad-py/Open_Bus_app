from flask import Flask, render_template, request, jsonify, redirect, url_for, flash



app = Flask(__name__)
app.secret_key = "super_secret_key"  # Cambia esto por algo más seguro

# Simulación de usuarios registrados (puedes cambiarlo por una base de datos)
usuarios = {
    "admin": "1234",
    "hiram": "pass123"
}

@app.route("/")
def index():
    return render_template("index.html")  # Renderiza el login

if __name__ == "__main__":
    app.run(debug=True)
