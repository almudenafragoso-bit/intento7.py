import tkinter as tk

ventana = tk.Tk()
ventana.title("Prevencion del bullying")
ventana.geometry("600x500")
ventana.configure(bg="lightblue")

def salir():
    ventana.destroy()

def registrar():
    tk.Label(
        ventana,
        text="Hola soy un asistente virtual que atiende diversos tipos de bullying y brinda consejos sobre como enfrentarse a estas situaciones",
        bg="lightblue"
    ).pack()

    tk.Label(ventana, text="Tipos de bullying", bg="lightblue").pack()
    tk.Label(ventana, text="1. Fisico", bg="lightblue").pack()
    tk.Label(ventana, text="2. Verbal", bg="lightblue").pack()
    tk.Label(ventana, text="3. Psicologico", bg="lightblue").pack()
    tk.Label(ventana, text="4. Social", bg="lightblue").pack()
    tk.Label(ventana, text="5. Ciberbullying", bg="lightblue").pack()
    tk.Label(ventana, text="6. Sexual", bg="lightblue").pack()
    tk.Label(ventana, text="7. Otros", bg="lightblue").pack()

    tk.Label(
        ventana,
        text="Selecciona el tipo de bullying que estas viviendo",
        bg="lightblue"
    ).pack()

registrar()

tipo = tk.Entry(ventana)
tipo.pack()

def bullying_fisico():
    ventana1 = tk.Toplevel(ventana)
    ventana1.title("Bullying Fisico")
    ventana1.configure(bg="lightyellow")

    tk.Label(
        ventana1,
        text="Reporta de inmediato las agresiones",
        bg="lightyellow"
    ).pack()

def relacionar():
    opcion = tipo.get()

    if opcion == "1":
        bullying_fisico()

tk.Button(
    ventana,
    text="Relacionar",
    command=relacionar,
    bg="green",
    fg="white"
).pack()

tk.Label(
    ventana,
    text="¿Quieres hacer un reporte? (si/no)",
    bg="lightblue"
).pack()

reporte = tk.Entry(ventana)
reporte.pack()

def reportar():
    respuesta = reporte.get().lower()

    if respuesta == "si":
        tk.Label(
            ventana,
            text="Ingresa tu nombre completo:",
            bg="lightblue"
        ).pack()

        global nombre_completo, tipo_bullying, lugar, descripcion

        nombre_completo = tk.Entry(ventana)
        nombre_completo.pack()

        tk.Label(
            ventana,
            text="Tipo de bullying:",
            bg="lightblue"
        ).pack()

        tipo_bullying = tk.Entry(ventana)
        tipo_bullying.pack()

        tk.Label(
            ventana,
            text="Lugar del incidente:",
            bg="lightblue"
        ).pack()

        lugar = tk.Entry(ventana)
        lugar.pack()

        tk.Label(
            ventana,
            text="Describe lo ocurrido:",
            bg="lightblue"
        ).pack()

        descripcion = tk.Entry(ventana)
        descripcion.pack()

    elif respuesta == "no":
        tk.Label(
            ventana,
            text="Gracias por usar el programa",
            bg="lightblue"
        ).pack()

def guardar():
    tk.Label(
        ventana,
        text="Reporte registrado correctamente",
        bg="lightblue"
    ).pack()

    tk.Label(
        ventana,
        text="Nombre: " + nombre_completo.get(),
        bg="lightblue"
    ).pack()

    tk.Label(
        ventana,
        text="Tipo de bullying: " + tipo_bullying.get(),
        bg="lightblue"
    ).pack()

    tk.Label(
        ventana,
        text="Lugar del incidente: " + lugar.get(),
        bg="lightblue"
    ).pack()

    tk.Label(
        ventana,
        text="Descripcion: " + descripcion.get(),
        bg="lightblue"
    ).pack()

tk.Button(
    ventana,
    text="Presiona para hacer un reporte",
    command=reportar,
    bg="orange"
).pack()

tk.Button(
    ventana,
    text="Presiona para guardar tu reporte",
    command=guardar,
    bg="blue",
    fg="white"
).pack()

tk.Button(
    ventana,
    text="Salir",
    command=salir,
    bg="red",
    fg="white"
).pack()

tk.Label(
    ventana,
    text="Gracias por confiar en mi. Hasta luego :)",
    bg="lightblue"
).pack()

ventana.mainloop()
