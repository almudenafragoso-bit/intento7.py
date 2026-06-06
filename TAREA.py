import tkinter as tk
from tkinter import ttk, messagebox, scrolledtext
import json
import os
from datetime import datetime

class AplicacionBullying:
    def __init__(self, ventana_principal):
        self.ventana_principal = ventana_principal
        self.ventana_principal.title("Sistema de Prevención del Bullying")
        self.ventana_principal.geometry("600x500")
        self.ventana_principal.configure(bg="#ffe8f3")
        
        self.archivo_datos = "reportes.json"
        self.cargar_datos()
        
        self.crear_ventana_principal()
    
    def cargar_datos(self):
        """Carga los reportes desde el archivo JSON"""
        if os.path.exists(self.archivo_datos):
            with open(self.archivo_datos, 'r', encoding='utf-8') as f:
                self.reportes = json.load(f)
        else:
            self.reportes = {}
    
    def guardar_datos(self):
        """Guarda los reportes en el archivo JSON"""
        with open(self.archivo_datos, 'w', encoding='utf-8') as f:
            json.dump(self.reportes, f, ensure_ascii=False, indent=2)
    
    def crear_ventana_principal(self):
        """Crea la ventana principal con botones de navegación"""
        # Título
        titulo = tk.Label(
            self.ventana_principal,
            text="🩷 Sistema de Prevención del Bullying 🩷",
            font=("Arial", 18, "bold"),
            bg="#ffe8f3",
            fg="#c2185b"
        )
        titulo.pack(pady=20)
        
        # Frame para botones
        frame_botones = tk.Frame(self.ventana_principal, bg="#ffe8f3")
        frame_botones.pack(pady=20)
        
        botones_info = [
            ("📋 Recomendaciones para Víctimas", self.abrir_recomendaciones),
            ("🤝 Ayuda para quien comete bullying", self.abrir_ayuda_agresor),
            ("📝 Registrar Reporte", self.abrir_registro_reporte),
            ("🔍 Buscar Reporte", self.abrir_buscar_reporte),
            ("📊 Ver Todos los Reportes", self.abrir_ver_reportes),
        ]
        
        for texto, comando in botones_info:
            btn = tk.Button(
                frame_botones,
                text=texto,
                command=comando,
                bg="#e91e63",
                fg="white",
                font=("Arial", 11, "bold"),
                width=35,
                height=2,
                cursor="hand2"
            )
            btn.pack(pady=10)
        
        # Botón salir
        btn_salir = tk.Button(
            self.ventana_principal,
            text="❌ Salir",
            command=self.ventana_principal.quit,
            bg="#d32f2f",
            fg="white",
            font=("Arial", 10),
            width=35
        )
        btn_salir.pack(pady=20)
    
    def abrir_recomendaciones(self):
        """Abre ventana con recomendaciones según tipo de bullying"""
        ventana = tk.Toplevel(self.ventana_principal)
        ventana.title("Recomendaciones para Víctimas")
        ventana.geometry("700x600")
        ventana.configure(bg="#ffd1e8")
        
        tk.Label(
            ventana,
            text="Selecciona el tipo de bullying",
            font=("Arial", 14, "bold"),
            bg="#ffd1e8",
            fg="#c2185b"
        ).pack(pady=10)
        
        tipos_bullying = {
            "Físico": [
                "✓ Reporta las agresiones a un adulto de confianza.",
                "✓ Guarda evidencias (fotos, videos).",
                "✓ Busca apoyo médico si es necesario.",
                "✓ Acompáñate de otros estudiantes."
            ],
            "Verbal": [
                "✓ No respondas insultando.",
                "✓ Habla con alguien de confianza.",
                "✓ Documenta las palabras hirientes.",
                "✓ Usa frases como 'Eso no me afecta'."
            ],
            "Psicológico": [
                "✓ Busca apoyo emocional inmediato.",
                "✓ Acude a orientación escolar.",
                "✓ Practica técnicas de relajación.",
                "✓ Confía en alguien."
            ],
            "Social": [
                "✓ Acércate a personas de confianza.",
                "✓ Participa en actividades grupales.",
                "✓ No aisles a otros que sufren lo mismo.",
                "✓ Busca nuevos amigos con tus intereses."
            ],
            "Ciberbullying": [
                "✓ Bloquea a los agresores inmediatamente.",
                "✓ Guarda capturas de pantalla.",
                "✓ No contestes mensajes negativos.",
                "✓ Reporta el contenido a la plataforma."
            ],
            "Sexual": [
                "✓ Denuncia inmediatamente.",
                "✓ Busca ayuda de un adulto de confianza.",
                "✓ Acude a las autoridades escolares.",
                "✓ Busca apoyo psicológico profesional."
            ]
        }
        
        # Variable para seleccionar tipo
        tipo_seleccionado = tk.StringVar(value="Físico")
        
        # Dropdown
        dropdown = ttk.Combobox(
            ventana,
            textvariable=tipo_seleccionado,
            values=list(tipos_bullying.keys()),
            state="readonly",
            font=("Arial", 11),
            width=30
        )
        dropdown.pack(pady=10)
        
        # Área de texto para mostrar recomendaciones
        texto_area = scrolledtext.ScrolledText(
            ventana,
            height=15,
            width=70,
            font=("Arial", 11),
            bg="white",
            fg="#333"
        )
        texto_area.pack(pady=10, padx=10)
        
        def actualizar_recomendaciones():
            texto_area.delete(1.0, tk.END)
            tipo = tipo_seleccionado.get()
            contenido = f"📌 Recomendaciones para bullying {tipo}:\n\n"
            contenido += "\n".join(tipos_bullying[tipo])
            texto_area.insert(1.0, contenido)
        
        # Botón para actualizar
        tk.Button(
            ventana,
            text="Ver Recomendaciones",
            command=actualizar_recomendaciones,
            bg="#e91e63",
            fg="white",
            font=("Arial", 10, "bold")
        ).pack(pady=10)
        
        actualizar_recomendaciones()
    
    def abrir_ayuda_agresor(self):
        """Abre ventana para quien comete bullying"""
        ventana = tk.Toplevel(self.ventana_principal)
        ventana.title("Reflexión y Cambio")
        ventana.geometry("600x500")
        ventana.configure(bg="#fff9c4")
        
        tk.Label(
            ventana,
            text="🤔 Espacio de Reflexión",
            font=("Arial", 16, "bold"),
            bg="#fff9c4",
            fg="#f57f17"
        ).pack(pady=20)
        
        texto_reflexion = """
Querido estudiante,

Si estás aquí es porque reconoces que has cometido bullying. 
Ese es el primer paso importante hacia el cambio.

REFLEXIONA:
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
1. ¿Cómo crees que se siente la otra persona?
2. ¿Qué te llevó a actuar de esa manera?
3. ¿Cómo te sentirías si fueras tú la víctima?
4. ¿Qué puedes hacer para cambiar?

ACCIONES PARA CAMBIAR:
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
✓ Ofrece una disculpa sincera
✓ Busca ayuda de un adulto
✓ Participa en talleres de empatía
✓ Mantén distancia del comportamiento negativo
✓ Apoyo a las víctimas de bullying

Recuerda: Siempre es tiempo para cambiar y ser mejor persona.
        """
        
        texto = scrolledtext.ScrolledText(
            ventana,
            height=20,
            width=65,
            font=("Arial", 10),
            bg="white",
            fg="#333"
        )
        texto.pack(pady=10, padx=10)
        texto.insert(1.0, texto_reflexion)
        texto.config(state=tk.DISABLED)
        
        tk.Button(
            ventana,
            text="Entendido, buscar�� ayuda",
            command=ventana.destroy,
            bg="#4caf50",
            fg="white",
            font=("Arial", 11, "bold")
        ).pack(pady=10)
    
    def abrir_registro_reporte(self):
        """Abre ventana para registrar un nuevo reporte"""
        ventana = tk.Toplevel(self.ventana_principal)
        ventana.title("Registrar Reporte de Bullying")
        ventana.geometry("700x700")
        ventana.configure(bg="#e3f2fd")
        
        tk.Label(
            ventana,
            text="📝 Nuevo Reporte de Bullying",
            font=("Arial", 14, "bold"),
            bg="#e3f2fd",
            fg="#1976d2"
        ).pack(pady=10)
        
        # Formulario
        campos = {}
        
        # Nombre
        tk.Label(ventana, text="Nombre completo:", bg="#e3f2fd", font=("Arial", 10)).pack(anchor="w", padx=20, pady=5)
        campos['nombre'] = tk.Entry(ventana, width=50)
        campos['nombre'].pack(padx=20, pady=5)
        
        # Tipo de bullying
        tk.Label(ventana, text="Tipo de bullying:", bg="#e3f2fd", font=("Arial", 10)).pack(anchor="w", padx=20, pady=5)
        campos['tipo'] = ttk.Combobox(
            ventana,
            values=["Físico", "Verbal", "Psicológico", "Social", "Ciberbullying", "Sexual", "Otros"],
            state="readonly"
        )
        campos['tipo'].pack(padx=20, pady=5)
        
        # Lugar
        tk.Label(ventana, text="Lugar del incidente:", bg="#e3f2fd", font=("Arial", 10)).pack(anchor="w", padx=20, pady=5)
        campos['lugar'] = tk.Entry(ventana, width=50)
        campos['lugar'].pack(padx=20, pady=5)
        
        # Fecha
        tk.Label(ventana, text="Fecha (DD/MM/YYYY):", bg="#e3f2fd", font=("Arial", 10)).pack(anchor="w", padx=20, pady=5)
        campos['fecha'] = tk.Entry(ventana, width=50)
        campos['fecha'].insert(0, datetime.now().strftime("%d/%m/%Y"))
        campos['fecha'].pack(padx=20, pady=5)
        
        # Descripción
        tk.Label(ventana, text="Descripción detallada:", bg="#e3f2fd", font=("Arial", 10)).pack(anchor="w", padx=20, pady=5)
        campos['descripcion'] = scrolledtext.ScrolledText(ventana, height=8, width=60)
        campos['descripcion'].pack(padx=20, pady=5)
        
        def guardar_reporte():
            if not campos['nombre'].get() or not campos['tipo'].get() or not campos['descripcion'].get():
                messagebox.showerror("Error", "Por favor completa todos los campos")
                return
            
            codigo = f"R{len(self.reportes) + 1}"
            self.reportes[codigo] = {
                'codigo': codigo,
                'nombre': campos['nombre'].get(),
                'tipo': campos['tipo'].get(),
                'lugar': campos['lugar'].get(),
                'fecha': campos['fecha'].get(),
                'descripcion': campos['descripcion'].get(1.0, tk.END)
            }
            
            self.guardar_datos()
            messagebox.showinfo("Éxito", f"Reporte guardado con código: {codigo}")
            ventana.destroy()
        
        tk.Button(
            ventana,
            text="💾 Guardar Reporte",
            command=guardar_reporte,
            bg="#4caf50",
            fg="white",
            font=("Arial", 11, "bold"),
            width=50
        ).pack(pady=20)
    
    def abrir_buscar_reporte(self):
        """Abre ventana para buscar un reporte"""
        ventana = tk.Toplevel(self.ventana_principal)
        ventana.title("Buscar Reporte")
        ventana.geometry("600x500")
        ventana.configure(bg="#f3e5f5")
        
        tk.Label(
            ventana,
            text="🔍 Buscar Reporte",
            font=("Arial", 14, "bold"),
            bg="#f3e5f5",
            fg="#7b1fa2"
        ).pack(pady=10)
        
        tk.Label(ventana, text="Código del reporte (ej. R1):", bg="#f3e5f5", font=("Arial", 10)).pack(pady=10)
        
        entrada_codigo = tk.Entry(ventana, width=30, font=("Arial", 11))
        entrada_codigo.pack(pady=5)
        
        resultado_area = scrolledtext.ScrolledText(ventana, height=15, width=65, font=("Arial", 10))
        resultado_area.pack(pady=10, padx=10)
        
        def buscar():
            codigo = entrada_codigo.get().strip().upper()
            resultado_area.delete(1.0, tk.END)
            
            if codigo in self.reportes:
                reporte = self.reportes[codigo]
                texto = f"""
📋 REPORTE ENCONTRADO
{'='*40}
Código: {reporte['codigo']}
Nombre: {reporte['nombre']}
Tipo: {reporte['tipo']}
Lugar: {reporte['lugar']}
Fecha: {reporte['fecha']}
Descripción:
{reporte['descripcion']}
                """
                resultado_area.insert(1.0, texto)
            else:
                resultado_area.insert(1.0, "❌ Reporte no encontrado")
        
        tk.Button(
            ventana,
            text="Buscar",
            command=buscar,
            bg="#7b1fa2",
            fg="white",
            font=("Arial", 10, "bold")
        ).pack(pady=10)
    
    def abrir_ver_reportes(self):
        """Abre ventana con todos los reportes"""
        ventana = tk.Toplevel(self.ventana_principal)
        ventana.title("Ver Todos los Reportes")
        ventana.geometry("800x600")
        ventana.configure(bg="#e8f5e9")
        
        tk.Label(
            ventana,
            text="📊 Todos los Reportes Registrados",
            font=("Arial", 14, "bold"),
            bg="#e8f5e9",
            fg="#2e7d32"
        ).pack(pady=10)
        
        area_reportes = scrolledtext.ScrolledText(ventana, height=25, width=90, font=("Arial", 9))
        area_reportes.pack(pady=10, padx=10)
        
        if self.reportes:
            texto = "LISTA DE REPORTES\n" + "="*80 + "\n\n"
            for codigo, reporte in self.reportes.items():
                texto += f"""
Código: {reporte['codigo']} | Nombre: {reporte['nombre']} | Tipo: {reporte['tipo']}
Lugar: {reporte['lugar']} | Fecha: {reporte['fecha']}
Descripción: {reporte['descripcion'][:100]}...
{'-'*80}
"""
            area_reportes.insert(1.0, texto)
        else:
            area_reportes.insert(1.0, "No hay reportes registrados aún.")
        
        area_reportes.config(state=tk.DISABLED)

# Crear la aplicación
if __name__ == "__main__":
    ventana_raiz = tk.Tk()
    app = AplicacionBullying(ventana_raiz)
    ventana_raiz.mainloop()
