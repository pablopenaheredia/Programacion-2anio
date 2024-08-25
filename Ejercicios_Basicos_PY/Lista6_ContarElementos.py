#Contar elementos: Escribe una función que reciba una lista y un valor, y devuelva
#cuántas veces aparece ese valor en la lista.

def contarElementos(lista, valor):
    contador = 0
    for i in lista:
        if i == valor:
            contador += 1
    return contador

numeros = input("Ingrese una lista de numeros separados por coma: ")
lista = list(map(int, numeros.split(",")))
n = int(input("Ingrese un valor, para saber cuantas veces aparece ese valor en la lista: "))
print("El numero de veces que aparece el valor ingresado es de:", contarElementos(lista, n), "veces")