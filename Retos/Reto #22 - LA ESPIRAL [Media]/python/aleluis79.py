# Crea una función que dibuje una espiral como la del ejemplo.
# - Únicamente se indica de forma dinámica el tamaño del lado.
# - Símbolos permitidos: ═ ║ ╗ ╔ ╝ ╚
# Ejemplo espiral de lado 5 (5 filas y 5 columnas):
# ════╗
# ╔══╗║
# ║╔╗║║
# ║╚═╝║
# ╚═══╝

import math


def espiral(lado):
    superior = (math.ceil(lado / 2))
    
    for i in range(superior):
        if (i == 0):
            print(("═"*(lado-1)) + "╗")
        else:
            print(("║"*(i-1)+ "╔" + "═"*(lado - (2*i)-1)) + "╗" + "║"*i)
    
    for i in range(superior, lado):
        print("║"*(lado-i-1)+ "╚" + "═"*((2*i)-lado) + "╝" + "║"*(lado-i-1))
    
espiral(3)
espiral(5)
espiral(10)
espiral(30)