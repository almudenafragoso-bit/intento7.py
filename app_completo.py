from flask import Flask, request, jsonify, render_template_string
import json
import os
from datetime import datetime

app = Flask(__name__)
ARCHIVO_DATOS = "reportes.json"

# Cargar datos
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

# HTML CSS INTEGRADO
CSS_ESTILOS = """
* {
    margin: 0;
    padding: 0;
    box-sizing: border-box;
}

body {
    font-family: 'Arial', sans-serif;
    background-color: #f0f4ff;
    color: #1f2937;
}

.container {
    max-width: 900px;
    margin: 0 auto;
    background-color: #ffffff;
    min-height: 100vh;
    display: flex;
    flex-direction: column;
}

.header {
    padding: 40px 20px;
    text-align: center;
    color: white;
}

.header h1 {
    font-size: 2em;
    margin-bottom: 10px;
}

.subtitle {
    font-style: italic;
    opacity: 0.9;
    font-size: 1.1em;
}

.main-content {
    flex: 1;
    padding: 30px 20px;
}

.section {
    margin-bottom: 30px;
}

.section-title {
    font-size: 1.3em;
    margin-bottom: 15px;
    font-weight: bold;
}

.separator {
    border: none;
    border-top: 2px solid #e5e7eb;
    margin: 25px 0;
}

.button-group {
    display: flex;
    flex-direction: column;
    gap: 10px;
    margin-bottom: 15px;
}

.btn {
    padding: 12px 20px;
    border: none;
    border-radius: 8px;
    color: white;
    font-weight: bold;
    font-size: 1em;
    cursor: pointer;
    text-decoration: none;
    display: block;
    text-align: center;
    transition: all 0.3s ease;
}

.btn:hover {
    transform: translateY(-2px);
    box-shadow: 0 5px 15px rgba(0, 0, 0, 0.2);
}

.btn-exit {
    width: 100%;
    padding: 12px;
    background-color: #ef4444;
    color: white;
    border: none;
    border-radius: 8px;
    font-weight: bold;
    cursor: pointer;
    transition: all 0.3s ease;
}

.btn-exit:hover {
    background-color: #dc2626;
}

.form {
    max-width: 600px;
    margin: 0 auto;
}

.form-group {
    margin-bottom: 20px;
}

.form-group label {
    display: block;
    font-weight: bold;
    margin-bottom: 8px;
    color: #6366f1;
}

.form-control {
    width: 100%;
    padding: 10px;
    border: 2px solid #e5e7eb;
    border-radius: 8px;
    font-family: 'Arial', sans-serif;
    font-size: 1em;
    transition: border-color 0.3s ease;
}

.form-control:focus {
    outline: none;
    border-color: #6366f1;
}

textarea.form-control {
    resize: vertical;
    font-family: 'Arial', sans-serif;
}

.recommendations-box {
    background-color: #f8fafc;
    padding: 20px;
    border-radius: 8px;
    margin: 20px 0;
    border-left: 4px solid #ec4899;
}

.recommendations-box h3 {
    color: #ec4899;
    margin-bottom: 15px;
    font-size: 1.3em;
}

.recomendaciones-list {
    list-style: none;
    margin-left: 0;
}

.recomendaciones-list li {
    padding: 10px 0;
    color: #059669;
    font-weight: 500;
}

.reflexion-box {
    background-color: #fef3c7;
    padding: 30px;
    border-radius: 8px;
    margin: 20px 0;
    border: 2px solid #f59e0b;
}

.reflexion-box h2 {
    color: #f59e0b;
    text-align: center;
    font-size: 0.9em;
    margin: 10px 0;
}

.reflexion-box h3 {
    color: #f59e0b;
    margin-top: 25px;
    margin-bottom: 15px;
}

.reflexion-list {
    margin-left: 20px;
    padding: 15px;
    background-color: white;
    border-radius: 8px;
}

.reflexion-list li {
    margin-bottom: 15px;
    line-height: 1.6;
}

.acciones-list {
    list-style: none;
    margin-left: 0;
    background-color: white;
    padding: 15px;
    border-radius: 8px;
}

.acciones-list li {
    padding: 10px 0;
    font-weight: 500;
}

.reporte-card {
    background-color: #f8fafc;
    border: 1px solid #e5e7eb;
    border-radius: 8px;
    padding: 20px;
    margin-bottom: 20px;
    border-left: 4px solid #6366f1;
}

.reporte-header {
    background-color: #6366f1;
    color: white;
    padding: 10px 15px;
    border-radius: 4px;
    margin-bottom: 15px;
    font-weight: bold;
}

.reporte-body p {
    margin-bottom: 10px;
    line-height: 1.6;
}

.reporte-empty {
    background-color: #f8fafc;
    border: 2px dashed #e5e7eb;
    border-radius: 8px;
    padding: 40px;
    text-align: center;
    color: #6b7280;
}

.reporte-empty h3 {
    color: #6366f1;
    margin-bottom: 10px;
}

.result-box {
    margin: 20px 0;
    min-height: 100px;
}

.reportes-container {
    margin: 20px 0;
}

.footer {
    padding: 20px;
    border-top: 1px solid #e5e7eb;
    background-color: #f8fafc;
}

@media (max-width: 768px) {
    .container {
        margin: 0;
        border-radius: 0;
    }

    .header h1 {
        font-size: 1.5em;
    }

    .main-content {
        padding: 20px;
    }

    .btn {
        font-size: 0.95em;
        padding: 10px 15px;
    }

    .reflexion-box {
        padding: 20px;
    }
}
"""

