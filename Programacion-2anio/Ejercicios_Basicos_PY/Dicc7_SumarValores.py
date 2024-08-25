#Sumar valores: Escribe una función que reciba un diccionario con valores numéricos y
#devuelva la suma de todos los valores.

def sumarValores(diccionario):
    suma = 0
    for i in diccionario:
        suma += diccionario[i]
    return suma

diccionario = {'a':1,
               'b':2,
               'c':3,
               'd':6}

print(f"La suma de todos los valores de {diccionario} es: " ,sumarValores(diccionario))