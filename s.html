from flask import Flask, render_template, request, redirect
import json
import os

app = Flask(_name_)

ARCHIVO = "reportes.json"

if not os.path.exists(ARCHIVO):
    with open(ARCHIVO, "w") as f:
        json.dump([], f)


@app.route("/")
def inicio():
    return render_template("index.html")


@app.route("/guardar", methods=["POST"])
def guardar():
    nombre = request.form["nombre"]
    tipo = request.form["tipo"]
    lugar = request.form["lugar"]
    descripcion = request.form["descripcion"]

    with open(ARCHIVO, "r") as f:
        reportes = json.load(f)

    codigo = f"R{len(reportes)+1}"

    reporte = {
        "codigo": codigo,
        "nombre": nombre,
        "tipo": tipo,
        "lugar": lugar,
        "descripcion": descripcion
    }

    reportes.append(reporte)

    with open(ARCHIVO, "w") as f:
        json.dump(reportes, f, indent=4)

    return render_template("guardar.html", reporte=reporte)


@app.route("/buscar", methods=["POST"])
def buscar():
    codigo = request.form["codigo"]

    with open(ARCHIVO, "r") as f:
        reportes = json.load(f)

    encontrado = None

    for r in reportes:
        if r["codigo"] == codigo:
            encontrado = r
            break

    return render_template("buscar.html", reporte=encontrado)


@app.route("/historial")
def historial():
    with open(ARCHIVO, "r") as f:
        reportes = json.load(f)

    return render_template("historial.html", reportes=reportes)


if _name_ == "_main_":
    app.run(debug=True)<!DOCTYPE html>
<html lang="es">
<head>
<meta charset="UTF-8">
<title>Prevención del Bullying</title>
<link rel="stylesheet" href="{{ url_for('static', filename='estilo.css') }}">
</head>
<body>

<div class="container">

<h1>🛡️ Sistema de Prevención del Bullying</h1>

<h2>Registrar Reporte</h2>

<form action="/guardar" method="post">

<label>Nombre</label>
<input type="text" name="nombre" required>

<label>Tipo</label>
<select name="tipo">
<option>Físico</option>
<option>Verbal</option>
<option>Psicológico</option>
<option>Social</option>
<option>Ciberbullying</option>
<option>Sexual</option>
</select>

<label>Lugar</label>
<input type="text" name="lugar" required>

<label>Descripción</label>
<textarea name="descripcion" required></textarea>

<button type="submit">
Guardar Reporte
</button>

</form>

<hr>

<h2>Buscar Reporte</h2>

<form action="/buscar" method="post">

<input type="text" name="codigo" placeholder="Ej. R1">

<button type="submit">
Buscar
</button>

</form>

<br>

<a href="/historial">
<button>Ver Historial</button>
</a>

</div>

</body>
</html>body{
font-family:Arial;
background:linear-gradient(135deg,#667eea,#764ba2);
}

.container{
width:80%;
margin:auto;
background:white;
padding:30px;
border-radius:20px;
margin-top:30px;
}

h1{
color:#d32f2f;
text-align:center;
}

input,select,textarea{
width:100%;
padding:10px;
margin:10px 0;
}

button{
background:#d32f2f;
color:white;
border:none;
padding:12px 20px;
border-radius:10px;
cursor:pointer;
}
