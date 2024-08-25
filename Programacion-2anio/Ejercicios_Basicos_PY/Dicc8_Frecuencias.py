#Diccionario de frecuencias: Escribe una función que reciba una lista de palabras y
#devuelva un diccionario con la frecuencia de cada palabra.

def frecuencia(lista):
    diccionariofrecuencia = {}
    for i in lista:
        if i in diccionariofrecuencia:
            diccionariofrecuencia[i] += 1
        else:
            diccionariofrecuencia[i] = 1
    return diccionariofrecuencia
            

diccionario = ["hola", "hola", "chau", "hola", "bien", "chau"]
print(f"La lista de palabras es:", frecuencia(diccionario))