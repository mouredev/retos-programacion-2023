# Crea una función que sea capaz de leer el número representado por el ábaco.
# - El ábaco se representa por un array con 7 elementos.
# - Cada elemento tendrá 9 "O" (aunque habitualmente tiene 10 para realizar operaciones)
#   para las cuentas y una secuencia de "---" para el alambre.
# - El primer elemento del array representa los millones, y el último las unidades.
# - El número en cada elemento se representa por las cuentas que están a la izquierda del alambre.


ROWS_WEIGHTING = [
    1_000_000,
    100_000,
    10_000,
    1_000,
    100,
    10,
    1
]


def read_abacus(abacus_sequence: list[str]) -> int:
    # Yep
    #if not abacus_sequence or len(abacus_sequence) != 7 or any([(not "---" in row or row.count("O") != 9) for row in abacus_sequence]):
    if not abacus_sequence or len(abacus_sequence) != 7:
        raise ValueError("Introduce un ábaco válido")
    
    for row in abacus_sequence:
        if not "---" in row or row.count("O") != 9:
            raise ValueError("Introduce un ábaco válido")

    return sum((len(row.split("---")[0]) * ROWS_WEIGHTING[i]) for i, row in enumerate(abacus_sequence))


if __name__ == "__main__":
    abacus_sequence_1 = ["O---OOO0OOOO",
                         "OOO---OOOOOO",
                         "---OOOOOOOOO",
                         "OO---OOOOOOO",
                         "OOOOOOO---OO",
                         "OOOOOOOOO---",
                         "---OOOOOOOOO"]
    
    result1 = read_abacus(abacus_sequence_1)
    assert result1 == 1_302_790
    print(result1)

    abacus_sequence_2 = ["OOOO---OOOOO",
                         "O---OOOOOOOO",
                         "OOOOOOOOO---",
                         "OOOOOOOO---O",
                         "OOOO---OOOOO",
                         "---OOOOOOOOO",
                         "OOOOO---OOOO"]
    
    result2 = read_abacus(abacus_sequence_2)
    assert result2 == 4_198_405
    print(result2)