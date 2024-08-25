print("Piensa en un número entre 1 y 100.")
minimo = 1
maximo = 100

while True:
    adivinanza = (minimo + maximo) // 2
    respuesta = input(f"¿Tu número es {adivinanza}? (si/mayor/menor): ")

    if respuesta == 'si':
        print("Adiviné tu número.")
        break
    elif respuesta == 'mayor':
        minimo = adivinanza + 1
    elif respuesta == 'menor':
        maximo = adivinanza - 1