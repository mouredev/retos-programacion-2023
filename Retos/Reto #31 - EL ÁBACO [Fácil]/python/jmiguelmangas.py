"""```
/*
 * Crea una función que sea capaz de leer el número representado por el ábaco.
 * - El ábaco se representa por un array con 7 elementos.
 * - Cada elemento tendrá 9 "O" (aunque habitualmente tiene 10 para realizar operaciones)
 *   para las cuentas y una secuencia de "---" para el alambre.
 * - El primer elemento del array representa los millones, y el último las unidades.
 * - El número en cada elemento se representa por las cuentas que están a la izquierda del alambre.
 *
 * Ejemplo de array y resultado:
 * ["O---OOOOOOOO",
 *  "OOO---OOOOOO",
 *  "---OOOOOOOOO",
 *  "OO---OOOOOOO",
 *  "OOOOOOO---OO",
 *  "OOOOOOOOO---",
 *  "---OOOOOOOOO"]
 *
 *  Resultado: 1.302.790
 */
```"""


def check_abaco(list_abaco):
    for abaco_row in list_abaco:
        counter_o = 0
        counter_space = 0
        for character in abaco_row:
            match (character):
                case "O":
                    counter_o += 1
                case "-":
                    counter_space += 1
                case _:
                    return False
        if counter_o > 9 or counter_space > 3:
            return False
    return True


def translate_abaco_number(abaco):
    lista_numeros = []
    for abaco_row in abaco:
        counter_row = 0
        for character in abaco_row:
            if character == "O":
                counter_row += 1
            else:
                break
        lista_numeros.append(str(counter_row))
    return lista_numeros


def main():
    abaco = [
        "OO---OOOOOOO",
        "OOO---OOOOOO",
        "---OOOOOOOOO",
        "OO---OOOOOOO",
        "OOOOOOO---OO",
        "OOOOOOOOO---",
        "---OOOOOOOOO",
    ]
    print(abaco)
    if check_abaco(abaco):
        print("".join(translate_abaco_number(abaco)))
    else:
        raise ValueError("El abaco introducido no es correcto")


if __name__ == "__main__":
    main()
