'''
/*
 * Escribe un programa que reciba un texto y transforme lenguaje natural a
 * "lenguaje hacker" (conocido realmente como "leet" o "1337"). Este lenguaje
 *  se caracteriza por sustituir caracteres alfanuméricos.
 * - Utiliza esta tabla (https://www.gamehouse.com/blog/leet-speak-cheat-sheet/) 
 *   con el alfabeto y los números en "leet".
 *   (Usa la primera opción de cada transformación. Por ejemplo "4" para la "a")
 */

'''



import string

leet_alphabet = ['4','I3','[',')','3','|=','&','#','1',',_|','>|','1', ' /\/\ ','^/','0','|*','(_,)','I2','5','7','(_)','\/','\/\/','><','j','2']
leet_numbers = ['L','R','E','A','S','b','T','B','g','o',' ']

my_hacker_list = leet_alphabet + leet_numbers

my_normal_list = [i for i in string.ascii_lowercase] + ['1','2','3','4','5','6','7','8','9','0',' ']

def to_hacker_language (my_str):
    my_list = []
    my_leet_list = []

    for a in my_str.lower():
        my_list.append(a)
    for b in my_list:
        my_index = my_normal_list.index(b)
        my_leet_list.append(my_hacker_list[my_index])
        my_leet_str = ''.join(my_leet_list)

    print(f'{my_str} en lenguaje hacker es: {my_leet_str}')


to_hacker_language('Retos de programacion semanal 2023')