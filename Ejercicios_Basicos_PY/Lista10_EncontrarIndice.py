#Encontrar índice: Escribe una función que reciba una lista y un valor, y devuelva el
#índice de la primera aparición de ese valor en la lista, o -1 si el valor no está presente.

def encontrarIndice(lista, valor):
    for i in range (len(lista)):
        if lista[i] == valor:
            return i+1
    return -1

lista = input("Ingrese una lista de numeros separados por coma: ")
lista_numeros = list(map(int, lista.split(",")))
valor = int(input("Ingrese un numero indice: "))