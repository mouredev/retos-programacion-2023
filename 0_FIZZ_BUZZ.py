def fizz_buzz(primer_numero: int = 1, segundo_numero: int = 100) -> None:
    """
    Imprime una serie de números desde `primer_numero` hasta `segundo_numero` junto con palabras especiales
    dependiendo de si son múltiplos de `primer_numero`, `segundo_numero` o ambos.

    Parámetros:
    - primer_numero (int): El primer número del rango.
    - segundo_numero (int): El último número del rango.

    Ejemplo de uso:
    fizz_buzz(1, 100)
    """
    for i in range(primer_numero, segundo_numero + 1):
        if i % 3 == 0 and i % 5 == 0:
            print(f"{i} FIZZ AND BUZZ")
        elif i % 3 == 0:
            print(f"{i} FIZZ")
        elif i % 5 == 0:
            print(f"{i} BUZZ")
        else:
            print(i)

fizz_buzz()

"""
la función fizz_buzz tiene una complejidad O(n) porque el tiempo de ejecución es linealmente proporcional a la longitud del rango de números especificado por primer_numero y segundo_numero.

"""