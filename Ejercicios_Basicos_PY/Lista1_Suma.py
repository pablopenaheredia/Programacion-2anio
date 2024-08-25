#Suma de elementos: Escribe una función que tome una lista de números y devuelva la
#suma de todos los elementos en la lista.

def sumalista(listanumeros):
    suma = 0
    for i in listanumeros:
        suma += i
    return suma

lista_numeros = []
numeros = input("Ingrese la lista de numeros separados por comas: ")
lista_numeros = map(float, numeros.split(","))
suma = sumalista(lista_numeros)
print(f"La suma de los elementos de la lista es: {suma}")