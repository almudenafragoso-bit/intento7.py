import tkinter as tk
import csv
import os

# ---------------- VENTANA PRINCIPAL ----------------

ventana = tk.Tk()
ventana.title("Prevención del Bullying")
ventana.geometry("700x700")
ventana.configure(bg="#F5E6D3")

archivo = "reportes.csv"

if not os.path.exists(archivo):
    with open(archivo, "w", newline="", encoding="utf-8") as f:
        escritor = csv.writer(f)
        escritor.writerow(
            ["codigo", "nombre", "tipo", "lugar", "descripcion"]
        )

def obtener_siguiente_codigo():

    if not os.path.exists(archivo):
        return 1

    with open(archivo, "r", encoding="utf-8") as f:

        lector = csv.reader(f)
        filas = list(lector)

        if len(filas) <= 1:
            return 1

        ultimo_codigo = filas[-1][0]

        return int(ultimo_codigo.replace("R", "")) + 1


contador = obtener_siguiente_codigo()
formulario_creado = False

# ---------------- FUNCIONES ----------------

def recomendaciones_agresor():

    v = tk.Toplevel()
    v.title("Reflexión")
    v.geometry("450x250")
    v.configure(bg="#F5F0E8")

    tk.Label(
        v,
        text="Recomendaciones para quien comete bullying",
        font=("Arial", 12, "bold"),
        bg="#F5F0E8"
    ).pack(pady=10)

    tk.Label(
        v,
        text="1. Reflexiona sobre cómo tus acciones afectan a otras personas.",
        bg="#F5F0E8",
        wraplength=400
    ).pack(pady=5)

    tk.Label(
        v,
        text="2. Ofrece una disculpa sincera y busca mejorar tu comportamiento.",
        bg="#F5F0E8",
        wraplength=400
    ).pack(pady=5)

    tk.Button(
        v,
        text="Cerrar",
        command=v.destroy,
        bg="#FF69B4",
        fg="white"
    ).pack(pady=10)

def salir():
    ventana.destroy()

def obtener_tipo():
    tipos = {
        "1": "Físico",
        "2": "Verbal",
        "3": "Psicológico",
        "4": "Social",
        "5": "Ciberbullying",
        "6": "Sexual",
        "7": "Otros"
    }

    return tipos.get(tipo.get(), "No especificado")

def mostrar_recomendaciones(titulo, r1, r2):

    v = tk.Toplevel()
    v.title(titulo)
    v.geometry("400x200")
    v.configure(bg="#F5F0E8")

    tk.Label(
        v,
        text=titulo,
        font=("Arial", 12, "bold"),
        bg="#F5F0E8"
    ).pack(pady=10)

    tk.Label(v, text=r1, bg="#F5F0E8").pack()
    tk.Label(v, text=r2, bg="#F5F0E8").pack()

    tk.Button(
        v,
        text="Cerrar",
        command=v.destroy,
        bg="#FF69B4",
        fg="white"
    ).pack(pady=10)

def relacionar():

    opcion = tipo.get()

    if opcion == "1":
        mostrar_recomendaciones(
            "Bullying Físico",
            "1. Reporta las agresiones a un adulto.",
            "2. Guarda evidencias."
        )

    elif opcion == "2":
        mostrar_recomendaciones(
            "Bullying Verbal",
            "1. No respondas con insultos.",
            "2. Habla con alguien de confianza."
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
            "2. Busca apoyo en tu escuela."
        )

def reportar():

    global formulario_creado
    global lbl_nombre, nombre_completo
    global lbl_lugar, lugar
    global lbl_descripcion, descripcion

    if formulario_creado:
        return

    if reporte.get().lower() == "si":

        lbl_nombre = tk.Label(
            ventana,
            text="Nombre completo:",
            bg="#F5E6D3"
        )
        lbl_nombre.pack()

        nombre_completo = tk.Entry(ventana)
        nombre_completo.pack()

        lbl_lugar = tk.Label(
            ventana,
            text="Lugar del incidente:",
            bg="#F5E6D3"
        )
        lbl_lugar.pack()

        lugar = tk.Entry(ventana)
        lugar.pack()

        lbl_descripcion = tk.Label(
            ventana,
            text="Descripción:",
            bg="#F5E6D3"
        )
        lbl_descripcion.pack()

        descripcion = tk.Entry(ventana)
        descripcion.pack()

        formulario_creado = True

