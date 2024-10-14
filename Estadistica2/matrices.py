from tkinter import messagebox

def gauss_jordan(matriz, resultados):
    n = len(matriz)
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
            fila_temp = matriz[i]
            matriz[i] = matriz[fila_pivote]
            matriz[fila_pivote] = fila_temp
            temp = resultados[i]
            resultados[i] = resultados[fila_pivote]
            resultados[fila_pivote] = temp

        # Verificar si hay división por 0
        if matriz[i][i] == 0:
            messagebox.showerror("Error", "División por 0. El sistema no tiene solución, es incompatible.")
            return

        # Hacer cero los elementos debajo del pivote
        for k in range(i+1, n):
            factor = matriz[k][i] / matriz[i][i]
            for j in range(i, n):
                matriz[k][j] -= factor * matriz[i][j]
            resultados[k] -= factor * resultados[i]

    # Calcular rangos de matrices
    rango_coeficiente = len(list(filter(lambda row: any(row), matriz)))
    rango_matriz_aumentada = len(list(filter(lambda row: any(row), matriz + [resultados])))

    # Verificar si hay un número infinito de soluciones
    if rango_coeficiente < rank_matriz_aumentada:
        messagebox.showinfo("El sistema tiene infinitas soluciones.")
        return None

    # Calcular soluciones
    soluciones = [0] * n
    for i in range(n-1, -1, -1):
        # Verificar si hay división por 0
        if matriz[i][i] == 0:
            messagebox.showerror("Error", "División por 0. El sistema no tiene solución única.")
            return
        soluciones[i] = resultados[i]
        for j in range(i+1, n):
            soluciones[i] -= matriz[i][j] * soluciones[j]
        soluciones[i] /= matriz[i][i]

    return soluciones
