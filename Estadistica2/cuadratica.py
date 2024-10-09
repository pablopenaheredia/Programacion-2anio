import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import quad

def calcular_area_cuadratica(a, b, c, intervalo_inicio, intervalo_fin, num_rectangulos):
    # Calcular área real utilizando la función quad de scipy
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

    return suma_inferior, suma_superior, area_real, error

def graficar_funcion(a, b, c, intervalo_inicio, intervalo_fin, num_rectangulos):
    x_plot = np.linspace(intervalo_inicio - 10, intervalo_fin + 10, 1000)
    y_plot = [a * x**2 + b * x + c for x in x_plot]

    plt.plot(x_plot, y_plot, label='Función cuadrática', color='blue')
    plt.fill_between(x_plot, y_plot, color='blue', alpha=0.1)

    ancho = (intervalo_fin - intervalo_inicio) / num_rectangulos
    for i in range(num_rectangulos):
        xi = intervalo_inicio + i * ancho
        altura = a * xi**2 + b * xi + c
        plt.bar(xi, max(0, altura), width=ancho, color='green', alpha=0.3, edgecolor='black', align='edge')

    for i in range(1, num_rectangulos + 1):
        xi = intervalo_inicio + i * ancho
        altura = a * xi**2 + b * xi + c
        plt.bar(xi - ancho, max(0, altura), width=ancho, color='blue', alpha=0.3, edgecolor='black', align='edge')

    plt.xlabel('x')
    plt.ylabel('f(x)')
    plt.title('Gráfico de la función cuadrática y las sumas')
    plt.legend()
    plt.grid(True)

    plt.ylim(min(y_plot) - 10, max(y_plot) + 10)

    plt.show()
