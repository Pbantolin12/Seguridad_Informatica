

def extendKey(key, text):
    timesToRepeat = len(text) // len(key)  # Hacemos la división entera para saber cuántas veces tenemos que repetir la clave
    keyExtended = key * timesToRepeat  # Repetimos la clave el número de veces que sea necesario
    keyExtended += key[:len(text) % len(key)]  # Hacemos el módulo de la división entre la longitud de la palabra y la clave para añadir los caracteres que faltan (ya que la clave no está entera)
    keySpaced = ""  # Variable para elmacenar la clave con espacios
    for i in range(len(text)):  # Recorremos desde cero hasta la longitud de la palabra
        if text[i] == ' ':  # En el caso de que el caracter sea un espacio
            keySpaced = keyExtended[:i] + ' ' + keyExtended[i: - 1]  # Con la posición del espacio dividimos la clave, añadimos un espacio y añadimos la otras parte de la clave que hemos dividido quitándole un caracter ya que al añadir el espacio sobra uno
    if keySpaced != "":  # En el caso de que la clave tenga espacios la devolvemos
        return keySpaced
    else:  # Si no teiene espacios la devolvemos isn espacios
        return keyExtended


def encodeVig(text, dictionary, key):
    outText = ""  # Variable en la que vamos a almacenar el texto que devolvamos
    for i in range(len(text)):  # Recorremos desde la posición cero hasta la última posición de la palabra
        if text[i] != ' ':  # Si el no es un espacio
            charPos = dictionary.find(text[i])  # Obtenemos la posición del caracter de la palabra
            keyPos = dictionary.find(key[i])  # Obtenemos la posición del caracter de la clave
            encodedPos = charPos + keyPos  # Sumamos las dos posiciones para obtener las posición final que tendrá la codificación
            if encodedPos >= len(dictionary):  # En el caso de que la posición se salga del rango del diccionario
                encodedPos -= len(dictionary)  # Restamos la longitud del diccionario
            outText += dictionary[encodedPos]  # Añadimos el nuevo caracter al texto que vamos a devolver
        else:  # En el caso de que el caracter sea un espacio
            outText += ' '  # Agregamos un espacio al texto que vamos a devolver
    return outText


def decodeVig(text, dictionary, key):
    outText = ""  # Variable en la que vamos a almacenar el texto que devolvamos
    for i in range(len(text)):  # Recorremos desde la posición cero hasta la última posición de la palabra
        if text[i] != ' ':  # Si el no es un espacio
            charPos = dictionary.find(text[i])  # Obtenemos la posición del caracter de la palabra
            keyPos = dictionary.find(key[i])  # Obtenemos la posición del caracter de la clave
            encodedPos = charPos - keyPos  # Restamos las dos posiciones para obtener las posición final que tendrá la codificación
            if encodedPos < 0:  # En el caso de que la posición sea menor que el rango del diccionario
                encodedPos += len(dictionary)  # Restamos la longitud del diccionario
            outText += dictionary[encodedPos]  # Añadimos el nuevo caracter al texto que vamos a devolver
        else:  # En el caso de que el caracter sea un espacio
            outText += ' '  # Agregamos un espacio al texto que vamos a devolver
    return outText


def menu():  # Menu de inicio
    print(" ________________________")
    print("|________Vigenere________|")
    print("| 1.Decodificar          |")
    print("| 2.Codificar            |")
    print("| 3.Cambiar palabra      |")
    print("| 4.Salir                |")
    print("|________________________|")
    opt = int(input(">>Seleccione una opción: ") + "\n")
    return opt


def main():
    dictionary = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"  # Diccionario que usaremos para encriptar y desencriptar
    key = "Vinagre"  # Clave del cifrado
    option = 0  # Inicializamos la opción del menú (da igual el valor porque va a cambiar)

    print()
    text = input(">>Introduzca la palabra: ")  # Texto introducido por el usuario
    key = extendKey(key, text)

    while option != 4:  # Mientras que la opción no sea 5 (salir) ejecutamos el programa

        option = menu()  # Llamamos al menú

        # Dependiendo de la opción que hayamos seleccionado en el menú
        if option == 1:
            print()
            print("Decodificado [" + text + "] --> " + decodeVig(text, dictionary, key) + "\n")
        elif option == 2:
            print()
            print("Codificado [" + text + "] --> " + encodeVig(text, dictionary, key) + "\n")
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
