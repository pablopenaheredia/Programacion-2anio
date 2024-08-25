#Agrupar por longitud: Escribe una función que reciba una lista de palabras y devuelva
#un diccionario donde las claves son las longitudes de las palabras y los valores son
#listas de palabras con esa longitud.

def agrupar(lista):
    diccionario = {}
    for i in lista:
        longitud = len(i)
        if longitud in diccionario:
            diccionario[longitud].append(i)
        else:
            diccionario[longitud] = [i]
    return diccionario

palabras = ["hola", "bien", "vos", "como", "estas", "chau"]
print(agrupar(palabras))