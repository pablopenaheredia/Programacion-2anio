#Crea una función “calcularMaxMin” que recibe una lista con valores numéricos y devuelve el
#valor máximo y el mínimo. Crea un programa que pida números por teclado y muestre el
#máximo y el mínimo, utilizando la función anterior.

def calcularMaxMin(lista_numeros):
    maximo = max(lista_numeros)
    minimo = min(lista_numeros)
    return maximo, minimo

def main():

    numeros = []
    while True:
        num = input("Introduce un número (o 'fin' para terminar): ")
        if num.lower() == 'fin':
            break
        else: 
            numeros.append(float(num))

    maximo, minimo = calcularMaxMin(numeros)
    print(f"El máximo es: {maximo}")
    print(f"El mínimo es: {minimo}")

if __name__ == "__main__":
    main()