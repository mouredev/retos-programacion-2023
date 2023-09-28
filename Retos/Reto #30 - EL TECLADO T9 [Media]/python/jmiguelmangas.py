"""```
/*
 * Los primeros dispositivos móviles tenían un teclado llamado T9
 * con el que se podía escribir texto utilizando únicamente su
 * teclado numérico (del 0 al 9).
 *
 * Crea una función que transforme las pulsaciones del T9 a su
 * representación con letras.
 * - Debes buscar cuál era su correspondencia original.
 * - Cada bloque de pulsaciones va separado por un guión.
 * - Si un bloque tiene más de un número, debe ser siempre el mismo.
 * - Ejemplo:
 *     Entrada: 6-666-88-777-33-3-33-888
 *     Salida: MOUREDEV
 */
```"""
keyboard = {
    "1": ",.?!",
    "2": "ABC",
    "3": "DEF",
    "4": "GHI",
    "5": "JKL",
    "6": "MNO",
    "7": "PQRS",
    "8": "TUV",
    "9": "WXYZ",
    "0": " ",
}


def get_t9_code():
    return input("Escribe el codigo T9: ").strip().split("-")


def check_t9_code(list_t9):
    for block in list_t9:
        for i in range(len(block)):
            if block[i] != block[0]:
                raise ValueError("Los caracteres de cada bloque tienen que ser iguales")
    return list_t9


def translate_t9(list_t9):
    translation = []
    for block in list_t9:
        if block[0] in keyboard:
            traduction_string = keyboard[block[0]]
        translation.append(traduction_string[len(block) - 1])
    return translation


def main():
    lista = check_t9_code(get_t9_code())
    print("".join(translate_t9(lista)))


if __name__ == "__main__":
    main()
