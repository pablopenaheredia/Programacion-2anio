#Elementos mayores que un valor: Escribe una función que tome una lista de números
#y un valor n, y devuelva una nueva lista con los elementos mayores que n.

def mayorQueN(lista, n):
    nuevalista = []
    for i in lista:
        if n < i:
            nuevalista.append(i) ##aca agrego el I que sea mayor que n a la nueva lista
    return nuevalista
    
numeros = input("Ingrese una lista de numeros separados por coma: ")
lista = list(map(int, numeros.split(",")))
n = int(input("Ingrese el numero n: "))
print("Los elementos mayores que el n ingresado son:", mayorQueN(lista, n))

