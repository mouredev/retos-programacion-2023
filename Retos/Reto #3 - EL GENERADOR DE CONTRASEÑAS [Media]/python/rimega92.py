# Escribe un programa que sea capaz de generar contraseñas de forma aleatoria.
# Podrás configurar generar contraseñas con los siguientes parámetros:
# - Longitud: Entre 8 y 16.
# - Con o sin letras mayúsculas.
# - Con o sin números.
# - Con o sin símbolos.
# (Pudiendo combinar todos estos parámetros entre ellos)

import random
import string

def generar_contrasena(longitud, mayusculas, numeros, simbolos):
      caracteres = string.ascii_lowercase
      if mayusculas:
         caracteres += string.ascii_uppercase
      if numeros:
         caracteres += string.digits
      if simbolos:
         caracteres += string.punctuation
      contrasena = ''.join(random.choice(caracteres) for i in range(longitud))
      return contrasena

def main():
   longitud = int(input("Longitud de la contraseña: "))
   mayusculas = input("¿Incluir mayúsculas? (S/N): ")
   numeros = input("¿Incluir números? (S/N): ")
   simbolos = input("¿Incluir símbolos? (S/N): ")
   if mayusculas == 'S':
      mayusculas = True
   else:
      mayusculas = False
   if numeros == 'S':
      numeros = True
   else:
      numeros = False
   if simbolos == 'S':
      simbolos = True
   else:
      simbolos = False
   contrasena = generar_contrasena(longitud, mayusculas, numeros, simbolos)
   print(contrasena)

if __name__ == '__main__':
   main()