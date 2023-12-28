'''/*
 * Escribe un programa que sea capaz de generar contraseñas de forma aleatoria.
 * Podrás configurar generar contraseñas con los siguientes parámetros:
 * - Longitud: Entre 8 y 16.
 * - Con o sin letras mayúsculas.
 * - Con o sin números.
 * - Con o sin símbolos.
 * (Pudiendo combinar todos estos parámetros entre ellos)
 */'''
import secrets
import string

lowercase_list = string.ascii_lowercase
uppercase_list = string.ascii_uppercase
numbers_list = string.digits
symbols_list = string.punctuation

options_list = {lowercase_list:True, uppercase_list:False, numbers_list:False, symbols_list:False}

def pass_generator():
    
#Aquí recibo las opciones por consola
    while True:
        value = input("Longitud de la contraseña (8-16): ")
        if value.isdigit() and 8 <= int(value) <= 16:
            long_pass = int(value)
            break
        print("La longitud de la contraseña debe ser de 8 a 16 caracteres.")

    options_quest = {}
    questions = ['¿Quieres mayúsculas?','¿Quieres números?','¿Quieres símbolos?']

    for question in questions:
        while True:
            answer = input(question + " (si/no): ").lower()
            if answer == "si":
                options_quest[question] = True
                break
            elif answer == "no":
                options_quest[question] = False
                break
            else:
                print("Ingresa sólo si o no")

    #Marco las opciones True en options_list
    if options_quest["¿Quieres mayúsculas?"] is True:
        options_list[uppercase_list] = True
    if options_quest["¿Quieres números?"] is True:
        options_list[numbers_list] = True
    if options_quest["¿Quieres símbolos?"] is True:
        options_list[symbols_list] = True

    #Genero la contraseña, teniendo en cuenta que se usen caracteres de todas
    #las opciones y que no se repitan
    password_chars = []
    for key, value in options_list.items():
        if value == True:
            password_chars += list(key)

    password = ''.join(secrets.choice(password_chars) for _ in range(long_pass))
    print(password)

pass_generator()
