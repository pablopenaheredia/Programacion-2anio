#Crea un función “ConvertirEspaciado”, que reciba como parámetro un texto y devuelve una
#cadena con un espacio adicional tras cada letra. Por ejemplo, “Hola, tú” devolverá “H o l a , t
#ú “. Crea un programa principal donde se use dicha función luego del ingreso del usuario.

def convertirEspaciado(texto):    
    texto_espaciado = ""
    for i in texto:
        texto_espaciado += i + " "
    return texto_espaciado


#Programa principal

def main():
    texto_ingresado = input("Ingrese un texto a espaciar: ")
    texto_convertido = convertirEspaciado(texto_ingresado)
    print(f"El texto espaciado es: {texto_convertido}")

if __name__ == "__main__":
    main()