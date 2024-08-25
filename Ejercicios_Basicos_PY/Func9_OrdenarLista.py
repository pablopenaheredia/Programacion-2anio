#Ordenar lista de cadenas: Escribe una función que tome una lista de cadenas y devuelva una
#lista ordenada alfabéticamente de esas cadenas, ignorando mayúsculas y minúsculas.

def ordenar_cadenas(lista_cadenas):
    return sorted(lista_cadenas, key=lambda s: s.lower())

lista_cadenas = ['Manzana', 'banana', 'Pera', 'manzana', 'Banana', 'pera']
lista_ordenada = ordenar_cadenas(lista_cadenas)

print(lista_ordenada)