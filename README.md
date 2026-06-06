# Sistema de Prevención del Bullying

## Descripción
Aplicación web en Flask para la prevención del bullying. Proporciona un espacio seguro para víctimas y agresores, con recomendaciones, registro de reportes y un área de reflexión.

## Requisitos
- Python 3.7+
- Flask 2.3.0

## Instalación

1. Clonar el repositorio:
```bash
git clone https://github.com/almudenafragoso-bit/intento7.py.git
cd intento7.py
```

2. Instalar dependencias:
```bash
pip install -r requirements.txt
```

## Ejecución

```bash
python app.py
```

Luego accede a `http://localhost:5000` en tu navegador.

## Estructura del Proyecto

```
intento7.py/
├── app.py                 # Aplicación principal Flask
├── requirements.txt       # Dependencias del proyecto
├── reportes.json          # Base de datos de reportes
├── templates/             # Plantillas HTML
│   ├── index.html         # Página principal
│   ├── recomendaciones.html
│   ├── registro.html
│   ├── buscar.html
│   ├── agresor.html
│   └── reportes.html
└── static/                # Archivos estáticos
    └── style.css          # Estilos CSS
```

## Funcionalidades

### Para Víctimas
- **Recomendaciones**: Consejos específicos según el tipo de bullying
- **Registrar Reporte**: Formulario para registrar un incidente
- **Buscar Reporte**: Recuperar un reporte anterior usando su código

### Para Agresores
- **Espacio de Reflexión**: Preguntas y acciones para cambiar

### General
- **Ver Reportes**: Listado de todos los reportes registrados

## API Endpoints

- `GET /api/reportes` - Obtener todos los reportes
- `GET /api/reportes/<codigo>` - Obtener un reporte específico
- `POST /api/reportes` - Crear un nuevo reporte

## Datos

Los reportes se guardan en formato JSON en `reportes.json`.

## Autor
Almudena Fragoso

## Licencia
MIT
