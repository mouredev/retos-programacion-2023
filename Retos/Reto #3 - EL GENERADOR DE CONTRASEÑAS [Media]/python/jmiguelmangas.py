# Reto #3: EL GENERADOR DE CONTRASEÑAS
#### Dificultad: Media | Publicación: 16/01/23 | Corrección: 23/01/23

## Enunciado

"""
/*
 * Escribe un programa que sea capaz de generar contraseñas de forma aleatoria.
 * Podrás configurar generar contraseñas con los siguientes parámetros:
 * - Longitud: Entre 8 y 16.
 * - Con o sin letras mayúsculas.
 * - Con o sin números.
 * - Con o sin símbolos.
 * (Pudiendo combinar todos estos parámetros entre ellos)
 */
"""
import random
import string
def gen_password(number_characters):
    password = ""
    gen_list = ("int","char","caps","symbol")
    for _ in range(number_characters):
        set_character = random.choice(gen_list)
        match set_character:
            case "int": 
                password = password + str(random.randrange(10))
            case "char":
                password = password  + random.choice(string.ascii_letters)
            case "caps":
                password = password + random.choice(string.ascii_letters).upper()
            case "symbol":
                password = password + random.choice(string.punctuation)
    return password

def main():
    number_characters = random.randrange(8,16)
    
    print(f"Your random {number_characters} password is: {gen_password(number_characters)}")

if __name__ == "__main__":
    main()
