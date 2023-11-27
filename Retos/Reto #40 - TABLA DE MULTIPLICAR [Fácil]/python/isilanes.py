def print_table_of(num: int | float) -> None:
    """
    Dado un número 'num' (no se especifica si entero, real,
    positivo o negativo), imprime su "tabla de multiplicar",
    tal que:
    num x  1 = ...
    num x  2 = ...
    ...
    num x 10 = ...

    Args:
        num (int, float): número cuya tabla queremos imprimir.

    Returns:
        Nada. Imprime directamente.
    """
    if not isinstance(num, (int, float)):
        print(f"{num} no es un número válido. Ignorando...")
        return

    for i in range(1, 11):
        print(f"{num} x {i:2d} = {num*i}")


def get_number() -> int | float | None:
    """
    Solicita un número al usuario. Introducir un valor que no pueda
    procesarse no eleva un error, sino que ignora e imprime un mensaje.

    Returns:
        Devuelve el input del usuario, convertido en int o float. Si el usuario
        desea salir, introducirá una "q", y la función devolverá None.
    """
    while True:
        number = input("Introduce un número (q = salir): ")

        if number == "q":
            return None

        try:
            if "." in number:
                return float(number)
            else:
                return int(number)
        except ValueError:
            print("Ese valor es inválido. Introduce un número, o la letra 'q' para salir.")


if __name__ == "__main__":
    while True:
        input_number = get_number()
        if input_number is None:
            break
        print_table_of(input_number)
