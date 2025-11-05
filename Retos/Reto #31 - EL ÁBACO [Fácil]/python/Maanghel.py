"""
Crea una función que sea capaz de leer el número representado por el ábaco.
- El ábaco se representa por un array con 7 elementos.
- Cada elemento tendrá 9 "O" (aunque habitualmente tiene 10 para realizar
    operaciones) para las cuentas y una secuencia de "---" para el alambre.
- El primer elemento del array representa los millones, y el último las unidades.
- El número en cada elemento se representa por las cuentas que están a
    la izquierda del alambre.

Ejemplo de array y resultado:
["O---OOOOOOOO",
"OOO---OOOOOO",
"---OOOOOOOOO",
"OO---OOOOOOO",
"OOOOOOO---OO",
"OOOOOOOOO---",
"---OOOOOOOOO"]

Resultado: 1.302.790
"""

def abacus(sequence: list[str]) -> int:
    """
    Interpreta el valor numérico representado por un ábaco japonés (soroban simplificado).

    args:
    sequence : list[str]
        Lista de 7 cadenas, donde cada cadena representa una fila del ábaco.
        Cada fila contiene una secuencia de "O" (cuentas) y "---" (el alambre separador).
        Las cuentas situadas a la izquierda del alambre representan el valor de la posición.
        - La primera fila corresponde a los millones.
        - La última fila corresponde a las unidades.

    Ejemplo
    -------
    >>> abacus([
    ... "O---OOOOOOOO",
    ... "OOO---OOOOOO",
    ... "---OOOOOOOOO",
    ... "OO---OOOOOOO",
    ... "OOOOOOO---OO",
    ... "OOOOOOOOO---",
    ... "---OOOOOOOOO"])

    returns:
    int: El número entero correspondiente al valor indicado por el ábaco.

    Excepciones
    -----------
    TypeError
        Si el argumento no es una lista.
    ValueError
        Si la lista no contiene exactamente 7 elementos o si alguno no es una cadena.

    Notas
    -----
    - Cada línea debe tener 9 cuentas "O" en total, divididas por el alambre "---".
    - Este tipo de representación se usa comúnmente en ejercicios de lógica y programación.
    """
    if not isinstance(sequence, list):
        raise TypeError("Error. Solo se acepta una lista para representar el abaco.")
    if not sequence or len(sequence) < 7:
        raise ValueError("Error. La lista debe contener 7 elementos.")
    if not all(isinstance(value, str) for value in sequence):
        raise ValueError("Error. La lista solo puede contener cadenas de texto.")

    result = 0
    for index, line in enumerate(sequence, 1):
        digit = line.split("---")[0].count("O")
        result += digit * (10 ** (7 - index))
    return int(result)

if __name__ == "__main__":
    value = ["O---OOOOOOOO",
            "OOO---OOOOOO",
            "---OOOOOOOOO",
            "OO---OOOOOOO",
            "OOOOOOO---OO",
            "OOOOOOOOO---",
            "---OOOOOOOOO"]

    print(abacus(value))