# PLANTILLA HTML PRINCIPAL
HTML_PRINCIPAL = """
<!DOCTYPE html>
<html lang="es">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Sistema de Prevención del Bullying</title>
    <style>{{ css_estilos }}</style>
</head>
<body>
    <div class="container">
        <header class="header" style="background: linear-gradient(135deg, #6366f1 0%, #ec4899 100%);">
            <h1>🛡️ Sistema de Prevención del Bullying 🛡️</h1>
            <p class="subtitle">Un espacio seguro para víctimas y agresores</p>
        </header>

        <main class="main-content">
            <section class="section">
                <h2 class="section-title" style="color: #ec4899;">👥 PARA VÍCTIMAS</h2>
                <div class="button-group">
                    <a href="/recomendaciones" class="btn" style="background-color: #ec4899;">
                        📋 Recomendaciones de Autoprotección
                    </a>
                    <a href="/registro" class="btn" style="background-color: #ec4899;">
                        📝 Registrar tu Reporte
                    </a>
                    <a href="/buscar" class="btn" style="background-color: #ec4899;">
                        🔍 Ver tu Reporte
                    </a>
                </div>
            </section>

            <hr class="separator">

            <section class="section">
                <h2 class="section-title" style="color: #f59e0b;">💭 PARA AGRESORES</h2>
                <div class="button-group">
                    <a href="/agresor" class="btn" style="background-color: #f59e0b;">
                        🤝 Espacio de Reflexión y Cambio
                    </a>
                </div>
            </section>

            <hr class="separator">

            <section class="section">
                <h2 class="section-title" style="color: #10b981;">📊 INFORMACIÓN GENERAL</h2>
                <div class="button-group">
                    <a href="/reportes" class="btn" style="background-color: #10b981;">
                        📊 Ver Todos los Reportes
                    </a>
                </div>
            </section>
        </main>

        <footer class="footer">
            <button onclick="window.close()" class="btn-exit">❌ Salir de la Aplicación</button>
        </footer>
    </div>
</body>
</html>
"""

