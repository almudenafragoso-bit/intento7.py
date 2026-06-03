import customtkinter as ctk

ctk.set_appearance_mode("light")

ventana = ctk.CTk()
ventana.geometry("500x400")
ventana.title("Prueba")

titulo = ctk.CTkLabel(
    ventana,
    text="🩷 Hola Almudena 🩷",
    font=("Arial", 24, "bold")
)
titulo.pack(pady=20)

entrada = ctk.CTkEntry(
    ventana,
    placeholder_text="Escribe algo..."
)
entrada.pack(pady=10)

boton = ctk.CTkButton(
    ventana,
    text="Aceptar",
    corner_radius=20
)
boton.pack(pady=10)

ventana.mainloop()
