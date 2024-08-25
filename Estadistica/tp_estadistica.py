import scipy.integrate as integrate
from scipy.integrate import quad
from tabulate import tabulate
import statistics
import math

    # Funciones estadísticas.
    

def calcular_media(lista):
        return round(statistics.mean(lista), 4)

def calcular_moda(lista):
        frecuencias = {}
        for num in lista:
            frecuencias[num] = frecuencias.get(num, 0) + 1
        moda_frecuencia_maxima = max(frecuencias.values())
        moda = [num for num, freq in frecuencias.items() if freq == moda_frecuencia_maxima]
        if len(set(frecuencias.values())) == 1:
            return None, None
        else:
            return moda, moda_frecuencia_maxima

def calcular_mediana(lista):
        lista_ordenada = sorted(lista)
        return round(statistics.median(lista_ordenada), 4)

def calcular_desviacion(lista):
        desviacion_estandar = statistics.stdev(lista)
        return round(desviacion_estandar, 4)

def calcular_varianza(lista):
        varianza = statistics.variance(lista)
        return round(varianza, 4)

def frecuencia_absoluta(lista):
        frecuencias = {}
        for num in lista:
            frecuencias[num] = frecuencias.get(num, 0) + 1
        return frecuencias

def frecuencia_relativa(lista):
        total = len(lista)
        frec_abs = frecuencia_absoluta(lista)
        frec_relativa = {}
        for clave, valor in frec_abs.items():
            frec_relativa[clave] = round(valor / total, 4)
        return frec_relativa

def frecuencia_porcentual(lista):
        frec_rel = frecuencia_relativa(lista)
        frec_porcentual = {}
        for clave, valor in frec_rel.items():
            frec_porcentual[clave] = round(valor * 100, 4)
        return frec_porcentual

def frecuencia_absoluta_acumulada(lista):
        frec_abs = frecuencia_absoluta(lista)
        acumulado = 0
        frec_abs_acum = {}
        for clave, valor in sorted(frec_abs.items()):
            acumulado += valor
            frec_abs_acum[clave] = acumulado
        return frec_abs_acum

def frecuencia_relativa_acumulada(lista):
        total = len(lista)
        frec_rel = frecuencia_relativa(lista)
        acumulado = 0
        frec_rel_acum = {}
        for clave, valor in sorted(frec_rel.items()):
            acumulado += valor
            frec_rel_acum[clave] = round(acumulado, 4)
        return frec_rel_acum

def frecuencia_porcentual_acumulada(lista):
        frec_porcent = frecuencia_porcentual(lista)
        acumulado = 0
        frec_porcent_acum = {}
        for clave, valor in sorted(frec_porcent.items()):
            acumulado += valor
            frec_porcent_acum[clave] = f"{round(acumulado, 4)}%"
        return frec_porcent_acum

def factorial(x):
    if x == 0 or x == 1:
        return 1
    else:
        result = 1
        for i in range(2, x+1):
            result *= i
        return result
    
    # Función para calcular combinaciones C(n, k)
def combinacion(n, k):
        return factorial(n) // (factorial(k) * factorial(n - k))

    # Función para la distribución binomial
def distribucion_binomial(n, p, k):
        combinaciones = combinacion(n, k)
        probabilidad = combinaciones * (p ** k) * ((1 - p) ** (n - k))
        return probabilidad

    # Función para la distribución de Poisson
def distribucion_poisson(lambd, k):
        probabilidad = (lambd ** k) * (math.e ** -lambd) / factorial(k)
        return probabilidad

    # Función para la distribución hipergeométrica
def distribucion_hipergeometrica(n, M, N, k):
        probabilidad = (combinacion(M, k) * combinacion(N - M, n - k)) / combinacion(N, n)
        return probabilidad

    # Función para la distribución normal (gaussiana)
def distribucion_normal(x, mu, sigma):
    coeficiente = 1 / (2 * math.pi * (sigma ** 2)) ** 0.5
    exponente = -((x - mu) ** 2) / (2 * sigma ** 2)
    densidad = coeficiente * math.exp(exponente)
    return densidad

def calcular_integral(mu, sigma, primer_parametro, segundo_parametro):
    if primer_parametro > segundo_parametro:
        raise ValueError("El primer parámetro de integración debe ser menor o igual que el segundo")
    integral, error = quad(distribucion_normal, primer_parametro, segundo_parametro, args=(mu, sigma))
    return integral

