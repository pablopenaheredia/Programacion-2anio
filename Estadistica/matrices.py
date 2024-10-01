import numpy as np

def gauss_jordan():
    """
    Función para transformar una matriz en forma escalonada reducida (MERF)
    mediante el teorema de Gauss-Jordan.

    Pide al usuario insertar las ecuaciones para una matriz 3x3.
    """
    print("Ingrese las ecuaciones para la matriz 3x3:")

    # Inicializar la matriz
    matriz = np.zeros((3, 3))

    # Pedir al usuario insertar las ecuaciones
    for i in range(3):
        for j in range(3):
            while True:
                try:
                    matriz[i, j] = float(input(f"Ingrese el coeficiente a_{i+1}{j+1}: "))
                    break
                except ValueError:
                    print("Error: debe ingresar un número.")

    print("\nMatriz original:")
    print(matriz)

    # Transformar la matriz en forma escalonada reducida (MERF)
    numero_filas = len(matriz)
    for i in range(numero_filas):
        # Buscar el elemento pivote en la columna i
        maximo_elemento = abs(matriz[i][i])
        fila_maximo = i
        for k in range(i+1, numero_filas):
            if abs(matriz[k][i]) > maximo_elemento:
                maximo_elemento = abs(matriz[k][i])
                fila_maximo = k

        # Intercambiar filas si es necesario
        if fila_maximo != i:
            matriz[[i, fila_maximo]] = matriz[[fila_maximo, i]]

        # Normalizar la fila i
        pivote = matriz[i][i]
        if pivote != 0:
            matriz[i] = matriz[i] / pivote

        # Eliminar los elementos debajo del pivote en la columna i
        for j in range(i+1, numero_filas):
            factor = matriz[j][i]
            matriz[j] = matriz[j] - factor * matriz[i]

    # Eliminar los elementos encima del pivote en cada columna
    for i in range(numero_filas-1, -1, -1):
        for j in range(i-1, -1, -1):
            factor = matriz[j][i]
            matriz[j] = matriz[j] - factor * matriz[i]

    print("\nMatriz en forma escalonada reducida (MERF):")
    print(matriz)

# Ejecutar la función
gauss_jordan()
