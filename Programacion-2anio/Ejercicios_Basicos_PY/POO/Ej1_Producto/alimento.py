from producto import Producto

class Alimento(Producto):  #Se crea un objeto hijo (alimento) a partir de la clase padre Producto
    def __init__(self, nombre, precio, cantidad, fecha_expiracion):#Debe crearse con todos los atributos del padre mas los propios de alimento
        super().__init__(nombre, precio, cantidad) #super se usa para llamar los atributos de la clase padre
        self.fecha_expiracion = fecha_expiracion #fecha_expiracion es el atributo propios del objeto alimento

    
    def mostrar_info_alimento(self): #funcion para mostrar los atributos del objeto hijo alimento
       super().mostrar_info_producto() #se llama al método para mostrar la info del producto padre, y se suma los del hijo
       print(f"Fecha de Expiracion: {self.fecha_expiracion}")