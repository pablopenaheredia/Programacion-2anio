#Palíndromo: Escribe una función que determine si una palabra o frase es un palíndromo (se
#lee igual de adelante hacia atrás que de atrás hacia adelante), ignorando espacios y signos
#de puntuación.

def saberPalindromo(frase):
    cadena = list(frase)
    cadena_inversa = list(frase)
    cadena_inversa.reverse()
    
    if cadena == cadena_inversa: 
        return True
    else:
        return False
    
cadena = input("Ingrese una frase para saber si es palindromo: ")
if saberPalindromo(cadena):
    print("La frase es un palindromo!")
else:
    print("La frase no es un palindromo.")
        
