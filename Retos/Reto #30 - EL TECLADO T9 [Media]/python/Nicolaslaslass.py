#  * Los primeros dispositivos móviles tenían un teclado llamado T9
#  * con el que se podía escribir texto utilizando únicamente su
#  * teclado numérico (del 0 al 9).
#  *
#  * Crea una función que transforme las pulsaciones del T9 a su
#  * representación con letras.
#  * - Debes buscar cuál era su correspondencia original.
#  * - Cada bloque de pulsaciones va separado por un guión.
#  * - Si un bloque tiene más de un número, debe ser siempre el mismo.
#  * - Ejemplo:
#  *     Entrada: 6-666-88-777-33-3-33-888
#  *     Salida: MOUREDEV
#  */


t9_dict = {'2': 'A', '22': 'B', '222': 'C', '3': 'D', '33': 'E', '333': 'F', '4': 'G', '44': 'H', '444': 'I', '5': 'J', '55': 'K', '555':'L', '6':'M', '66':'N', '666': 'O',
           '7': 'P', '77': 'Q', '777': 'R', '7777': 'S', '8': 'T', '88': 'U', '888': 'V', '9':'W', '99': 'X', '999':'Y', '9999':'Z'}

entrada = input('Entrada:')

def separador(entrada):
    
    letra = entrada.split('-') #el metodo split ya crea una lista por si misma.
    return letra

def t9_to_text(entrada):
    
    lista_convertida = separador(entrada) #
    t9_list = []
    
    for i in lista_convertida:
        if i in t9_dict.keys():
            t9_list.append(t9_dict[i])
        elif i not in t9_dict.keys():
            print('secuencia no valida')
            break

    t9_word = ''.join(t9_list) #recordar que exite join
    return t9_word

print(t9_to_text(entrada))













        
        


