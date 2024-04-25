def crypt(text, n, dictionary):
    outText = ""  # Texto que vamos a devolver
    for char in text:  # Obtenemos cada letra del texto
        if char in dictionary:  # Si la letra está en el diccionario
            charCode = dictionary.find(char)  # Buscamos la letra en el diccionario obteniendo su posición
            charCode += n  # Sumamos a la posición de la letra el desplazamiento
            if charCode >= len(dictionary):  # Si la nueva posición de la letra es mayor que el número de letras
                charCode -= len(dictionary)  # Restamos a la posición la longitud del diccionario, de esta forma evitamos que el algoritmo se salga del diccionario
            outText += dictionary[charCode]  # Metemos en el texto que vamos a devolver la letra
        else:  # En el caso de que no esté
            outText += char  # Metemos la letra en el texto para que no se desplacen el resto de letras y rompa el algoritmo
    return outText  # Devolvemos el texto


def decrypt(text, n, dictionary):
    outText = ""  # Texto que vamos a devolver
    for char in text:  # Obtenemos cada letra del texto
        if char in dictionary:  # Si la letra está en el diccionario
            charCode = dictionary.find(char)  # Buscamos la letra en el diccionario obteniendo su posición
            charCode -= n  # Restamos a la posición de la letra el desplazamiento
            if charCode < 0:  # Si la nueva posición de la letra es menor que cero (ya que  no hay índices menores que cero)
                charCode += len(dictionary)  # Sumamos a la posición la longitud del diccionario, de esta forma evitamos que el algoritmo se salga del diccionario
            outText += dictionary[charCode]  # Metemos en el texto que vamos a devolver la letra
        else:  # En el caso de que no esté
            outText += char  # Metemos la letra en el texto para que no se desplacen el resto de letras y rompa el algoritmo
    return outText  # Devolvemos el texto


def menu():  # Menu de inicio
    print(" _________________________________")
    print("|________Cifrado_del_Cesar________|")
    print("| 1.Desencriptar                  |")
    print("| 2.Encriptar                     |")
    print("| 3.Cambiar desplazamiento        |")
    print("| 4.Desencriptar por fuerza bruta |")
    print("| 5.Cambiar palabra               |")
    print("| 6.Salir                         |")
    print("|_________________________________|")
    opt = int(input(">>Seleccione una opción: ") + "\n")
    return opt


def main():
    dictionary = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"  # Diccionario que usaremos para encriptar y desencriptar
    n = 3  # Desplazamiento
    option = 0  # Inicializamos la opción del menú (da igual el valor porque va a cambiar)

    print()
    text = input(">>Introduzca la palabra: ")  # Texto introducido por el usuario

    while option != 6:  # Mientras que la opción no sea 5 (salir) ejecutamos el programa

        option = menu()  # Llamamos al menú

        # Dependiendo de la opción que hayamos seleccionado en el menú
        if option == 1:
            print()
            print("Desencriptado [" + text + "] --> " + decrypt(text, n, dictionary) + "\n")
        elif option == 2:
            print()
            print("Encriptado [" + text + "] --> " + crypt(text, n, dictionary) + "\n")
        elif option == 3:
            print()
            print("El desplazamiento actual es de: " + str(n) + " caracteres\n")

            n = int(input(">>Introduzca el nuevo desplazamiento: ") + "\n")

        elif option == 4:
            print()
            start = int(input(">>Introduzca el desplazamiento por el que empezar: ") + "\n")
            end = int(input(">>Introduzca el desplazamiento por el que terminar: ") + "\n")

            for i in range(start, end + 1):  # Llamamos a la función desencriptar pasándo diferentes desplazamientos
                print("Desencriptado[" + str(i) + "] [" + text + "] --> " + decrypt(text, i, dictionary))
        elif option == 5:
            print()
            print("La palabra actual es: " + text)
            print()
            text = input(">Introduce la nueva palabra: ")
        elif option == 6:
            print()
            print("Saliendo...")
        else:
            print()
            print("||-ERROR-|| --> La opcion introducida no es valida\n")


if __name__ == "__main__":
    main()
