#Intercambiar valores: Crea una función que tome un diccionario y dos claves, e
#intercambie los valores de esas dos claves en el diccionario.

def intercambiarValores(dicc, a, b):
    if a in dicc and b in dicc :
        dicc[a], dicc[b] = dicc[b], dicc[a]
    return dicc

diccionario = {'nombre': 'pablo',
               'apellido': 'pena',
               'pais': 'argentina'}
print(f"El diccionario es {diccionario}")
a = input("Ingrese la primera clave a cambiar: ")
b = input("Ingrese la segunda clave a cambiar: ")


print(intercambiarValores(diccionario, a, b))