def coeficiente_curtosis(lista):    
    n = len(lista)  
    media = calcular_media(lista)
    desviacion = calcular_desviacion(lista)
    
    suma_cuarta_potencia = sum((x - media) ** 4 for x in lista)

    curtosis = (n * (n + 1) * suma_cuarta_potencia) / ((n - 1) * (n - 2) * (n - 3) * (desviacion ** 4)) \
               - (3 * (n - 1) ** 2) / ((n - 2) * (n - 3))
    
    if curtosis == 0:
        print("La distribución es mesocúrtica")
        interpretación= "La distribucion es mesocúrtica"
    if curtosis > 0:
        print("La distribución es leptocúrtica")
        interpretación= "La distribucion es leptocúrtica"
    if curtosis < 0:
        print("La distribución es platicúrtica")
        interpretación= "La distribucion es platicúrtica"
        
    return round(curtosis, 4), interpretación

def menu_estadistico(numeros):
        while True:
            try:
                print("\nEstadística - Seleccione las opciones deseadas (separadas por comas):")
                print("1. Visualizar la MEDIA.")
                print("2. Visualizar la MODA.")
                print("3. Visualizar la MEDIANA.")
                print("4. Visualizar la DESVIACIÓN ESTÁNDAR.")
                print("5. Visualizar la VARIANZA.")
                print("6. Visualizar FRECUENCIA ABSOLUTA.")
                print("7. Visualizar FRECUENCIA RELATIVA.")
                print("8. Visualizar FRECUENCIA PORCENTUAL.")
                print("9. Visualizar FRECUENCIA ABSOLUTA ACUMULADA.")
                print("10. Visualizar FRECUENCIA RELATIVA ACUMULADA.")
                print("11. Visualizar FRECUENCIA PORCENTUAL ACUMULADA.")
                print("12. Calcular y mostrar el COEFICIENTE DE CURTOSIS.")
                print("13. Visualizar TODOS los cálculos estadísticos.")
                print("0. Regresar al menú principal\n")

                opciones = input("Ingrese los números de las opciones que desea visualizar, separados por comas (por ejemplo: 1,2,3): ")
                opciones = [opcion.strip() for opcion in opciones.split(',')]

                if '0' in opciones:
                    return

                resultados = []
                for opcion in opciones:
                    if opcion == '1':
                        resultados.append(["MEDIA", calcular_media(numeros)])
                    elif opcion == '2':
                        moda, frecuencia = calcular_moda(numeros)
                        if moda is None:
                            resultados.append(["MODA", "No hay moda en los datos."])
                        else:
                            resultados.append(["MODA", f"{moda} (Frecuencia: {frecuencia})"])
                    elif opcion == '3':
                        resultados.append(["MEDIANA", calcular_mediana(numeros)])
                    elif opcion == '4':
                        resultados.append(["DESVIACIÓN ESTÁNDAR", calcular_desviacion(numeros)])
                    elif opcion == '5':
                        resultados.append(["VARIANZA", calcular_varianza(numeros)])
                    elif opcion == '6':
                        resultados.append(["FRECUENCIA ABSOLUTA", frecuencia_absoluta(numeros)])
                    elif opcion == '7':
                        resultados.append(["FRECUENCIA RELATIVA", frecuencia_relativa(numeros)])
                    elif opcion == '8':
                        resultados.append(["FRECUENCIA PORCENTUAL", frecuencia_porcentual(numeros)])
                    elif opcion == '9':
                        resultados.append(["FRECUENCIA ABSOLUTA ACUMULADA", frecuencia_absoluta_acumulada(numeros)])
                    elif opcion == '10':
                        resultados.append(["FRECUENCIA RELATIVA ACUMULADA", frecuencia_relativa_acumulada(numeros)])
                    elif opcion == '11':
                        resultados.append(["FRECUENCIA PORCENTUAL ACUMULADA", frecuencia_porcentual_acumulada(numeros)])
                    elif opcion == '12':
                        resultados.append(["COEFICIENTE DE CURTOSIS", coeficiente_curtosis(numeros)])
                    elif opcion == '13':
                        resultados.append(["MEDIA", calcular_media(numeros)])
                        resultados.append(["MODA", calcular_moda(numeros)[0] if calcular_moda(numeros)[0] is not None else "No hay moda en los datos."])
                        resultados.append(["MEDIANA", calcular_mediana(numeros)])
                        resultados.append(["DESVIACIÓN ESTÁNDAR", calcular_desviacion(numeros)])
                        resultados.append(["VARIANZA", calcular_varianza(numeros)])
                        resultados.append(["FRECUENCIA ABSOLUTA", frecuencia_absoluta(numeros)])
                        resultados.append(["FRECUENCIA RELATIVA", frecuencia_relativa(numeros)])
                        resultados.append(["FRECUENCIA PORCENTUAL", frecuencia_porcentual(numeros)])
                        resultados.append(["FRECUENCIA ABSOLUTA ACUMULADA", frecuencia_absoluta_acumulada(numeros)])
                        resultados.append(["FRECUENCIA RELATIVA ACUMULADA", frecuencia_relativa_acumulada(numeros)])
                        resultados.append(["FRECUENCIA PORCENTUAL ACUMULADA", frecuencia_porcentual_acumulada(numeros)])
                        resultados.append(["COEFICIENTE DE CURTOSIS", coeficiente_curtosis(numeros)])
                    else:
                        print(f"Opción {opcion} no válida.")
                print(tabulate(resultados, headers=["Operación", "Resultado"], tablefmt="grid"))
            except ValueError:
                print("Entrada no válida. Por favor, ingrese opciones válidas.")

