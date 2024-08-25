#Producto de elementos: Escribe una función que tome una lista de números y
#devuelva el producto de todos los elementos.

def producto(listanumeros):
    producto = 1
    for i in listanumeros:
        producto *= i
    return producto
    
numeros = input("Ingrese una lista de numeros separados por comas: ")
lista = list(map(int, numeros.split(",")))
print(f"El producto de toda la lista es: ", producto(lista))