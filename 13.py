import customtkinter as ctk
import csv
import os
from PIL import Image, ImageDraw

# Configurar tema
ctk.set_appearance_mode("light")
ctk.set_default_color_theme("pink")

# ---------------- VENTANA PRINCIPAL ----------------

ventana = ctk.CTk()
ventana.title("Prevención del Bullying")
ventana.geometry("700x900")
ventana.configure(fg_color="#F5E6D3")

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

    v = ctk.CTkToplevel()
    v.title("Reflexión")
    v.geometry("450x250")
    v.configure(fg_color="#F5F0E8")

    ctk.CTkLabel(
        v,
        text="Recomendaciones para quien comete bullying",
        font=("Arial", 12, "bold"),
        text_color="#000000"
    ).pack(pady=10)

    ctk.CTkLabel(
        v,
        text="1. Reflexiona sobre cómo tus acciones afectan a otras personas.",
        text_color="#000000",
        wraplength=400
    ).pack(pady=5)

    ctk.CTkLabel(
        v,
        text="2. Ofrece una disculpa sincera y busca mejorar tu comportamiento.",
        text_color="#000000",
        wraplength=400
    ).pack(pady=5)

    ctk.CTkButton(
        v,
        text="Cerrar",
        command=v.destroy,
        fg_color="#FF69B4",
        text_color="white",
        corner_radius=15,
        hover_color="#DB7093"
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

    v = ctk.CTkToplevel()
    v.title(titulo)
    v.geometry("400x200")
    v.configure(fg_color="#F5F0E8")

    ctk.CTkLabel(
        v,
        text=titulo,
        font=("Arial", 12, "bold"),
        text_color="#000000"
    ).pack(pady=10)

    ctk.CTkLabel(v, text=r1, text_color="#000000").pack()
    ctk.CTkLabel(v, text=r2, text_color="#000000").pack()

    ctk.CTkButton(
        v,
        text="Cerrar",
        command=v.destroy,
        fg_color="#FF69B4",
        text_color="white",
        corner_radius=15,
        hover_color="#DB7093"
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

        lbl_nombre = ctk.CTkLabel(
            ventana,
            text="Nombre completo:",
            text_color="#000000"
        )
        lbl_nombre.pack()

        nombre_completo = ctk.CTkEntry(ventana, corner_radius=10)
        nombre_completo.pack(pady=5)

        lbl_lugar = ctk.CTkLabel(
            ventana,
            text="Lugar del incidente:",
            text_color="#000000"
        )
        lbl_lugar.pack()

        lugar = ctk.CTkEntry(ventana, corner_radius=10)
        lugar.pack(pady=5)

        lbl_descripcion = ctk.CTkLabel(
            ventana,
            text="Descripción:",
            text_color="#000000"
        )
        lbl_descripcion.pack()

        descripcion = ctk.CTkEntry(ventana, corner_radius=10)
        descripcion.pack(pady=5)

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

    ventana_reporte = ctk.CTkToplevel()
    ventana_reporte.title("Reporte Guardado")
    ventana_reporte.geometry("450x320")
    ventana_reporte.configure(fg_color="#F5E6D3")

    ctk.CTkLabel(
        ventana_reporte,
        text="Reporte guardado correctamente",
        font=("Arial", 12, "bold"),
        text_color="#000000"
    ).pack(pady=10)

    ctk.CTkLabel(
        ventana_reporte,
        text="Código: " + codigo,
        text_color="#000000"
    ).pack()

    ctk.CTkLabel(
        ventana_reporte,
        text="Nombre: " + nombre_completo.get(),
        text_color="#000000"
    ).pack()

    ctk.CTkLabel(
        ventana_reporte,
        text="Tipo: " + obtener_tipo(),
        text_color="#000000"
    ).pack()

    ctk.CTkLabel(
        ventana_reporte,
        text="Lugar: " + lugar.get(),
        text_color="#000000"
    ).pack()

    ctk.CTkLabel(
        ventana_reporte,
        text="Descripción: " + descripcion.get(),
        text_color="#000000"
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

    ctk.CTkButton(
        ventana_reporte,
        text="Volver al menú",
        command=volver_menu,
        fg_color="#FF69B4",
        text_color="white",
        corner_radius=15,
        hover_color="#DB7093"
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

                v = ctk.CTkToplevel()
                v.title("Reporte Encontrado")
                v.geometry("450x250")
                v.configure(fg_color="#F5F0E8")

                ctk.CTkLabel(
                    v,
                    text="Código: " + fila[0],
                    text_color="#000000"
                ).pack()

                ctk.CTkLabel(
                    v,
                    text="Nombre: " + fila[1],
                    text_color="#000000"
                ).pack()

                ctk.CTkLabel(
                    v,
                    text="Tipo: " + fila[2],
                    text_color="#000000"
                ).pack()

                ctk.CTkLabel(
                    v,
                    text="Lugar: " + fila[3],
                    text_color="#000000"
                ).pack()

                ctk.CTkLabel(
                    v,
                    text="Descripción: " + fila[4],
                    text_color="#000000"
                ).pack()

                break

    if not encontrado:

        ctk.CTkLabel(
            ventana,
            text="Reporte no encontrado",
            text_color="#000000"
        ).pack()

# ---------------- INTERFAZ ----------------

ctk.CTkLabel(
    ventana,
    text="🩷 SISTEMA DE PREVENCIÓN DEL BULLYING 🩷",
    font=("Comic Sans MS", 18, "bold"),
    text_color="#000000"
).pack(pady=10)

ctk.CTkLabel(
    ventana,
    text="1. Físico\n2. Verbal\n3. Psicológico\n4. Social\n5. Ciberbullying\n6. Sexual\n7. Otros",
    text_color="#000000"
).pack()

ctk.CTkLabel(
    ventana,
    text="Selecciona el tipo de bullying:",
    text_color="#000000"
).pack()

tipo = ctk.CTkEntry(ventana, corner_radius=10)
tipo.pack(pady=5)

ctk.CTkButton(
    ventana,
    text="Mostrar recomendaciones",
    command=relacionar,
    fg_color="#FF69B4",
    text_color="white",
    corner_radius=15,
    hover_color="#DB7093"
).pack(pady=5)

ctk.CTkButton(
    ventana,
    text="Soy quien comete bullying",
    command=recomendaciones_agresor,
    fg_color="#DB7093",
    text_color="white",
    corner_radius=15,
    hover_color="#FF69B4"
).pack(pady=5)

ctk.CTkLabel(
    ventana,
    text="¿Deseas hacer un reporte? (si/no)",
    text_color="#000000"
).pack()

reporte = ctk.CTkEntry(ventana, corner_radius=10)
reporte.pack(pady=5)

ctk.CTkButton(
    ventana,
    text="Hacer reporte",
    command=reportar,
    fg_color="#FF69B4",
    text_color="white",
    corner_radius=15,
    hover_color="#DB7093"
).pack(pady=5)

ctk.CTkButton(
    ventana,
    text="Guardar reporte",
    command=guardar,
    fg_color="#DB7093",
    text_color="white",
    corner_radius=15,
    hover_color="#FF69B4"
).pack(pady=5)

ctk.CTkLabel(
    ventana,
    text="Buscar reporte por código:",
    text_color="#000000"
).pack()

codigo_busqueda = ctk.CTkEntry(ventana, corner_radius=10)
codigo_busqueda.pack(pady=5)

ctk.CTkButton(
    ventana,
    text="Buscar",
    command=buscar_reporte,
    fg_color="#C71585",
    text_color="white",
    corner_radius=15,
    hover_color="#FF69B4"
).pack(pady=5)

ctk.CTkButton(
    ventana,
    text="Salir",
    command=salir,
    fg_color="red",
    text_color="white",
    corner_radius=15,
    hover_color="#8B0000"
).pack(pady=10)

ventana.mainloop()
