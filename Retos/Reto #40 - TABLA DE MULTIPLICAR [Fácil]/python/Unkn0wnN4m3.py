#   Crea un programa que sea capaz de solicitarte un número y se
#   encargue de imprimir su tabla de multiplicar entre el 1 y el 10.
#   - Debe visualizarse qué operación se realiza y su resultado.
#     Ej: 1 x 1 = 1
#         1 x 2 = 2
#         1 x 3 = 3
#         ...


def m_table(number: int) -> None:
    txt = "{} x {} = {}"

    for i in range(1, 11):
        result = i * number
        print(txt.format(number, i, result))


def main():
    try:
        n = int(input("Give me a number: "))
    except ValueError as e:
        print("Invalid number:", e)
    else:
        m_table(n)


if __name__ == "__main__":
    main()