# PLANTILLA RECOMENDACIONES
HTML_RECOMENDACIONES = """
<!DOCTYPE html>
<html lang="es">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Recomendaciones para Víctimas</title>
    <style>{{ css_estilos }}</style>
</head>
<body>
    <div class="container">
        <header class="header" style="background-color: #ec4899;">
            <h1>📋 Recomendaciones de Autoprotección</h1>
            <p class="subtitle">Selecciona el tipo de bullying para obtener consejos específicos</p>
        </header>

        <main class="main-content">
            <div class="form-group">
                <label for="tipo-bullying">Tipo de bullying:</label>
                <select id="tipo-bullying" onchange="actualizarRecomendaciones()" class="form-control">
                    <option value="fisico">🥊 Físico</option>
                    <option value="verbal">💬 Verbal</option>
                    <option value="psicologico">🧠 Psicológico</option>
                    <option value="social">🚫 Social</option>
                    <option value="ciberbullying">📱 Ciberbullying</option>
                    <option value="sexual">⚠️ Sexual</option>
                </select>
            </div>

            <div id="recomendaciones" class="recommendations-box"></div>

            <div class="button-group">
                <a href="/" class="btn" style="background-color: #6366f1;">
                    ← Volver al Inicio
                </a>
            </div>
        </main>
    </div>

    <script>
        const recomendaciones = {
            fisico: [
                "✓ Reporta las agresiones a un adulto de confianza.",
                "✓ Guarda evidencias (fotos, videos).",
                "✓ Busca apoyo médico si es necesario.",
                "✓ Acompáñate de otros estudiantes.",
                "✓ No estés solo en espacios vulnerables."
            ],
            verbal: [
                "✓ No respondas insultando.",
                "✓ Habla con alguien de confianza.",
                "✓ Documenta las palabras hirientes.",
                "✓ Usa frases como 'Eso no me afecta'.",
                "✓ Busca refugio en amigos solidarios."
            ],
            psicologico: [
                "✓ Busca apoyo emocional inmediato.",
                "✓ Acude a orientación escolar.",
                "✓ Practica técnicas de relajación.",
                "✓ Confía en alguien de confianza.",
                "✓ Recuerda que no es tu culpa."
            ],
            social: [
                "✓ Acércate a personas de confianza.",
                "✓ Participa en actividades grupales.",
                "✓ No aisles a otros que sufren lo mismo.",
                "✓ Busca nuevos amigos con tus intereses.",
                "✓ Participa en clubs o grupos escolares."
            ],
            ciberbullying: [
                "✓ Bloquea a los agresores inmediatamente.",
                "✓ Guarda capturas de pantalla.",
                "✓ No contestes mensajes negativos.",
                "✓ Reporta el contenido a la plataforma.",
                "✓ Privacidad: revisa tus configuraciones."
            ],
            sexual: [
                "✓ Denuncia inmediatamente.",
                "✓ Busca ayuda de un adulto de confianza.",
                "✓ Acude a las autoridades escolares.",
                "✓ Busca apoyo psicológico profesional.",
                "✓ Conoce tus derechos sobre tu cuerpo."
            ]
        };

        function actualizarRecomendaciones() {
            const tipo = document.getElementById('tipo-bullying').value;
            const recomendacionesDiv = document.getElementById('recomendaciones');
            const iconos = { fisico: '🥊', verbal: '💬', psicologico: '🧠', social: '🚫', ciberbullying: '📱', sexual: '⚠️' };
            const nombres = { fisico: 'Físico', verbal: 'Verbal', psicologico: 'Psicológico', social: 'Social', ciberbullying: 'Ciberbullying', sexual: 'Sexual' };

            let html = `<h3>${iconos[tipo]} ${nombres[tipo]}</h3>`;
            html += '<ul class="recomendaciones-list">';
            recomendaciones[tipo].forEach(rec => {
                html += `<li>${rec}</li>`;
            });
            html += '</ul>';

            recomendacionesDiv.innerHTML = html;
        }

        actualizarRecomendaciones();
    </script>
</body>
</html>
"""

