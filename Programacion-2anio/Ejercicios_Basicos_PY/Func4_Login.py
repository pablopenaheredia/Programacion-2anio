#Crear una subrutina llamada “Login”, que recibe un nombre de usuario y una contraseña y te
#devuelve Verdadero si el nombre de usuario es “usuario1” y la contraseña es “asdasd”.
#Además recibe el número de intentos que se ha intentado hacer login y si no se ha podido
#hacer login incremente este valor, validar con otra función la cantidad de intentos posibles en
#3 oportunidades.

def Login(usuario, contraseña):
    if usuario == "usuario1" and contraseña == "asdasd":
        return True
    else:
        return False
    
def validarIntentos(cantidadintentos):

    if cantidadintentos < 3:
        return True
    else:
        return False
    
def main():
    intentos = 0
    while validarIntentos(intentos):
        usuario = input("Ingrese su usuario: ")
        contraseña = input("Ingrese su contraseña: ")
        if Login(usuario, contraseña):
            print("Has logeado correctamente")
            break
        else:
            print("Intente nuevamente.")
            intentos += 1

if __name__ == "__main__":
    main()