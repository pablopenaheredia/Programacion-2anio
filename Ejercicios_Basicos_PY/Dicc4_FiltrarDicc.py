#Filtrar diccionario: Escribe una función que reciba un diccionario y una lista de claves,
#y devuelva un nuevo diccionario solo con las claves especificadas.

def filtrarDicc(diccionario, claves):
    nuevodicc = {}
    for clave in claves:
        if clave in diccionario:
            nuevodicc[clave] = diccionario[clave]
    return nuevodicc

diccionario = {"a": 3,
               "b": 7,
               "c": 0}

claves = ['a', 'c']

print(f"Diccionario de ejemplo: {diccionario}")
print(f"Claves de ejemplo: {claves}")
print(filtrarDicc(diccionario, claves))