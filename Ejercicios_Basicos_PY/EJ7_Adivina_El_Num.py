import random

numero_secreto = random.randint(1, 100)
#La función .randint() es una función del módulo random en Python.
#Se utiliza para generar un número entero aleatorio dentro de un rango específico.
adivinanza = None

while adivinanza != numero_secreto:
    adivinanza = int(input("Adivina el número entre 1 y 100: "))
    if adivinanza < numero_secreto:
        print("¡Demasiado bajo!")
    elif adivinanza > numero_secreto:
        print("¡Demasiado alto!")

print("¡Bien hecho! Has adivinado el número.")
