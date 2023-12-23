# Reto #22: La espiral
#### Dificultad: Media | Publicación: 29/05/23 | Corrección: 06/06/23 | Solución : 30/11/23

## Enunciado

"""
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

import math

def draw_spiral(n):
    half = math.ceil(n / 2)
    print(f"Espiral de longitud: {n}")
    #dibujo superior
    print('═' * (n - 1)  + '╗')
    for i in range(1,half):
        print('║' * (i - 1) + '╔' + '═' * (n - 2 * i - 1) + '╗' + '║' * i)
    
    #dibujo inferior
    for i in range(n - half):
        print('║' * (n - half - i - 1) + '╚' + '═' * ((n % 2) + 2 * i) + '╝' + '║' * (n - half - i - 1))
        
            
if __name__ == "__main__":
    draw_spiral(5)
    draw_spiral(7)
    draw_spiral(11)
    draw_spiral(21)