def menu_distribuciones():
    while True:
        try:
            print("\nDistribuciones - Seleccione una opción:")
            print("1. Distribución Binomial.")
            print("2. Distribución de Poisson.")
            print("3. Distribución Hipergeométrica.")
            print("4. Distribución Normal (Gaussiana).")
            print("0. Regresar al menú principal\n")

            opcion = int(input("Ingrese el número de la opción que desea utilizar: "))
            if opcion == 0:
                return
            elif opcion == 1:
                n = int(input("Ingrese el número de ensayos (n): "))
                p = float(input("Ingrese la probabilidad de éxito (p): "))
                k = input("Ingrese el número de éxitos deseados (k) [rango (x1, x2), valor fijo, 'menor que x' o 'mayor que x']: ")
                
                if "," in k:
                    x1, x2 = map(int, k.split(","))
                    if x1 >= x2:
                        raise ValueError("El rango x1 debe ser menor que x2.")
                    resultados = []
                    for i in range(x1, x2 + 1):
                        resultado = distribucion_binomial(n, p, i)
                        resultados.append([f"k = {i}", f"P(k = {i}) = {resultado:.4f}"])
                    print(tabulate(resultados, headers=["k", "Probabilidad Binomial"], tablefmt="grid"))
                    
                    sumar_probabilidades = input("¿Desea sumar las probabilidades? (si/no): ")
                    if sumar_probabilidades.lower() == "si":
                        probabilidad_acumulada = sum([distribucion_binomial(n, p, i) for i in range(x1, x2 + 1)])
                        print(f"P(k ∈ [{x1}, {x2}]) = {probabilidad_acumulada:.4f}")
                
                elif k.startswith("menor que"):
                    x = int(k.split()[2])
                    resultados = []
                    for i in range(x + 1):
                        resultado = distribucion_binomial(n, p, i)
                        resultados.append([f"P(k ≤ {i})", f"{resultado:.4f}"])
                    print(tabulate(resultados, headers=["k", "Probabilidad Binomial"], tablefmt="grid"))
                    
                    sumar_probabilidades = input("¿Desea sumar las probabilidades? (si/no): ")
                    if sumar_probabilidades.lower() == "si":
                        probabilidad_acumulada = sum([distribucion_binomial(n, p, i) for i in range(x + 1)])
                        print(f"P(k ≤ {x}) = {probabilidad_acumulada:.4f}")
                
                elif k.startswith("mayor que"):
                    x = int(k.split()[2])
                    resultados = []
                    for i in range(x + 1, n + 1):
                        resultado = distribucion_binomial(n, p, i)
                        resultados.append([f"P(k ≥ {i})", f"{resultado:.4f}"])
                    print(tabulate(resultados, headers=["k", "Probabilidad Binomial"], tablefmt="grid"))
                    
                    sumar_probabilidades = input("¿Desea sumar las probabilidades? (si/no): ")
                    if sumar_probabilidades.lower() == "si":
                        probabilidad_acumulada = sum([distribucion_binomial(n, p, i) for i in range(x + 1, n + 1)])
                        print(f"P(k ≥ {x}) = {probabilidad_acumulada:.4f}")
                
                else:
                    k = int(k)
                    resultado = distribucion_binomial(n, p, k)
                    print(tabulate([[f"k = {k}", f"P(k = {k}) = {resultado:.4f}"]], headers=["k", "Probabilidad Binomial"], tablefmt="grid"))
            
            elif opcion == 2:
                lambd = float(input("Ingrese el valor de lambda (λ): "))
                k = input("Ingrese el número de ocurrencias deseadas (k) [rango (x1, x2), valor fijo, 'menor que x' o 'mayor que x']: ")
                
                if "," in k:
                    x1, x2 = map(int, k.split(","))
                    if x1 >= x2:
                        raise ValueError("El rango x1 debe ser menor que x2.")
                    resultados = []
                    for i in range(x1, x2 + 1):
                        resultado = distribucion_poisson(lambd, i)
                        resultados.append([f"k = {i}", f"P(k = {i}) = {resultado:.4f}"])
                    print(tabulate(resultados, headers=["k", "Probabilidad Poisson"], tablefmt="grid"))
                    
                    sumar_probabilidades = input("¿Desea sumar las probabilidades? (si/no): ")
                    if sumar_probabilidades.lower() == "si":
                        probabilidad_acumulada = sum([distribucion_poisson(lambd, i) for i in range(x1, x2 + 1)])
                        print(f"P(k ∈ [{x1}, {x2}]) = {probabilidad_acumulada:.4f}")
                
                elif k.startswith("menor que"):
                    x = int(k.split()[2])
                    resultados = []
                    for i in range(x + 1):
                        resultado = distribucion_poisson(lambd, i)
                        resultados.append([f"P(k ≤ {i})", f"{resultado:.4f}"])
                    print(tabulate(resultados, headers=["k", "Probabilidad Poisson"], tablefmt="grid"))
                    
                    sumar_probabilidades = input("¿Desea sumar las probabilidades? (si/no): ")
                    if sumar_probabilidades.lower() == "si":
                        probabilidad_acumulada = sum([distribucion_poisson(lambd, i) for i in range(x + 1)])
                        print(f"P(k ≤ {x}) = {probabilidad_acumulada:.4f}")
                
                elif k.startswith("mayor que"):
                    x = int(k.split()[2])
                    resultados = []
                    for i in range(x + 1, int(lambd * 2) + 1):
                        resultado = distribucion_poisson(lambd, i)
                        resultados.append([f"P(k ≥ {i})", f"{resultado:.4f}"])
                    print(tabulate(resultados, headers=["k", "Probabilidad Poisson"], tablefmt="grid"))
                    
                    sumar_probabilidades = input("¿Desea sumar las probabilidades? (si/no): ")
                    if sumar_probabilidades.lower() == "si":
                        probabilidad_acumulada = sum([distribucion_poisson(lambd, i) for i in range(x + 1, int(lambd * 2) + 1)])
                        print(f"P(k ≥ {x}) = {probabilidad_acumulada:.4f}")
                
                else:
                    k = int(k)
                    resultado = distribucion_poisson(lambd, k)
                    print(tabulate([[f"k = {k}", f"P(k = {k}) = {resultado:.4f}"]], headers=["k", "Probabilidad Poisson"], tablefmt="grid"))

            elif opcion == 3:
                # código para distribución hipergeométrica
                N = int(input("Ingrese el tamaño de la población (N): "))
                M = int(input("Ingrese el número de éxitos en la población (M): "))
                n = int(input("Ingrese el tamaño de la muestra (n): "))
                k = input("Ingrese el número de éxitos deseados (k) [rango (x1, x2), valor fijo, 'menor que x' o 'mayor que x']: ")
                if "," in k:
                    x1, x2 = map(int, k.split(","))
                    if x1 >= x2:
                        raise ValueError("El rango x1 debe ser menor que x2.")
                    resultados = []
                    for i in range(x1, x2 + 1):
                        resultado = distribucion_hipergeometrica(n, M, N, i)
                        resultados.append([f"k = {i}", f"P(k = {i}) = {resultado:.4f}"])
                    print(tabulate(resultados, headers=["k", "Probabilidad Hipergeométrica"], tablefmt="grid"))
                    
                    sumar_probabilidades = input("¿Desea sumar las probabilidades? (si/no): ")
                    if sumar_probabilidades.lower() == "si":
                        probabilidad_acumulada = sum([distribucion_hipergeometrica(n, M, N, i) for i in range(x1, x2 + 1)])
                        print(f"P(k ∈ [{x1}, {x2}]) = {probabilidad_acumulada:.4f}")
                
                elif k.startswith("menor que"):
                    x = int(k.split()[2])
                    resultados = []
                    for i in range(x + 1):
                        resultado = distribucion_hipergeometrica(n, M, N, i)
                        resultados.append([f"P(k ≤ {i})", f"{resultado:.4f}"])
                    print(tabulate(resultados, headers=["k", "Probabilidad Hipergeométrica"], tablefmt="grid"))
                    
                    sumar_probabilidades = input("¿Desea sumar las probabilidades? (si/no): ")
                    if sumar_probabilidades.lower() == "si":
                        probabilidad_acumulada = sum([distribucion_hipergeometrica(n, M, N, i) for i in range(x + 1)])
                        print(f"P(k ≤ {x}) = {probabilidad_acumulada:.4f}")
                
                elif k.startswith("mayor que"):
                    x = int(k.split()[2])
                    resultados = []
                    for i in range(x, n + 1):
                        resultado = distribucion_hipergeometrica(n, M, N, i)
                        resultados.append([f"P(k ≥ {i})", f"{resultado:.4f}"])
                    print(tabulate(resultados, headers=["k", "Probabilidad Hipergeométrica"], tablefmt="grid"))
                    
                    sumar_probabilidades = input("¿Desea sumar las probabilidades? (si/no): ")
                    if sumar_probabilidades.lower() == "si":
                        probabilidad_acumulada = sum([distribucion_hipergeometrica(n, M, N, i) for i in range(x, n + 1)])
                        print(f"P(k ≥ {x}) = {probabilidad_acumulada:.4f}")
                
                else:
                    k = int(k)
                    resultado = distribucion_hipergeometrica(n, M, N, k)
                    print(tabulate([[f"k = {k}", f"P(k = {k}) = {resultado:.4f}"]], headers=["k", "Probabilidad Hipergeométrica"], tablefmt="grid"))
                                                                
            elif opcion == 4:
                    mu = float(input("Ingrese la media (μ): "))
                    sigma = float(input("Ingrese la desviación estándar (σ > 0): "))
                    if sigma <= 0:
                        raise ValueError("La desviación estándar debe ser mayor que 0")
                    x = float(input("Ingrese el valor de x: "))
                    
                    tipo_distribucion = input("¿Desea calcular la probabilidad para x <= valor, x >= valor o x = valor? (menor que, mayor que, igual a): ")

                    if tipo_distribucion == "menor que":
                        resultado = calcular_integral(mu, sigma, -float('inf'), x)
                        print(f"P(x ≤ {x}) = {resultado:.4f}")
        
                        sumar_probabilidades = input("¿Desea sumar las probabilidades? (si/no): ")
                        if sumar_probabilidades.lower() == "si":
                            probabilidad_acumulada = resultado
                            print(f"P(x ≤ {x}) = {probabilidad_acumulada:.4f}")
    
                    elif tipo_distribucion == "mayor que":
                        resultado = calcular_integral(mu, sigma, x, float('inf'))
                        print(f"P(x ≥ {x}) = {resultado:.4f}")
        
                        sumar_probabilidades = input("¿Desea sumar las probabilidades? (si/no): ")
                        if sumar_probabilidades.lower() == "si":
                            probabilidad_acumulada = resultado
                            print(f"P(x ≥ {x}) = {probabilidad_acumulada:.4f}")
    
                    elif tipo_distribucion == "igual a":
                        resultado = distribucion_normal(x, mu, sigma)
                        print(f"P(x = {x}) = {resultado:.4f}")
        
                        #sumar_probabilidades = input("¿Desea sumar las probabilidades? (si/no): ")
                        #if sumar_probabilidades.lower() == "si":
                            #probabilidad_acumulada = resultado
                            #print(f"P(x = {x}) = {probabilidad_acumulada:.4f}")
    
                    else:
                        raise ValueError("Opción de distribución no válida.")
                
        except ValueError as e:
            print(f"Error: {e}")
    
        except KeyboardInterrupt:
            print("\nSaliendo del menú de distribuciones...")

def ingresar_datos():
        cantidad = 0
        numeros = []
        print('Ingrese los datos uno por uno (ENTER), luego para ir al menú ingrese "n" \n')
        while True:
            numero = input(f"Ingrese el dato número {cantidad + 1}: ")
            if numero.lower() == "n":
                break
            else:
                try:
                    numero = float(numero)
                    cantidad += 1
                    numeros.append(numero)
                except ValueError:
                    print("Por favor, ingrese un número válido o escriba 'n' para terminar.")
        return numeros


def main():
        while True:
            try:
                print("\nMenú Principal:")
                print("A. Cálculos Estadísticos")
                print("B. Cálculos de Distribuciones")
                print("0. Salir")

                opcion_principal = input("Ingrese la opción que desea seleccionar: ").upper()

                if opcion_principal == "0":
                    print("Saliendo del programa...")
                    break
                elif opcion_principal == "A":
                    numeros = ingresar_datos()
                    menu_estadistico(numeros)
                elif opcion_principal == "B":
                    menu_distribuciones()
                else:
                    print("Opción no válida. Intente nuevamente.")
            except ValueError:
                print("Entrada no válida. Por favor, ingrese un número válido.")

if __name__ == "__main__":
        main()