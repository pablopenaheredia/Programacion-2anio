import random
palabras = [
    'ciberseguridad',
    'fullstack',
    'algoritmo',
    'blockchain',
    'backup',
    'analista',
    'testing',
    'hipertexto']
palabra = random.choice(palabras)
adivinanza = ['_'] * len(palabra)
intentos = 6
while intentos > 0 and '_' in adivinanza:
        print(' '.join(adivinanza))
        print('Intentos restantes:', intentos)
        letra = input('Ingresa una letra: ')
        if letra in palabra:
            for i in range(len(palabra)):
                if palabra[i] == letra:
                    adivinanza[i] = letra
        else:
            intentos -= 1
if '_' in adivinanza:
        print('Perdiste, la palabra era:', palabra)
else:
        print('Ganaste, la palabra era:', palabra)