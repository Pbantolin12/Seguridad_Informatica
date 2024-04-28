from Crypto.Cipher import AES
from Crypto.Util.Padding import pad


def encodeAES(text, key, iv):
    cipher = AES.new(key, AES.MODE_CBC, iv)  # Creamos un nuevo objeto de cifrado AES en modo CBC
    ciphertext = cipher.encrypt(pad(text.encode('utf-8'), AES.block_size))  # Con el objeto creado anteriormente ciframos el texto, rellenándolo con la función pad para que el tamaño sea de 16 bytes
    return ciphertext.hex()  # Devolvemos el texto cifrado en formato hexadecimal


def decodeAES(text, key, iv):
    cipher = AES.new(key, AES.MODE_CBC, iv)  # Creamos un nuevo objeto de cifrado AES en modo CBC
    decrypted = cipher.decrypt(bytes.fromhex(text))   # Decodifica el texto cifrado a binario
    return decrypted.decode('utf-8')  # Devolvemos el texto cifrado en formato hexadecimal


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
    key = b'SeguridadInforma'  # Clave del cifrado
    iv = b'SeguridadInforma'  # iv del cifrado
    option = 0  # Inicializamos la opción del menú (da igual el valor porque va a cambiar)


    print()
    text = input(">>Introduzca la palabra: ")  # Texto introducido por el usuario

    while option != 4:  # Mientras que la opción no sea 5 (salir) ejecutamos el programa

        option = menu()  # Llamamos al menú

        # Dependiendo de la opción que hayamos seleccionado en el menú
        if option == 1:
            print()
            print("Decodificado [" + text + "] --> " + decodeAES(text, key, iv) + "\n")
        elif option == 2:
            print()
            print("Codificado [" + text + "] --> " + encodeAES(text, key, iv) + "\n")
        elif option == 3:
            print()
            print("La palabra actual es: " + text)
            print()
            text = input(">Introduce la nueva palabra: ")
        elif option == 4:
            print()
            print("Saliendo...")
        else:
            print()
            print("||-ERROR-|| --> La opcion introducida no es valida\n")


if __name__ == "__main__":
    main()