#Actualizar diccionario: Escribe una función que tome un diccionario y una lista de
#tuplas (clave, valor) y actualice el diccionario con esas tuplas.

def actualizarDiccionario(diccionario, lista):
    for k, v in lista:
        diccionario[k] = v
    return diccionario

diccionario = {'a': 3,
               'b': 7,
               'c': 8}

lista_tupla = [('c', 9),
                ('b', 10)]

print(f"El diccionario base es {diccionario}, la lista de tuplas es {lista_tupla} y el diccionario actualizado es: ", actualizarDiccionario(diccionario, lista_tupla))