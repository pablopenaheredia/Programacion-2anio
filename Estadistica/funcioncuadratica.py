import numpy as np
import matplotlib.pyplot as plt

def calcular_area_cuadratica(a, b, c, intervalo_inicio, intervalo_fin, num_rectangulos):
    # Calcular área real utilizando la función quad de scipy
    from scipy.integrate import quad
    def funcion_cuadratica(x):
        return a * x**2 + b * x + c
    area_real, _ = quad(funcion_cuadratica, intervalo_inicio, intervalo_fin)

    # Calcular suma inferior y suma superior utilizando el método de rectángulos
    x_values = np.linspace(intervalo_inicio, intervalo_fin, num_rectangulos + 1)
    y_values = [a * x**2 + b * x + c for x in x_values]
    suma_inferior = 0
    suma_superior = 0
    for i in range(num_rectangulos):
        suma_inferior += (x_values[i+1] - x_values[i]) * min(y_values[i], y_values[i+1])
        suma_superior += (x_values[i+1] - x_values[i]) * max(y_values[i], y_values[i+1])

    # Calcular error de cálculo
    error = abs(area_real - (suma_inferior + suma_superior) / 2)

    # Mostrar resultados
    print(f"Suma inferior: {suma_inferior:.2f}")
    print(f"Suma superior: {suma_superior:.2f}")
    print(f"Área real: {area_real:.2f}")
    print(f"Error de cálculo: {error:.2f}")

    # Agregar utilidad: mostrar gráfico de la función cuadrática
    x_plot = np.linspace(intervalo_inicio, intervalo_fin, 400)
    y_plot = [a * x**2 + b * x + c for x in x_plot]
    plt.plot(x_plot, y_plot)
    plt.xlabel("x")
    plt.ylabel("y")
    plt.title("Gráfico de la función cuadrática")
    plt.show()

# Ingresar parámetros por teclado
a = float(input("Ingrese el coeficiente a: "))
b = float(input("Ingrese el coeficiente b: "))
c = float(input("Ingrese el coeficiente c: "))
intervalo_inicio = float(input("Ingrese el inicio del intervalo: "))
intervalo_fin = float(input("Ingrese el fin del intervalo: "))
num_rectangulos = int(input("Ingrese el número de rectángulos: "))

calcular_area_cuadratica(a, b, c, intervalo_inicio, intervalo_fin, num_rectangulos)
