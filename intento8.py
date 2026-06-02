import tkinter as tk

ventana = tk.Tk()
ventana.title("Prevención del Bullying")
ventana.geometry("600x600")
ventana.configure(bg="lightblue")

def salir():
    ventana.destroy()

def obtener_tipo():
    opcion = tipo.get()

    if opcion == "1":
        return "Físico"
    elif opcion == "2":
        return "Verbal"
    elif opcion == "3":
        return "Psicológico"
    elif opcion == "4":
        return "Social"
    elif opcion == "5":
        return "Ciberbullying"
    elif opcion == "6":
        return "Sexual"
    elif opcion == "7":
        return "Otros"
    else:
        return "No especificado"

def bullying_fisico():
    v = tk.Toplevel()
    v.title("Bullying Físico")

    tk.Label(v, text="1. Reporta las agresiones a un adulto.").pack()
    tk.Label(v, text="2. Guarda evidencias si es posible.").pack()

def bullying_verbal():
    v = tk.Toplevel()
    v.title("Bullying Verbal")

    tk.Label(v, text="1. No respondas con insultos.").pack()
    tk.Label(v, text="2. Habla con una persona de confianza.").pack()

def bullying_psicologico():
    v = tk.Toplevel()
    v.title("Bullying Psicológico")

    tk.Label(v, text="1. Busca apoyo emocional.").pack()
    tk.Label(v, text="2. Acude a orientación psicológica.").pack()

def bullying_social():
    v = tk.Toplevel()
    v.title("Bullying Social")

    tk.Label(v, text="1. Acércate a personas de confianza.").pack()
    tk.Label(v, text="2. Participa en actividades grupales.").pack()

def ciberbullying():
    v = tk.Toplevel()
    v.title("Ciberbullying")

    tk.Label(v, text="1. Bloquea a los agresores.").pack()
    tk.Label(v, text="2. Guarda capturas de pantalla.").pack()

def bullying_sexual():
    v = tk.Toplevel()
    v.title("Bullying Sexual")

    tk.Label(v, text="1. Denuncia inmediatamente.").pack()
    tk.Label(v, text="2. Busca ayuda de un adulto.").pack()

def otros():
    v = tk.Toplevel()
    v.title("Otros")

    tk.Label(v, text="1. Habla con alguien de confianza.").pack()
    tk.Label(v, text="2. Busca apoyo en tu escuela o familia.").pack()

def relacionar():
    opcion = tipo.get()

    if opcion == "1":
        bullying_fisico()
    elif opcion == "2":
        bullying_verbal()
    elif opcion == "3":
        bullying_psicologico()
    elif opcion == "4":
        bullying_social()
    elif opcion == "5":
        ciberbullying()
    elif opcion == "6":
        bullying_sexual()
    elif opcion == "7":
        otros()

def reportar():
    respuesta = reporte.get().lower()

    if respuesta == "si":

        tk.Label(ventana,
                 text="Nombre completo:",
                 bg="lightblue").pack()

        global nombre_completo, lugar, descripcion

        nombre_completo = tk.Entry(ventana)
        nombre_completo.pack()

        tk.Label(ventana,
                 text="Lugar del incidente:",
                 bg="lightblue").pack()

        lugar = tk.Entry(ventana)
        lugar.pack()

        tk.Label(ventana,
                 text="Descripción de lo ocurrido:",
                 bg="lightblue").pack()

        descripcion = tk.Entry(ventana)
        descripcion.pack()

    elif respuesta == "no":

        tk.Label(ventana,
                 text="Gracias por usar el programa",
                 bg="lightblue").pack()

def guardar():

    tk.Label(ventana,
             text="REPORTE REGISTRADO",
             bg="lightblue").pack()

    tk.Label(ventana,
             text="Nombre: " + nombre_completo.get(),
             bg="lightblue").pack()

    tk.Label(ventana,
             text="Tipo de bullying: " + obtener_tipo(),
             bg="lightblue").pack()

    tk.Label(ventana,
             text="Lugar: " + lugar.get(),
             bg="lightblue").pack()

    tk.Label(ventana,
             text="Descripción: " + descripcion.get(),
             bg="lightblue").pack()

tk.Label(
    ventana,
    text="PREVENCIÓN DEL BULLYING",
    text="hola soy un asistente que te ayudara a solucionar diferentes tipos de bullying :)",
    font=("Arial", 14, "bold"),
    bg="lightblue"
).pack()

tk.Label(
    ventana,
    text="Tipos de bullying",
    bg="lightblue"
).pack()

tk.Label(ventana, text="1. Físico", bg="lightblue").pack()
tk.Label(ventana, text="2. Verbal", bg="lightblue").pack()
tk.Label(ventana, text="3. Psicológico", bg="lightblue").pack()
tk.Label(ventana, text="4. Social", bg="lightblue").pack()
tk.Label(ventana, text="5. Ciberbullying", bg="lightblue").pack()
tk.Label(ventana, text="6. Sexual", bg="lightblue").pack()
tk.Label(ventana, text="7. Otros", bg="lightblue").pack()

tk.Label(
    ventana,
    text="Selecciona el tipo de bullying:",
    bg="lightblue"
).pack()

tipo = tk.Entry(ventana)
tipo.pack()

tk.Button(
    ventana,
    text="Relacionar",
    command=relacionar,
    bg="green",
    fg="white"
).pack()

tk.Label(
    ventana,
    text="¿Deseas hacer un reporte? (si/no)",
    bg="lightblue"
).pack()

reporte = tk.Entry(ventana)
reporte.pack()

tk.Button(
    ventana,
    text="Hacer reporte",
    command=reportar,
    bg="orange"
).pack()

tk.Button(
    ventana,
    text="Guardar reporte",
    text="gracias por confiar en nosotros :)",
    command=guardar,
    bg="pink",
    fg="white"
).pack()

tk.Button(
    ventana,
    text="Salir",
    command=salir,
    bg="red",
    fg="white"
).pack()

ventana.mainloop()
