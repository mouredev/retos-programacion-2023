# Reto #3: EL GENERADOR DE CONTRASEÑAS
#### Dificultad: Media | Publicación: 16/01/23 | Corrección: 23/01/23

## Enunciado

'''
/*
 * Escribe un programa que sea capaz de generar contraseñas de forma aleatoria.
 * Podrás configurar generar contraseñas con los siguientes parámetros:
 * - Longitud: Entre 8 y 16.
 * - Con o sin letras mayúsculas.
 * - Con o sin números.
 * - Con o sin símbolos.
 * (Pudiendo combinar todos estos parámetros entre ellos)
 */
 '''
 
import random, string

def create_password():
    dictionary = list(string.ascii_lowercase)
    characters = int(input('Indique la cantidad de caracteres entre 8 y 16 => '))
    if characters < 8 or characters > 17:
        print('La password debe estar entre los valores mencionados')
        exit()
    upper = input('Coloque "Y" si desea que contenga letras en mayusculas, en caso contrario coloque "N" => ').upper()
    number = input('Coloque "Y" si desea que contenga numeros, en caso contrario coloque "N" => ').upper()
    symbol = input('Coloque "Y" si desea que contenga simbolos, en caso contrario coloque "N" => ').upper()
    if upper not in ['Y','N'] or number not in ['Y','N'] or symbol not in ['Y','N']:
        print('Alguna opcion fue incorrecta...')
        exit()
    
    if upper == 'Y':
        dictionary += list(string.ascii_uppercase)
    if number == 'Y':
        dictionary += list(string.digits)
    if symbol == 'Y':
        dictionary += list(string.punctuation)
    password=''.join(random.sample(dictionary,characters))
    return(password)
   
    
print(create_password())
