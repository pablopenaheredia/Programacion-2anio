#Contar letras: Escribe una función que reciba una cadena y devuelva un diccionario
#con la frecuencia de cada letra en la cadena.

def transformarCadena(cadena):
    palabras = {}
    for letra in cadena:
        if letra in palabras:
            palabras[letra] += 1
        else:
            palabras[letra] = 1
    return palabras


cadenaingresada = input("Ingrese una cadena de texto: ")
print("Frecuencia de cada letra en la cadena ingresada (Letra:Numero de veces que se muestra): ", transformarCadena(cadenaingresada))