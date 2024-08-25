import string
import random

def generar_pw():
    caracteres = string.ascii_letters + string.digits + string.punctuation
##.ascii hace que incluye mayus y minus, .digits=numeros y punctuation=simbolos
    pw = "".join(random.choice(caracteres) for _ in range(12))
#for _ in range(12)): Esto es una expresión generadora. Crea un objeto generador que produce 12 caracteres aleatorios,
#uno por cada número en el rango de 0 a 11.
#"".join(...): Este método une todos los caracteres generados en una sola cadena.
#El resultado es una cadena de 12 caracteres aleatorios.
    return pw

print("Tu contraseña aleatoria es: ", generar_pw())
