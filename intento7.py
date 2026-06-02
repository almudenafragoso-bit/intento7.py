import tkinter as tk

ventana = tk.Tk()
ventana.title("Prevención del Bullying")
ventana.config(bg="#E3F2FD")

def registrar():
    tk.Label(ventana,
             text="Hola, soy un asistente virtual que atiende diversos tipos de bullying.",
             bg="#E3F2FD").pack()

    tk.Label(ventana, text="Tipos de bullying", bg="#E3F2FD",
             fg="darkblue").pack()

    tk.Label(ventana, text="1. Físico", bg="#E3F2FD").pack()
    tk.Label(ventana, text="2. Verbal", bg="#E3F2FD").pack()
    tk.Label(ventana, text="3. Psicológico", bg="#E3F2FD").pack()
    tk.Label(ventana, text="4. Social", bg="#E3F2FD").pack()
    tk.Label(ventana, text="5. Ciberbullying", bg="#E3F2FD").pack()
    tk.Label(ventana, text="6. Sexual", bg="#E3F2FD").pack()
    tk.Label(ventana, text="7. Otros", bg="#E3F2FD").pack()

    tk.Label(ventana,
             text="Selecciona el tipo de bullying que estás viviendo",
             bg="#E3F2FD").pack()

registrar()

tipo = tk.Entry(ventana)
tipo.pack()

def bullying_fisico():
    v = tk.Toplevel(ventana)
    v.title("Bullying Físico")
    tk.Label(v, text="Reporta las agresiones y busca ayuda.").pack()

def bullying_verbal():
    v = tk.Toplevel(ventana)
    v.title("Bullying Verbal")
    tk.Label(v, text="Recuerda tus cualidades personales.").pack()

def bullying_psicologico():
    v = tk.Toplevel(ventana)
    v.title("Bullying Psicológico")
    tk.Label(v, text="Busca apoyo profesional.").pack()

def bullying_social():
    v = tk.Toplevel(ventana)
    v.title("Bullying Social")
    tk.Label(v, text="Participa en actividades grupales.").pack()

def ciberbullying():
    v = tk.Toplevel(ventana)
    v.title("Ciberbullying")
    tk.Label(v, text="Guarda evidencias.").pack()

def bullying_sexual():
    v = tk.Toplevel(ventana)
    v.title("Bullying Sexual")
    tk.Label(v, text="Denuncia inmediatamente.").pack()

def otros():
    v = tk.Toplevel(ventana)
    v.title("Otros")
    tk.Label(v, text="No guardes silencio.").pack()

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

    tipo.delete(0, tk.END)

def reportar():
    global nombre_completo, tipo_bullying, lugar, descripcion

    tk.Label(ventana, text="Nombre completo:", bg="#E3F2FD").pack()
    nombre_completo = tk.Entry(ventana)
    nombre_completo.pack()

    tk.Label(ventana, text="Tipo de bullying:", bg="#E3F2FD").pack()
    tipo_bullying = tk.Entry(ventana)
    tipo_bullying.pack()

    tk.Label(ventana, text="Lugar del incidente:", bg="#E3F2FD").pack()
    lugar = tk.Entry(ventana)
    lugar.pack()

    tk.Label(ventana, text="Descripción:", bg="#E3F2FD").pack()
    descripcion = tk.Entry(ventana)
    descripcion.pack()

def guardar():
    tk.Label(ventana,
             text="Reporte registrado correctamente",
             bg="#E3F2FD",
             fg="green").pack()

    tk.Label(ventana,
             text="Nombre: " + nombre_completo.get(),
             bg="#E3F2FD").pack()

    tk.Label(ventana,
             text="Tipo de bullying: " + tipo_bullying.get(),
             bg="#E3F2FD").pack()

    tk.Label(ventana,
             text="Lugar: " + lugar.get(),
             bg="#E3F2FD").pack()

    tk.Label(ventana,
             text="Descripción: " + descripcion.get(),
             bg="#E3F2FD").pack()

def salir():
    ventana.destroy()

tk.Button(ventana,
          text="Relacionar",
          command=relacionar,
          bg="#1976D2",
          fg="white").pack()

tk.Button(ventana,
          text="Hacer reporte",
          command=reportar,
          bg="#388E3C",
          fg="white").pack()

tk.Button(ventana,
          text="Guardar reporte",
          command=guardar,
          bg="#F57C00",
          fg="white").pack()

tk.Button(ventana,
          text="Salir",
          command=salir,
          bg="red",
          fg="white").pack()

ventana.mainloop()
