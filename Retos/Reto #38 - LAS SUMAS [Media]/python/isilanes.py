# Solution to Reto #38 - LAS SUMAS.
from typing import Optional


def grow(initial: list[int], remaining: list[int], left: int) -> list[tuple[list, Optional[list], int]]:
    """
    Dadas dos lista de enteros 'initial' y 'remaining', y un entero 'left', devolver todas las tuplas
    (a, b, c), tales que:
    - a: lista compuesta por la adición a 'initial' de UN elemento 'x' de 'remaining' tal que x <= left
    - b: lista compuesta por los elementos de 'remaining' a la derecha de 'x'
    - c: resultante de restar 'x' a 'left'

    Args:
        initial (list): lista de enteros que queremos crecer en un elemento.
        remaining (list): lista de enteros de la que tomaremos un elemento
                          para añadir a 'initial'.
        left (int): entero cuyo valor no puede sobrepasar el elemento
                    de 'remaining' que añadamos a 'initial'.

    Returns:
        Conjunto de todos los tríos de valores (a, b, c) que cumplan las condiciones expuestas.
    """
    results = []
    for i, value in enumerate(remaining):
        if value > left:
            break

        new_initial = initial + [value]  # no uso list.append() pq quiero copiar, no modificar in place
        new_remaining = [] if value == left else remaining[i+1:]
        new_left = left - value
        results.append((new_initial, new_remaining, new_left))

    return results


def run(numbers: list[int], target: int, verbose: bool = False) -> list:
    """
    Resuelve el problema.
    """
    so_far = [([], sorted(numbers), target)]

    growth = True
    while growth:
        growth = False
        new_so_far = []
        for combo in so_far:
            # Los combos que ya están bien, los dejamos tal cual:
            if combo[-1] == 0 and combo not in new_so_far:
                new_so_far.append(combo)
                continue

            # Los combos que pueden crecer, los hacemos crecer:
            new = grow(*combo)
            if new:
                growth = True

            for new_combo in new:
                new_so_far.append(new_combo)

        so_far = new_so_far

    result = [c[0] for c in so_far]

    if verbose:
        print(f"Requested target '{target}' from list '{numbers}'.\nResults:")
        for combo in result:
            print(combo)

    return result


if __name__ == "__main__":
    run(numbers=[1, 5, 3, 2], target=4, verbose=True)
    run(numbers=[1, 5, 3, 2, 2, 4, 1], target=4, verbose=True)
    run(numbers=[1, 1, 1, 2, 2, 2], target=3, verbose=True)


