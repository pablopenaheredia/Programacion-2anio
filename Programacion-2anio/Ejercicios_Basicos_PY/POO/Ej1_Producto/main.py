#se importa la clase Producto de producto.py, Electronico del archivo electronico.py, lo mismo con alimento
from producto import Producto
from electronico import Electronico
from alimento import Alimento

def main(): #Se define el programa principal creando un objeto producto, uno electronico y uno alimento, con sus atributos propios

    producto = Producto("Perfume", 25000, 35)
    producto.mostrar_info_producto()

    electronico = Electronico("Celular", 60000, 10, "Motorola", "G31")
    electronico.mostrar_info_electronico()

    alimento = Alimento("Mayonesa", 2000, 15, "31/06/2026") #idem objeto electronico, pero con el objeto alimento
    alimento.mostrar_info_alimento()

if __name__ == "__main__":
    main()