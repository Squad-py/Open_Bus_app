from flask import Flask, render_template, request, jsonify, redirect, url_for, flash
from werkzeug.utils import secure_filename
import requests
import json
import os
import pymysql
import base64

# Configuración para la carpeta de subida
UPLOAD_FOLDER = 'static/uploads'
ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg', 'gif'}


app = Flask(__name__)
app.secret_key = "super_secret_key"  # Cambia esto por algo más seguro

@app.route("/")
def index():
    return render_template("index.html")   

@app.route('/house')
def home():
    return render_template('house.html')

if __name__ == "__main__":
    app.run(debug=True)
