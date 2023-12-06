"""
¡El nuevo "The Legend of Zelda: Tears of the Kingdom" ya está disponible! 
Crea un programa que dibuje una Trifuerza de "Zelda" formada por asteriscos *.
- Debes indicarle el número de filas de los triángulos con un entero positivo (n).
- Cada triángulo calculará su fila mayor utilizando la fórmula 2n-1.

Ejemplo: Trifuerza 2
    *
   ***
  *   *
 *** ***
"""

#funcion trifuerza a la que le llega un número entero. 
#con ella despliego el resto de cálculos ya dados en el enunciado. Uso 2 variables auxiliares para multiplicar "*" y " ".
#La clave reside en el método center(longitud, relleno) que nos ayudará a centrar el texto para una longitud concreta.
def trifuerza(n):
    asterisco = 1
    espacio = 1
#en este while pintamos el triangulo superior de la trifuerza
    while asterisco <= (2*n-1):
        cadena = "*"*asterisco
        print(cadena.center(1+(2*n-1)*2, " "))
        asterisco = asterisco+2
        espacio=espacio+1
#en este while pintamos el otro grupo de dos triangulo de la trifuerza
    asterisco = 1
    espacio = 1
    while asterisco <= (2*n-1):
        cadena = "*"*asterisco
        print(cadena.center(2*n-1, " ") +" "+ cadena.center(2*n-1, " "))
        asterisco = asterisco+2
        espacio=espacio+1

filas = input("DAME EL NÚMERO DE FILAS")
if filas.isdigit():
    trifuerza(int(filas))
else:
    print("NO HAY ~TRIFUEZA~ PARA ESE VALOR")
