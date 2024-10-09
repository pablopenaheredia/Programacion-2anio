import tkinter as tk
from tkinter import messagebox
from cuadratica import calcular_area_cuadratica, graficar_funcion

def obtener_parametros():
    try:
        a = float(entry_a.get())
        b = float(entry_b.get())
        c = float(entry_c.get())
        intervalo_inicio = float(entry_intervalo_inicio.get())
        intervalo_fin = float(entry_intervalo_fin.get())
        num_rectangulos = int(entry_num_rectangulos.get())
        
        suma_inferior, suma_superior, area_real, error = calcular_area_cuadratica(
            a, b, c, intervalo_inicio, intervalo_fin, num_rectangulos
        )

        texto_resultado.delete(1.0, tk.END)
        texto_resultado.insert(tk.END, f"Suma inferior: {suma_inferior:.2f}\n")
        texto_resultado.insert(tk.END, f"Suma superior: {suma_superior:.2f}\n")
        texto_resultado.insert(tk.END, f"Área real: {area_real:.2f}\n")
        texto_resultado.insert(tk.END, f"Error de cálculo: {error:.2f}\n")

        graficar_funcion(a, b, c, intervalo_inicio, intervalo_fin, num_rectangulos)
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