# PLANTILLA REGISTRO
HTML_REGISTRO = """
<!DOCTYPE html>
<html lang="es">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Registrar Reporte</title>
    <style>{{ css_estilos }}</style>
</head>
<body>
    <div class="container">
        <header class="header" style="background-color: #6366f1;">
            <h1>📝 Nuevo Reporte de Bullying</h1>
            <p class="subtitle">Tu reporte es confidencial e importante</p>
        </header>

        <main class="main-content">
            <form id="formulario-reporte" class="form" onsubmit="guardarReporte(event)">
                <div class="form-group">
                    <label for="nombre">Nombre completo:</label>
                    <input type="text" id="nombre" name="nombre" class="form-control" required>
                </div>

                <div class="form-group">
                    <label for="tipo">Tipo de bullying:</label>
                    <select id="tipo" name="tipo" class="form-control" required>
                        <option value="">-- Selecciona --</option>
                        <option value="🥊 Físico">🥊 Físico</option>
                        <option value="💬 Verbal">💬 Verbal</option>
                        <option value="🧠 Psicológico">🧠 Psicológico</option>
                        <option value="🚫 Social">🚫 Social</option>
                        <option value="📱 Ciberbullying">📱 Ciberbullying</option>
                        <option value="⚠️ Sexual">⚠️ Sexual</option>
                        <option value="🔸 Otros">🔸 Otros</option>
                    </select>
                </div>

                <div class="form-group">
                    <label for="lugar">Lugar del incidente:</label>
                    <input type="text" id="lugar" name="lugar" class="form-control">
                </div>

                <div class="form-group">
                    <label for="fecha">Fecha (DD/MM/YYYY):</label>
                    <input type="text" id="fecha" name="fecha" class="form-control" placeholder="DD/MM/YYYY">
                </div>

                <div class="form-group">
                    <label for="descripcion">Descripción detallada:</label>
                    <textarea id="descripcion" name="descripcion" class="form-control" rows="8" required></textarea>
                </div>

                <div class="button-group">
                    <button type="submit" class="btn" style="background-color: #10b981;">
                        💾 Guardar Reporte
                    </button>
                    <a href="/" class="btn" style="background-color: #6366f1;">
                        ← Volver al Inicio
                    </a>
                </div>
            </form>
        </main>
    </div>

    <script>
        document.addEventListener('DOMContentLoaded', function() {
            const fecha = new Date();
            const dia = String(fecha.getDate()).padStart(2, '0');
            const mes = String(fecha.getMonth() + 1).padStart(2, '0');
            const anio = fecha.getFullYear();
            document.getElementById('fecha').value = `${dia}/${mes}/${anio}`;
        });

        async function guardarReporte(event) {
            event.preventDefault();

            const nombre = document.getElementById('nombre').value;
            const tipo = document.getElementById('tipo').value;
            const lugar = document.getElementById('lugar').value;
            const fecha = document.getElementById('fecha').value;
            const descripcion = document.getElementById('descripcion').value;

            if (!nombre || !tipo || !descripcion) {
                alert('Por favor completa todos los campos requeridos');
                return;
            }

            try {
                const response = await fetch('/api/reportes', {
                    method: 'POST',
                    headers: {
                        'Content-Type': 'application/json'
                    },
                    body: JSON.stringify({
                        nombre: nombre,
                        tipo: tipo,
                        lugar: lugar,
                        fecha: fecha,
                        descripcion: descripcion
                    })
                });

                if (response.ok) {
                    const data = await response.json();
                    alert(`✅ Éxito\\n\\nReporte registrado exitosamente.\\n\\nCódigo: ${data.codigo}\\n\\nGuarda este código para consultar tu reporte.`);
                    document.getElementById('formulario-reporte').reset();
                    window.location.href = '/';
                } else {
                    alert('Error al registrar el reporte');
                }
            } catch (error) {
                console.error('Error:', error);
                alert('Error en la conexión');
            }
        }
    </script>
</body>
</html>
"""

# PLANTILLA BUSCAR
HTML_BUSCAR = """
<!DOCTYPE html>
<html lang="es">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Buscar Reporte</title>
    <style>{{ css_estilos }}</style>
</head>
<body>
    <div class="container">
        <header class="header" style="background-color: #8b5cf6;">
            <h1>🔍 Buscar tu Reporte</h1>
            <p class="subtitle">Ingresa el código de tu reporte para recuperarlo</p>
        </header>

        <main class="main-content">
            <div class="form-group">
                <label for="codigo-reporte">Código del reporte (ej. R0001):</label>
                <input type="text" id="codigo-reporte" class="form-control" placeholder="R0001" onkeypress="if(event.key==='Enter') buscarReporte()">
            </div>

            <div class="button-group">
                <button onclick="buscarReporte()" class="btn" style="background-color: #8b5cf6;">
                    🔍 Buscar Reporte
                </button>
            </div>

            <div id="resultado" class="result-box"></div>

            <div class="button-group">
                <a href="/" class="btn" style="background-color: #6366f1;">
                    ← Volver al Inicio
                </a>
            </div>
        </main>
    </div>

    <script>
        async function buscarReporte() {
            const codigo = document.getElementById('codigo-reporte').value.trim().toUpperCase();
            const resultadoDiv = document.getElementById('resultado');

            if (!codigo) {
                resultadoDiv.innerHTML = '<p style="color: #ef4444;">Por favor ingresa un código</p>';
                return;
            }

            try {
                const response = await fetch(`/api/reportes/${codigo}`);
                const data = await response.json();

                if (response.ok) {
                    let html = `
                    <div class="reporte-card">
                        <h3>📋 REPORTE ENCONTRADO</h3>
                        <p><strong>Código:</strong> ${data.codigo}</p>
                        <p><strong>Nombre:</strong> ${data.nombre}</p>
                        <p><strong>Tipo:</strong> ${data.tipo}</p>
                        <p><strong>Lugar:</strong> ${data.lugar}</p>
                        <p><strong>Fecha:</strong> ${data.fecha}</p>
                        <hr>
                        <h4>Descripción:</h4>
                        <p>${data.descripcion.replace(/\\n/g, '<br>')}</p>
                        <hr>
                        <p><strong>Estado:</strong> ✅ Registrado</p>
                        <p><strong>Acceso:</strong> Confidencial</p>
                    </div>
                    `;
                    resultadoDiv.innerHTML = html;
                } else {
                    resultadoDiv.innerHTML = '<p style="color: #ef4444;">❌ Reporte no encontrado. Verifica que el código sea correcto (ej. R0001)</p>';
                }
            } catch (error) {
                console.error('Error:', error);
                resultadoDiv.innerHTML = '<p style="color: #ef4444;">Error en la conexión</p>';
            }
        }
    </script>
</body>
</html>
"""

