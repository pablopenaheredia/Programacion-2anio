#Diccionario de cuadrados: Escribe una función que reciba un número n y devuelva un
#diccionario con los números de 1 a n como claves y sus cuadrados como valores.

def cuadrados(n):
    nuevodiccionario = {}
    clave = 1
    while clave <= n:
        nuevodiccionario[clave] = clave ** 2
        clave += 1
    return nuevodiccionario

numeron = int(input("Ingrese el numero N para que se genere un diccionario de cuadrados\n, donde 1 a n sera la clave y n al cuadrado será su valor: "))
print(cuadrados(numeron))