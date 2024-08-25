#Solicitamos al usuario que ingrese los números
numeros = input("Ingrese los números separados por espacios: ")
lista_numeros = list(map(float, numeros.split()))
promedio = sum(lista_numeros) / len(lista_numeros)

print("El promedio de los números ingresados es: ", promedio)