# PLANTILLA AGRESOR
HTML_AGRESOR = """
<!DOCTYPE html>
<html lang="es">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Reflexión y Cambio</title>
    <style>{{ css_estilos }}</style>
</head>
<body>
    <div class="container">
        <header class="header" style="background-color: #f59e0b;">
            <h1>💭 Espacio de Reflexión y Cambio</h1>
            <p class="subtitle">El primer paso es reconocer el problema</p>
        </header>

        <main class="main-content">
            <div class="reflexion-box">
                <h2>━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━</h2>
                <h2 style="text-align: center;">REFLEXIÓN IMPORTANTE</h2>
                <h2>━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━</h2>

                <p style="text-align: center; font-size: 1.1em; margin: 20px 0;">
                    Si estás aquí es porque reconoces que has cometido bullying.<br>
                    <strong>ESE ES EL PRIMER PASO IMPORTANTE HACIA EL CAMBIO.</strong>
                </p>

                <h3 style="margin-top: 30px;">❓ PREGUNTAS PARA LA REFLEXIÓN</h3>
                <ol class="reflexion-list">
                    <li>
                        <strong>¿Cómo crees que se siente la otra persona?</strong><br>
                        → Imagina el dolor que causaste
                    </li>
                    <li>
                        <strong>¿Qué te llevó a actuar de esa manera?</strong><br>
                        → Busca la raíz del problema (ira, inseguridad, presión)
                    </li>
                    <li>
                        <strong>¿Cómo te sentirías si fueras tú la víctima?</strong><br>
                        → Practica la empatía
                    </li>
                    <li>
                        <strong>¿Qué puedes hacer para cambiar?</strong><br>
                        → Planifica acciones concretas
                    </li>
                </ol>

                <h3 style="margin-top: 30px;">✅ ACCIONES PARA CAMBIAR</h3>
                <ul class="acciones-list">
                    <li>✓ Ofrece una disculpa sincera y meaningful</li>
                    <li>✓ Busca ayuda de un adulto o counselor</li>
                    <li>✓ Participa en talleres de empatía</li>
                    <li>✓ Mantén distancia del comportamiento negativo</li>
                    <li>✓ Apoya a las víctimas en lugar de atacarlas</li>
                    <li>✓ Trabaja en tu autoestima de forma saludable</li>
                    <li>✓ Busca actividades que canalicen tu energía</li>
                </ul>

                <div style="text-align: center; margin: 30px 0; padding: 20px; background-color: #fef3c7; border-radius: 10px;">
                    <p style="font-size: 1.1em; font-weight: bold;">
                        Recuerda: SIEMPRE ES TIEMPO PARA CAMBIAR Y SER MEJOR PERSONA.
                    </p>
                    <p style="font-size: 1.1em; margin-top: 10px;">
                        La gente puede cambiar. <strong>TÚ PUEDES CAMBIAR.</strong>
                    </p>
                </div>
            </div>

            <div class="button-group">
                <a href="/" class="btn" style="background-color: #10b981;">
                    ✅ Entiendo, buscaré ayuda
                </a>
            </div>
        </main>
    </div>
</body>
</html>
"""

