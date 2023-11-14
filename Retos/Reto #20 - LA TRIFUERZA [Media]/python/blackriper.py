"""
 La solucion esta hecha de forma recursiva para quien no sabe
 que es es una funcion que se llama o retorna asi misma al hacer
 esto es como si fuera un ciclo por eso usamos la condicion
 if valor == 0: return para cuando el valor sea cero la llamada
 del metodo termine y no forme un loop infinito.


"""


def space_tri(space: int):
    if space == 0:
        return
    print(" ", end="")
    space_tri(space-1)


def triangle(n: int):
    if n == 0:
        return
    return '* '*n
    triangle(n-1)


def triangle_top(n: int, count: int, base: int):
    if n == 0:
        return
    space_tri(base)
    print(triangle(count-n+1))
    return triangle_top(n-1, count, base-1)


def triangle_bottom(n: int, count: int, base: int):
    if n == 0:
        return
    space_tri(n-1)
    print(triangle(count-n+1), end="")
    space_tri(n-1)
    space_tri(n-1)
    print(triangle(count-n+1))
    return triangle_bottom(n-1, count, base-1)


def triforce(n: int):
    if n == 0:
        print(" ")
    height = 2*n
    base = height-1
    triangle_top(n, n, base)
    triangle_bottom(n, n, base)


def main():
    n = int(input("Introduce el numero de filas de la triforce: "))
    triforce(n)


if __name__ == "__main__":
    main()
