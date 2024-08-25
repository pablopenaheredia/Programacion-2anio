#Invertir lista: Escribe una función que tome una lista y devuelva una nueva lista con los
#elementos en orden inverso.

def invertirLista(lista):
    listainversa = list(lista)
    listainversa.reverse()
    return listainversa


numeros = input("Ingrese una lista de numeros separadas por comas: ")
lista = list(map(int, numeros.split(",")))
print(f"Su lista es {lista} y la lista inversa es: ", invertirLista(lista))

    