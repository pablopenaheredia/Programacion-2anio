from producto import Producto

class Electronico(Producto): #Se crea un objeto hijo (Electronico) a partir de la clase padre Producto
    def __init__(self, nombre, precio, cantidad, marca, modelo): #Debe crearse con todos los atributos del padre mas los propios de electronico
        super().__init__(nombre, precio, cantidad) #super se usa para llamar los atributos de la clase padre
        self.marca = marca #marca y modelo son los atributos propios del objeto electronico
        self.modelo = modelo

    
    def mostrar_info_electronico(self): #funcion para mostrar los atributos del objeto hijo electronico
        super().mostrar_info_producto()  #se llama al método para mostrar la info del producto padre, y se suma los del hijo
        print(f"Marca: {self.marca}"
              f"\nModelo: {self.modelo}")