def guardar():

    global contador

    if not formulario_creado:
        return

    codigo = "R" + str(contador)

    with open(archivo, "a", newline="", encoding="utf-8") as f:

        escritor = csv.writer(f)

        escritor.writerow([
            codigo,
            nombre_completo.get(),
            obtener_tipo(),
            lugar.get(),
            descripcion.get()
        ])

    contador += 1

    ventana_reporte = tk.Toplevel()
    ventana_reporte.title("Reporte Guardado")
    ventana_reporte.geometry("450x320")
    ventana_reporte.configure(bg="#F5E6D3")

    tk.Label(
        ventana_reporte,
        text="Reporte guardado correctamente",
        font=("Arial", 12, "bold"),
        bg="#F5E6D3"
    ).pack(pady=10)

    tk.Label(
        ventana_reporte,
        text="Código: " + codigo,
        bg="#F5E6D3"
    ).pack()

    tk.Label(
        ventana_reporte,
        text="Nombre: " + nombre_completo.get(),
        bg="#F5E6D3"
    ).pack()

    tk.Label(
        ventana_reporte,
        text="Tipo: " + obtener_tipo(),
        bg="#F5E6D3"
    ).pack()

    tk.Label(
        ventana_reporte,
        text="Lugar: " + lugar.get(),
        bg="#F5E6D3"
    ).pack()

    tk.Label(
        ventana_reporte,
        text="Descripción: " + descripcion.get(),
        bg="#F5E6D3"
    ).pack()

    def volver_menu():

        global formulario_creado

        tipo.delete(0, tk.END)
        reporte.delete(0, tk.END)

        lbl_nombre.destroy()
        nombre_completo.destroy()

        lbl_lugar.destroy()
        lugar.destroy()

        lbl_descripcion.destroy()
        descripcion.destroy()

        formulario_creado = False

        ventana_reporte.destroy()

    tk.Button(
        ventana_reporte,
        text="Volver al menú",
        command=volver_menu,
        bg="#FF69B4",
        fg="white"
    ).pack(pady=15)

def buscar_reporte():

    codigo = codigo_busqueda.get()

    encontrado = False

    with open(
        archivo,
        "r",
        encoding="utf-8"
    ) as f:

        lector = csv.reader(f)

        next(lector)

        for fila in lector:

            if fila[0] == codigo:

                encontrado = True

                v = tk.Toplevel()
                v.title("Reporte Encontrado")
                v.geometry("450x250")
                v.configure(bg="#F5F0E8")

                tk.Label(
                    v,
                    text="Código: " + fila[0],
                    bg="#F5F0E8"
                ).pack()

                tk.Label(
                    v,
                    text="Nombre: " + fila[1],
                    bg="#F5F0E8"
                ).pack()

                tk.Label(
                    v,
                    text="Tipo: " + fila[2],
                    bg="#F5F0E8"
                ).pack()

                tk.Label(
                    v,
                    text="Lugar: " + fila[3],
                    bg="#F5F0E8"
                ).pack()

                tk.Label(
                    v,
                    text="Descripción: " + fila[4],
                    bg="#F5F0E8"
                ).pack()

                break

    if not encontrado:

        tk.Label(
            ventana,
            text="Reporte no encontrado",
            bg="#F5E6D3"
        ).pack()

# ---------------- INTERFAZ ----------------

tk.Label(
    ventana,
    text="🩷 SISTEMA DE PREVENCIÓN DEL BULLYING 🩷",
    font=("Comic Sans MS", 18, "bold"),
    bg="#F5E6D3"
).pack(pady=10)

tk.Label(
    ventana,
    text="1. Físico\n2. Verbal\n3. Psicológico\n4. Social\n5. Ciberbullying\n6. Sexual\n7. Otros",
    bg="#F5E6D3"
).pack()

tk.Label(
    ventana,
    text="Selecciona el tipo de bullying:",
    bg="#F5E6D3"
).pack()

tipo = tk.Entry(ventana)
tipo.pack()

tk.Button(
    ventana,
    text="Mostrar recomendaciones",
    command=relacionar,
    bg="#FF69B4",
    fg="white"
).pack(pady=5)

tk.Button(
    ventana,
    text="Soy quien comete bullying",
    command=recomendaciones_agresor,
    bg="#DB7093",
    fg="white"
).pack(pady=5)

tk.Label(
    ventana,
    text="¿Deseas hacer un reporte? (si/no)",
    bg="#F5E6D3"
).pack()

reporte = tk.Entry(ventana)
reporte.pack()

tk.Button(
    ventana,
    text="Hacer reporte",
    command=reportar,
    bg="#FF69B4",
    fg="white"
).pack(pady=5)

tk.Button(
    ventana,
    text="Guardar reporte",
    command=guardar,
    bg="#DB7093",
    fg="white"
).pack(pady=5)

tk.Label(
    ventana,
    text="Buscar reporte por código:",
    bg="#F5E6D3"
).pack()

codigo_busqueda = tk.Entry(ventana)
codigo_busqueda.pack()

tk.Button(
    ventana,
    text="Buscar",
    command=buscar_reporte,
    bg="#C71585",
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
