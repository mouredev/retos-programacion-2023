# Reto #20: La Trifuerza
#### Dificultad: Media | Publicación: 15/05/23 | Corrección: 22/05/23 | Mi Solución : 20/11/23
## Enunciado
"""
 	¡El nuevo "The Legend of Zelda: Tears of the Kingdom" ya está disponible! 
 
  Crea un programa que dibuje una Trifuerza de "Zelda"
  formada por asteriscos.
  - Debes indicarle el número de filas de los triángulos con un entero positivo (n).
  - Cada triángulo calculará su fila mayor utilizando la fórmula 2n-1.
 
  Ejemplo: Trifuerza 2
  
     *
    ***
   *   *
  *** ***
"""

def trifuerza(n: int) -> None:
    longitud = 2 * n

    for i in range(1, n + 1):
        text = "*" * (2 * i - 1)
        text = text.center(longitud * 2)
        print(text)

    for i in range(1, n + 1):
        text = "*" * (2 * i - 1)
        text = text.center(longitud)*2        
        print(text)    


if __name__ == "__main__":
    trifuerza(abs(int(input("Indica tu fuerza: "))))