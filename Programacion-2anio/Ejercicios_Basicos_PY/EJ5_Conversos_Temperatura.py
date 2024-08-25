def celsius_farenheit(celsius):
    farhenheit = (celsius * 9/5) + 32
    return farhenheit

def farhenheit_celsius(fahrenheit):
    celsius = (fahrenheit - 32) * 5/9
    return celsius

def main ():
    print("Convertidor de temperatura, eliga la opcion que desee")
    print("Opcion 1: Convertir de Cº a Fº")
    print("Opcion 2: Convertir de Fº a Cº")
    opcion = input("Ingrese la opcion: ")

    if opcion == '1':
        celsius = float(input("Ingrese los grados a convertir: "))
        fahrenheit = celsius_farenheit(celsius)
        print(f"{celsius} grados Cº son {fahrenheit} grados Fº")
    elif opcion == '2':
        farhenheit = float(input("Ingrese los grados a convertir"))
        celsius = farhenheit_celsius(farhenheit)
        print(f"{farhenheit} grados Fº son {celsius} grados Fº")