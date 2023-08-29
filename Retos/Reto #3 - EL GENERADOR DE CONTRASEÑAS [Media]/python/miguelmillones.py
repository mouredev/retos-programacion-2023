#Reto #3: EL GENERADOR DE CONTRASEÑAS
## Enunciado
# Escribe un programa que sea capaz de generar contraseñas de forma aleatoria.
# Podrás configurar generar contraseñas con los siguientes parámetros:
#* - Longitud: Entre 8 y 16.
#* - Con o sin letras mayúsculas.
#* - Con o sin números.
#* - Con o sin símbolos.
#* (Pudiendo combinar todos estos parámetros entre ellos)
import string
import random

N=0
MAYUS=''
NUM=''
CHAR=''

def parameters(mayus,num,char,n):
    data_lower=string.ascii_lowercase
    password=''.join(random.choices(data_lower,k=n))
    if mayus=='yes':
        may=password[0]
        data_upper=string.ascii_uppercase
        passw=''.join(random.choices(data_upper,k=n))
        password=passw+password
        password=''.join(random.choices(password,k=n))
        may=passw[0]+may
        n=n-2
        password=may+password[0:n]

    if num=='yes':
        n=N
        memory=password[0:2]
        data_num=string.digits
        passn=''.join(random.choices(data_num,k=n))
        password=passn+password
        password=''.join(random.choices(password,k=n))
        numer=passn[0]+memory
        n=n-3
        password=numer+password[0:n]

    if char=='yes':
        n=N
        memory=password[0:3]
        data_char=string.punctuation
        passc=''.join(random.choices(data_char,k=n))
        password=passc+password
        password=''.join(random.choices(password,k=n))
        chara=passc[0]+memory
        n=n-4
        password=chara+password[0:n]
    random.shuffle(list(password))
    return password

print('***Welcome to the password generator***')
while not (N>7 and N<17):
    N=int(input("Enter password length (8-16): "))
while not (MAYUS=='yes' or MAYUS=='no'):
    MAYUS=input("With capital letters? (yes/no): ")
while not (NUM=='yes' or NUM=='no'):
    NUM=input("With numbers? (yes/no): ")
while not (CHAR=='yes' or CHAR=='no'):
    CHAR=input("With characters? (yes/no): ")

PASSWORD=parameters(MAYUS,NUM,CHAR,N)

print("PASSWORD:",PASSWORD)
