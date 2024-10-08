import tkinter as tk
from tkinter import messagebox
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

    # Mostrar resultados
    texto_resultado.delete(1.0, tk.END)
    texto_resultado.insert(tk.END, f"Suma inferior: {suma_inferior:.2f}\n")
    texto_resultado.insert(tk.END, f"Suma superior: {suma_superior:.2f}\n")
    texto_resultado.insert(tk.END, f"Área real: {area_real:.2f}\n")
    texto_resultado.insert(tk.END, f"Error de cálculo: {error:.2f}\n")

    # Agregar utilidad: mostrar gráfico de la función cuadrática
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

def obtener_parametros():
    try:
        a = float(entry_a.get())
        b = float(entry_b.get())
        c = float(entry_c.get())
        intervalo_inicio = float(entry_intervalo_inicio.get())
        intervalo_fin = float(entry_intervalo_fin.get())
        num_rectangulos = int(entry_num_rectangulos.get())
        calcular_area_cuadratica(a, b, c, intervalo_inicio, intervalo_fin, num_rectangulos)
    except ValueError:
        messagebox.showerror("Error", "Debes ingresar números válidos.")

root = tk.Tk()
root.title("Cálculo de área de una función cuadrática")

label_a = tk.Label(root, text="Coeficiente a:")
label_a.grid(row=0, column=0, padx=10, pady=10)
entry_a = tk.Entry(root)
entry_a.grid(row=0, column=1, padx=10, pady=10)

label_b = tk.Label(root, text="Coeficiente b:")
label_b.grid(row=1, column=0, padx=10, pady=10)
entry_b = tk.Entry(root)
entry_b.grid(row=1, column=1, padx=10, pady=10)

label_c = tk.Label(root, text="Coeficiente c:")
label_c.grid(row=2, column=0, padx=10, pady=10)
entry_c = tk.Entry(root)
entry_c.grid(row=2, column=1, padx=10, pady=10)

label_intervalo_inicio = tk.Label(root, text="Inicio del intervalo:")
label_intervalo_inicio.grid(row=3, column=0, padx=10, pady=10)
entry_intervalo_inicio = tk.Entry(root)
entry_intervalo_inicio.grid(row=3, column=1, padx=10, pady=10)

label_intervalo_fin = tk.Label(root, text="Fin del intervalo:")
label_intervalo_fin.grid(row=4, column=0, padx=10, pady=10)
entry_intervalo_fin = tk.Entry(root)
entry_intervalo_fin.grid(row=4, column=1, padx=10, pady=10)

label_num_rectangulos = tk.Label(root, text="Número de rectángulos:")
label_num_rectangulos.grid(row=5, column=0, padx=10, pady=10)
entry_num_rectangulos = tk.Entry(root)
entry_num_rectangulos.grid(row=5, column=1, padx=10, pady=10)

boton_calcular = tk.Button(root, text="Calcular", command=obtener_parametros)
boton_calcular.grid(row=6, column=0, columnspan=2, padx=10, pady=10)

texto_resultado = tk.Text(root)
texto_resultado.grid(row=7, column=0, columnspan=2, padx=10, pady=10)

root.mainloop()
