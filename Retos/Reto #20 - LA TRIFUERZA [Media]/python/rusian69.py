"""
 *	¡El nuevo "The Legend of Zelda: Tears of the Kingdom" ya está disponible! 
 *
 * Crea un programa que dibuje una Trifuerza de "Zelda"
 * formada por asteriscos.
 * - Debes indicarle el número de filas de los triángulos con un entero positivo (n).
 * - Cada triángulo calculará su fila mayor utilizando la fórmula 2n-1.
 *
 * Ejemplo: Trifuerza 2
 * 
 *    *
 *   ***
 *  *   *
 * *** ***
 *
Con n = 2 saldría:

no vean el simbolo sino que generen cuadros separados que den la forma toda la explicacion esta en la funcion detallada

1:☐☐☐★☐☐☐☐
2:☐☐★★★☐☐☐

3:☐★☐☐☐★☐☐
4:★★★☐★★★☐

 *
"""
def trifuerza (n: int) -> None:
    longitud = 2 * n
#triagulo superior

    for iten in range(1, n + 1): #desde 1 a  (n) rango que surcara
        simbol = "*" * (2 * iten - 1) # cantidad de asteriscos que usara es igual a 2 * valor de iten - 1
        simbol = simbol.center(longitud * 2) # centraliza la cantidad de asteriscos en la longitud multiplicada por 2
        print(simbol)# imprime
#triagulos inferiores

    for iten in range(1, n + 1): #desde 1 a (n) rango que surcara
        simbol = "*" * (2 * iten - 1) # cantidad de asteriscos que usara es igual a 2 * valor de iten - 1
        simbol = simbol.center(longitud) # centraliza la cantidad de asteriscos en la longitud ya establecida
        simbol = simbol * 2 # multiplica el resultado del calculo de la longitud anterior
        print(simbol)# imprime
# funcion main
def main():
    n = int(input("Ingrese el numero: "))
    trifuerza(n)

#llamada a la funcion
if __name__ == "__main__":
    main()
