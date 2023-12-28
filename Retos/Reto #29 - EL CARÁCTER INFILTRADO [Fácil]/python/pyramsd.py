def diferencia(arg1:str, arg2:str) -> list:
    """Resumen

    Args:
        arg1: (str)
        arg2: (str)

    Raises:
        ValueError: Si la longitud de los argumentos no son iguales

    Returns:
        list: lista de diferencias entre los argumentos
    """
    
    if len(arg1) != len(arg2):
        raise ValueError("Los argumentos deben ser de la misma longitud")

    lista_diferencia = []
    for i in range(len(arg1)):
        if arg1[i] != arg2[i]:
            lista_diferencia.append(arg2[i])
    
    print(lista_diferencia)


diferencia("Me llamo mouredev", "Me llemo mouredov")
