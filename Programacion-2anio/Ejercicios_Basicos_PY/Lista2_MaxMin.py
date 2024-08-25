#Máximo y mínimo: Escribe una función que reciba una lista de números y devuelva el
#valor máximo y el mínimo de la lista.

def maxmin(lista_numeros):
    maximo = max(lista_numeros)
    minimo = min(lista_numeros)
    return maximo, minimo

lista_numeros = []
numeros = input("Ingrese los numeros separados por espacios: ")
numeros = list(map(int, numeros.split()))
maximo, minimo = maxmin(numeros)
for numero in numeros:
    lista_numeros.append(numero)
print(f"El numero maximo es {maximo} y el minimo es {minimo}")
print(lista_numeros[2])