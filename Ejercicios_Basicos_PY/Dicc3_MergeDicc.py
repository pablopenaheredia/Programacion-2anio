#Merge de diccionarios: Crea una función que tome dos diccionarios y devuelva uno
#nuevo que combine ambos (en caso de conflicto, usa los valores del segundo
#diccionario).

def merge(diccionario1, diccionario2):
    diccionario2.update(diccionario1)
    return diccionario2

diccionario1 = {'a': 6,
                'b': 5,
                'c': 8}

diccionario2 = {'d': 3,
                'e': 8,
                'f': 9,}
print(f"El primer diccionario es {diccionario1}, y el segundo es: {diccionario2}")
print("La combinacion de ambos es", merge(diccionario1, diccionario2))  