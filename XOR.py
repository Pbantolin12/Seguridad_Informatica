

def extendKey(key, text):
    timesToRepeat = len(text) // len(key)  # Hacemos la división entera para saber cuántas veces tenemos que repetir la clave
    keyExtended = key * timesToRepeat  # Repetimos la clave el número de veces que sea necesario
    keyExtended += key[:len(text) % len(key)]  # Hacemos el módulo de la división entre la longitud de la palabra y la clave para añadir los caracteres que faltan (ya que la clave no está entera)
    return keyExtended


  # En este caso sólo tenemos una función ya que la operción contraria a XOR es la misma operación XOR, por lo que hay que tratar el texto de la misma manera en ambos casos
def codeDecodeXOR(text, key):
    outText = ""  # Variable en la que vamos a almacenar el texto que devolvamos
    for i in range(len(text)):  # Recorremos desde la posición cero hasta la última posición de la palabra
        XorOperation = ord(text[i]) ^ ord(key[i])  # Pasamos los caracteres de la clave y el texto a su valor hexadecimal en ascii y hacemos la operación XOR
        outText += chr(XorOperation)  # Convertimos el valor que hemos obtenido a caracter y lo añadimos al texto que vamos a devolver
    return outText


def menu():  # Menu de inicio
    print(" _________________________________")
    print("|_______________XOR_______________|")
    print("| 1.Desencriptar                  |")
    print("| 2.Encriptar                     |")
    print("| 3.Cambiar palabra               |")
    print("| 4.Salir                         |")
    print("|_________________________________|")
    opt = int(input(">>Seleccione una opción: ") + "\n")
    return opt


def main():
    option = 0   # Inicializamos la opción del menú (da igual el valor porque va a cambiar)
    key = "XOR"

    print()
    text = input(">>Introduzca la palabra: ")  # Texto introducido por el usuario
    key = extendKey(key, text)

    while option != 4:  # Mientras que la opción no sea 5 (salir) ejecutamos el programa

        option = menu()  # Llamamos al menú

        # Dependiendo de la opción que hayamos seleccionado en el menú
        if option == 1:
            print()
            print("Decodificado [" + text + "] --> " + codeDecodeXOR(text, key) + "\n")
        elif option == 2:
            print()
            print("Codificado [" + text + "] --> " + codeDecodeXOR(text, key) + "\n")
        elif option == 3:
            print()
            print("La palabra actual es: " + text)
            print()
            text = input(">Introduce la nueva palabra: ")
            key = extendKey(key, text)
        elif option == 4:
            print()
            print("Saliendo...")
        else:
            print()
            print("||-ERROR-|| --> La opcion introducida no es valida\n")


if __name__ == "__main__":
    main()
