def saludo(nombre:str="kerry Berga") -> str:
    """Esta Función imprimi un saludo a la esa persona a la que desea sorprender.

    Args:
        nombre (str): nombre de la persona.

    Returns:
        str: Returna un saludo con el valor de entrada.
    """

    return print(f"!Hola {nombre}! :)")

if __name__ == "__main__":
    saludo()