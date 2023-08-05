# Reto 31: EL ábaco
# by gerickt
import time


# Calculo de tiempo
def time_func(func):
    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        end = time.time()
        print(f"Tiempo transcurrido: {(end - start)*1000:.3f} ms")
        return result

    return wrapper


# iteradores
@time_func
def read_abacus(abaco: list):
    numero = ""
    for cuenta in abaco:
        index = cuenta.find("-")
        numero += str(index)
    return "Resultado: {:,}".format(int(numero)).replace(",", ".")


# list comprehension
@time_func
def read_abacus_comprehension(abaco: list):
    lista = [str(cuenta.find("-")) for cuenta in abaco]
    numero = int("".join(lista))
    return "Resultado: {:,}".format(numero).replace(",", ".")


if __name__ == "__main__":
    input = [
        "O---OOOOOOOO",
        "OOO---OOOOOO",
        "---OOOOOOOOO",
        "OO---OOOOOOO",
        "OOOOOOO---OO",
        "OOOOOOOOO---",
        "---OOOOOOOOO",
    ]

    print(read_abacus(input))
    print(read_abacus_comprehension(input))
