'''
/*
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
'''

def built_stairway(number:int) -> None:
    up:str = '_|'
    down:str = '|_'
    first_line:str= (' '*( number+2 ) )+ '_'

    if number== 0:
        print('__') 
    else:
        print(first_line)
        for i in range(abs(number)):
            sttairway = ( ' '*(number-i) )+ up if number>0 else ( ' '* i ) + down
            print(sttairway)

   
built_stairway(4)
