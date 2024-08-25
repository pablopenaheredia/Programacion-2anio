#Concatenar listas: Escribe una función que reciba dos listas y devuelva una nueva lista
#que sea la concatenación de ambas.

def concatenarLista(lista1, lista2):
    resultado = lista1 + lista2
    return resultado

frase1 = input("Ingrese la primera lista: ")
lista1 = list(map(str, frase1.split(" ")))

frase2 = input("Ingrese la segunda lista: ")
lista2 = list(map(str, frase2.split(" ")))

print(f"La concatenacion de {lista1} y {lista2} es: ", concatenarLista(lista1, lista2))