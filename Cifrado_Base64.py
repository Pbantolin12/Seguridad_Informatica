
def binaryToGroups(bin, nGruop):
    binaryGroup = []  # Creamos una variable para ir añadiendo los grupos binarios de 6 bits
    for i in range(0, len(bin), nGruop):  # Recorremos el binario desde el principio hasta el final, con incrementos de 6 posiciones
        group = bin[i:i + nGruop]  # Obtenemos la parte del binario que va desde la posición 'i' hasta la posición 'i + 6', es decir, 6 bits
        binaryGroup.append(group)  # Añadimos el grupo de 6 bits al resto de grupos
    return binaryGroup


def encodeBase(text, dictionary):
    outText = ""
    charToBin = ''  # Variable para almacenar el texto en binario
    for char in text:  # Recorremos el texto letra por letra
        charToBin += format(ord(char), '08b')  # Obtenemos el código ascii de cada letra y lo pasamos a binario (8 bits)
    binaryGroups = binaryToGroups(charToBin, 6)  # Llamamamos a la función para obtener los grupos binarios de  6 bits
    for group in binaryGroups:  # Obtenemos cada grupo del grupo de binarios de 6 bits
        if len(group) == 6:  # Si el grupo es de 6 bits
            binToInt = int(group, 2)  # Convertimos el grupo de bits a un número decimal
            outText += dictionary[binToInt]  # Convertimos el número decimal que es el código ascii de un caracter en el propio caracter
        else:  # En el caso de que no sea de 6 bits
            binToInt = int(group.zfill(6), 2)  # Rellenamos le grupo binario para que sea de 6 bits y lo convertimos a decimal
            outText += dictionary[binToInt]  # Añadimos al texto que vamos a imprimir la letra teniendo en cuenta la posición de la letra en el diccionario
            outText += '='  # Añadimos el caracter '=' para indicar que hemos rellenado con bits
    return outText


def decodeBase(text, dictionary):
    outText = ""  # Variable para almacenar el texto que vamos a devolver
    valueToBin = ''  # Lista para almacenar los valores binarios
    decimalValues = []  # Variable para almacenar la posición de la letra en el diccionario
    for char in text:  # Recorremos el texto caracter por caracter
        if char != '=':  # Si el caracter es distinto de '='
            charPos = dictionary.find(char)  # Obtenemos la posición del caracter en el diccionario
            decimalValues.append(charPos)  # Añadimos el valor de la posición a la lista
    for value in decimalValues:  # Recorremos la lista de valores
        valueToBin += bin(value)[2:].zfill(6)  # Pasamos el valor a binario, teniendo 6 bits
    binaryGroups = (binaryToGroups(valueToBin, 8))  # El binario que tenemos lo dividimos en grupos de 8 bits
    for group in binaryGroups:  # Recorremos la lista de binarios obteniendo cada grupo de 8 bits
        if len(group) == 8:  # Si el grupo es de  8 bits
            binToHex = hex(int(group, 2))  # Pasamos el binario a decimal y posteriormente a hexadecimal
            hexToChar = chr(int(binToHex, 16))  # Una vez que tenemos el hexadecimal lo pasamos a decimal y posteriormente obtenemos el caracter ascii
            outText += hexToChar  # Añadimos el caracter ascii al texto que vamos a devolver 
        else:
            groupCompleted = group.zfill(8)
            binToHex = hex(int(groupCompleted, 2))
            hexToChar = chr(int(binToHex, 16))
            if hexToChar != '\x00':
                outText += hexToChar
    return outText


def menu():  # Menu de inicio
    print(" ________________________")
    print("|_________Base64_________|")
    print("| 1.Decodificar          |")
    print("| 2.Codificar            |")
    print("| 3.Cambiar palabra      |")
    print("| 4.Salir                |")
    print("|________________________|")
    opt = int(input(">>Seleccione una opción: ") + "\n")
    return opt


def main():
    dictionary = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+/"  # Diccionario que usaremos para encriptar y desencriptar
    option = 0  # Inicializamos la opción del menú (da igual el valor porque va a cambiar)

    print()
    text = input(">>Introduzca la palabra: ")  # Texto introducido por el usuario

    while option != 4:  # Mientras que la opción no sea 5 (salir) ejecutamos el programa

        option = menu()  # Llamamos al menú

        # Dependiendo de la opción que hayamos seleccionado en el menú
        if option == 1:
            print()
            print("Decodificado [" + text + "] --> " + decodeBase(text, dictionary) + "\n")
        elif option == 2:
            print()
            print("Codificado [" + text + "] --> " + encodeBase(text, dictionary) + "\n")
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
