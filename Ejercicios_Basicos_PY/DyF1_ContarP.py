#Contar palabras en frases: Escribe una función que reciba una lista de frases y
#devuelva un diccionario donde las claves son las palabras y los valores son las
#frecuencias de esas palabras en todas las frases.

def contarPalabras(lista):
    nuevodiccionario = {}
    for frase in lista:
        palabras = frase.split()
        for palabra in palabras:
            if palabra in nuevodiccionario:
                nuevodiccionario[palabra] += 1
            else :
                nuevodiccionario[palabra] = 1
    return nuevodiccionario

ingreso = input("Ingrese una frase a analizar: ")
lista = list(map(str, ingreso.split()))
print("Las veces que aparece cada palabra de la frase es de: ", contarPalabras(lista))