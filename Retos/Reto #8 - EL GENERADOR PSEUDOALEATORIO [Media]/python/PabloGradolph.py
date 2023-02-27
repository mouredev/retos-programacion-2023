'''
/*
 * Crea un generador de números pseudoaleatorios entre 0 y 100.
 * - No puedes usar ninguna función "random" (o semejante) del lenguaje de programación seleccionado.
 *
 * Es más complicado de lo que parece...
 */
 '''
import time

def generador(cantidad: int, maxim: int, infl: str) -> list:
    u = [] # Lista donde guardaremos los números aleatorios

    # Valores iniciales (semillas)
    m = 2**31 - 1
    a = 7**5
    x0 = time.time_ns()

    # Cálculo número aleatorio
    for n in range(cantidad):
        if n >= 69: # Si n > 69 trae problemas al elevar.
            x0 = time.time_ns()
            n = 1
        xn = (a**n * x0 + (a**n - 1)/(a-1)) % m
        if infl == "Enteros":
            un = round(xn/m * maxim)
        else:
            un = round(xn/m * maxim, 2)
        u.append(un)

    return u

def main():
    print("GENERADOR DE NÚMEROS ALEATORIOS")
    cantidad = int(input("¿Cuántos números aleatorios quieres generar? "))
    maximo = int(input("Números aleatorios desde el 0 hasta el... "))
    tipo = int(input("1 - Enteros \
                 2 - Decimales \
                     Elige: "))
    if tipo == 1:
        u = generador(cantidad , maximo, "Enteros")
    elif tipo == 2:
        u = generador(cantidad , maximo, "Decimales")
    else:
        print("Error en la entrada. Ejecute de nuevo.")
    print(f"Tus números aleatorios son: {u}")

if __name__ == "__main__":
    main()