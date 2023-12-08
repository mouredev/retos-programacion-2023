# Reto #16: La escalera
#### Dificultad: Media | Publicación: 17/04/23 | Corrección: 24/04/23 | Mi Solucion: 18/10/23
## Enunciado
"""
 * Crea una función que dibuje una escalera según su número de escalones.
 * - Si el número es positivo, será ascendente de izquiera a derecha.
 * - Si el número es negativo, será descendente de izquiera a derecha.
 * - Si el número es cero, se dibujarán dos guiones bajos (__).
 * 
 * Ejemplo: 4
 *         _
 *       _|       
 *     _|
 *   _|
 * _|
 * 
 */
"""

def escaleras(escalones: int):
    if escalones>0:
        for escalon in range(escalones +1):
            #el valor es un doble espacio en blanco porque sino queda superpuesta visualmente
            espacios = "  "*(escalones - escalon)
            peldaño = "_" if escalon==0 else "_|"
            print(f"{espacios}{peldaño}")
            
    elif escalones<0:
        #como escalones es una variable negativa lo transformamos a un valor positivo con abs()
        for escalon in range(abs(escalones) +1):
            espacios = " "*(escalon*2 - 1)
            peldaño = "_" if escalon==0 else "|_"
            print(f"{espacios}{peldaño}")
    else:
        print("__")

if __name__ == "__main__":        
    escaleras(0)
    escaleras(5)
    escaleras(-5)