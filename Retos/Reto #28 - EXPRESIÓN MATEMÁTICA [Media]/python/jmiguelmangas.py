"""
```
/*
 * Crea una función que reciba una expresión matemática (String)
 * y compruebe si es correcta. Retornará true o false.
 * - Para que una expresión matemática sea correcta debe poseer
 *   un número, una operación y otro número separados por espacios.
 *   Tantos números y operaciones como queramos.
 * - Números positivos, negativos, enteros o decimales.
 * - Operaciones soportadas: + - * / % 
 *
 * Ejemplos:
 * "5 + 6 / 7 - 4" -> true
 * "5 a 6" -> false
 */
```"""


def get_operation():
    try:
        return input("Operacion Matematica: ").strip().split(sep=" ")
    except ValueError:
        print(
            "Introduce una operacion matematica valida separada por espacios: (1 + 2, 3 / 4)"
        )


def check_valid_operation(valores):
    for i in range(len(valores)):
        if i % 2 != 0:
            match (valores[i]):
                case "*" | "/" | "+" | "-":
                    continue
                case _:
                    return False
                    break
        else:
            try:
                float(valores[i])
            except:
                return False
    return True


def main():
    if check_valid_operation(get_operation()):
        print("Operación Valida")
    else:
        print("Operación Incorrecta")


if __name__ == "__main__":
    main()
