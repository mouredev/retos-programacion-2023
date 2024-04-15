# Reto #29: El carácter infiltrado
#### Dificultad: Fácil | Publicación: 17/07/23 | Corrección: 24/07/23

## Enunciado

"""
/*
 * Crea una función que reciba dos cadenas de texto casi iguales,
 * a excepción de uno o varios caracteres. 
 * La función debe encontrarlos y retornarlos en formato lista/array.
 * - Ambas cadenas de texto deben ser iguales en longitud.
 * - Las cadenas de texto son iguales elemento a elemento.
 * - No se pueden utilizar operaciones propias del lenguaje
 *   que lo resuelvan directamente.
 * 
 * Ejemplos:
 * - Me llamo mouredev / Me llemo mouredov -> ["e", "o"]
 * - Me llamo.Brais Moure / Me llamo brais moure -> [" ", "b", "m"]
 */
"""



def infiltrated_characters(first_text, second_text):
    new_list = []

    if len(first_text) == len(second_text):
        i = 0
        while i < len(first_text):
            if first_text[i] != second_text[i]:
                new_list.append(second_text[i])
            
            i = i + 1
        return new_list
    
    else:
        return "La longitud de ambos textos no son iguales."

print(infiltrated_characters("La llama es un mamifero", "La Llana es un mamífero"))
print(infiltrated_characters("Ñono es un niño feliz", "Ñoño es un nino feliz"))
print(infiltrated_characters("Te Llama la yama", "Te llama la llama"))