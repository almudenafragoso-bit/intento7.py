import tkinter as tk
from tkinter import ttk, messagebox, scrolledtext
import json
import os
from datetime import datetime

class AplicacionBullying:
    def __init__(self, ventana_principal):
        self.ventana_principal = ventana_principal
        self.ventana_principal.title("Sistema de Prevención del Bullying")
        self.ventana_principal.geometry("700x650")
        self.ventana_principal.configure(bg="#f0f4ff")
        
        # Colores temáticos
        self.color_primario = "#6366f1"
        self.color_secundario = "#ec4899"
        self.color_exito = "#10b981"
        self.color_peligro = "#ef4444"
        self.color_fondo = "#f0f4ff"
        self.color_fondo_claro = "#f8fafc"
        
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
        # Frame superior con gradiente (simulado con colores)
        frame_header = tk.Frame(self.ventana_principal, bg=self.color_primario, height=120)
        frame_header.pack(fill=tk.X, pady=0)
        frame_header.pack_propagate(False)
        
        # Título principal
        titulo = tk.Label(
            frame_header,
            text="🛡️ Sistema de Prevención del Bullying 🛡️",
            font=("Arial", 18, "bold"),
            bg=self.color_primario,
            fg="white"
        )
        titulo.pack(pady=15)
        
        # Subtítulo
        subtitulo = tk.Label(
            frame_header,
            text="Un espacio seguro para víctimas y agresores",
            font=("Arial", 11, "italic"),
            bg=self.color_primario,
            fg="#e0e7ff"
        )
        subtitulo.pack(pady=5)
        
        # Frame principal con scroll (si es necesario)
        frame_main = tk.Frame(self.ventana_principal, bg=self.color_fondo)
        frame_main.pack(fill=tk.BOTH, expand=True, padx=20, pady=20)
        
        # Sección: Para Víctimas
        self.crear_seccion_botones(
            frame_main,
            "👥 PARA VÍCTIMAS",
            self.color_secundario,
            [
                ("📋 Recomendaciones de Autoprotección", self.abrir_recomendaciones),
                ("📝 Registrar tu Reporte", self.abrir_registro_reporte),
                ("🔍 Ver tu Reporte", self.abrir_buscar_reporte),
            ]
        )
        
        # Separador
        ttk.Separator(frame_main, orient=tk.HORIZONTAL).pack(fill=tk.X, pady=15)
        
        # Sección: Para Agresores
        self.crear_seccion_botones(
            frame_main,
            "💭 PARA AGRESORES",
            "#f59e0b",
            [
                ("🤝 Espacio de Reflexión y Cambio", self.abrir_ayuda_agresor),
            ]
        )
        
        # Separador
        ttk.Separator(frame_main, orient=tk.HORIZONTAL).pack(fill=tk.X, pady=15)
        
        # Sección: Información General
        self.crear_seccion_botones(
            frame_main,
            "📊 INFORMACIÓN GENERAL",
            self.color_exito,
            [
                ("📊 Ver Todos los Reportes", self.abrir_ver_reportes),
            ]
        )
        
        # Frame inferior con botón salir
        frame_footer = tk.Frame(self.ventana_principal, bg=self.color_fondo)
        frame_footer.pack(fill=tk.X, padx=20, pady=10)
        
        btn_salir = tk.Button(
            frame_footer,
            text="❌ Salir de la Aplicación",
            command=self.ventana_principal.quit,
            bg=self.color_peligro,
            fg="white",
            font=("Arial", 11, "bold"),
            padx=20,
            pady=8,
            relief=tk.FLAT,
            cursor="hand2"
        )
        btn_salir.pack(fill=tk.X)
    
    def crear_seccion_botones(self, parent, titulo, color, botones_lista):
        """Crea una sección con título y botones"""
        frame_seccion = tk.Frame(parent, bg=self.color_fondo)
        frame_seccion.pack(fill=tk.X, pady=10)
        
        # Título de sección
        titulo_label = tk.Label(
            frame_seccion,
            text=titulo,
            font=("Arial", 12, "bold"),
            bg=self.color_fondo,
            fg=color
        )
        titulo_label.pack(anchor="w", pady=(0, 10))
        
        # Botones
        for texto, comando in botones_lista:
            btn = tk.Button(
                frame_seccion,
                text=texto,
                command=comando,
                bg=color,
                fg="white",
                font=("Arial", 10, "bold"),
                padx=15,
                pady=10,
                relief=tk.FLAT,
                cursor="hand2",
                activebackground=self.oscurecer_color(color)
            )
            btn.pack(fill=tk.X, pady=5)
    
    def oscurecer_color(self, color_hex):
        """Oscurece un color hexadecimal"""
        color_hex = color_hex.lstrip('#')
        r, g, b = tuple(int(color_hex[i:i+2], 16) for i in (0, 2, 4))
        r = max(0, r - 30)
        g = max(0, g - 30)
        b = max(0, b - 30)
        return f'#{r:02x}{g:02x}{b:02x}'
    
    def abrir_recomendaciones(self):
        """Abre ventana con recomendaciones según tipo de bullying"""
        ventana = tk.Toplevel(self.ventana_principal)
        ventana.title("Recomendaciones para Víctimas")
        ventana.geometry("750x700")
        ventana.configure(bg=self.color_fondo)
        
        # Header
        frame_header = tk.Frame(ventana, bg=self.color_secundario, height=80)
        frame_header.pack(fill=tk.X, pady=0)
        frame_header.pack_propagate(False)
        
        tk.Label(
            frame_header,
            text="📋 Recomendaciones de Autoprotección",
            font=("Arial", 16, "bold"),
            bg=self.color_secundario,
            fg="white"
        ).pack(pady=15)
        
        tk.Label(
            frame_header,
            text="Selecciona el tipo de bullying para obtener consejos específicos",
            font=("Arial", 10),
            bg=self.color_secundario,
            fg="#fce7f3"
        ).pack()
        
        # Frame principal
        frame_main = tk.Frame(ventana, bg=self.color_fondo)
        frame_main.pack(fill=tk.BOTH, expand=True, padx=20, pady=20)
        
        tipos_bullying = {
            "🥊 Físico": [
                "✓ Reporta las agresiones a un adulto de confianza.",
                "✓ Guarda evidencias (fotos, videos).",
                "✓ Busca apoyo médico si es necesario.",
                "✓ Acompáñate de otros estudiantes.",
                "✓ No estés solo en espacios vulnerables."
            ],
            "💬 Verbal": [
                "✓ No respondas insultando.",
                "✓ Habla con alguien de confianza.",
                "✓ Documenta las palabras hirientes.",
                "✓ Usa frases como 'Eso no me afecta'.",
                "✓ Busca refugio en amigos solidarios."
            ],
            "🧠 Psicológico": [
                "✓ Busca apoyo emocional inmediato.",
                "✓ Acude a orientación escolar.",
                "✓ Practica técnicas de relajación.",
                "✓ Confía en alguien de confianza.",
                "✓ Recuerda que no es tu culpa."
            ],
            "🚫 Social": [
                "✓ Acércate a personas de confianza.",
                "✓ Participa en actividades grupales.",
                "✓ No aisles a otros que sufren lo mismo.",
                "✓ Busca nuevos amigos con tus intereses.",
                "✓ Participa en clubs o grupos escolares."
            ],
            "📱 Ciberbullying": [
                "✓ Bloquea a los agresores inmediatamente.",
                "✓ Guarda capturas de pantalla.",
                "✓ No contestes mensajes negativos.",
                "✓ Reporta el contenido a la plataforma.",
                "✓ Privacidad: revisa tus configuraciones."
            ],
            "⚠️ Sexual": [
                "✓ Denuncia inmediatamente.",
                "✓ Busca ayuda de un adulto de confianza.",
                "✓ Acude a las autoridades escolares.",
                "✓ Busca apoyo psicológico profesional.",
                "✓ Conoce tus derechos sobre tu cuerpo."
            ]
        }
        
        tipo_seleccionado = tk.StringVar(value="🥊 Físico")
        
        # Dropdown mejorado
        tk.Label(frame_main, text="Tipo de bullying:", font=("Arial", 11, "bold"), bg=self.color_fondo, fg=self.color_primario).pack(anchor="w", pady=(0, 5))
        
        dropdown = ttk.Combobox(
            frame_main,
            textvariable=tipo_seleccionado,
            values=list(tipos_bullying.keys()),
            state="readonly",
            font=("Arial", 11),
            width=45
        )
        dropdown.pack(fill=tk.X, pady=(0, 15))
        
        # Área de texto mejorada
        texto_area = scrolledtext.ScrolledText(
            frame_main,
            height=18,
            width=75,
            font=("Arial", 11),
            bg="white",
            fg="#1f2937",
            relief=tk.FLAT,
            borderwidth=2
        )
        texto_area.pack(fill=tk.BOTH, expand=True, pady=(0, 15))
        
        # Configurar tags para estilos
        texto_area.tag_config("titulo", font=("Arial", 12, "bold"), foreground=self.color_secundario)
        texto_area.tag_config("consejo", foreground="#059669", font=("Arial", 11))
        
        def actualizar_recomendaciones():
            texto_area.delete(1.0, tk.END)
            tipo = tipo_seleccionado.get()
            
            texto_area.insert(tk.END, f"📌 {tipo}\n", "titulo")
            texto_area.insert(tk.END, "=" * 60 + "\n\n")
            
            for consejo in tipos_bullying[tipo]:
                texto_area.insert(tk.END, consejo + "\n", "consejo")
                texto_area.insert(tk.END, "\n")
        
        tk.Button(
            frame_main,
            text="🔄 Ver Recomendaciones",
            command=actualizar_recomendaciones,
            bg=self.color_secundario,
            fg="white",
            font=("Arial", 11, "bold"),
            relief=tk.FLAT,
            padx=20,
            pady=8
        ).pack(fill=tk.X)
        
        actualizar_recomendaciones()
    
    def abrir_ayuda_agresor(self):
        """Abre ventana para quien comete bullying"""
        ventana = tk.Toplevel(self.ventana_principal)
        ventana.title("Reflexión y Cambio")
        ventana.geometry("700x750")
        ventana.configure(bg=self.color_fondo)
        
        # Header
        frame_header = tk.Frame(ventana, bg="#f59e0b", height=80)
        frame_header.pack(fill=tk.X, pady=0)
        frame_header.pack_propagate(False)
        
        tk.Label(
            frame_header,
            text="💭 Espacio de Reflexión y Cambio",
            font=("Arial", 16, "bold"),
            bg="#f59e0b",
            fg="white"
        ).pack(pady=15)
        
        tk.Label(
            frame_header,
            text="El primer paso es reconocer el problema",
            font=("Arial", 10),
            bg="#f59e0b",
            fg="#fef3c7"
        ).pack()
        
        # Frame principal
        frame_main = tk.Frame(ventana, bg=self.color_fondo)
        frame_main.pack(fill=tk.BOTH, expand=True, padx=20, pady=20)
        
        texto_reflexion = """
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
                    REFLEXIÓN IMPORTANTE
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

Si estás aquí es porque reconoces que has cometido bullying.
ESE ES EL PRIMER PASO IMPORTANTE HACIA EL CAMBIO.

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
❓ PREGUNTAS PARA LA REFLEXIÓN
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

1. ¿Cómo crees que se siente la otra persona?
   → Imagina el dolor que causaste

2. ¿Qué te llevó a actuar de esa manera?
   → Busca la raíz del problema (ira, inseguridad, presión)

3. ¿Cómo te sentirías si fueras tú la víctima?
   → Practica la empatía

4. ¿Qué puedes hacer para cambiar?
   → Planifica acciones concretas

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
✅ ACCIONES PARA CAMBIAR
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

✓ Ofrece una disculpa sincera y meaningful
✓ Busca ayuda de un adulto o counselor
✓ Participa en talleres de empatía
✓ Mantén distancia del comportamiento negativo
✓ Apoya a las víctimas en lugar de atacarlas
✓ Trabaja en tu autoestima de forma saludable
✓ Busca actividades que canalicen tu energía

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

Recuerda: SIEMPRE ES TIEMPO PARA CAMBIAR Y SER MEJOR PERSONA.

La gente puede cambiar. TÚ PUEDES CAMBIAR.

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
        """
        
        texto = scrolledtext.ScrolledText(
            frame_main,
            height=25,
            width=75,
            font=("Arial", 10),
            bg="white",
            fg="#1f2937",
            relief=tk.FLAT,
            borderwidth=2
        )
        texto.pack(fill=tk.BOTH, expand=True, pady=(0, 15))
        texto.insert(1.0, texto_reflexion)
        texto.config(state=tk.DISABLED)
        
        tk.Button(
            frame_main,
            text="✅ Entiendo, buscaré ayuda",
            command=ventana.destroy,
            bg=self.color_exito,
            fg="white",
            font=("Arial", 12, "bold"),
            relief=tk.FLAT,
            padx=20,
            pady=10
        ).pack(fill=tk.X)
    
    def abrir_registro_reporte(self):
        """Abre ventana para registrar un nuevo reporte"""
        ventana = tk.Toplevel(self.ventana_principal)
        ventana.title("Registrar Reporte de Bullying")
        ventana.geometry("750x850")
        ventana.configure(bg=self.color_fondo)
        
        # Header
        frame_header = tk.Frame(ventana, bg=self.color_primario, height=80)
        frame_header.pack(fill=tk.X, pady=0)
        frame_header.pack_propagate(False)
        
        tk.Label(
            frame_header,
            text="📝 Nuevo Reporte de Bullying",
            font=("Arial", 16, "bold"),
            bg=self.color_primario,
            fg="white"
        ).pack(pady=15)
        
        tk.Label(
            frame_header,
            text="Tu reporte es confidencial y importante",
            font=("Arial", 10),
            bg=self.color_primario,
            fg="#e0e7ff"
        ).pack()
        
        # Canvas con scroll
        canvas = tk.Canvas(ventana, bg=self.color_fondo, highlightthickness=0)
        scrollbar = ttk.Scrollbar(ventana, orient="vertical", command=canvas.scroll)
        scrollable_frame = tk.Frame(canvas, bg=self.color_fondo)
        
        scrollable_frame.bind(
            "<Configure>",
            lambda e: canvas.configure(scrollregion=canvas.bbox("all"))
        )
        
        canvas.create_window((0, 0), window=scrollable_frame, anchor="nw")
        canvas.configure(yscrollcommand=scrollbar.set)
        
        canvas.pack(side="left", fill="both", expand=True, padx=20, pady=20)
        scrollbar.pack(side="right", fill="y")
        
        campos = {}
        
        # Nombre
        self.crear_campo_formulario(scrollable_frame, "Nombre completo:", campos, 'nombre')
        
        # Tipo de bullying
        tk.Label(scrollable_frame, text="Tipo de bullying:", bg=self.color_fondo, font=("Arial", 11, "bold"), fg=self.color_primario).pack(anchor="w", pady=(15, 5))
        campos['tipo'] = ttk.Combobox(
            scrollable_frame,
            values=["🥊 Físico", "💬 Verbal", "🧠 Psicológico", "🚫 Social", "📱 Ciberbullying", "⚠️ Sexual", "🔸 Otros"],
            state="readonly",
            font=("Arial", 10),
            width=45
        )
        campos['tipo'].pack(fill=tk.X, pady=(0, 10))
        
        # Lugar
        self.crear_campo_formulario(scrollable_frame, "Lugar del incidente:", campos, 'lugar')
        
        # Fecha
        self.crear_campo_formulario(scrollable_frame, "Fecha (DD/MM/YYYY):", campos, 'fecha', valor_defecto=datetime.now().strftime("%d/%m/%Y"))
        
        # Descripción
        tk.Label(scrollable_frame, text="Descripción detallada:", bg=self.color_fondo, font=("Arial", 11, "bold"), fg=self.color_primario).pack(anchor="w", pady=(15, 5))
        campos['descripcion'] = scrolledtext.ScrolledText(scrollable_frame, height=10, width=63, font=("Arial", 10), bg="white", relief=tk.FLAT, borderwidth=2)
        campos['descripcion'].pack(fill=tk.BOTH, expand=True, pady=(0, 15))
        
        def guardar_reporte():
            if not campos['nombre'].get() or not campos['tipo'].get() or not campos['descripcion'].get(1.0, tk.END).strip():
                messagebox.showerror("Error", "Por favor completa todos los campos requeridos")
                return
            
            codigo = f"R{len(self.reportes) + 1:04d}"
            self.reportes[codigo] = {
                'codigo': codigo,
                'nombre': campos['nombre'].get(),
                'tipo': campos['tipo'].get(),
                'lugar': campos['lugar'].get(),
                'fecha': campos['fecha'].get(),
                'descripcion': campos['descripcion'].get(1.0, tk.END).strip()
            }
            
            self.guardar_datos()
            messagebox.showinfo("✅ Éxito", f"Reporte registrado exitosamente.\n\nCódigo: {codigo}\n\nGuarda este código para consultar tu reporte.")
            ventana.destroy()
        
        tk.Button(
            scrollable_frame,
            text="💾 Guardar Reporte",
            command=guardar_reporte,
            bg=self.color_exito,
            fg="white",
            font=("Arial", 12, "bold"),
            relief=tk.FLAT,
            padx=20,
            pady=10
        ).pack(fill=tk.X, pady=(0, 10))
    
    def crear_campo_formulario(self, parent, etiqueta, campos, clave, valor_defecto=""):
        """Crea un campo de formulario estándar"""
        tk.Label(parent, text=etiqueta, bg=self.color_fondo, font=("Arial", 11, "bold"), fg=self.color_primario).pack(anchor="w", pady=(15, 5))
        campos[clave] = tk.Entry(parent, width=60, font=("Arial", 10), relief=tk.FLAT, borderwidth=2)
        if valor_defecto:
            campos[clave].insert(0, valor_defecto)
        campos[clave].pack(fill=tk.X, pady=(0, 10))
    
    def abrir_buscar_reporte(self):
        """Abre ventana para buscar un reporte"""
        ventana = tk.Toplevel(self.ventana_principal)
        ventana.title("Buscar Reporte")
        ventana.geometry("700x700")
        ventana.configure(bg=self.color_fondo)
        
        # Header
        frame_header = tk.Frame(ventana, bg="#8b5cf6", height=80)
        frame_header.pack(fill=tk.X, pady=0)
        frame_header.pack_propagate(False)
        
        tk.Label(
            frame_header,
            text="🔍 Buscar tu Reporte",
            font=("Arial", 16, "bold"),
            bg="#8b5cf6",
            fg="white"
        ).pack(pady=15)
        
        tk.Label(
            frame_header,
            text="Ingresa el código de tu reporte para recuperarlo",
            font=("Arial", 10),
            bg="#8b5cf6",
            fg="#ede9fe"
        ).pack()
        
        # Frame principal
        frame_main = tk.Frame(ventana, bg=self.color_fondo)
        frame_main.pack(fill=tk.BOTH, expand=True, padx=20, pady=20)
        
        tk.Label(frame_main, text="Código del reporte (ej. R0001):", bg=self.color_fondo, font=("Arial", 11, "bold"), fg=self.color_primario).pack(anchor="w", pady=(0, 5))
        
        entrada_codigo = tk.Entry(frame_main, width=40, font=("Arial", 11), relief=tk.FLAT, borderwidth=2)
        entrada_codigo.pack(fill=tk.X, pady=(0, 15))
        
        resultado_area = scrolledtext.ScrolledText(frame_main, height=18, width=75, font=("Arial", 10), bg="white", fg="#1f2937", relief=tk.FLAT, borderwidth=2)
        resultado_area.pack(fill=tk.BOTH, expand=True, pady=(0, 15))
        
        def buscar():
            codigo = entrada_codigo.get().strip().upper()
            resultado_area.delete(1.0, tk.END)
            
            if codigo in self.reportes:
                reporte = self.reportes[codigo]
                texto = f"""
{'='*70}
                    📋 REPORTE ENCONTRADO
{'='*70}

Código:        {reporte['codigo']}
Nombre:        {reporte['nombre']}
Tipo:          {reporte['tipo']}
Lugar:         {reporte['lugar']}
Fecha:         {reporte['fecha']}

{'─'*70}
DESCRIPCIÓN:
{'─'*70}

{reporte['descripcion']}

{'='*70}

Estado: ✅ Registrado
Acceso: Confidencial
                """
                resultado_area.insert(1.0, texto)
            else:
                resultado_area.insert(1.0, "❌ Reporte no encontrado.\n\nVerifica que el código sea correcto (ej. R0001)")
        
        tk.Button(
            frame_main,
            text="🔍 Buscar Reporte",
            command=buscar,
            bg="#8b5cf6",
            fg="white",
            font=("Arial", 11, "bold"),
            relief=tk.FLAT,
            padx=20,
            pady=8
        ).pack(fill=tk.X)
    
    def abrir_ver_reportes(self):
        """Abre ventana con todos los reportes"""
        ventana = tk.Toplevel(self.ventana_principal)
        ventana.title("Ver Todos los Reportes")
        ventana.geometry("900x700")
        ventana.configure(bg=self.color_fondo)
        
        # Header
        frame_header = tk.Frame(ventana, bg=self.color_exito, height=80)
        frame_header.pack(fill=tk.X, pady=0)
        frame_header.pack_propagate(False)
        
        tk.Label(
            frame_header,
            text="📊 Todos los Reportes Registrados",
            font=("Arial", 16, "bold"),
            bg=self.color_exito,
            fg="white"
        ).pack(pady=15)
        
        tk.Label(
            frame_header,
            text=f"Total de reportes: {len(self.reportes)}",
            font=("Arial", 11),
            bg=self.color_exito,
            fg="#dcfce7"
        ).pack()
        
        # Frame principal
        frame_main = tk.Frame(ventana, bg=self.color_fondo)
        frame_main.pack(fill=tk.BOTH, expand=True, padx=20, pady=20)
        
        area_reportes = scrolledtext.ScrolledText(frame_main, height=25, width=100, font=("Courier", 9), bg="white", fg="#1f2937", relief=tk.FLAT, borderwidth=2)
        area_reportes.pack(fill=tk.BOTH, expand=True)
        
        if self.reportes:
            texto = """
╔════════════════════════════════════════════════════════════════════════════════════════════════╗
║                              LISTADO DE REPORTES REGISTRADOS                                  ║
╚════════════════════════════════════════════════════════════════════════════════════════════════╝

"""
            for codigo, reporte in self.reportes.items():
                descripcion_corta = reporte['descripcion'][:80].replace('\n', ' ')
                if len(reporte['descripcion']) > 80:
                    descripcion_corta += "..."
                
                texto += f"""
┌─ Código: {codigo} {'─' * (87 - len(codigo))}┐
│ Nombre:      {reporte['nombre']:<75} │
│ Tipo:        {reporte['tipo']:<75} │
│ Lugar:       {reporte['lugar']:<75} │
│ Fecha:       {reporte['fecha']:<75} │
│ Descripción: {descripcion_corta:<75} │
└{'─' * 90}┘

"""
            area_reportes.insert(1.0, texto)
        else:
            texto_vacio = """
╔════════════════════════════════════════════════════════════════════════════════════════════════╗
║                                NO HAY REPORTES REGISTRADOS                                    ║
║                                                                                                ║
║  Sé el primero en registrar un reporte. Tu voz importa y puede ayudar a otros.               ║
╚════════════════════════════════════════════════════════════════════════════════════════════════╝
            """
            area_reportes.insert(1.0, texto_vacio)
        
        area_reportes.config(state=tk.DISABLED)

# Crear la aplicación
if __name__ == "__main__":
    ventana_raiz = tk.Tk()
    app = AplicacionBullying(ventana_raiz)
    ventana_raiz.mainloop()
