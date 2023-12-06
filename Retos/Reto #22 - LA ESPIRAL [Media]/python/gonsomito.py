"""
 * Crea una función que dibuje una espiral como la del ejemplo.
 * - Únicamente se indica de forma dinámica el tamaño del lado.
 * - Símbolos permitidos: ═ ║ ╗ ╔ ╝ ╚
 *
 * Ejemplo espiral de lado 5 (5 filas y 5 columnas):
 * ═ ═ ═ ═ ╗
 * ╔ ═ ═ ╗ ║
 * ║ ╔ ╗ ║ ║
 * ║ ╚ ═ ╝ ║
 * ╚ ═ ═ ═ ╝
"""
#cuando tengo un valor entero, compruebo que sea mayor que 1 para pintar, 
#ya que estrictamente, una espiral de 1x1 podría ser un ".".
#Pinto la primera fila, y las sucesivas según corresponda. Mitad con codos abajo, mitad codos arriba
def espirulina(lines):
    if lines > 1:
        print("═ "*(lines-1)+"╗")
        for l in range(1,lines-(lines//2)):
            print("║ "*(l-1) + "╔ " + "═ "*(lines-(2*l) - 1) + "╗ " + "║ "*l)
        for l in range(lines-(lines//2), lines):
            print("║ "*(lines-l-1) + "╚ " + "═ "*(2*l-lines) + "╝ " + "║ "*((lines-l)-1))      

#Pido tamaño de espiral y compruebo que me facilitan un entero.
lineas = input("Cual es el tamaño de la espiral: ")
if lineas.isdigit():
    espirulina(int(lineas))
else:
    print("No es un valor correcto. Me gustan las espirales de más grandes.")
