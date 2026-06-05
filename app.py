from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

reportes = []

@app.route("/")
def inicio():
    return render_template("index.html")

@app.route("/guardar", methods=["POST"])
def guardar():

    nombre = request.form["nombre"]
    tipo = request.form["tipo"]
    lugar = request.form["lugar"]
    descripcion = request.form["descripcion"]

    if nombre == "" or lugar == "" or descripcion == "":
        return render_template(
            "mensaje.html",
            titulo="Error",
            mensaje="Completa todos los campos."
        )

    codigo = "R" + str(len(reportes) + 1)

    reporte = {
        "codigo": codigo,
        "nombre": nombre,
        "tipo": tipo,
        "lugar": lugar,
        "descripcion": descripcion
    }

    reportes.append(reporte)

    return render_template(
        "mensaje.html",
        titulo="Reporte Guardado",
        mensaje="Tu código es: " + codigo
    )

@app.route("/buscar", methods=["POST"])
def buscar():

    codigo = request.form["codigo"]

    for reporte in reportes:
        if reporte["codigo"] == codigo:
            return render_template(
                "reporte.html",
                reporte=reporte
            )

    return render_template(
        "mensaje.html",
        titulo="No encontrado",
        mensaje="No existe un reporte con ese código."
    )

@app.route("/historial")
def historial():
    return render_template(
        "historial.html",
        reportes=reportes
    )

@app.route("/victima")
def victima():
    return render_template("victima.html")

@app.route("/agresor")
def agresor():
    return render_template("agresor.html")

@app.route("/educacion")
def educacion():
    return render_template("educacion.html")

@app.route("/recursos")
def recursos():
    return render_template("recursos.html")

@app.route("/tutorial")
def tutorial():
    return render_template("tutorial.html")

if __name__ == "__main__":
    app.run(debug=True)
