#Promedio de una lista: Crea una función que calcule el promedio de los números en
#una lista dada.

def calcularPromedio(lista_numeros):
    suma = 0
    for i in lista_numeros:
        suma += i
    promedio = suma / len(lista_numeros)
    return suma, promedio

numeros = input("Introduzca los numeros que quiere sumar para luego sacar el promedio, separados por comas: ")
lista = list(map(float, numeros.split(",")))
print(calcularPromedio(lista))
suma, promedio = calcularPromedio(lista)
print(f"La suma de los numeros ingresados es: {suma} y su promedio es de {promedio}")