#Contar elementos: Escribe una función que reciba una lista y un valor, y devuelva
#cuántas veces aparece ese valor en la lista.

def contarElementos(lista, valor):
    contador = 0
    for i in lista:
        if i == valor:
            contador += 1
    return contador

lista = [7,2,8,3,5,1,8,5]
valor = 5

print(contarElementos(lista, valor))