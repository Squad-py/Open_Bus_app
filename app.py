from flask import Flask, render_template, request, jsonify, redirect, url_for, flash
from werkzeug.utils import secure_filename
import requests
import json
import os
import base64

# Configuración para la carpeta de subida
UPLOAD_FOLDER = 'static/uploads'
ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg', 'gif'}
JSON_FILE = "reportes.json"

# Configuración de Flask
app = Flask(__name__, static_folder='static')
app.secret_key = 'Pitulillo$1'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER


# ------------------- FUNCIONES JSON -------------------

# Leer reportes
def get_reports():
    if os.path.exists(JSON_FILE):
        with open(JSON_FILE, "r", encoding="utf-8") as f:
            return json.load(f)
    return []

# Guardar todos los reportes
def save_reports(data):
    with open(JSON_FILE, "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=4)

# Insertar un reporte (con imagen en base64)
def save_report(bus_id, description, category, image_path=None):
    data = get_reports()
    new_id = (max([r["id"] for r in data], default=0) + 1)  # autoincrement

    image_base64 = None
    if image_path:
        with open(image_path, "rb") as img_file:
            image_base64 = base64.b64encode(img_file.read()).decode("utf-8")

    new_report = {
        "id": new_id,
        "bus_id": bus_id,
        "description": description,
        "category": category,
        "image_base64": image_base64
    }

    data.append(new_report)
    save_reports(data)
    print("✅ Reporte guardado en JSON.")

# Inserta un reporte (solo nombre de archivo de imagen, para subir desde /upload)
def insert_report(bus_id, description, category, image_filename=None):
    data = get_reports()
    new_id = (max([r["id"] for r in data], default=0) + 1)

    new_report = {
        "id": new_id,
        "bus_id": bus_id,
        "description": description,
        "category": category,
        "image": image_filename,  # aquí guardamos la ruta del archivo
        "image_base64": None
    }

    data.append(new_report)
    save_reports(data)

# Verifica si la extensión del archivo es válida
def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

# ------------------- RUTAS -------------------

@app.route('/')
def index():# es es el inicio atte ; diana estuvo aqui 
    return render_template('index.html')

@app.route('/<ruta_id>/gif')
def gif(ruta_id):
    url = "https://raw.githubusercontent.com/Yael200206/YOVOY/main/Rutas.json"
    response = requests.get(url)
    rutas_data = response.json() if response.status_code == 200 else {"routes": []}

    ruta_seleccionada = next((ruta for ruta in rutas_data["routes"] if ruta["id"] == ruta_id), None)
    if ruta_seleccionada is None:
        return "Ruta no encontrada", 404

    nombre_ruta = ruta_seleccionada["name"]
    partes = nombre_ruta.split(" - ", 1)
    origen = partes[0].split(" ", 1)[1] if len(partes) > 1 else "Desconocido"
    destino = partes[1] if len(partes) > 1 else "Desconocido"

    ruta_seleccionada["origen"] = origen
    ruta_seleccionada["destino"] = destino

    return render_template('gif.html', ruta=ruta_seleccionada)

@app.route('/house')
def home():
    return render_template('house.html')

@app.route('/rutas')
def rutas():
    url = "https://raw.githubusercontent.com/Yael200206/YOVOY/main/Rutas.json"
    response = requests.get(url)
    rutas_data = response.json() if response.status_code == 200 else {}
    return render_template('rutas.html', rutas=rutas_data)

@app.route('/reportes')
def reportes():
    reports = get_reports()
    return render_template('reportes.html', reports=reports)

@app.route('/upload', methods=['GET', 'POST'])
def upload_report():
    if request.method == 'POST':
        bus_id = request.form['bus_id']
        description = request.form['description']
        category = request.form['category']
        image_filename = None

        if 'image' in request.files:
            file = request.files['image']
            if file and file.filename != '' and allowed_file(file.filename):
                filename = secure_filename(file.filename)
                filepath = os.path.join(app.config['UPLOAD_FOLDER'], filename)
                file.save(filepath)
                image_filename = f"uploads/{filename}"
            elif file.filename != '':
                flash('Formato de archivo no permitido', 'error')
                return redirect(url_for('upload_report'))

        insert_report(bus_id, description, category, image_filename)
        flash('Reporte subido exitosamente', 'success')
        return redirect(url_for('reportes'))

    return render_template('reportes.html')

@app.route('/config')# config me manda a la configuracion del usuario 
def config():
    return render_template('config.html')

@app.route('/recargas')
def puntos_recarga():
    url = 'https://raw.githubusercontent.com/Yael200206/YOVOY/main/app/static/puntosRecarga.json'
    try:
        response = requests.get(url)
        data = response.json() if response.status_code == 200 else {}
    except requests.exceptions.RequestException as e:
        return jsonify({"error": f"Error en la solicitud: {str(e)}"}), 500
    return render_template('recargas.html', puntos=data)

@app.route('/api/puntos_recarga')
def api_puntos_recarga():
    url = 'https://raw.githubusercontent.com/Yael200206/YOVOY/main/app/static/puntosRecarga.json'
    try:
        response = requests.get(url)
        data = response.json() if response.status_code == 200 else {}
    except requests.exceptions.RequestException as e:
        return jsonify({"error": f"Error en la solicitud: {str(e)}"}), 500
    return jsonify(data)

@app.route('/buscar_rutas', methods=['GET'])
def buscar_rutas():
    destination = request.args.get('destination')
    if destination:
        origin = "José Ventura López 222"
        return render_template('buscarRutas.html', destination=destination, origin=origin)
    return "No se especificó un destino", 400


# ------------------- MAIN -------------------
if __name__ == '__main__':
    app.run(debug=True)
