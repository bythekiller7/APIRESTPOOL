import os
from flask import Flask, send_from_directory, render_template, redirect
from app import app as producto_app  # Importando la app de app.py
from flask import Blueprint

port = int(os.environ.get("PORT", 5000))

productos_blueprint = Blueprint('productos', __name__, url_prefix='/productos')  # Blueprint para la app de app.py

# Registrando el Blueprint en la app de app.py, NO en una nueva app
producto_app.register_blueprint(productos_blueprint)

@app.route('/static/<path:path>')
def serve_static(path):
    return send_from_directory('static', path)

@app.route('/')
def home():
   return render_template('index.html')

if __name__ == "__main__":
    producto_app.run(port=port)  # Ejecutando la app de app.py