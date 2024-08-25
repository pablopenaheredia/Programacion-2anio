'''Objetivo: Crear una clase padre llamada Producto y dos clases hijas que hereden de ella. Las clases hijas
deben heredar ciertos atributos de la clase Producto y agregar atributos específicos de cada tipo de
producto en esas clases hijas, deben estar en otro archivo .py cada una de ellas.

Detalles del Ejercicio
1. Definir la clase Producto:
○ La clase Producto debe tener los siguientes atributos:
■ nombre: El nombre del producto.
■ precio: El precio del producto.
■ cantidad: La cantidad disponible del producto.
○ La clase Producto debe tener un método para mostrar la información del producto.
2. Definir dos clases hijas:
○ Electronico:
■ Atributos adicionales: marca, modelo.
■ Método para mostrar la información específica del producto electrónico.
○ Alimento:
■ Atributos adicionales: fecha_expiracion.
■ Método para mostrar la información específica del producto alimenticio.

3. Implementar las clases:
○ Cada clase hija debe llamar al constructor de la clase Producto para inicializar los atributos
heredados.
○ Cada clase hija debe tener un método para mostrar la información completa del producto,
incluyendo los atributos específicos de la clase hija.
'''

class Producto: #Creacion del objeto producto con los atributos nombre, precio y cantidad
    def __init__(self, nombre, precio, cantidad):
        self.nombre = nombre
        self.precio = float(precio)
        self.cantidad = int(cantidad)   
    
    def mostrar_info_producto(self): #Funcion para mostrar los atributos
       print(f"\nLos datos del producto son:"
              f"\nNombre: {self.nombre}"
              f"\nPrecio: ${self.precio}"
              f"\nCantidad: {self.cantidad} unidades")
