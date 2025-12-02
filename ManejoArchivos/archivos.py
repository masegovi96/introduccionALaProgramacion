from io import open
# En Python existen los siguientes modos de lectura y escritura de archivos:
# 'r': Modo de lectura (read) -> Abre un archivo para leerlo. El archivo debe existir, sino existe el programa nos marcará un error.
# 'w': Modo de escritura (write) -> Abre un archivo para escribir en él. Si el archivo ya existe, se sobreescribe. Si no existe, se crea uno nuevo.
# 'a': Modo de anexado (append) -> Abre un archivo para agregar contenido al final del mismo. Si el archivo no existe, se crea uno nuevo.
# 'r+': Modo de lectura y escritura -> Abre un archivo para leer y escribir. Si el archivo no existe se marcará un error.
# 'w+': Modo de escritura y lectura -> Abre un archivo para escribir y leer. Si el archivo no existe, se crea uno nuevo. Sobreescribe el archivo si ya existe.
# 'a+': Modo de anexado y lectura -> Abre un archivo para agregar contenido al final y leerlo. Si el archivo no existe, se crea uno nuevo.

#Apertura de archivo
# open("ruta/archivo.txt", modo)

#Cerrar el archivo
# archivo.close()

# Podemos abrir el archivo haciendo uso de 'with', el cual cierra el archivo de manera automática al finalizar el bloque de código.

# with open("ruta/archivo.txt", modo) as archivo:
#     # Operaciones con el archivo

with open("archivo.txt", "r") as f:
    contenido = f.read() # Leer todo el contenido del archivo, y lo va a almacenar en la variable contenido
print(contenido)

with open("archivo.txt", "r") as f:
    for linea in f:  # Leer el archivo línea por línea
        print(linea.strip())  # Imprimir cada línea sin espacios adicionales

with open("archivo2.txt", "w") as f:
    f.write("Esta es una nueva linea escrita en el archivo.\n")
    f.write("Otra linea añadida al archivo.\n")
    
with open("archivo3.txt", "a") as f:
    f.write("Esta linea se ha añadido al final del archivo.\n")
    
with open("archivo.txt", 'r+') as f:
    contenido = f.read()
    f.write("\nEsta linea se ha añadido al final del archivo usando r+.\n")

with open("archivo2.txt", 'w+') as f:
    f.write("Escribiendo en archivo2 usando w+.\n")
    f.seek(0)  # Volver al inicio del archivo para leer lo que se escribió
    contenido = f.read()
    print(contenido)
    
with open("archivo3.txt", 'a+') as f:
    f.write("Añadiendo una linea usando a+.\n")
    f.seek(0)  # Volver al inicio del archivo para leer todo el contenido
    contenido = f.read()
    print(contenido)