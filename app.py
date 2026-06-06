from flask import Flask, render_template, request, jsonify
import json
import os
from datetime import datetime

app = Flask(__name__)
ARCHIVO_DATOS = "reportes.json"

def cargar_datos():
    """Carga los reportes desde el archivo JSON"""
    if os.path.exists(ARCHIVO_DATOS):
        with open(ARCHIVO_DATOS, 'r', encoding='utf-8') as f:
            return json.load(f)
    return {}

def guardar_datos(reportes):
    """Guarda los reportes en el archivo JSON"""
    with open(ARCHIVO_DATOS, 'w', encoding='utf-8') as f:
        json.dump(reportes, f, ensure_ascii=False, indent=2)

@app.route('/')
def index():
    """Página principal"""
    return render_template('index.html')

@app.route('/recomendaciones')
def recomendaciones():
    """Página de recomendaciones para víctimas"""
    return render_template('recomendaciones.html')

@app.route('/registro')
def registro():
    """Página de registro de reportes"""
    return render_template('registro.html')

@app.route('/buscar')
def buscar():
    """Página de búsqueda de reportes"""
    return render_template('buscar.html')

@app.route('/agresor')
def agresor():
    """Página de reflexión para agresores"""
    return render_template('agresor.html')

@app.route('/reportes')
def ver_reportes():
    """Página con todos los reportes"""
    return render_template('reportes.html')

@app.route('/api/reportes', methods=['GET'])
def api_get_reportes():
    """API para obtener todos los reportes"""
    reportes = cargar_datos()
    return jsonify(reportes)

@app.route('/api/reportes/<codigo>', methods=['GET'])
def api_get_reporte(codigo):
    """API para obtener un reporte específico"""
    reportes = cargar_datos()
    if codigo.upper() in reportes:
        return jsonify(reportes[codigo.upper()])
    return jsonify({'error': 'Reporte no encontrado'}), 404

@app.route('/api/reportes', methods=['POST'])
def api_crear_reporte():
    """API para crear un nuevo reporte"""
    data = request.get_json()
    
    # Validación
    campos_requeridos = ['nombre', 'tipo', 'descripcion']
    if not all(campo in data for campo in campos_requeridos):
        return jsonify({'error': 'Faltan campos requeridos'}), 400
    
    reportes = cargar_datos()
    codigo = f"R{len(reportes) + 1:04d}"
    
    reportes[codigo] = {
        'codigo': codigo,
        'nombre': data.get('nombre', ''),
        'tipo': data.get('tipo', ''),
        'lugar': data.get('lugar', ''),
        'fecha': data.get('fecha', datetime.now().strftime("%d/%m/%Y")),
        'descripcion': data.get('descripcion', '')
    }
    
    guardar_datos(reportes)
    return jsonify({'codigo': codigo, 'mensaje': 'Reporte registrado exitosamente'}), 201

if __name__ == '__main__':
    app.run(debug=True)
