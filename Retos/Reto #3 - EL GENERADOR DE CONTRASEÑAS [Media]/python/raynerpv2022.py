# /*
# Reto #3: EL GENERADOR DE CONTRASEÑAS
#  * Escribe un programa que sea capaz de generar contraseñas de forma aleatoria.
#  * Podrás configurar generar contraseñas con los siguientes parámetros:
#  * - Longitud: Entre 8 y 16.
#  * - Con o sin letras mayúsculas.
#  * - Con o sin números.
#  * - Con o sin símbolos.
#  * (Pudiendo combinar todos estos parámetros entre ellos)
#  */

import random
import string
# data
number = list(string.digits)
Upper_case = list(string.ascii_uppercase)
lower_case = list(string.ascii_lowercase)
symbol = list(string.punctuation)

def random_data():
     return random.choice([True,False])

# if element l is in  password list
def is_in(l,source):
     for i in l:
          if i in source:
               return True
     return False

#  validating password, dependind data value
def validate_passw(a):
    
    if upper_case :
        if  not is_in(a,Upper_case):
           return False
          
    if number_case :
        if  not is_in(a,number):
            return False
         
    if symbol_case :
        if  not is_in(a,symbol):
            return False
    return True
    
               

leng_passw = random.randrange(8,16)
upper_case =  random_data()
number_case =  random_data()
symbol_case =  random_data()
password_list = lower_case

if upper_case :
      password_list += "".join(Upper_case)
if number_case :
     password_list+= "".join(number)
if symbol_case :
    password_list += "".join(symbol)


print("LENG passWORD :", leng_passw)

print("UPPER CASE :",upper_case)
print("NUMBER :", number_case)
print("Symbol :",symbol_case)

# using random.sample
while True:
    a = "".join(random.sample(password_list,leng_passw))
    if validate_passw(a):
        break
          
     
print(a)
#  using list comprehention
while True:
    b = "".join([str(random.choice(password_list))  for x in range(leng_passw)])
    if validate_passw(b):
        break
print(b)


