"""
Crea un programa que realize el cifrado César de un texto y lo imprima.
También debe ser capaz de descifrarlo cuando así se lo indiquemos.

Te recomiendo que busques información para conocer en profundidad cómo
    realizar el cifrado. Esto también forma parte del reto.
"""

def cesar_cipher(
    text: str, shift: int, decipher: bool = False
    ) -> str:
    """
    Aplica el cifrado o descifrado César a un texto.

    Parámetros:
        text (str): Texto a procesar.
        shift (int): Número de posiciones a desplazar en el alfabeto.
        decipher (bool): Si es True, se aplica el descifrado (desplazamiento inverso).

    Retorna:
        str: Texto resultante tras aplicar el cifrado o descifrado.

    Lanza:
        TypeError: Si el valor de `text` no es una cadena.
    """

    if not isinstance(text, str):
        raise TypeError("Error. Solo se acepta texto como valor.")

    result = ""

    if decipher:
        shift *= -1

    for char in text:
        if char.isalpha():
            point_code = ord(char)
            if "A" <= char <= "Z":
                base = ord("A")
            elif "a" <= char <= "z":
                base = ord("a")
            new_point_code = ((point_code - base) + shift) % 26 + base
            result += chr(new_point_code)
        else:
            result += char

    return result


if __name__ == "__main__":
    print(cesar_cipher("Hola Mundo Yz XA", 2))
    print(cesar_cipher("Jqnc Owpfq Ab ZC", 2, decipher=True))
