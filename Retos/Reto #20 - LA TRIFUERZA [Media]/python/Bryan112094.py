'''
/*
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
 */
 '''

class trifuerza:
    def __init__(self) -> None:
        pass
    
    #Espacio inicial para los asteriscos
    def espace_init(self, espa):
        return ((2 * espa) - 1)
    
    #El numero de asteriscos por fila
    def total_asterisk(self, aste):
        return (('*') * (2 * aste - 1))
    
    #El espacio entre el inicio de la fila y el asterisco
    def total_espace(self, espa):
        return ((' ') * espa)
    
    #El espacio entre los triangulos de los asteriscos
    def total_espace2(self, espa):
        return ((' ') * (2 * espa + 1))

    #Pintar los triangulos
    def print_triangles(self, num):
        cant_espace = self.espace_init(num)

        for val in range(1, num + 1):
            print(f'{self.total_espace(cant_espace)}{self.total_asterisk(val)}')
            cant_espace -= 1
        
        for val in range(1, num + 1):            
            print(f'{self.total_espace(cant_espace)}{self.total_asterisk(val)}{self.total_espace2(cant_espace)}{self.total_asterisk(val)}')
            cant_espace -= 1

    def go(self):
        print("Trifuerza de \"Zelda\"")
        try:
            numero = int(input("Ingrese la cantidad de fuerza: "))
            if numero > 0:
                self.print_triangles(numero)
            else:
                print('Fuerza mayor a 0')
        except:
            print('Dato ingresado no válido')

tri = trifuerza()
tri.go()