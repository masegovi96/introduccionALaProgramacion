"""
Módulo de Introducción a Python
Contiene información interactiva sobre Python, su historia, características y aplicaciones
"""

import tkinter as tk
from tkinter import ttk, messagebox
import webbrowser
import subprocess
import sys


class IntroduccionPython:
    """Clase principal para la ventana de introducción a Python"""
    
    def __init__(self, parent=None):
        """Inicializa la ventana de introducción a Python"""
        self.parent = parent
        self.ventana = tk.Toplevel(parent) if parent else tk.Tk()
        self.setup_window()
        self.create_main_interface()
        
    def setup_window(self):
        """Configura la ventana principal"""
        self.ventana.title("Introducción a Python")
        self.ventana.geometry("900x700")
        self.ventana.configure(bg='#f0f8ff')
        
        # Centrar ventana
        self.ventana.update_idletasks()
        width = self.ventana.winfo_width()
        height = self.ventana.winfo_height()
        x = (self.ventana.winfo_screenwidth() // 2) - (width // 2)
        y = (self.ventana.winfo_screenheight() // 2) - (height // 2)
        self.ventana.geometry(f'{width}x{height}+{x}+{y}')
        
    def create_main_interface(self):
        """Crea la interfaz principal con los botones de temas"""
        # Frame principal
        main_frame = ttk.Frame(self.ventana, padding="20")
        main_frame.pack(fill=tk.BOTH, expand=True)
        
        # Título
        title_label = ttk.Label(main_frame, 
                               text="Introducción a Python",
                               font=('Arial', 24, 'bold'),
                               foreground='#2c3e50')
        title_label.pack(pady=(0, 10))
        
        # Subtítulo
        subtitle_label = ttk.Label(main_frame,
                                  text="Descubre todo sobre el lenguaje de programación más popular del mundo",
                                  font=('Arial', 12),
                                  foreground='#34495e')
        subtitle_label.pack(pady=(0, 30))
        
        # Frame para botones de temas
        temas_frame = ttk.Frame(main_frame)
        temas_frame.pack(fill=tk.BOTH, expand=True, pady=20)
        
        # Configurar grid
        for i in range(3):
            temas_frame.columnconfigure(i, weight=1)
        for i in range(3):
            temas_frame.rowconfigure(i, weight=1)
        
        # Definir temas
        temas = [
            ("¿Qué es Python?", self.mostrar_que_es_python, "#3498db"),
            ("Historia de Python", self.mostrar_historia, "#e74c3c"),
            ("Ventajas de Python", self.mostrar_ventajas, "#2ecc71"),
            ("Aplicaciones", self.mostrar_aplicaciones, "#f39c12"),
            ("Sintaxis Básica", self.mostrar_sintaxis, "#9b59b6"),
            ("Primeros Pasos", self.mostrar_primeros_pasos, "#1abc9c"),
            ("Recursos de Aprendizaje", self.mostrar_recursos, "#34495e"),
            ("Comunidad Python", self.mostrar_comunidad, "#e67e22"),
        ]
        
        # Crear botones para cada tema
        for i, (nombre, comando, color) in enumerate(temas):
            btn = ttk.Button(temas_frame,
                           text=nombre,
                           command=comando,
                           style='Tema.TButton')
            
            row = i // 3
            col = i % 3
            btn.grid(row=row, column=col, padx=10, pady=10, sticky='nsew')
        
        # Configurar estilo para botones
        style = ttk.Style()
        style.configure('Tema.TButton',
                       font=('Arial', 11, 'bold'),
                       padding=(15, 10))
        
        # Información de versión actual de Python
        version_frame = ttk.Frame(main_frame)
        version_frame.pack(fill=tk.X, pady=(20, 0))
        
        try:
            version_python = f"Python {sys.version.split()[0]}"
            version_label = ttk.Label(version_frame,
                                    text=f"Estás usando: {version_python}",
                                    font=('Arial', 10),
                                    foreground='#7f8c8d')
            version_label.pack()
        except:
            pass
    
    def mostrar_que_es_python(self):
        """Muestra información sobre qué es Python"""
        self.mostrar_tema("¿Qué es Python?", self.get_que_es_python_info(), 
                         self.crear_demo_python, "#3498db")
    
    def mostrar_historia(self):
        """Muestra la historia de Python"""
        self.mostrar_tema("Historia de Python", self.get_historia_info(), 
                         self.mostrar_linea_tiempo, "#e74c3c")
    
    def mostrar_ventajas(self):
        """Muestra las ventajas de Python"""
        self.mostrar_tema("Ventajas de Python", self.get_ventajas_info(), 
                         self.comparar_lenguajes, "#2ecc71")
    
    def mostrar_aplicaciones(self):
        """Muestra las aplicaciones de Python"""
        self.mostrar_tema("Aplicaciones de Python", self.get_aplicaciones_info(), 
                         self.mostrar_ejemplos_aplicaciones, "#f39c12")
    
    def mostrar_sintaxis(self):
        """Muestra la sintaxis básica de Python"""
        self.mostrar_tema("Sintaxis Básica de Python", self.get_sintaxis_info(), 
                         self.ejecutar_ejemplos_sintaxis, "#9b59b6")
    
    def mostrar_primeros_pasos(self):
        """Muestra los primeros pasos en Python"""
        self.mostrar_tema("Primeros Pasos", self.get_primeros_pasos_info(), 
                         self.guia_instalacion, "#1abc9c")
    
    def mostrar_recursos(self):
        """Muestra recursos de aprendizaje"""
        self.mostrar_tema("Recursos de Aprendizaje", self.get_recursos_info(), 
                         self.abrir_recursos_externos, "#34495e")
    
    def mostrar_comunidad(self):
        """Muestra información sobre la comunidad Python"""
        self.mostrar_tema("Comunidad Python", self.get_comunidad_info(), 
                         self.conectar_comunidad, "#e67e22")
    
    def mostrar_tema(self, titulo, contenido, funcion_interactiva, color):
        """Muestra la ventana de información de un tema específico"""
        # Crear nueva ventana
        ventana_tema = tk.Toplevel(self.ventana)
        ventana_tema.title(f"Python - {titulo}")
        ventana_tema.geometry("1000x800")
        ventana_tema.configure(bg='#f8f9fa')
        
        # Frame principal con scroll
        canvas = tk.Canvas(ventana_tema, bg='#f8f9fa')
        scrollbar = ttk.Scrollbar(ventana_tema, orient="vertical", command=canvas.yview)
        scrollable_frame = ttk.Frame(canvas)
        
        scrollable_frame.bind(
            "<Configure>",
            lambda e: canvas.configure(scrollregion=canvas.bbox("all"))
        )
        
        canvas.create_window((0, 0), window=scrollable_frame, anchor="nw")
        canvas.configure(yscrollcommand=scrollbar.set)
        
        # Pack canvas y scrollbar
        canvas.pack(side="left", fill="both", expand=True, padx=20, pady=20)
        scrollbar.pack(side="right", fill="y")
        
        # Título del tema
        title_label = ttk.Label(scrollable_frame,
                               text=titulo,
                               font=('Arial', 20, 'bold'),
                               foreground=color)
        title_label.pack(pady=(0, 20))
        
        # Información del tema
        info_frame = ttk.LabelFrame(scrollable_frame, text="Información", padding="15")
        info_frame.pack(fill=tk.X, pady=(0, 20))
        
        info_text = tk.Text(info_frame, height=15, wrap=tk.WORD, font=('Arial', 11))
        info_text.insert(tk.END, contenido)
        info_text.config(state=tk.DISABLED)
        info_text.pack(fill=tk.X)
        
        # Frame para actividad interactiva
        if funcion_interactiva:
            actividad_frame = ttk.LabelFrame(scrollable_frame, text="Actividad Interactiva", padding="15")
            actividad_frame.pack(fill=tk.X, pady=(0, 20))
            funcion_interactiva(actividad_frame)
        
        # Botón de cerrar
        btn_cerrar = ttk.Button(scrollable_frame,
                               text="Volver al Menú Principal",
                               command=ventana_tema.destroy)
        btn_cerrar.pack(pady=(20, 0))
    
    def crear_demo_python(self, parent_frame):
        """Crea una demostración interactiva de Python"""
        demo_label = ttk.Label(parent_frame, 
                              text="¡Prueba Python en vivo!",
                              font=('Arial', 12, 'bold'))
        demo_label.pack(pady=(0, 10))
        
        # Área de código
        code_frame = ttk.Frame(parent_frame)
        code_frame.pack(fill=tk.X, pady=(0, 10))
        
        ttk.Label(code_frame, text="Escribe código Python aquí:").pack(anchor='w')
        self.code_text = tk.Text(code_frame, height=5, font=('Courier', 10))
        self.code_text.pack(fill=tk.X)
        self.code_text.insert(tk.END, "# ¡Hola! Escribe código Python aquí\nprint('¡Hola, mundo desde Python!')\nnombre = 'Programador'\nprint(f'Bienvenido, {nombre}!')")
        
        # Área de resultado
        result_frame = ttk.Frame(parent_frame)
        result_frame.pack(fill=tk.X, pady=(10, 0))
        
        ttk.Label(result_frame, text="Resultado:").pack(anchor='w')
        self.result_text = tk.Text(result_frame, height=5, font=('Courier', 10), 
                                  bg='#f8f8f8', state=tk.DISABLED)
        self.result_text.pack(fill=tk.X)
        
        # Botón ejecutar
        btn_ejecutar = ttk.Button(parent_frame,
                                 text="Ejecutar Código",
                                 command=self.ejecutar_codigo_demo)
        btn_ejecutar.pack(pady=(10, 0))
    
    def ejecutar_codigo_demo(self):
        """Ejecuta el código Python del demo"""
        try:
            codigo = self.code_text.get("1.0", tk.END).strip()
            
            # Redirigir salida
            import io
            import contextlib
            
            salida = io.StringIO()
            
            with contextlib.redirect_stdout(salida):
                exec(codigo)
            
            resultado = salida.getvalue()
            
            # Mostrar resultado
            self.result_text.config(state=tk.NORMAL)
            self.result_text.delete("1.0", tk.END)
            self.result_text.insert(tk.END, resultado if resultado else "Código ejecutado sin salida")
            self.result_text.config(state=tk.DISABLED)
            
        except Exception as e:
            self.result_text.config(state=tk.NORMAL)
            self.result_text.delete("1.0", tk.END)
            self.result_text.insert(tk.END, f"Error: {str(e)}")
            self.result_text.config(state=tk.DISABLED)
    
    def mostrar_linea_tiempo(self, parent_frame):
        """Muestra una línea de tiempo interactiva de Python"""
        timeline_label = ttk.Label(parent_frame, 
                                  text="Línea de Tiempo de Python",
                                  font=('Arial', 12, 'bold'))
        timeline_label.pack(pady=(0, 10))
        
        # Lista de eventos
        eventos = [
            ("1989", "Guido van Rossum comienza a trabajar en Python"),
            ("1991", "Primera versión pública de Python 0.9.0"),
            ("1994", "Python 1.0 - Programación funcional"),
            ("2000", "Python 2.0 - Comprensiones de lista"),
            ("2008", "Python 3.0 - Grandes cambios y mejoras"),
            ("2020", "Python 2 llega al final de su vida útil"),
            ("2021", "Python se convierte en el lenguaje más popular")
        ]
        
        # Canvas para la línea de tiempo
        canvas_timeline = tk.Canvas(parent_frame, height=300, bg='white')
        canvas_timeline.pack(fill=tk.X, pady=(0, 10))
        
        # Dibujar línea de tiempo
        canvas_timeline.create_line(50, 150, 950, 150, width=3, fill='#3498db')
        
        for i, (año, evento) in enumerate(eventos):
            x = 50 + (i * 130)
            
            # Punto en la línea
            canvas_timeline.create_oval(x-5, 145, x+5, 155, fill='#e74c3c', outline='#c0392b')
            
            # Año
            canvas_timeline.create_text(x, 130, text=año, font=('Arial', 10, 'bold'))
            
            # Evento (texto envuelto)
            words = evento.split()
            line1 = ' '.join(words[:3])
            line2 = ' '.join(words[3:]) if len(words) > 3 else ""
            
            canvas_timeline.create_text(x, 180, text=line1, font=('Arial', 8), width=100)
            if line2:
                canvas_timeline.create_text(x, 195, text=line2, font=('Arial', 8), width=100)
    
    def comparar_lenguajes(self, parent_frame):
        """Compara Python con otros lenguajes"""
        comparacion_label = ttk.Label(parent_frame, 
                                     text="Python vs Otros Lenguajes",
                                     font=('Arial', 12, 'bold'))
        comparacion_label.pack(pady=(0, 10))
        
        # Tabla de comparación
        tree = ttk.Treeview(parent_frame, columns=('Python', 'Java', 'C++'), show='tree headings', height=8)
        tree.pack(fill=tk.X)
        
        # Configurar columnas
        tree.column('#0', width=150)
        tree.column('Python', width=150)
        tree.column('Java', width=150)
        tree.column('C++', width=150)
        
        tree.heading('#0', text='Característica')
        tree.heading('Python', text='Python')
        tree.heading('Java', text='Java')
        tree.heading('C++', text='C++')
        
        # Datos de comparación
        comparaciones = [
            ('Facilidad de aprendizaje', 'Muy fácil', 'Moderada', 'Difícil'),
            ('Velocidad de ejecución', 'Moderada', 'Rápida', 'Muy rápida'),
            ('Líneas de código', 'Pocas', 'Moderadas', 'Muchas'),
            ('Legibilidad', 'Excelente', 'Buena', 'Compleja'),
            ('Comunidad', 'Muy activa', 'Activa', 'Activa'),
            ('Uso en IA/ML', 'Excelente', 'Bueno', 'Limitado'),
            ('Desarrollo web', 'Excelente', 'Bueno', 'Limitado'),
        ]
        
        for caracteristica, python, java, cpp in comparaciones:
            tree.insert('', 'end', text=caracteristica, values=(python, java, cpp))
    
    def mostrar_ejemplos_aplicaciones(self, parent_frame):
        """Muestra ejemplos de aplicaciones famosas hechas en Python"""
        ejemplos_label = ttk.Label(parent_frame, 
                                  text="Aplicaciones Famosas Hechas en Python",
                                  font=('Arial', 12, 'bold'))
        ejemplos_label.pack(pady=(0, 10))
        
        # Frame para ejemplos
        ejemplos_frame = ttk.Frame(parent_frame)
        ejemplos_frame.pack(fill=tk.X)
        
        ejemplos = [
            ("YouTube", "Plataforma de videos más grande del mundo"),
            ("Instagram", "Red social de fotos y videos"),
            ("Spotify", "Servicio de streaming de música"),
            ("Uber", "Aplicación de transporte"),
            ("Netflix", "Plataforma de streaming de películas"),
            ("DropBox", "Servicio de almacenamiento en la nube"),
        ]
        
        for i, (app, descripcion) in enumerate(ejemplos):
            app_frame = ttk.Frame(ejemplos_frame)
            app_frame.pack(fill=tk.X, pady=5)
            
            ttk.Label(app_frame, text=app, font=('Arial', 11, 'bold')).pack(side=tk.LEFT)
            ttk.Label(app_frame, text=f" - {descripcion}", font=('Arial', 10)).pack(side=tk.LEFT)
    
    def ejecutar_ejemplos_sintaxis(self, parent_frame):
        """Permite ejecutar ejemplos de sintaxis Python"""
        sintaxis_label = ttk.Label(parent_frame, 
                                  text="Ejemplos Interactivos de Sintaxis",
                                  font=('Arial', 12, 'bold'))
        sintaxis_label.pack(pady=(0, 10))
        
        # Combobox para seleccionar ejemplo
        ttk.Label(parent_frame, text="Selecciona un ejemplo:").pack(anchor='w')
        self.ejemplo_var = tk.StringVar()
        ejemplo_combo = ttk.Combobox(parent_frame, textvariable=self.ejemplo_var, 
                                    values=["Variables", "Listas", "Funciones", "Clases", "Bucles"])
        ejemplo_combo.pack(fill=tk.X, pady=(0, 10))
        ejemplo_combo.bind('<<ComboboxSelected>>', self.cargar_ejemplo_sintaxis)
        
        # Área de código de ejemplo
        self.ejemplo_text = tk.Text(parent_frame, height=8, font=('Courier', 10))
        self.ejemplo_text.pack(fill=tk.X, pady=(0, 10))
        
        # Botón para ejecutar ejemplo
        btn_ejecutar_ejemplo = ttk.Button(parent_frame,
                                         text="Ejecutar Ejemplo",
                                         command=self.ejecutar_ejemplo_sintaxis)
        btn_ejecutar_ejemplo.pack()
        
        # Cargar primer ejemplo
        ejemplo_combo.set("Variables")
        self.cargar_ejemplo_sintaxis(None)
    
    def cargar_ejemplo_sintaxis(self, event):
        """Carga el ejemplo de sintaxis seleccionado"""
        ejemplos = {
            "Variables": """# Variables en Python
nombre = "Python"
version = 3.11
es_genial = True

print(f"Lenguaje: {nombre}")
print(f"Versión: {version}")
print(f"Es genial: {es_genial}")""",
            
            "Listas": """# Listas en Python
frutas = ["manzana", "banana", "naranja"]
numeros = [1, 2, 3, 4, 5]

print("Frutas:", frutas)
print("Primera fruta:", frutas[0])
print("Números:", numeros)

# Agregar elemento
frutas.append("uva")
print("Frutas después de agregar:", frutas)""",
            
            "Funciones": """# Funciones en Python
def saludar(nombre):
    return f"¡Hola, {nombre}!"

def sumar(a, b):
    return a + b

# Usar las funciones
mensaje = saludar("Programador")
resultado = sumar(5, 3)

print(mensaje)
print(f"5 + 3 = {resultado}")""",
            
            "Clases": """# Clases en Python
class Persona:
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad
    
    def presentarse(self):
        return f"Hola, soy {self.nombre} y tengo {self.edad} años"

# Crear una persona
persona = Persona("Ana", 25)
print(persona.presentarse())""",
            
            "Bucles": """# Bucles en Python
print("Bucle for con lista:")
colores = ["rojo", "verde", "azul"]
for color in colores:
    print(f"- {color}")

print("\\nBucle for con rango:")
for i in range(1, 6):
    print(f"Número: {i}")

print("\\nBucle while:")
contador = 0
while contador < 3:
    print(f"Vuelta {contador + 1}")
    contador += 1"""
        }
        
        ejemplo_seleccionado = self.ejemplo_var.get()
        if ejemplo_seleccionado in ejemplos:
            self.ejemplo_text.delete("1.0", tk.END)
            self.ejemplo_text.insert(tk.END, ejemplos[ejemplo_seleccionado])
    
    def ejecutar_ejemplo_sintaxis(self):
        """Ejecuta el ejemplo de sintaxis actual"""
        try:
            codigo = self.ejemplo_text.get("1.0", tk.END).strip()
            
            # Crear ventana para mostrar resultado
            resultado_ventana = tk.Toplevel(self.ventana)
            resultado_ventana.title("Resultado del Ejemplo")
            resultado_ventana.geometry("500x300")
            
            resultado_text = tk.Text(resultado_ventana, font=('Courier', 10))
            resultado_text.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)
            
            # Ejecutar código y capturar salida
            import io
            import contextlib
            
            salida = io.StringIO()
            
            with contextlib.redirect_stdout(salida):
                exec(codigo)
            
            resultado = salida.getvalue()
            resultado_text.insert(tk.END, resultado if resultado else "Código ejecutado sin salida")
            
        except Exception as e:
            messagebox.showerror("Error", f"Error en el código: {str(e)}")
    
    def guia_instalacion(self, parent_frame):
        """Muestra una guía de instalación de Python"""
        guia_label = ttk.Label(parent_frame, 
                              text="Guía de Instalación",
                              font=('Arial', 12, 'bold'))
        guia_label.pack(pady=(0, 10))
        
        # Instrucciones paso a paso
        instrucciones = [
            "1. Ve a python.org",
            "2. Descarga la versión más reciente",
            "3. Ejecuta el instalador",
            "4. ¡Importante! Marca 'Add Python to PATH'",
            "5. Abre una terminal y escribe: python --version"
        ]
        
        for instruccion in instrucciones:
            ttk.Label(parent_frame, text=instruccion, font=('Arial', 10)).pack(anchor='w', pady=2)
        
        # Botón para abrir python.org
        btn_python_org = ttk.Button(parent_frame,
                                   text="Ir a python.org",
                                   command=lambda: webbrowser.open("https://python.org"))
        btn_python_org.pack(pady=(10, 0))
    
    def abrir_recursos_externos(self, parent_frame):
        """Muestra y permite abrir recursos de aprendizaje externos"""
        recursos_label = ttk.Label(parent_frame, 
                                  text="Recursos Recomendados",
                                  font=('Arial', 12, 'bold'))
        recursos_label.pack(pady=(0, 10))
        
        recursos = [
            ("Tutorial Oficial de Python", "https://docs.python.org/es/3/tutorial/"),
            ("Python.org para Principiantes", "https://www.python.org/about/gettingstarted/"),
            ("Codecademy Python", "https://www.codecademy.com/learn/learn-python-3"),
            ("Real Python", "https://realpython.com/"),
            ("Automate the Boring Stuff", "https://automatetheboringstuff.com/"),
        ]
        
        for nombre, url in recursos:
            btn_recurso = ttk.Button(parent_frame,
                                   text=nombre,
                                   command=lambda u=url: webbrowser.open(u))
            btn_recurso.pack(fill=tk.X, pady=2)
    
    def conectar_comunidad(self, parent_frame):
        """Muestra información para conectar con la comunidad Python"""
        comunidad_label = ttk.Label(parent_frame, 
                                   text="Únete a la Comunidad",
                                   font=('Arial', 12, 'bold'))
        comunidad_label.pack(pady=(0, 10))
        
        comunidades = [
            ("Python Software Foundation", "https://www.python.org/psf/"),
            ("Reddit r/Python", "https://reddit.com/r/python"),
            ("Python Discord", "https://discord.gg/python"),
            ("Stack Overflow Python", "https://stackoverflow.com/questions/tagged/python"),
            ("Twitter #Python", "https://twitter.com/hashtag/python"),
        ]
        
        for nombre, url in comunidades:
            btn_comunidad = ttk.Button(parent_frame,
                                     text=nombre,
                                     command=lambda u=url: webbrowser.open(u))
            btn_comunidad.pack(fill=tk.X, pady=2)
    
    def get_que_es_python_info(self):
        """Información sobre qué es Python"""
        return """¿QUÉ ES PYTHON?

Python es un lenguaje de programación de alto nivel, interpretado y de propósito general. Fue diseñado para ser fácil de leer y escribir, lo que lo convierte en una excelente opción tanto para principiantes como para programadores experimentados.

CARACTERÍSTICAS PRINCIPALES:

• FÁCIL DE APRENDER: Su sintaxis es clara y sencilla, similar al inglés natural
• INTERPRETADO: No necesitas compilar el código antes de ejecutarlo
• MULTIPLATAFORMA: Funciona en Windows, Mac, Linux y más
• OPEN SOURCE: Es gratuito y su código fuente está disponible para todos
• TIPADO DINÁMICO: No necesitas declarar el tipo de las variables
• ORIENTADO A OBJETOS: Soporta programación orientada a objetos

FILOSOFÍA DE PYTHON:
"La legibilidad cuenta" - Python fue diseñado para que el código sea fácil de leer y entender.

NOMBRE CURIOSO:
¿Sabías que Python recibió su nombre del grupo de comedia británico "Monty Python"? Su creador, Guido van Rossum, era un gran fan del grupo.

Python se ha convertido en uno de los lenguajes más populares del mundo gracias a su simplicidad y versatilidad. Es usado por gigantes tecnológicos como Google, YouTube, Instagram, Netflix y muchos más."""

    def get_historia_info(self):
        """Información sobre la historia de Python"""
        return """HISTORIA DE PYTHON

LOS INICIOS (1989-1991)
Python nació en diciembre de 1989, cuando Guido van Rossum comenzó a trabajar en él en el Centro de Matemáticas e Informática (CWI) en Países Bajos. Guido quería crear un sucesor del lenguaje ABC que fuera más poderoso y fácil de usar.

PRIMERA VERSIÓN PÚBLICA (1991)
En febrero de 1991, Guido publicó la primera versión de Python (0.9.0) en el grupo de noticias alt.sources. Ya incluía clases con herencia, manejo de excepciones, funciones y tipos de datos como listas y diccionarios.

EVOLUCIÓN TEMPRANA (1994-2000)
• Python 1.0 (1994): Incluyó programación funcional con lambda, map, filter y reduce
• Python 1.4 (1996): Agregó argumentos con palabras clave
• Python 1.5 (1997): Mejoró el rendimiento significativamente

LA ERA MODERNA (2000-2008)
• Python 2.0 (2000): Introdujo las comprensiones de lista y el recolector de basura
• Python 2.2 (2001): Unificó tipos y clases
• Python 2.7 (2010): La última versión de Python 2

LA GRAN TRANSICIÓN (2008-2020)
• Python 3.0 (2008): Grandes cambios para mejorar el lenguaje, no compatible con Python 2
• 2020: Python 2 llegó oficialmente al final de su vida útil
• La transición de Python 2 a Python 3 tomó más de 10 años

PYTHON HOY (2020-presente)
Python se ha convertido en el lenguaje de programación más popular del mundo, especialmente en:
• Ciencia de datos e inteligencia artificial
• Desarrollo web
• Automatización y scripting
• Educación en programación

El "Benevolent Dictator For Life" (BDFL) Guido van Rossum se retiró de su rol de liderazgo en 2018, y ahora Python es dirigido por un consejo directivo."""

    def get_ventajas_info(self):
        """Información sobre las ventajas de Python"""
        return """VENTAJAS DE PYTHON

• FACILIDAD DE APRENDIZAJE
• Sintaxis limpia y legible, similar al inglés
• Menos líneas de código que otros lenguajes
• Excelente para principiantes en programación
• Curva de aprendizaje suave

• PRODUCTIVIDAD
• Desarrollo rápido de aplicaciones
• Menos tiempo escribiendo código repetitivo
• Enfoque en resolver problemas, no en sintaxis compleja
• Prototipado rápido de ideas

• BIBLIOTECA ESTÁNDAR EXTENSA
• "Batteries included" - viene con muchas herramientas integradas
• Módulos para casi cualquier tarea común
• No necesitas instalar librerías externas para tareas básicas

• ECOSISTEMA RICO
• PyPI (Python Package Index) con más de 400,000 paquetes
• Librerías especializadas para todo tipo de aplicaciones
• Comunidad activa que contribuye constantemente

• MULTIPLATAFORMA
• Funciona en Windows, macOS, Linux
• El mismo código funciona en diferentes sistemas operativos
• Ideal para equipos con sistemas mixtos

• INTERPRETADO E INTERACTIVO
• No necesitas compilar antes de ejecutar
• Prueba código línea por línea en el intérprete
• Depuración más fácil y rápida
• Ideal para experimentación y aprendizaje

• VERSÁTIL
• Desarrollo web, ciencia de datos, IA, automatización
• Desde scripts simples hasta aplicaciones empresariales
• Backend, frontend, desktop, mobile, IoT

• GRATUITO Y OPEN SOURCE
• Completamente gratis para usar
• Código fuente disponible
• Transparencia total en su funcionamiento
• Puedes contribuir al desarrollo del lenguaje

• GRAN COMUNIDAD
• Millones de desarrolladores en todo el mundo
• Abundante documentación y tutoriales
• Foros activos y ayuda rápida
• Conferencias y eventos regulares (PyCon)

• RESPALDO CORPORATIVO
• Usado por Google, Netflix, Instagram, Spotify
• Inversión continua en mejoras
• Garantía de continuidad y evolución"""

    def get_aplicaciones_info(self):
        """Información sobre aplicaciones de Python"""
        return """APLICACIONES DE PYTHON

DESARROLLO WEB
Python es excelente para crear sitios web y aplicaciones web:
• Django: Framework completo para aplicaciones web robustas
• Flask: Framework ligero y flexible
• FastAPI: Framework moderno para APIs rápidas
• Usado por: YouTube, Instagram, Pinterest, Mozilla

CIENCIA DE DATOS Y ANÁLISIS
Python es el líder indiscutible en análisis de datos:
• NumPy: Computación numérica
• Pandas: Manipulación y análisis de datos
• Matplotlib/Seaborn: Visualización de datos
• Jupyter Notebooks: Análisis interactivo
• Usado por: Netflix (recomendaciones), Uber (análisis de datos)

INTELIGENCIA ARTIFICIAL Y MACHINE LEARNING
Python domina el mundo de la IA:
• TensorFlow: Framework de Google para deep learning
• PyTorch: Framework de Facebook para investigación en IA
• Scikit-learn: Machine learning tradicional
• OpenCV: Visión por computadora
• Usado por: Tesla (autopilot), Google (búsqueda), Amazon (Alexa)

INVESTIGACIÓN CIENTÍFICA
Python es muy popular en la comunidad científica:
• SciPy: Algoritmos científicos
• Biopython: Bioinformática
• Astropy: Astronomía
• Usado por: NASA, CERN, universidades de todo el mundo

DESARROLLO DE VIDEOJUEGOS
Aunque no es el más común, Python se usa en juegos:
• Pygame: Framework para juegos 2D
• Panda3D: Motor 3D
• Usado por: Civilization IV, Battlefield 2

FINANZAS Y TRADING
Python es muy popular en el sector financiero:
• Análisis de riesgo
• Trading algorítmico
• Análisis de mercados
• Usado por: Goldman Sachs, JPMorgan, Bloomberg

AUTOMATIZACIÓN EMPRESARIAL
Python automatiza tareas repetitivas:
• Scripts de automatización
• Procesamiento de archivos
• Integración de sistemas
• Scraping web
• Usado por: empresas de todos los tamaños

APLICACIONES DE ESCRITORIO
Python puede crear aplicaciones con interfaz gráfica:
• Tkinter: Interfaz básica incluida con Python
• PyQt/PySide: Interfaces profesionales
• Kivy: Aplicaciones multiplataforma
• Usado por: Dropbox, BitTorrent

CLOUD Y DEVOPS
Python es esencial en infraestructura moderna:
• Automatización de servidores
• Orchestración de contenedores
• Monitoreo de sistemas
• Usado por: Google Cloud, AWS, OpenStack

INTERNET DE LAS COSAS (IoT)
Python funciona en dispositivos pequeños:
• Raspberry Pi
• MicroPython para microcontroladores
• Automatización del hogar
• Sensores y robótica"""

    def get_sintaxis_info(self):
        """Información sobre sintaxis básica de Python"""
        return """SINTAXIS BÁSICA DE PYTHON

• INDENTACIÓN
Python usa indentación (espacios o tabs) para definir bloques de código:

```python
if True:
    print("Esto está dentro del if")
    print("Esto también")
print("Esto está fuera del if")
```

• VARIABLES
No necesitas declarar el tipo de variable:

```python
nombre = "Juan"          # String
edad = 25               # Integer  
altura = 1.75           # Float
es_estudiante = True    # Boolean
```

• COMENTARIOS
Usa # para comentarios de una línea:

```python
# Esto es un comentario
print("Hola")  # Comentario al final de línea
```

• FUNCIONES
Usa 'def' para definir funciones:

```python
def saludar(nombre):
    return f"Hola, {nombre}!"

mensaje = saludar("Ana")
```

• LISTAS
Colecciones ordenadas de elementos:

```python
frutas = ["manzana", "banana", "naranja"]
numeros = [1, 2, 3, 4, 5]
mixta = [1, "texto", True, 3.14]
```

• DICCIONARIOS
Pares clave-valor:

```python
persona = {
    "nombre": "Juan",
    "edad": 30,
    "ciudad": "Madrid"
}
```

• BUCLES
For loop:
```python
for fruta in frutas:
    print(fruta)

for i in range(5):
    print(i)
```

While loop:
```python
contador = 0
while contador < 5:
    print(contador)
    contador += 1
```

• CONDICIONALES
```python
if edad >= 18:
    print("Es mayor de edad")
elif edad >= 13:
    print("Es adolescente")
else:
    print("Es niño")
```

• CLASES
```python
class Persona:
    def __init__(self, nombre):
        self.nombre = nombre
    
    def saludar(self):
        return f"Hola, soy {self.nombre}"
```

• MANEJO DE EXCEPCIONES
```python
try:
    numero = int(input("Ingresa un número: "))
    resultado = 10 / numero
except ValueError:
    print("No es un número válido")
except ZeroDivisionError:
    print("No se puede dividir por cero")
```

• IMPORTAR MÓDULOS
```python
import math
from datetime import datetime
import requests as req
```

PRINCIPIOS DE SINTAXIS PYTHON:
• Simple es mejor que complejo
• La legibilidad cuenta
• Debe haber una forma obvia de hacerlo
• Hermoso es mejor que feo"""

    def get_primeros_pasos_info(self):
        """Información sobre primeros pasos en Python"""
        return """PRIMEROS PASOS EN PYTHON

PASO 1: INSTALACIÓN
1. Ve a python.org
2. Descarga la versión más reciente (Python 3.x)
3. Durante la instalación, marca "Add Python to PATH"
4. Verifica la instalación abriendo terminal y escribiendo: python --version

PASO 2: ELIGE UN EDITOR
Para principiantes:
• IDLE (incluido con Python)
• Thonny (perfecto para principiantes)
• VS Code (con extensión de Python)

Para nivel intermedio/avanzado:
• PyCharm
• Visual Studio Code
• Sublime Text
• Atom

PASO 3: TU PRIMER PROGRAMA
Crea un archivo llamado "hola.py" y escribe:

```python
print("¡Hola, mundo!")
nombre = input("¿Cómo te llamas? ")
print(f"¡Hola, {nombre}! Bienvenido a Python")
```

Ejecuta con: python hola.py

PASO 4: CONCEPTOS BÁSICOS A APRENDER
1. Variables y tipos de datos
2. Operadores (matemáticos, lógicos)
3. Estructuras de control (if, for, while)
4. Funciones
5. Listas y diccionarios
6. Clases y objetos

PASO 5: PROYECTOS PARA PRINCIPIANTES
• Calculadora simple
• Juego de adivinanza de números
• Lista de tareas (To-Do List)
• Conversor de unidades
• Analizador de texto simple

PASO 6: RECURSOS DE APRENDIZAJE
• Tutorial oficial de Python
• Python.org para principiantes
• Codecademy Python
• Real Python
• YouTube: canales como "Programación ATS"

PASO 7: INSTALA PAQUETES ÚTILES
Aprende a usar pip (gestor de paquetes):

```bash
pip install requests    # Para hacer peticiones web
pip install matplotlib  # Para gráficos
pip install pandas     # Para análisis de datos
```

CONSEJOS PARA PRINCIPIANTES:
• Practica todos los días, aunque sean 15 minutos
• No tengas miedo de cometer errores
• Usa la documentación oficial
• Únete a comunidades de Python
• Haz proyectos reales, no solo ejercicios
• Lee código de otros programadores

PASO 8: HERRAMIENTAS IMPORTANTES
• pip: Gestor de paquetes
• virtual environments: Ambientes aislados
• Git: Control de versiones
• GitHub: Repositorio de código

RUTA DE APRENDIZAJE SUGERIDA:
1. Semana 1-2: Sintaxis básica y variables
2. Semana 3-4: Estructuras de control
3. Semana 5-6: Funciones y módulos
4. Semana 7-8: Clases y objetos
5. Semana 9-10: Manejo de archivos y excepciones
6. Semana 11-12: Librerías estándar
7. Semana 13+: Especialización (web, data, etc.)"""

    def get_recursos_info(self):
        """Información sobre recursos de aprendizaje"""
        return """RECURSOS DE APRENDIZAJE DE PYTHON

DOCUMENTACIÓN OFICIAL
• python.org - La fuente más confiable
• Tutorial oficial en español
• Documentación de librerías estándar
• PEPs (Python Enhancement Proposals) para entender la evolución

CURSOS ONLINE GRATUITOS
• Codecademy Python Course
• Python.org para principiantes
• FreeCodeCamp Python
• edX: Introduction to Computer Science and Programming Using Python (MIT)
• Coursera: Python for Everybody (Universidad de Michigan)

LIBROS RECOMENDADOS

Para Principiantes:
• "Automate the Boring Stuff with Python" - Al Sweigart
• "Python Crash Course" - Eric Matthes
• "Learn Python the Hard Way" - Zed Shaw
• "Think Python" - Allen Downey

Para Nivel Intermedio:
• "Fluent Python" - Luciano Ramalho
• "Effective Python" - Brett Slatkin
• "Python Tricks" - Dan Bader

Para Especialización:
• "Data Science from Scratch" - Joel Grus
• "Flask Web Development" - Miguel Grinberg
• "Deep Learning with Python" - François Chollet

CANALES DE YOUTUBE
En Español:
• Programación ATS
• Píldoras Informáticas
• MoureDev
• La Geekipedia De Ernesto

En Inglés:
• Corey Schafer
• Real Python
• sentdex
• Tech With Tim

SITIOS WEB Y PLATAFORMAS
• Real Python - Tutoriales de alta calidad
• Python Weekly - Newsletter semanal
• Planet Python - Agregador de blogs
• Stack Overflow - Para resolver dudas
• GitHub - Código fuente y proyectos

PLATAFORMAS DE PRÁCTICA
• HackerRank - Problemas de programación
• LeetCode - Algoritmos y estructuras de datos
• Codewars - Desafíos de código (kata)
• Project Euler - Problemas matemáticos
• Advent of Code - Desafío anual de programación

APRENDIZAJE INTERACTIVO
• Python Tutor - Visualiza la ejecución del código
• Repl.it - IDE online
• Jupyter Notebooks - Para experimentación
• Google Colab - Notebooks gratuitos en la nube

COMUNIDADES
• Reddit r/Python
• Python Discord
• Stack Overflow (tag: python)
• Python Forum
• LinkedIn grupos de Python

APLICACIONES MÓVILES
• SoloLearn
• Programming Hero
• Mimo
• Enki

CERTIFICACIONES
• Python Institute (PCAP, PCPP)
• Microsoft Python Certification
• Google Python Certification

PROYECTOS PRÁCTICOS
• Automatización de tareas
• Scraping web
• API REST con Flask/Django
• Análisis de datos con Pandas
• Chatbot simple
• Juegos con Pygame

CONSEJOS PARA MAXIMIZAR EL APRENDIZAJE:
• Combina teoría con práctica
• Únete a grupos de estudio
• Contribuye a proyectos open source
• Enseña lo que aprendes
• Participa en hackathons
• Mantente actualizado con Python Weekly

RECURSOS COMPLETAMENTE GRATUITOS:
• Documentación oficial de Python
• Python.org tutorial
• FreeCodeCamp
• CS50x (Harvard)
• Automate the Boring Stuff (disponible online)
• Real Python (algunos artículos gratis)

La clave está en la consistencia: dedica tiempo regularmente, practica con proyectos reales y no tengas miedo de experimentar."""

    def get_comunidad_info(self):
        """Información sobre la comunidad Python"""
        return """COMUNIDAD PYTHON

UNA COMUNIDAD GLOBAL
La comunidad Python es una de las más grandes y acogedoras del mundo de la programación, con millones de desarrolladores en más de 200 países. Se caracteriza por su diversidad, inclusión y espíritu colaborativo.

CÓDIGO DE CONDUCTA
La comunidad Python sigue un código de conducta basado en:
• Respeto mutuo
• Inclusión y diversidad
• Colaboración constructiva
• Tolerancia cero al acoso
• Ambiente acogedor para principiantes

PYTHON SOFTWARE FOUNDATION (PSF)
• Organización sin fines de lucro que dirige Python
• Promueve el desarrollo del lenguaje
• Organiza conferencias y eventos
• Proporciona becas y subvenciones
• Mantiene la infraestructura de Python

EVENTOS Y CONFERENCIAS

Conferencias Principales:
• PyCon US - La conferencia Python más grande
• PyCon Europa - Conferencia europea anual
• PyCon Latinoamérica - Para la comunidad hispana
• PyCon Australia, Asia, África...

Eventos Locales:
• Python meetups en ciudades de todo el mundo
• Workshops y talleres
• Hackathons temáticos
• Python Ladies meetups

PLATAFORMAS DE COMUNICACIÓN

Forums y Sitios:
• Python Forum - Discusiones oficiales
• Reddit r/Python - 900k+ miembros
• Stack Overflow - Preguntas y respuestas
• Python Discourse

Chat y Mensajería:
• Python Discord - Chat en tiempo real
• IRC #python en Freenode
• Telegram grupos regionales
• Slack workspaces especializados

INICIATIVAS DE DIVERSIDAD

PyLadies:
• Comunidad internacional de mujeres en Python
• Talleres y eventos exclusivos
• Mentorías y networking
• Presente en más de 100 ciudades

Otras Iniciativas:
• Django Girls - Workshops de programación web
• Python en Español - Comunidad hispanohablante
• Black Python Devs - Desarrolladores afroamericanos
• Queer Python - Comunidad LGBTQ+

CONTRIBUCIONES OPEN SOURCE

Formas de Contribuir:
• Reportar bugs en GitHub
• Escribir documentación
• Traducir contenido
• Contribuir código a proyectos
• Crear y mantener paquetes PyPI

Proyectos Populares:
• CPython (el intérprete principal)
• Django, Flask (frameworks web)
• NumPy, Pandas (ciencia de datos)
• Requests, Beautiful Soup (web scraping)

RECURSOS COMUNITARIOS

Educación:
• Real Python - Tutoriales premium
• Python Weekly - Newsletter
• Planet Python - Agregador de blogs
• Talk Python To Me - Podcast popular

Desarrollo:
• PyPI - 400,000+ paquetes
• GitHub - Millones de repositorios Python
• Read the Docs - Documentación gratuita
• Travis CI/GitHub Actions - Integración continua

RECONOCIMIENTOS

Distinguished Service Awards:
• Reconoce contribuciones excepcionales
• Otorgado por la PSF anualmente
• Incluye desarrolladores, educadores, organizadores

Community Awards:
• Python Community Service Awards
• Recognition para voluntarios
• Destacar trabajo no reconocido

PROGRAMAS DE MENTORÍA

Python Mentors:
• Conecta principiantes con expertos
• Mentorías gratuitas
• Guía personalizada de carrera

Google Summer of Code:
• Programa de verano para estudiantes
• Trabajo remunerado en proyectos open source
• Mentores experimentados

COMUNIDADES REGIONALES

América Latina:
• Python Argentina, Brasil, México
• PyCon Latinoamérica
• Grupos de Telegram y WhatsApp

Europa:
• EuroPython Society
• Python España, Italia, Francia
• European Python conferences

Asia-Pacífico:
• PyCon Australia, Japón, India
• Python Taiwan, Singapur
• Growing tech communities

CÓMO UNIRSE A LA COMUNIDAD

Para Principiantes:
1. Únete a foros locales y online
2. Asiste a meetups en tu ciudad
3. Participa en Discord/Reddit
4. Haz preguntas en Stack Overflow
5. Sigue desarrolladores en Twitter

Para Contribuir:
1. Encuentra un proyecto que te interese
2. Lee las guías de contribución
3. Empieza con issues marcados como "good first issue"
4. Participa en sprints de desarrollo
5. Ofrece ayuda en documentación

BENEFICIOS DE PARTICIPAR

Profesionales:
• Networking con otros desarrolladores
• Oportunidades de trabajo
• Mejora de habilidades técnicas
• Reconocimiento en la industria

Personales:
• Amistades duraderas
• Crecimiento personal
• Satisfacción de ayudar
• Acceso a conocimiento exclusivo

La comunidad Python no es solo sobre código - es sobre personas que comparten la pasión por la programación y quieren hacer del mundo un lugar mejor a través de la tecnología."""

    def cerrar_ventana(self):
        """Cierra la ventana"""
        if self.parent:
            self.ventana.destroy()
        else:
            self.ventana.quit()


def crear_ventana_introduccion_python(parent=None):
    """Función para crear la ventana de introducción a Python"""
    return IntroduccionPython(parent)


if __name__ == "__main__":
    # Para testing independiente
    root = tk.Tk()
    root.withdraw()  # Ocultar ventana principal
    app = IntroduccionPython()
    root.mainloop()