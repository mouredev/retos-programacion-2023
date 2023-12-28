# Escribe un programa que sea capaz de generar contraseñas de forma aleatoria.
# Podrás configurar generar contraseñas con los siguientes parámetros:
# - Longitud: Entre 8 y 16.
# - Con o sin letras mayúsculas.
# - Con o sin números.
# - Con o sin símbolos.
# (Pudiendo combinar todos estos parámetros entre ellos)
#
import random
symbol_flag=False
number_flag=False
cap_let_flag=False
lowercase_letters="abcdefghijklmnñsopqrstuvwxyz"
capital_letters="ABCDEFGHIJKLMNÑOPQRSTUVWXYZ"
symbols="!#$%&/()=?\¿¡[{]}+*-|°.:,;_"
numbers="0123456789"
string=f"{lowercase_letters}"
while True:
    length=input("Ingrese la cantidad de caracteres de su contraseña: ")
    if not length.isnumeric()==True:
        print("¡Ingrese un número!")
    else:
        #length=int(length)
        break

if int(length)>=8 and int(length)<=16:

    sim_quest=input("¿Desea que su contraseña contenga símbolos? ¿Si/No?: ")
    sim_quest=sim_quest.upper()
    if sim_quest=="SI" or sim_quest=="NO":
        if sim_quest=="SI":
            string=string+symbols
            symbol_flag=True
    else:
        print("¡Se escogió 'no' por haber introducido incorrectamente la respuesta!")
    
    num_quest=input("¿Desea que su contraseña contanga números? ¿Si/No?: ")
    num_quest=num_quest.upper()
    if num_quest=="SI" or num_quest=="NO":
        if num_quest=="SI":
            string=string+numbers
            number_flag=True
    else:
        print("¡Se escogió 'no' por haber introducido incorrectamente la respuesta!")

    cap_lett_quest=input("¿Desea que su contraseña contenga mayúsculas? ¿Si/No?: ")
    cap_lett_quest=cap_lett_quest.upper()
    if cap_lett_quest=="SI" or cap_lett_quest=="NO":
        if cap_lett_quest=="SI":
            string=string+capital_letters
            cap_let_flag=True
    else:
        print("¡Se escogió 'no' por haber introducido incorrectamente la respuesta!")
    
    
    while True:
        cap_let_pass=False
        num_pass=False
        sym_pass=False
        extention=random.sample(string, length)
        password="".join(extention)
        

        if symbol_flag==True:
            for n in password:
                if n in symbols:
                  sym_pass=True

        if number_flag==True:
            for n in password:
                if n in numbers:
                  num_pass=True

        if cap_let_flag==True:
            for n in password:
                if n in capital_letters:
                  cap_let_pass=True

        if symbol_flag==sym_pass and number_flag==num_pass and cap_let_flag==cap_let_pass:
            print(f"Su contraseña es: '{password}'")
            break
            
else:
    print("ERROR: ¡La contraseña debe ser entre 8 y 16 caracteres!")