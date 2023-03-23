"""
    * Escribe un programa que muestre por consola (con un print) los
    * números de 1 a 100 (ambos incluidos y con un salto de línea entre
    * cada impresión), sustituyendo los siguientes:
    * - Múltiplos de 3 por la palabra "fizz".
    * - Múltiplos de 5 por la palabra "buzz".
    * - Múltiplos de 3 y de 5 a la vez por la palabra "fizzbuzz".
"""


def build_str(i: int) -> str:
    if i % 3 == 0 and i % 5 == 0:
        return 'fizzbuzz'

    if i % 3 == 0:
        return 'fizz'

    if i % 5 == 0:
        return 'buzz'

    return str(i)


def run(i: int = 1, data_fold: str = '') -> str:
    if i > 100:
        return data_fold

    return run(i+1, f'{data_fold}\n{build_str(i)}')


if __name__ == '__main__':
    print(run())
