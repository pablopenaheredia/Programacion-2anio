import string
password = input("Ingrese una contraseña: ")

long_minima = len(password) >= 8
mayus = any(char.isupper() for char in password)
minus = any(char.islower() for char in password)
num = any(char.isdigit() for char in password)
#importar string hace que pueda validar aun mas signos, al usar "any(char in "!@#$%^&*()" for char in password)", me limitaba los signos.
sp_char = any(char in string.punctuation for char in password)

# Verificar que la contraseña cumple los requisitos
if long_minima and mayus and minus and num and sp_char:
    print("La contraseña es válida.")
else:
    print("La contraseña no es válida.")
