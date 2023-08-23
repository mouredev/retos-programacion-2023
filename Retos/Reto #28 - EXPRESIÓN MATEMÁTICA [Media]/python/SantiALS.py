'''
/*
 * Crea una función que reciba una expresión matemática (String)
 * y compruebe si es correcta. Retornará true o false.
 * - Para que una expresión matemática sea correcta debe poseer
 *   un número, una operación y otro número separados por espacios.
 *   Tantos números y operaciones como queramos.
 * - Números positivos, negativos, enteros o decimales.
 * - Operaciones soportadas: + - * / % 
 *
 * Ejemplos:
 * "5 + 6 / 7 - 4" -> true
 * "5 a 6" -> false
 
 *'''


def reto_23(ecuetion: str): # La función fuerza a que el parámetro de entrada sea un str
    
    terms = ecuetion.split() # Separo los términos de la ecuación en una lista para analizarlos individualmente.

    if len(terms) < 3 or '**' in terms or '//' in terms: # Si la cantidad de elementos de la lista es menor a 3 quiere decir que la ecuación es del tipo ('1 +') ó ('1 ') ó ('1') 
         veredicto = 'False'
    else:

        aprobado=[]
        contador = 0
       
        find_alpha = [caracter.isalpha() for caracter in ecuetion]  #Busca si hay letras en la ecuación, si las hay devuelve un true para invalidar la ecuación.
        check = any(find_alpha)

        if check == True: # Si hay letras en la ecuación sale de la función con veredicto FALSO
            veredicto = 'False'

        else:
            for x in terms: # Analiza cada término de la ecuación para corroborar que sean todos números ó solamente un signo de operación
            
                if '+' in x or '-' in x or '*' in x or '/' in x or '%' in x: # Analiza si el término tiene signos
                    aprobado.append(False) # Si el término tiene signo se le asigna un valor FALSE a la lista de "aprobado"
                else:
                    aprobado.append(True) # Si el término no tiene signo se le asigna un valor TRUE a la lista de "aprobado"
                
                if any(caracter.isnumeric() for caracter in x): # Si el término tiene algún número se mantiene el valor asignado en el análisis de signo del la línea:21,
                                                                # lo que indica que es un término que tiene signo y número sin espacio intercalado entre ellos.
                    pass
                else:
                    aprobado[contador] = True #Si no contiene números según el análisis de la línea:26, entonces es un término de sólo signo y toma el valor de TRUE
                
                contador += 1
            
            check = all(aprobado) # Si todos los valores de la lista aprobados son TREU, la ecuación se corresponde con el enunciado.
            if  check == False:
                veredicto = 'False'
            else:
                veredicto = 'True'

    return print (f'{ecuetion} --> {veredicto}')


reto_23('10 + 56')
reto_23('10.5 + 56 - 2 / 2 * 5')
reto_23('10.5 + 56- 2')
reto_23('10.5a + 56- 2')
reto_23('6')
reto_23('10.5 + 56 ** 2 - 2')
reto_23('10.5 + 56 // 2 - 2')
reto_23('10.5 + 56** 2 - 2')
reto_23('10.5 + 56// 2 - 2')



