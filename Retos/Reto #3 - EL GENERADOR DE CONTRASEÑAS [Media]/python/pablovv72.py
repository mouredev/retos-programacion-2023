from random import choice, shuffle


def genera_clave(longitud=8, mayusculas=True, numeros=True, simbolos=True):
    caracteres_minusculas = 'abcdefghijklmnñopqrstuvwxyz'
    caracteres_mayusculas = 'ABCDEFGHIJKLMNÑOPQRSTUVWXYZ'
    caracteres_numeros = '0123456789'
    caracteres_simbolos = 'ºª\\!|"@·#$%&/()=?\'¿¡€^`[*+]¨´{}><;,:._-'
    
    contraseña = ''
    
    # Asegura que almenos exista un caracter del tipo elegido en la contraseña
    contraseña += choice(caracteres_mayusculas) if mayusculas else ''
    contraseña += choice(caracteres_numeros) if numeros else ''
    contraseña += choice(caracteres_simbolos) if simbolos else ''
    
    # Genera una paleta de la cual se eligirán los caracteres
    paleta = caracteres_minusculas + (
        caracteres_mayusculas if mayusculas else '') + (
            caracteres_numeros if numeros else '') + (
                caracteres_simbolos if simbolos else '')
                
    # Rellena caracteres hasta completar el tamaño de la contraseña
    while len(contraseña) < longitud:
        contraseña += choice(paleta)
    
    # Mezcla todos los caracteres de la contraseña
    contraseña = list(contraseña)
    shuffle(contraseña)
    
    return ''.join(contraseña)
