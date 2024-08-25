#Suma de pares: Escribe una función que tome una lista de números y devuelva la suma de
#los números pares en la lista.

def sumaPares(listanumeros):
    suma = 0
    for i in range(len(listanumeros)):
        if listanumeros[i] % 2 == 0:
            suma += listanumeros[i]
    return suma
    
def main():
    numeros = input("Ingrese numeros separados por espacios: ")
    lista = list(map(int, numeros.split()))
    suma = sumaPares(lista)
    print(f"La suma de los pares es: {suma}")

if __name__ == "__main__":
    main()