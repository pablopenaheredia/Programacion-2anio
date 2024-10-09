import tkinter as tk
from tkinter import messagebox
from matrices import gauss_jordan

def obtener_matriz_y_resultados():
    try:
        n = int(entry_n.get())
        if n <= 0 or n > 6:
            messagebox.showerror("Error", "El tamaño de la matriz debe ser un número entero entre 1 y 6.")
            return

        matriz = []
        resultados = []
        for i in range(n):
            fila = []
            for j in range(n):
                fila.append(float(entry_matriz[i][j].get()))
            matriz.append(fila)
            resultados.append(float(entry_resultados[i].get()))

        soluciones = gauss_jordan(matriz, resultados)
        if soluciones is not None:
            mensaje = "Sistema Compatible Determinado\n"
            for i in range(n):
                mensaje += f"x{i+1} = {round(soluciones[i], 4)}\n"
            messagebox.showinfo("Resultados", mensaje)
    except ValueError:
        messagebox.showerror("Error", "Debes ingresar números válidos.")

def crear_entradas():
    try:
        n = int(entry_n.get())
        if n <= 0 or n > 6:
            messagebox.showerror("Error", "El tamaño de la matriz debe ser un número entero entre 1 y 6.")
            return

        for widget in frame_matriz.winfo_children():
            widget.destroy()

        global entry_matriz
        global entry_resultados
        entry_matriz = []
        entry_resultados = []
        for i in range(n):
            fila = []
            for j in range(n):
                label = tk.Label(frame_matriz, text=f"a{i+1}{j+1}:")
                label.grid(row=i, column=j*2, padx=5, pady=5)
                entry = tk.Entry(frame_matriz)
                entry.grid(row=i, column=j*2+1, padx=5, pady=5)
                fila.append(entry)
            entry_matriz.append(fila)
            label_resultado = tk.Label(frame_matriz, text=f"b{i+1}:")
            label_resultado.grid(row=i, column=n*2, padx=5, pady=5)
            entry_resultado_i = tk.Entry(frame_matriz)
            entry_resultado_i.grid(row=i, column=n*2+1, padx=5, pady=5)
            entry_resultados.append(entry_resultado_i)
    except ValueError:
        messagebox.showerror("Error", "Debes ingresar un número entero válido para el tamaño de la matriz.")

root = tk.Tk()
root.title("Método de Gauss-Jordan")
root.configure(bg="#f0f0f0")

label_n = tk.Label(root, text="Tamaño de la matriz (n):", bg="#f0f0f0")
label_n.grid(row=0, column=0, padx=10, pady=10)

entry_n = tk.Entry(root, width=5)
entry_n.grid(row=0, column=1, padx=10, pady=10)

boton_crear_entradas = tk.Button(root, text="Crear entradas", command=crear_entradas, bg="#cccccc")
boton_crear_entradas.grid(row=0, column=2, padx=10, pady=10)

frame_matriz = tk.Frame(root, bg="#f0f0f0")
frame_matriz.grid(row=1, column=0, columnspan=3, padx=10, pady=10)

boton_calcular = tk.Button(root, text="Calcular", command=obtener_matriz_y_resultados, bg="#cccccc")
boton_calcular.grid(row=2, column=0, columnspan=3, padx=10, pady=10)

# Make the GUI responsive
root.grid_columnconfigure(0, weight=1)
root.grid_columnconfigure(1, weight=1)
root.grid_columnconfigure(2, weight=1)
root.grid_rowconfigure(0, weight=1)
root.grid_rowconfigure(1, weight=1)
root.grid_rowconfigure(2, weight=1)

root.mainloop()
