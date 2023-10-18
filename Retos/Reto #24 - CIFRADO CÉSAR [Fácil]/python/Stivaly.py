# Creamos una lista estatica con el abecedario y una lista de tuplas dinamica para poder movilizar los valores y mantener la trazabilidad.
main_cesar = ["A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z"]
cesar_roulette = [("A", 0),("B", 1),("C", 2),("D" , 3),("E", 4),("F", 5),("G", 6),("H", 7),("I", 8),("J", 9),("K", 10),("L", 11),("M", 12),("N", 13),
                  ("O", 14),("P", 15),("Q", 16),("R", 17),("S", 18),("T", 19),("U", 20),("V", 21),("W", 22),("X", 23),("Y", 24),("Z", 25)]

# Generamos el proceso de encriptación con la opción 1
while True:
    opcion = int(input("Escoge 1 para encriptar o 2 para descencriptar: "))
    if opcion == 1:
        # Solicitamos la clave para realizar la encriptación y la frase que vamos a encriptar
            key = int(input("Ingresa clave del 0 al 25"))
            phrase = input("Ingresa la palabra que deseas cifrar").replace(" ","")
            # Movilizamos la posición de los indices de la lista dinamica
            cesar_roulette = cesar_roulette[-key:] + cesar_roulette[:-key]
            encrypt = ""
            # Realizamos el proceso de encriptación
            for letter in phrase:
                for index, letter_list in enumerate(main_cesar):
                    if letter == letter_list:
                        encrypt += cesar_roulette[index][0]

            print(encrypt)
            break
    elif opcion == 2:
        # Solicitamos la clave para realizar la descencriptación y la frase que vamos a encriptar
            key = int(input("Ingresa clave del 0 al 25"))
            phrase = input("Ingresa la palabra que deseas cifrar").replace(" ","").upper()
            # Movilizamos la posición de los indices de la lista dinamicas
            cesar_roulette = cesar_roulette[-key:] + cesar_roulette[:-key]
            decrypt = ""
            # Realizamos el proceso de encriptación
            for letter in phrase:
                for index, letter_list in enumerate(cesar_roulette):
                    if letter == letter_list[0]:
                        decrypt += main_cesar[index]
            print(decrypt)
            break
    else:
            print("Opción inválida.")
