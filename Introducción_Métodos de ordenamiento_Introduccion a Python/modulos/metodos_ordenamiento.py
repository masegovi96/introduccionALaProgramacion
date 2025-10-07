"""
Módulo de Métodos de Ordenamiento
Contiene implementaciones y visualizaciones de algoritmos de ordenamiento
"""

import tkinter as tk
from tkinter import ttk, messagebox
import time
import random
import threading


class MetodosOrdenamiento:
    """Clase principal para la ventana de métodos de ordenamiento"""
    
    def __init__(self, parent=None):
        """Inicializa la ventana de métodos de ordenamiento"""
        self.parent = parent
        self.ventana = tk.Toplevel(parent) if parent else tk.Tk()
        self.setup_window()
        self.create_main_interface()
        
        # Variables para las animaciones
        self.array_original = []
        self.array_actual = []
        self.animacion_activa = False
        self.velocidad_animacion = 800  # milliseconds (más lento)
        self.paso_actual = ""
        self.etiqueta_paso = None
        
    def setup_window(self):
        """Configura la ventana principal"""
        self.ventana.title("Métodos de Ordenamiento")
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
        """Crea la interfaz principal con los botones de algoritmos"""
        # Frame principal
        main_frame = ttk.Frame(self.ventana, padding="20")
        main_frame.pack(fill=tk.BOTH, expand=True)
        
        # Título
        title_label = ttk.Label(main_frame, 
                               text="Métodos de Ordenamiento",
                               font=('Arial', 24, 'bold'),
                               foreground='#2c3e50')
        title_label.pack(pady=(0, 20))
        
        # Subtítulo
        subtitle_label = ttk.Label(main_frame,
                                  text="Selecciona un algoritmo de ordenamiento para aprender:",
                                  font=('Arial', 12),
                                  foreground='#34495e')
        subtitle_label.pack(pady=(0, 30))
        
        # Frame para botones de algoritmos
        algoritmos_frame = ttk.Frame(main_frame)
        algoritmos_frame.pack(fill=tk.BOTH, expand=True, pady=20)
        
        # Configurar grid
        for i in range(3):
            algoritmos_frame.columnconfigure(i, weight=1)
        for i in range(2):
            algoritmos_frame.rowconfigure(i, weight=1)
        
        # Definir algoritmos (sin emojis)
        algoritmos = [
            ("Bubble Sort", self.mostrar_bubble_sort),
            ("Insertion Sort", self.mostrar_insertion_sort),
            ("Selection Sort", self.mostrar_selection_sort),
            ("Merge Sort", self.mostrar_merge_sort),
            ("Quick Sort", self.mostrar_quick_sort)
        ]
        
        # Crear botones para cada algoritmo
        for i, (nombre, comando) in enumerate(algoritmos):
            btn = ttk.Button(algoritmos_frame,
                           text=nombre,
                           command=comando,
                           style='Algoritmo.TButton')
            
            row = i // 3
            col = i % 3
            btn.grid(row=row, column=col, padx=10, pady=10, sticky='nsew')
        
        # Configurar estilo para botones
        style = ttk.Style()
        style.configure('Algoritmo.TButton',
                       font=('Arial', 12, 'bold'),
                       padding=(15, 10))
    
    def mostrar_bubble_sort(self):
        """Muestra la explicación y animación de Bubble Sort"""
        self.mostrar_algoritmo("Bubble Sort", self.get_bubble_sort_info(), self.animar_bubble_sort)
    
    def mostrar_insertion_sort(self):
        """Muestra la explicación y animación de Insertion Sort"""
        self.mostrar_algoritmo("Insertion Sort", self.get_insertion_sort_info(), self.animar_insertion_sort)
    
    def mostrar_selection_sort(self):
        """Muestra la explicación y animación de Selection Sort"""
        self.mostrar_algoritmo("Selection Sort", self.get_selection_sort_info(), self.animar_selection_sort)
    
    def mostrar_merge_sort(self):
        """Muestra la explicación y animación de Merge Sort"""
        self.mostrar_algoritmo("Merge Sort", self.get_merge_sort_info(), self.animar_merge_sort)
    
    def mostrar_quick_sort(self):
        """Muestra la explicación y animación de Quick Sort"""
        self.mostrar_algoritmo("Quick Sort", self.get_quick_sort_info(), self.animar_quick_sort)
    
    def mostrar_algoritmo(self, nombre, info, funcion_animacion):
        """Muestra la ventana de explicación de un algoritmo específico"""
        # Crear nueva ventana
        ventana_algo = tk.Toplevel(self.ventana)
        ventana_algo.title(f"Algoritmo: {nombre}")
        ventana_algo.geometry("1000x800")
        ventana_algo.configure(bg='#f8f9fa')
        
        # Frame principal con scroll
        canvas = tk.Canvas(ventana_algo, bg='#f8f9fa')
        scrollbar = ttk.Scrollbar(ventana_algo, orient="vertical", command=canvas.yview)
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
        
        # Título del algoritmo
        title_label = ttk.Label(scrollable_frame,
                               text=f"{nombre}",
                               font=('Arial', 20, 'bold'),
                               foreground='#2c3e50')
        title_label.pack(pady=(0, 20))
        
        # Información del algoritmo
        info_frame = ttk.LabelFrame(scrollable_frame, text="¿Cómo funciona este algoritmo?", padding="15")
        info_frame.pack(fill=tk.X, pady=(0, 20))
        
        info_text = tk.Text(info_frame, height=12, wrap=tk.WORD, font=('Arial', 11))
        info_text.insert(tk.END, info)
        info_text.config(state=tk.DISABLED)
        info_text.pack(fill=tk.X)
        
        # Frame para mostrar el paso actual
        paso_frame = ttk.LabelFrame(scrollable_frame, text="Paso Actual", padding="15")
        paso_frame.pack(fill=tk.X, pady=(0, 20))
        
        self.etiqueta_paso = ttk.Label(paso_frame,
                                      text="Presiona 'Iniciar Animación' para comenzar",
                                      font=('Arial', 12, 'bold'),
                                      foreground='#e74c3c')
        self.etiqueta_paso.pack()
        
        # Frame para animación
        animacion_frame = ttk.LabelFrame(scrollable_frame, text="Visualización", padding="15")
        animacion_frame.pack(fill=tk.X, pady=(0, 20))
        
        # Canvas para la animación
        self.canvas_animacion = tk.Canvas(animacion_frame, height=200, bg='white')
        self.canvas_animacion.pack(fill=tk.X, pady=(0, 10))
        
        # Frame para controles de animación
        controles_frame = ttk.Frame(animacion_frame)
        controles_frame.pack(fill=tk.X)
        
        # Botones de control
        btn_generar = ttk.Button(controles_frame,
                                text="Generar Números Aleatorios",
                                command=self.generar_array_aleatorio)
        btn_generar.pack(side=tk.LEFT, padx=(0, 10))
        
        btn_animar = ttk.Button(controles_frame,
                               text="Iniciar Animación",
                               command=lambda: self.iniciar_animacion(funcion_animacion))
        btn_animar.pack(side=tk.LEFT, padx=(0, 10))
        
        btn_parar = ttk.Button(controles_frame,
                              text="Parar",
                              command=self.parar_animacion)
        btn_parar.pack(side=tk.LEFT, padx=(0, 10))
        
        # Control de velocidad
        ttk.Label(controles_frame, text="Velocidad:").pack(side=tk.LEFT, padx=(20, 5))
        self.velocidad_scale = ttk.Scale(controles_frame, from_=500, to=2000, orient=tk.HORIZONTAL,
                                        value=self.velocidad_animacion, length=100)
        self.velocidad_scale.pack(side=tk.LEFT, padx=(0, 10))
        self.velocidad_scale.bind("<Motion>", self.actualizar_velocidad)
        
        # Botón de cerrar
        btn_cerrar = ttk.Button(scrollable_frame,
                               text="Volver a Algoritmos",
                               command=ventana_algo.destroy)
        btn_cerrar.pack(pady=(20, 0))
        
        # Generar array inicial
        self.generar_array_aleatorio()
    
    def generar_array_aleatorio(self):
        """Genera un array aleatorio para las animaciones"""
        self.array_original = random.sample(range(10, 100), 12)
        self.array_actual = self.array_original.copy()
        self.dibujar_array()
    
    def dibujar_array(self, comparando=None, intercambiando=None):
        """Dibuja el array en el canvas"""
        if not hasattr(self, 'canvas_animacion'):
            return
            
        self.canvas_animacion.delete("all")
        
        if not self.array_actual:
            return
        
        canvas_width = self.canvas_animacion.winfo_width()
        canvas_height = self.canvas_animacion.winfo_height()
        
        if canvas_width <= 1:  # Canvas no inicializado
            self.canvas_animacion.after(100, self.dibujar_array)
            return
        
        bar_width = canvas_width // len(self.array_actual) - 2
        max_val = max(self.array_actual) if self.array_actual else 1
        
        for i, val in enumerate(self.array_actual):
            x1 = i * (bar_width + 2) + 10
            y1 = canvas_height - 10
            x2 = x1 + bar_width
            y2 = canvas_height - (val / max_val * (canvas_height - 30)) - 10
            
            # Determinar color de la barra
            color = "#3498db"  # Azul por defecto
            if comparando and i in comparando:
                color = "#e74c3c"  # Rojo para comparación
            elif intercambiando and i in intercambiando:
                color = "#2ecc71"  # Verde para intercambio
            
            # Dibujar barra
            self.canvas_animacion.create_rectangle(x1, y1, x2, y2, fill=color, outline="black")
            
            # Dibujar valor
            self.canvas_animacion.create_text((x1 + x2) // 2, y2 - 10, text=str(val), font=('Arial', 9))
    
    def actualizar_paso(self, mensaje):
        """Actualiza el mensaje del paso actual"""
        if self.etiqueta_paso:
            self.etiqueta_paso.config(text=mensaje)
    
    def actualizar_velocidad(self, event):
        """Actualiza la velocidad de animación"""
        self.velocidad_animacion = int(self.velocidad_scale.get())
    
    def iniciar_animacion(self, funcion_animacion):
        """Inicia la animación del algoritmo"""
        if not self.animacion_activa:
            self.animacion_activa = True
            self.array_actual = self.array_original.copy()
            self.actualizar_paso("Preparando animación...")
            threading.Thread(target=funcion_animacion, daemon=True).start()
    
    def parar_animacion(self):
        """Para la animación"""
        self.animacion_activa = False
        self.actualizar_paso("Animación detenida")
    
    def animar_bubble_sort(self):
        """Animación de Bubble Sort con explicaciones paso a paso"""
        arr = self.array_actual.copy()
        n = len(arr)
        
        self.actualizar_paso("Iniciando Bubble Sort...")
        time.sleep(self.velocidad_animacion / 1000)
        
        for i in range(n):
            if not self.animacion_activa:
                break
            
            self.actualizar_paso(f"Vuelta {i + 1}: Buscando el número más grande y llevándolo al final")
            time.sleep(self.velocidad_animacion / 1000)
                
            for j in range(0, n - i - 1):
                if not self.animacion_activa:
                    break
                
                # Mostrar comparación
                self.actualizar_paso(f"Comparando {arr[j]} con {arr[j + 1]}")
                self.canvas_animacion.after(0, lambda: self.dibujar_array(comparando=[j, j + 1]))
                time.sleep(self.velocidad_animacion / 1000)
                
                if arr[j] > arr[j + 1]:
                    # Mostrar intercambio
                    self.actualizar_paso(f"{arr[j]} es mayor que {arr[j + 1]}, los intercambiamos")
                    self.canvas_animacion.after(0, lambda: self.dibujar_array(intercambiando=[j, j + 1]))
                    arr[j], arr[j + 1] = arr[j + 1], arr[j]
                    self.array_actual = arr.copy()
                    time.sleep(self.velocidad_animacion / 1000)
                else:
                    self.actualizar_paso(f"{arr[j]} es menor que {arr[j + 1]}, no los intercambiamos")
                    time.sleep(self.velocidad_animacion / 1000)
            
            self.actualizar_paso(f"El número {arr[n - i - 1]} ya está en su posición final")
            time.sleep(self.velocidad_animacion / 1000)
        
        self.animacion_activa = False
        self.actualizar_paso("¡Lista ordenada! Bubble Sort completado")
        self.canvas_animacion.after(0, self.dibujar_array)
    
    def animar_insertion_sort(self):
        """Animación de Insertion Sort con explicaciones paso a paso"""
        arr = self.array_actual.copy()
        
        self.actualizar_paso("Iniciando Insertion Sort...")
        time.sleep(self.velocidad_animacion / 1000)
        
        for i in range(1, len(arr)):
            if not self.animacion_activa:
                break
                
            key = arr[i]
            j = i - 1
            
            # Mostrar elemento a insertar
            self.actualizar_paso(f"Tomando el número {key} para insertarlo en su lugar correcto")
            self.canvas_animacion.after(0, lambda: self.dibujar_array(comparando=[i]))
            time.sleep(self.velocidad_animacion / 1000)
            
            while j >= 0 and arr[j] > key and self.animacion_activa:
                # Mostrar comparación
                self.actualizar_paso(f"Comparando {key} con {arr[j]}. Como {arr[j]} es mayor, lo movemos a la derecha")
                self.canvas_animacion.after(0, lambda: self.dibujar_array(comparando=[j, j + 1]))
                time.sleep(self.velocidad_animacion / 1000)
                
                arr[j + 1] = arr[j]
                j -= 1
                self.array_actual = arr.copy()
                self.canvas_animacion.after(0, self.dibujar_array)
                time.sleep(self.velocidad_animacion / 1000)
            
            arr[j + 1] = key
            self.array_actual = arr.copy()
            self.actualizar_paso(f"Insertando {key} en su posición correcta")
            self.canvas_animacion.after(0, self.dibujar_array)
            time.sleep(self.velocidad_animacion / 1000)
        
        self.animacion_activa = False
        self.actualizar_paso("¡Lista ordenada! Insertion Sort completado")
    
    def animar_selection_sort(self):
        """Animación de Selection Sort con explicaciones paso a paso"""
        arr = self.array_actual.copy()
        
        self.actualizar_paso("Iniciando Selection Sort...")
        time.sleep(self.velocidad_animacion / 1000)
        
        for i in range(len(arr)):
            if not self.animacion_activa:
                break
                
            min_idx = i
            self.actualizar_paso(f"Vuelta {i + 1}: Buscando el número más pequeño en la lista")
            time.sleep(self.velocidad_animacion / 1000)
            
            for j in range(i + 1, len(arr)):
                if not self.animacion_activa:
                    break
                
                # Mostrar comparación
                self.actualizar_paso(f"Comparando {arr[min_idx]} (actual mínimo) con {arr[j]}")
                self.canvas_animacion.after(0, lambda: self.dibujar_array(comparando=[min_idx, j]))
                time.sleep(self.velocidad_animacion / 1000)
                
                if arr[j] < arr[min_idx]:
                    min_idx = j
                    self.actualizar_paso(f"¡Encontré uno más pequeño! Ahora {arr[j]} es el nuevo mínimo")
                    time.sleep(self.velocidad_animacion / 1000)
            
            # Mostrar intercambio
            if min_idx != i:
                self.actualizar_paso(f"Intercambiando {arr[i]} con {arr[min_idx]} (el más pequeño encontrado)")
                self.canvas_animacion.after(0, lambda: self.dibujar_array(intercambiando=[i, min_idx]))
                arr[i], arr[min_idx] = arr[min_idx], arr[i]
                self.array_actual = arr.copy()
                time.sleep(self.velocidad_animacion / 1000)
            else:
                self.actualizar_paso(f"{arr[i]} ya está en su lugar correcto")
                time.sleep(self.velocidad_animacion / 1000)
        
        self.animacion_activa = False
        self.actualizar_paso("¡Lista ordenada! Selection Sort completado")
        self.canvas_animacion.after(0, self.dibujar_array)
    
    def animar_merge_sort(self):
        """Animación de Merge Sort con explicaciones paso a paso"""
        def merge_sort_recursivo(arr, inicio, fin, nivel=0):
            if not self.animacion_activa or inicio >= fin:
                return
            
            medio = (inicio + fin) // 2
            
            # Mostrar división
            self.actualizar_paso(f"Nivel {nivel + 1}: Dividiendo la lista en partes más pequeñas")
            self.canvas_animacion.after(0, lambda: self.dibujar_array(comparando=list(range(inicio, fin + 1))))
            time.sleep(self.velocidad_animacion / 1000)
            
            merge_sort_recursivo(arr, inicio, medio, nivel + 1)
            merge_sort_recursivo(arr, medio + 1, fin, nivel + 1)
            
            if self.animacion_activa:
                self.actualizar_paso(f"Nivel {nivel + 1}: Juntando las partes ordenadas")
                time.sleep(self.velocidad_animacion / 1000)
                self.merge(arr, inicio, medio, fin)
        
        arr = self.array_actual.copy()
        self.actualizar_paso("Iniciando Merge Sort...")
        time.sleep(self.velocidad_animacion / 1000)
        
        merge_sort_recursivo(arr, 0, len(arr) - 1)
        self.animacion_activa = False
        self.actualizar_paso("¡Lista ordenada! Merge Sort completado")
    
    def merge(self, arr, inicio, medio, fin):
        """Función auxiliar para merge sort con explicaciones"""
        izq = arr[inicio:medio + 1]
        der = arr[medio + 1:fin + 1]
        
        self.actualizar_paso(f"Mezclando dos grupos ordenados: {izq} y {der}")
        time.sleep(self.velocidad_animacion / 1000)
        
        i = j = 0
        k = inicio
        
        while i < len(izq) and j < len(der) and self.animacion_activa:
            self.actualizar_paso(f"Comparando {izq[i]} con {der[j]}")
            self.canvas_animacion.after(0, lambda: self.dibujar_array(comparando=[k]))
            time.sleep(self.velocidad_animacion / 1000)
            
            if izq[i] <= der[j]:
                arr[k] = izq[i]
                self.actualizar_paso(f"Tomando {izq[i]} porque es menor o igual")
                i += 1
            else:
                arr[k] = der[j]
                self.actualizar_paso(f"Tomando {der[j]} porque es menor")
                j += 1
            k += 1
            self.array_actual = arr.copy()
            time.sleep(self.velocidad_animacion / 1000)
        
        while i < len(izq) and self.animacion_activa:
            self.actualizar_paso(f"Copiando el resto: {izq[i]}")
            arr[k] = izq[i]
            i += 1
            k += 1
            self.array_actual = arr.copy()
            time.sleep(self.velocidad_animacion / 1000)
        
        while j < len(der) and self.animacion_activa:
            self.actualizar_paso(f"Copiando el resto: {der[j]}")
            arr[k] = der[j]
            j += 1
            k += 1
            self.array_actual = arr.copy()
            time.sleep(self.velocidad_animacion / 1000)
    
    def animar_quick_sort(self):
        """Animación de Quick Sort con explicaciones paso a paso"""
        def quick_sort_recursivo(arr, bajo, alto, nivel=0):
            if not self.animacion_activa or bajo >= alto:
                return
                
            self.actualizar_paso(f"Nivel {nivel + 1}: Ordenando desde posición {bajo} hasta {alto}")
            time.sleep(self.velocidad_animacion / 1000)
            
            # Mostrar el pivote
            self.actualizar_paso(f"Eligiendo {arr[alto]} como pivote (el último número)")
            self.canvas_animacion.after(0, lambda: self.dibujar_array(comparando=[alto]))
            time.sleep(self.velocidad_animacion / 1000)
            
            pi = self.partition(arr, bajo, alto)
            
            self.actualizar_paso(f"El pivote {arr[pi]} ya está en su lugar final")
            time.sleep(self.velocidad_animacion / 1000)
            
            quick_sort_recursivo(arr, bajo, pi - 1, nivel + 1)
            quick_sort_recursivo(arr, pi + 1, alto, nivel + 1)
        
        arr = self.array_actual.copy()
        self.actualizar_paso("Iniciando Quick Sort...")
        time.sleep(self.velocidad_animacion / 1000)
        
        quick_sort_recursivo(arr, 0, len(arr) - 1)
        self.animacion_activa = False
        self.actualizar_paso("¡Lista ordenada! Quick Sort completado")
    
    def partition(self, arr, bajo, alto):
        """Función de partición para Quick Sort con explicaciones"""
        pivot = arr[alto]
        i = bajo - 1
        
        self.actualizar_paso(f"Organizando números alrededor del pivote {pivot}")
        time.sleep(self.velocidad_animacion / 1000)
        
        for j in range(bajo, alto):
            if not self.animacion_activa:
                break
                
            # Mostrar comparación con pivot
            self.actualizar_paso(f"Comparando {arr[j]} con el pivote {pivot}")
            self.canvas_animacion.after(0, lambda: self.dibujar_array(comparando=[j, alto]))
            time.sleep(self.velocidad_animacion / 1000)
            
            if arr[j] <= pivot:
                i += 1
                if i != j:
                    self.actualizar_paso(f"{arr[j]} es menor o igual al pivote, lo movemos a la izquierda")
                    arr[i], arr[j] = arr[j], arr[i]
                    self.array_actual = arr.copy()
                    self.canvas_animacion.after(0, lambda: self.dibujar_array(intercambiando=[i, j]))
                    time.sleep(self.velocidad_animacion / 1000)
                else:
                    self.actualizar_paso(f"{arr[j]} es menor o igual al pivote, ya está en lugar correcto")
                    time.sleep(self.velocidad_animacion / 1000)
            else:
                self.actualizar_paso(f"{arr[j]} es mayor al pivote, se queda a la derecha")
                time.sleep(self.velocidad_animacion / 1000)
        
        # Poner el pivot en su lugar final
        self.actualizar_paso(f"Poniendo el pivote {pivot} en su posición final")
        arr[i + 1], arr[alto] = arr[alto], arr[i + 1]
        self.array_actual = arr.copy()
        self.canvas_animacion.after(0, lambda: self.dibujar_array(intercambiando=[i + 1, alto]))
        time.sleep(self.velocidad_animacion / 1000)
        
        return i + 1
    
    def get_bubble_sort_info(self):
        """Información sobre Bubble Sort"""
        return """BUBBLE SORT (Ordenamiento Burbuja)

¿QUÉ ES?
Bubble Sort es como ordenar cartas comparando de a pares. Imagínate que tienes una fila de números y quieres ordenarlos de menor a mayor. Este método compara cada número con su vecino y los intercambia si están en el orden incorrecto.

¿CÓMO FUNCIONA?
1. Compara el primer número con el segundo
2. Si el primero es más grande, los intercambia
3. Sigue comparando el segundo con el tercero, y así sucesivamente
4. Al terminar una vuelta completa, el número más grande "burbujea" hasta el final
5. Repite el proceso para encontrar el segundo más grande, tercero, etc.
6. Para cuando ya no necesites hacer intercambios

VENTAJAS:
• Es muy fácil de entender
• No necesita memoria extra
• Funciona bien para listas pequeñas

DESVENTAJAS:
• Es lento para listas grandes
• Hace muchas comparaciones innecesarias

¿CUÁNDO USARLO?
• Para aprender cómo funcionan los algoritmos de ordenamiento
• Cuando tienes pocos números para ordenar
• Cuando quieres algo simple y no te importa la velocidad"""

    def get_insertion_sort_info(self):
        """Información sobre Insertion Sort"""
        return """INSERTION SORT (Ordenamiento por Inserción)

¿QUÉ ES?
Insertion Sort es como ordenar cartas en tu mano. Tomas una carta nueva y la insertas en el lugar correcto entre las cartas que ya tienes ordenadas.

¿CÓMO FUNCIONA?
1. Empiezas asumiendo que el primer número ya está "ordenado"
2. Tomas el segundo número y lo comparas con el primero
3. Lo insertas en la posición correcta (antes o después)
4. Tomas el tercer número y lo insertas en su lugar correcto entre los ya ordenados
5. Sigues así hasta que todos los números estén en su lugar

VENTAJAS:
• Funciona muy bien si la lista ya está casi ordenada
• Es eficiente para listas pequeñas
• Puedes ordenar mientras llegan nuevos números

DESVENTAJAS:
• Es lento para listas grandes
• Tiene que mover muchos números cuando inserta uno nuevo

¿CUÁNDO USARLO?
• Para listas pequeñas (menos de 50 números)
• Cuando los números llegan de a poco y quieres mantenerlos ordenados
• Como parte de otros algoritmos más complejos"""

    def get_selection_sort_info(self):
        """Información sobre Selection Sort"""
        return """SELECTION SORT (Ordenamiento por Selección)

¿QUÉ ES?
Selection Sort es como encontrar el más pequeño de un grupo y ponerlo al principio, luego encontrar el segundo más pequeño y ponerlo en segundo lugar, y así sucesivamente.

¿CÓMO FUNCIONA?
1. Busca el número más pequeño de toda la lista
2. Lo pone en la primera posición (intercambiándolo con lo que esté ahí)
3. Busca el segundo número más pequeño en lo que queda de la lista
4. Lo pone en la segunda posición
5. Sigue así hasta que todos estén ordenados

VENTAJAS:
• Fácil de entender
• Hace pocos intercambios (solo uno por vuelta)
• No necesita memoria extra

DESVENTAJAS:
• Es lento para listas grandes
• Siempre toma el mismo tiempo, aunque la lista ya esté ordenada
• No es estable (puede cambiar el orden de números iguales)

¿CUÁNDO USARLO?
• Cuando intercambiar números es muy costoso
• Para listas pequeñas
• Cuando quieres algo simple y predecible"""

    def get_merge_sort_info(self):
        """Información sobre Merge Sort"""
        return """MERGE SORT (Ordenamiento por Mezcla)

¿QUÉ ES?
Merge Sort usa la estrategia de "divide y vencerás". Es como partir una lista grande en pedazos pequeños, ordenar cada pedazo, y luego juntarlos de manera ordenada.

¿CÓMO FUNCIONA?
1. Divide la lista por la mitad
2. Divide cada mitad por la mitad otra vez
3. Sigue dividiendo hasta que tengas listas de un solo número
4. Ahora empieza a juntar las listas de a pares, pero manteniéndolas ordenadas
5. Sigue juntando hasta que tengas una sola lista completamente ordenada

VENTAJAS:
• Siempre es rápido, sin importar cómo estén los números al principio
• Es estable (mantiene el orden de números iguales)
• Funciona muy bien para listas grandes
• Se puede hacer en paralelo (varios procesadores a la vez)

DESVENTAJAS:
• Necesita memoria extra para las divisiones
• Es más complicado que otros algoritmos
• Para listas pequeñas puede ser más lento que algoritmos simples

¿CUÁNDO USARLO?
• Para listas grandes donde necesitas garantizar velocidad
• Cuando el orden de números iguales es importante
• En sistemas con múltiples procesadores"""

    def get_quick_sort_info(self):
        """Información sobre Quick Sort"""
        return """QUICK SORT (Ordenamiento Rápido)

¿QUÉ ES?
Quick Sort también usa "divide y vencerás", pero de manera diferente. Elige un número como "pivote" y organiza todos los demás números: los menores a la izquierda y los mayores a la derecha.

¿CÓMO FUNCIONA?
1. Elige un número de la lista (el "pivote")
2. Mueve todos los números menores al pivote hacia la izquierda
3. Mueve todos los números mayores al pivote hacia la derecha
4. Ahora el pivote está en su posición final correcta
5. Repite el proceso con los números de la izquierda y los de la derecha
6. Sigue hasta que todos estén ordenados

VENTAJAS:
• Muy rápido en la mayoría de los casos
• No necesita memoria extra (en la versión básica)
• Es el algoritmo favorito de muchos programadores
• Funciona muy bien en la práctica

DESVENTAJAS:
• En el peor caso puede ser lento (si siempre elige mal el pivote)
• No es estable (puede cambiar el orden de números iguales)
• Su velocidad depende de qué pivote elijas

¿CUÁNDO USARLO?
• Para la mayoría de casos cuando necesitas ordenar números
• Cuando la velocidad promedio es más importante que el peor caso
• Es el algoritmo que usan muchas librerías de programación"""

    def cerrar_ventana(self):
        """Cierra la ventana"""
        self.parar_animacion()
        if self.parent:
            self.ventana.destroy()
        else:
            self.ventana.quit()


def crear_ventana_metodos_ordenamiento(parent=None):
    """Función para crear la ventana de métodos de ordenamiento"""
    return MetodosOrdenamiento(parent)


if __name__ == "__main__":
    # Para testing independiente
    root = tk.Tk()
    root.withdraw()  # Ocultar ventana principal
    app = MetodosOrdenamiento()
    root.mainloop()
