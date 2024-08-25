#Inventario de productos : Escribe una función que recibe un diccionario donde las claves son los
#nombres de los productos y los valores son listas de precios históricos de esos productos.
#La función debe devolver un nuevo diccionario donde las claves son los nombres 
#de los productos y los valores son el precio promedio de cada producto.


def inventario_productos(diccionario_p):
    nuevo_dicc = {}
    for k, v in diccionario_p.items():
        promedio = sum(v) / len(v)
        nuevo_dicc[k] = diccionario_p[k]
        nuevo_dicc[k] = promedio
    return nuevo_dicc



diccionario_p = {
    'papa': [200, 300, 600],
    'lechuga': [500,200,100],
    'cebolla': [300,200,50]
}

print(inventario_productos(diccionario_p))