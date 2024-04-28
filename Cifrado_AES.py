from Cryptodome.Cipher import AES
from Cryptodome.Util.Padding import pad, unpad
import base64

def encodeAES(text, key):
    crypt = AES.new(key, AES.MODE_CBC)
    outText = crypt.encrypt(pad(text.encode(), AES.block_size))
    return base64.b64encode(crypt.iv + outText)


def decodeAES(text, key):
    encodedText = base64.b64decode(text)
    iv = encodedText[:AES.block_size]
    crypt = AES.new(key, AES.MODE_CBC, iv = iv)
    outText = unpad(crypt.decrypt(encodedText[:AES.block_size]), AES.block_size)
    return outText.decode()


def menu():  # Menu de inicio
    print(" _________________________")
    print("|___________AES___________|")
    print("| 1.Decodificar           |")
    print("| 2.Codificar             |")
    print("| 3.Cambiar palabra       |")
    print("| 4.Salir                 |")
    print("|_________________________|")
    opt = int(input(">>Seleccione una opción: ") + "\n")
    return opt


def main():
    dictionary = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"  # Diccionario que usaremos para encriptar y desencriptar
    key = "Vinagre"  # Clave del cifrado
    option = 0  # Inicializamos la opción del menú (da igual el valor porque va a cambiar)

    print()
    text = input(">>Introduzca la palabra: ")  # Texto introducido por el usuario

    while option != 4:  # Mientras que la opción no sea 5 (salir) ejecutamos el programa

        option = menu()  # Llamamos al menú

        # Dependiendo de la opción que hayamos seleccionado en el menú
        if option == 1:
            print()
            print("Decodificado [" + text + "] --> " + decodeAES(text, key) + "\n")
        elif option == 2:
            print()
            print("Codificado [" + text + "] --> " + encodeAES(text, key) + "\n")
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