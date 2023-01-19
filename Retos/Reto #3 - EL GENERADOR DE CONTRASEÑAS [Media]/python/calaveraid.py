#  Escribe un programa que sea capaz de generar contraseñas de forma aleatoria.
#  Podrás configurar generar contraseñas con los siguientes parámetros:
#  - Longitud: Entre 8 y 16.
#  - Con o sin letras mayúsculas.
#  - Con o sin números.
#  - Con o sin símbolos.
#  (Pudiendo combinar todos estos parámetros entre ellos)

from random import sample

def passwordCreator(lenght=8, caps=False, nums=False, symb=False):
    chars = [chr(x) for x in range(ord('a'), ord('z')+1)]
    if lenght < 8 or lenght > 16:
        print('Wrong lenght (8 -16)')
        return None
    if caps:
        chars.extend([chr(x) for x in range(ord('A'), ord('Z')+1)])
    if nums:
        chars.extend([chr(x) for x in range(ord('0'), ord('9')+1)])
    if symb:
        chars.extend(list(',;.:/*-+¡¿?!$&()=@#'))

    return ''.join(sample(chars, lenght))

print(passwordCreator(10, True, True, True))
print(passwordCreator(12, True))
print(passwordCreator(16, True, True))
print(passwordCreator(nums=True, symb=True))
