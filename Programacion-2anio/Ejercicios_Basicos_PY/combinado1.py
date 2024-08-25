#Notas de estudiantes : Escribe una función que recibe un diccionario donde las claves 
#son nombres de estudiantes y los valores son listas de sus calificaciones. 
#La función debe devolver un nuevo diccionario con las mismas claves pero 
#donde los valores son la calificación promedio de cada estudiante.

def notasEstudiantes(diccionario):
    nuevo_diccionario = {}
    for k, v in diccionario.items():
        promedio = sum(v) / len(v)
        nuevo_diccionario[k] = diccionario[k]
        nuevo_diccionario[k] = promedio
    return nuevo_diccionario

estudiantes = {
    'pablo': [10,8,7,9,5,6],
    'lauti': [7,9,4,7,9,4],
    'caty': [8,5,3,8,0]
}

print (notasEstudiantes(estudiantes))