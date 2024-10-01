def gauss_jordan(n):
    # Inicializar matriz y vector de resultados
    matriz = [[0 for _ in range(n)] for _ in range(n)]
    resultados = [0 for _ in range(n)]

    # Ingresar coeficientes y valores de igualdad
    for i in range(n):
        for j in range(n):
            while True:
                try:
                    matriz[i][j] = float(input(f"Ingrese coeficiente ({i+1}, {j+1}): "))
                    break
                except ValueError:
                    print("Error: debe ingresar un número válido.")
        while True:
            try:
                resultados[i] = float(input(f"Ingrese valor de igualdad {i+1}: "))
                break
            except ValueError:
                print("Error: debe ingresar un número válido.")

    # Aplicar método de Gauss-Jordan
    for i in range(n):
        # Buscar fila pivote
        max_valor = abs(matriz[i][i])
        fila_pivote = i
        for k in range(i+1, n):
            if abs(matriz[k][i]) > max_valor:
                max_valor = abs(matriz[k][i])
                fila_pivote = k

        # Intercambiar filas si es necesario
        if fila_pivote != i:
            matriz[i], matriz[fila_pivote] = matriz[fila_pivote], matriz[i]
            resultados[i], resultados[fila_pivote] = resultados[fila_pivote], resultados[i]

        # Verificar si hay división por 0
        if matriz[i][i] == 0:
            print("Error: división por 0. El sistema no tiene solución, es incompatible.")
            return

        # Hacer cero los elementos debajo del pivote
        for k in range(i+1, n):
            factor = matriz[k][i] / matriz[i][i]
            for j in range(i, n):
                matriz[k][j] -= factor * matriz[i][j]
            resultados[k] -= factor * resultados[i]

    # Calcular soluciones
    soluciones = [0 for _ in range(n)]
    for i in range(n-1, -1, -1):
        # Verificar si hay división por 0
        if matriz[i][i] == 0:
            print("Error: división por 0. El sistema no tiene solución única.")
            return
        soluciones[i] = resultados[i]
        for j in range(i+1, n):
            soluciones[i] -= matriz[i][j] * soluciones[j]
        soluciones[i] /= matriz[i][i]

    # Mostrar resultados
    if all(matriz[i][i] != 0 for i in range(n)):
        print("Sistema Compatible Determinado")
        for i in range(n):
            print(f"x{i+1} = {soluciones[i]:.2f}")
    elif any(matriz[i][i] == 0 for i in range(n)):
        if all(resultados[i] == 0 for i in range(n)):
            print("Sistema Compatible Indeterminado")
        else:
            print("Sistema Incompatible")

n = int(input("Ingrese el tamaño de la matriz (n): "))
while n <= 0:
    print("Error: el tamaño de la matriz debe ser un número entero positivo.")
    n = int(input("Ingrese el tamaño de la matriz (n): "))
gauss_jordan(n)
