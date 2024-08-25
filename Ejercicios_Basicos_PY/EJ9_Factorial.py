def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)
numero = int(input("Ingresa un número para calcular su factorial: "))
print("El factorial de", numero, "es", factorial(numero))