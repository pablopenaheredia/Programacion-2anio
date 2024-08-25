# Operaciones básicas con listas en Python

# Crear una lista
lista = [1, 2, 3, 4, 5]

# Acceder a elementos
primer_elemento = lista[0]  # Primer elemento
ultimo_elemento = lista[-1]  # Último elemento

# Modificar elementos
lista[2] = 10  # Cambiar el tercer elemento a 10

# Agregar elementos
lista.append(6)  # Añadir 6 al final de la lista
lista.insert(2, 7)  # Insertar 7 en la tercera posición

# Eliminar elementos
lista.remove(10)  # Eliminar el primer 10 encontrado
eliminado = lista.pop(2)  # Eliminar y retornar el tercer elemento
del lista[1]  # Eliminar el segundo elemento

# Iterar sobre una lista
for elemento in lista:
    print(elemento)

# Comprensiones de listas
cuadrados = [x**2 for x in lista]


# Métodos útiles para listas
suma = sum(lista)  # Suma de elementos
maximo = max(lista)  # Valor máximo
minimo = min(lista)  # Valor mínimo
sin_duplicados = list(set(lista))  # Eliminar duplicados
indice = lista.index(3)  # Índice de la primera aparición de 3
conteo = lista.count(2)  # Conteo de ocurrencias de 2
lista_invertida = lista[::-1]  # Lista invertida


# Operaciones básicas con diccionarios en Python

# Crear un diccionario
diccionario = {'clave1': 'valor1', 'clave2': 'valor2'}

# Acceder a valores
valor = diccionario['clave1']

# Modificar valores
diccionario['clave1'] = 'nuevo_valor'

# Agregar pares clave-valor
diccionario['clave3'] = 'valor3'

# Eliminar pares clave-valor
del diccionario['clave2']
valor = diccionario.pop('clave1')  # También retorna el valor eliminado

# Iterar sobre un diccionario
for clave, valor in diccionario.items():
    print(clave, valor)

# Métodos útiles para diccionarios
claves = diccionario.keys()  # Vista de claves
valores = diccionario.values()  # Vista de valores
items = diccionario.items()  # Vista de pares clave-valor
valor_por_defecto = diccionario.get('clave', 'valor_por_defecto')  # Valor por defecto si la clave no existe
diccionario.update({'nueva_clave': 'nuevo_valor'})  # Actualizar con otro diccionario


# Ejercicios combinados

# Contar palabras en frases
def contar_palabras(frases):
    conteo = {}
    for frase in frases:
        palabras = frase.split()
        for palabra in palabras:
            if palabra in conteo:
                conteo[palabra] += 1
            else:
                conteo[palabra] = 1
    return conteo

# Agrupar por longitud
def agrupar_por_longitud(palabras):
    agrupado = {}
    for palabra in palabras:
        longitud = len(palabra)
        if longitud in agrupado:
            agrupado[longitud].append(palabra)
        else:
            agrupado[longitud] = [palabra]
    return agrupado

# Diccionario de listas
def diccionario_de_listas(diccionario):
    todos_elementos = []
    for lista in diccionario.values():
        todos_elementos.extend(lista)
    return todos_elementos

