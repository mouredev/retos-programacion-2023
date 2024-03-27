#!/usr/bin/python3

"""
# Reto #22: La espiral
/*
 * Crea una función que dibuje una espiral como la del ejemplo.
 * - Únicamente se indica de forma dinámica el tamaño del lado.
 * - Símbolos permitidos: ═ ║ ╗ ╔ ╝ ╚
 *
 * Ejemplo espiral de lado 5 (5 filas y 5 columnas):
 * ════╗
 * ╔══╗║
 * ║╔╗║║
 * ║╚═╝║
 * ╚═══╝
 */
"""

__author__ = "Jorge Lambraño - jelambrar96"
__copyright__ = "Copyright 2024, retos-programacion-2023"
__credits__ = ["Brais Moure - mouredev"]
__license__ = "GPL"
__version__ = "1.0.1"
__maintainer__ = "Jorge Lambraño"
__email__ = "jelambrar@gmail.com"
__status__ = "Production"


LINES = ["═", "║"] 
ELBOWNS = ["╗", "╝", "╚", "╔"]  

def base_espiral(n: int): 
    base = []
    temp = []
    for j in range(n):
        temp.append('*')
    for i in range(n):
        base.append(temp[:])
    return base


def show_espiral(espiral):
    for row in espiral:
        print("".join(row))
        

def espiral(n: int):
    
    if n == 0:
        return []
    elif n == 1:
        return [["╗"]]

    base = base_espiral(n)    
    count = 0
    count_limit = n * n
    
    border = 0
    row = 0
    col = 0
    while border < n // 2:
        
        for i in range (border, n - border - 1):
            base[border][i] = "═"
        base[border][n - border - 1] = "╗"
        
        for i in range (border + 1, n - border - 1):
            base[i][n - border - 1] = "║"
        base[n - border - 1][n - border - 1] = "╝"
                    
        for i in range (n - border - 2, border, -1):
            base[n - 1 - border][i] = "═"
        base[n - 1 - border][border] = "╚"           
            
        for i in range(n - border - 2, border + 1, -1):
            base[i][border] = "║"
        base[border + 1][border] = "╔" 
        
        border += 1
    
    if n % 2 == 1:
        base[n//2][n//2] = "╗"
    else:
        base[n//2][n//2 - 1] = "╚"
    
    return base
        

if __name__ == '__main__':
    for i in range(20):
        show_espiral(espiral(i))
