import time

def generar_numero_pseudoaleatorio(semilla, inicio, fin):
    a = 1103515245
    c = 12345
    m = 2**31 - 1
    numero = (a * semilla + c) % m
    rango = fin - inicio + 1
    return inicio + (numero % rango)


def run():
    inicio = int(input('Inicio: '))
    fin = int(input('Fin: '))
    semilla = int(time.strftime("%S"))
    numero_aleatorio = generar_numero_pseudoaleatorio(semilla, inicio, fin)
    print('Tu numero aleatorio es:', numero_aleatorio)


if __name__ == '__main__':
    run()