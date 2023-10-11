def tabla_multiplicacion(number: int) -> str:
    """ Funcion encargue de imprimir su tabla de multiplicar entre el 1 y el 10.
    Args:
        number (int): Numero del cual se quiere obtener la tabla de multiplicar.
    Returns:
        str: Tabla de multiplicar del numero ingresado.
    Nota:
        Debe visualizarse qué operación se realiza y su resultado.
        Ej: 1 x 1 = 1
            1 x 2 = 2
            1 x 3 = 3
    """
    return "\n".join([f"{number} x {inicio} = {number*inicio}" for inicio in range(1, 11)])

if __name__ == "__main__":
    continuar = 'si'
    while continuar.lower() == "si":
        valor = int(input('Ingrese un numero para obtener su tabla de multiplicar \n'))
        if valor >= 0:
            print(tabla_multiplicacion(valor))
            continuar = input('¿Desea continuar? (si/no) \n')
            continue
        print('El numero ingresado debe ser positivo')