# PLANTILLA REPORTES
HTML_REPORTES = """
<!DOCTYPE html>
<html lang="es">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Ver Reportes</title>
    <style>{{ css_estilos }}</style>
</head>
<body>
    <div class="container">
        <header class="header" style="background-color: #10b981;">
            <h1>📊 Todos los Reportes Registrados</h1>
            <p class="subtitle" id="total-reportes">Total de reportes: 0</p>
        </header>

        <main class="main-content">
            <div id="reportes-container" class="reportes-container"></div>

            <div class="button-group">
                <a href="/" class="btn" style="background-color: #6366f1;">
                    ← Volver al Inicio
                </a>
            </div>
        </main>
    </div>

    <script>
        async function cargarReportes() {
            try {
                const response = await fetch('/api/reportes');
                const reportes = await response.json();

                const contenedor = document.getElementById('reportes-container');
                const totalReportes = document.getElementById('total-reportes');

                if (Object.keys(reportes).length === 0) {
                    contenedor.innerHTML = `
                    <div class="reporte-empty">
                        <h3>📋 SIN REPORTES REGISTRADOS</h3>
                        <p>Sé el primero en registrar un reporte. Tu voz importa y puede ayudar a otros.</p>
                    </div>
                    `;
                    totalReportes.textContent = 'Total de reportes: 0';
                } else {
                    totalReportes.textContent = `Total de reportes: ${Object.keys(reportes).length}`;

                    let html = '';
                    for (const [codigo, reporte] of Object.entries(reportes)) {
                        const descripcionCorta = reporte.descripcion.substring(0, 80).replace(/\\n/g, ' ') + (reporte.descripcion.length > 80 ? '...' : '');

                        html += `
                        <div class="reporte-card">
                            <div class="reporte-header">
                                <strong>Código:</strong> ${reporte.codigo}
                            </div>
                            <div class="reporte-body">
                                <p><strong>Nombre:</strong> ${reporte.nombre}</p>
                                <p><strong>Tipo:</strong> ${reporte.tipo}</p>
                                <p><strong>Lugar:</strong> ${reporte.lugar}</p>
                                <p><strong>Fecha:</strong> ${reporte.fecha}</p>
                                <p><strong>Descripción:</strong> ${descripcionCorta}</p>
                            </div>
                        </div>
                        `;
                    }
                    contenedor.innerHTML = html;
                }
            } catch (error) {
                console.error('Error:', error);
                document.getElementById('reportes-container').innerHTML = '<p style="color: #ef4444;">Error al cargar los reportes</p>';
            }
        }

        document.addEventListener('DOMContentLoaded', cargarReportes);
    </script>
</body>
</html>
"""

# RUTAS
@app.route('/')
def index():
    return render_template_string(HTML_PRINCIPAL, css_estilos=CSS_ESTILOS)

@app.route('/recomendaciones')
def recomendaciones():
    return render_template_string(HTML_RECOMENDACIONES, css_estilos=CSS_ESTILOS)

@app.route('/registro')
def registro():
    return render_template_string(HTML_REGISTRO, css_estilos=CSS_ESTILOS)

@app.route('/buscar')
def buscar():
    return render_template_string(HTML_BUSCAR, css_estilos=CSS_ESTILOS)

@app.route('/agresor')
def agresor():
    return render_template_string(HTML_AGRESOR, css_estilos=CSS_ESTILOS)

@app.route('/reportes')
def ver_reportes():
    return render_template_string(HTML_REPORTES, css_estilos=CSS_ESTILOS)

# API REST
@app.route('/api/reportes', methods=['GET'])
def api_get_reportes():
    reportes = cargar_datos()
    return jsonify(reportes)

@app.route('/api/reportes/<codigo>', methods=['GET'])
def api_get_reporte(codigo):
    reportes = cargar_datos()
    if codigo.upper() in reportes:
        return jsonify(reportes[codigo.upper()])
    return jsonify({'error': 'Reporte no encontrado'}), 404

@app.route('/api/reportes', methods=['POST'])
def api_crear_reporte():
    data = request.get_json()
    
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
