#Diseñar una función que calcule el área y el perímetro de una circunferencia. Utiliza dicha
#función en un programa principal que lea el radio de una circunferencia y muestre su área y
#perímetro.

def AreaYPerimetro(radio):
    pi = 3.141692
    area = pi * (radio ** 2)
    perimetro = (2 * pi) * radio
    return area, perimetro

def main():
    radio = float(input("Ingrese el radio de la circunferencia: "))
    area, perimetro = AreaYPerimetro(radio)
    print(f"El área de la circunferencia es: {area}")
    print(f"El perímetro de la circunferencia es: {perimetro}")

if __name__ == "__main__":
    main()