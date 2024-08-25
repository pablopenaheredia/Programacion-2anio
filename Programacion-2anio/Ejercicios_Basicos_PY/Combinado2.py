#Palabras por letra inicial : Escribe una función que tome una lista de palabras y devuelva 
#un diccionario donde las claves son las letras iniciales de las palabras y los valores son
#listas de palabras que comienzan con esa letra.

def palabrasporinicial(lista_palabras):
    nuevo_dicc = {}
    for palabra in lista_palabras:
        inicial = palabra[0]
        if inicial in nuevo_dicc:
            nuevo_dicc[inicial].append(palabra)
        else:
            nuevo_dicc[inicial] = [palabra]
    return nuevo_dicc


palabras = [
    "árbol", "luna", "montaña", "río", "casa", "libro", "gato", "perro", "sol", "mar",
    "cielo", "estrella", "flor", "jardín", "coche", "avión", "tren", "playa", "bosque", "campo",
    "ciudad", "nube", "viento", "lluvia", "nieve", "fuego", "tierra", "camino", "puente", "barco"
    ]

print(palabrasporinicial(palabras))