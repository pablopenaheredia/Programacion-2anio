#Diccionario inverso: Escribe una función que tome un diccionario y devuelva uno
#nuevo que invierta las claves y los valores.

def diccInverso(diccionario):
    diccionario_inverso = {v: k for k, v in diccionario.items()}
    return diccionario_inverso


diccionario = {"a": 99, "b": "Hola", "c": 30}
print(f"Diccionario de ejemplo: {diccionario}")
print("Diccionario inverso: ")
print(diccInverso(diccionario))