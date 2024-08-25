#Diccionario de listas: Escribe una función que tome un diccionario donde los valores
#son listas y devuelva una lista que contenga todos los elementos de las listas del
#diccionario.

def diccionario_a_lista(diccionario):
    lista = []
    for i in diccionario.values():
        lista.extend(i)
    return lista

diccionario = {'Casa': ['Ventana', 'Puerta', 'Habitacion'], 'Mascotas': ['Gato', 'Perro', 'Loro']}
print(f"El diccionario es: {diccionario}, y todos los elementos de las listas son: ", diccionario_a_lista(diccionario))
