import random, string
# titulo
print('*'.center(50,'*'))
print('GENERADOR ALEATORIO DE CONTRASEÑAS'.center(50,'-'))
print('*'.center(50,'*'))

# input
input_text = int(input('\nBienvenido\nla longitud debe ser de entre 8 y 16 caracteres\nlongitud de la contraseña: '))

# si no tiene entre 8 y 16 caracteres 
if input_text < 8 or input_text > 16:
     print('la longitud no es de entre 8 y 16 caracteres')

# si tiene entre 8 y 16 caracteres 
else:     
     print('\nOpciones:\n\n1. numeros\n2. letras\n3. caracteres especiales\n\n4. Finalizar\n')

     input_characters = '' # para agregar los caracteres
     while True:          
          option = int(input('escribe el numero para agregar la opcion:  '))
          match option:
               case 1: input_characters += string.digits # agrega numeros
               case 2: input_characters += string.ascii_letters # agrega letras
               case 3: input_characters += string.punctuation # agrega simbolos
               case 4: break # termina el programa
               case _: print('opcion invalida, puedes digitar 4 para finalizar\n')

     new_password = []
     for simbol in range(input_text): # rango de la longitud de la contraseña
          # agrega a la lista la cantidad de caracteres elejidos aleatoriamente
          new_password.append(random.choice(input_characters))
     
     print('\nLa contraseña es:      ' + "".join(new_password))

