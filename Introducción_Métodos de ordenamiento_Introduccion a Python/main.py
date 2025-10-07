import tkinter as tk
from tkinter import ttk, messagebox
import sys
import os

# Agregar la carpeta modulos al path
modulos_path = os.path.join(os.path.dirname(__file__), 'modulos')
if modulos_path not in sys.path:
    sys.path.append(modulos_path)


def abrir_metodos_ordenamiento():
    """Función que se ejecuta al presionar el botón de Métodos de Ordenamiento"""
    try:
        from metodos_ordenamiento import crear_ventana_metodos_ordenamiento  # type: ignore
        crear_ventana_metodos_ordenamiento(root)
        
    except ImportError as e:
        messagebox.showerror("Error", f"No se pudo cargar el módulo de Métodos de Ordenamiento.\nError: {e}")
    except Exception as e:
        messagebox.showerror("Error", f"Error inesperado: {e}")


def abrir_introduccion_programacion():
    """Función que se ejecuta al presionar el botón de Introducción a la Programación"""
    try:
        from introduccion_python import crear_ventana_introduccion_python  # type: ignore
        crear_ventana_introduccion_python(root)
        
    except ImportError as e:
        messagebox.showerror("Error", f"No se pudo cargar el módulo de Introducción a Python.\nError: {e}")
    except Exception as e:
        messagebox.showerror("Error", f"Error inesperado: {e}")


def salir_aplicacion():
    """Cierra la aplicación con confirmación"""
    if messagebox.askokcancel("Salir", "¿Estás seguro de que quieres salir?"):
        root.quit()


def main():
    """Función principal que crea la interfaz"""
    global root
    
    root = tk.Tk()
    root.title("Aplicación Educativa de Python")
    root.geometry("500x400")
    root.resizable(True, True)
    
    root.configure(bg='#f0f0f0')

    root.update_idletasks()
    width = root.winfo_width()
    height = root.winfo_height()
    x = (root.winfo_screenwidth() // 2) - (width // 2)
    y = (root.winfo_screenheight() // 2) - (height // 2)
    root.geometry(f'{width}x{height}+{x}+{y}')
    
    style = ttk.Style()
    style.theme_use('clam')
    
    style.configure('Title.TLabel', 
                   font=('Arial', 20, 'bold'),
                   background='#f0f0f0',
                   foreground='#2c3e50')
    
    style.configure('BigButton.TButton',
                   font=('Arial', 12, 'bold'),
                   padding=(20, 15))
    
    main_frame = ttk.Frame(root, padding="30")
    main_frame.pack(fill=tk.BOTH, expand=True)
    
    title_label = ttk.Label(main_frame, 
                           text="Segundo Parcial",
                           style='Title.TLabel')
    title_label.pack(pady=(0, 30))
    
    subtitle_label = ttk.Label(main_frame,
                              text="Selecciona el módulo que quieres explorar:",
                              font=('Arial', 12),
                              background='#f0f0f0',
                              foreground='#34495e')
    subtitle_label.pack(pady=(0, 40))
    
    buttons_frame = ttk.Frame(main_frame)
    buttons_frame.pack(fill=tk.BOTH, expand=True)
    
    btn_ordenamiento = ttk.Button(buttons_frame,
                                 text="Métodos de Ordenamiento",
                                 style='BigButton.TButton',
                                 command=abrir_metodos_ordenamiento)
    btn_ordenamiento.pack(pady=15, fill=tk.X)
    
    btn_introduccion = ttk.Button(buttons_frame,
                                 text="Introducción a Python",
                                 style='BigButton.TButton',
                                 command=abrir_introduccion_programacion)
    btn_introduccion.pack(pady=15, fill=tk.X)
    
    spacer = ttk.Label(buttons_frame, text="", background='#f0f0f0')
    spacer.pack(pady=20)
    
    info_text = "Aprende Python desde lo básico hasta algoritmos avanzados"
    info_label = ttk.Label(buttons_frame,
                          text=info_text,
                          font=('Arial', 10, 'italic'),
                          background='#f0f0f0',
                          foreground='#7f8c8d')
    info_label.pack(pady=10)
    
    btn_salir = ttk.Button(buttons_frame,
                          text="Salir",
                          command=salir_aplicacion)
    btn_salir.pack(pady=(20, 0))
    
    root.mainloop()


if __name__ == "__main__":
    main()
