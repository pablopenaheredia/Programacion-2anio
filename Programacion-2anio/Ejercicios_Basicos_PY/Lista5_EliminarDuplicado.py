#Eliminar duplicados: Crea una función que tome una lista y devuelva una nueva lista
#sin elementos duplicados.

def eliminarDuplicado(lista):
    nuevalista = []
    for i in lista:
        if i not in nuevalista:
            nuevalista.append(i)
    return nuevalista

numeros = input("Ingrese una lista de numeros separados por coma: ")
lista = list(map(int, numeros.split(",")))
print(f"La lista de numeros que ingresaste es: {lista}")
print(f"La nueva lista sin los duplicados es: ", eliminarDuplicado(lista))