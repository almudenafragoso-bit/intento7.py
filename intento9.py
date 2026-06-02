import tkinter as tk

ventana = tk.Tk()
ventana.title("Prevención del Bullying")
ventana.geometry("700x700")
ventana.configure(bg="lightblue")

reportes = {}
contador = 1

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

def mostrar_recomendaciones(titulo, rec1, rec2):
    v = tk.Toplevel()
    v.title(titulo)
    v.geometry("400x200")
    v.configure(bg="lightyellow")

    tk.Label(
        v,
        text=titulo,
        font=("Arial", 12, "bold"),
        bg="lightyellow"
    ).pack(pady=10)

    tk.Label(v, text=rec1, bg="lightyellow").pack()
    tk.Label(v, text=rec2, bg="lightyellow").pack()

def relacionar():
    opcion = tipo.get()

    if opcion == "1":
        mostrar_recomendaciones(
            "Bullying Físico",
            "1. Reporta las agresiones a un adulto.",
            "2. Guarda evidencias si es posible."
        )

    elif opcion == "2":
        mostrar_recomendaciones(
            "Bullying Verbal",
            "1. No respondas con insultos.",
            "2. Habla con una persona de confianza."
        )

    elif opcion == "3":
        mostrar_recomendaciones(
            "Bullying Psicológico",
            "1. Busca apoyo emocional.",
            "2. Acude a orientación psicológica."
        )

    elif opcion == "4":
        mostrar_recomendaciones(
            "Bullying Social",
            "1. Acércate a personas de confianza.",
            "2. Participa en actividades grupales."
        )

    elif opcion == "5":
        mostrar_recomendaciones(
            "Ciberbullying",
            "1. Bloquea a los agresores.",
            "2. Guarda capturas de pantalla."
        )

    elif opcion == "6":
        mostrar_recomendaciones(
            "Bullying Sexual",
            "1. Denuncia inmediatamente.",
            "2. Busca ayuda de un adulto."
        )

    elif opcion == "7":
        mostrar_recomendaciones(
            "Otros",
            "1. Habla con alguien de confianza.",
            "2. Busca apoyo en tu escuela o familia."
        )

def reportar():
    respuesta = reporte.get().lower()

    if respuesta == "si":

        tk.Label(
            ventana,
            text="Nombre completo:",
            bg="lightblue"
        ).pack()

        global nombre_completo, lugar, descripcion

        nombre_completo = tk.Entry(ventana)
        nombre_completo.pack()

        tk.Label(
            ventana,
            text="Lugar del incidente:",
            bg="lightblue"
        ).pack()

        lugar = tk.Entry(ventana)
        lugar.pack()

        tk.Label(
            ventana,
            text="Descripción:",
            bg="lightblue"
        ).pack()

        descripcion = tk.Entry(ventana)
        descripcion.pack()

    elif respuesta == "no":

        tk.Label(
            ventana,
            text="Gracias por utilizar el programa",
            bg="lightblue"
        ).pack()
def guardar():
    global contador

    codigo = "R" + str(contador)

    reportes[codigo] = {
        "nombre": nombre_completo.get(),
        "tipo": obtener_tipo(),
        "lugar": lugar.get(),
        "descripcion": descripcion.get()
    }

    tk.Label(
        ventana,
        text="Reporte guardado con código: " + codigo,
        bg="lightblue"
    ).pack()

    tk.Label(
        ventana,
        text="Nombre: " + nombre_completo.get(),
        bg="lightblue"
    ).pack()

    tk.Label(
        ventana,
        text="Tipo de bullying: " + obtener_tipo(),
        bg="lightblue"
    ).pack()

    tk.Label(
        ventana,
        text="Lugar: " + lugar.get(),
        bg="lightblue"
    ).pack()

    tk.Label(
        ventana,
        text="Descripción: " + descripcion.get(),
        bg="lightblue"
    ).pack()

    contador += 1
    
    tk.Button(
    ventana,
    text="Volver al menú",
    command=volver_menu,
    bg="gray",
    fg="white"
).pack()
def volver_menu():
    nombre_completo.delete(0, tk.END)
    lugar.delete(0, tk.END)
    descripcion.delete(0, tk.END)
    reporte.delete(0, tk.END)
    tipo.delete(0, tk.END)

def buscar_reporte():

    codigo = codigo_busqueda.get()

    if codigo in reportes:

        datos = reportes[codigo]

        ventana_busqueda = tk.Toplevel()
        ventana_busqueda.title("Reporte Encontrado")
        ventana_busqueda.geometry("400x300")

        tk.Label(
            ventana_busqueda,
            text="Código: " + codigo
        ).pack()

        tk.Label(
            ventana_busqueda,
            text="Nombre: " + datos["nombre"]
        ).pack()

        tk.Label(
            ventana_busqueda,
            text="Tipo: " + datos["tipo"]
        ).pack()

        tk.Label(
            ventana_busqueda,
            text="Lugar: " + datos["lugar"]
        ).pack()

        tk.Label(
            ventana_busqueda,
            text="Descripción: " + datos["descripcion"]
        ).pack()

    else:

        tk.Label(
            ventana,
            text="Reporte no encontrado",
            bg="lightblue"
        ).pack()

tk.Label(
    ventana,
    text="PREVENCIÓN DEL BULLYING\n Hola soy un asistente virtual que atiende diversos tipos de bullying y brinda consejos sobre como enfrentarse a estas situaciones",
    font=("Arial", 16, "bold"),
    bg="lightblue"
).pack(pady=10)

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
    text="Mostrar recomendaciones",
    command=relacionar,
    bg="green",
    fg="white"
).pack(pady=5)

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
).pack(pady=5)

tk.Button(
    ventana,
    text="Guardar reporte",
    command=guardar,
    bg="blue",
    fg="white"
).pack(pady=5)

tk.Label(
    ventana,
    text="Buscar reporte por código",
    bg="lightblue"
).pack()

codigo_busqueda = tk.Entry(ventana)
codigo_busqueda.pack()

tk.Button(
    ventana,
    text="Buscar",
    command=buscar_reporte,
    bg="purple",
    fg="white"
).pack(pady=5)

tk.Button(
    ventana,
    text="Salir",
    command=salir,
    bg="red",
    fg="white"
).pack(pady=10)

ventana.mainloop()
