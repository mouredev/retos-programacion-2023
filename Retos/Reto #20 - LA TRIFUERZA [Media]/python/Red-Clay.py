# /*
#  *	¡El nuevo "The Legend of Zelda: Tears of the Kingdom" ya está disponible! 
#  *
#  * Crea un programa que dibuje una Trifuerza de "Zelda"
#  * formada por asteriscos.
#  * - Debes indicarle el número de filas de los triángulos con un entero positivo (n).
#  * - Cada triángulo calculará su fila mayor utilizando la fórmula 2n-1.
#  *
#  * Ejemplo: Trifuerza 2
#  * 
#  *    *
#  *   ***
#  *  *   *
#  * *** ***
#  *
#  *      *
#  *     ***
#  *    *   *
#  *   *** ***
#  *  *   *   *
#  * *** *** ***
#  */
def zelda(filas):

    for x in range(1,filas+1):
        n=filas+1-x #3+1-1=3
        ast3=2*n-1  #2*3-1=5
        ast1=2*n    #2*3=6
        esp1=ast1*" " # 6 espacios
        esp2=ast3*" " # 5 espacios
        print(esp1+"*   "*x)
        print(esp2+"*** "*x)
        
def main():
    res=int(input("Trifuerza  "))
    zelda(res)

if __name__=="__main__":
    main()

    
