#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
 * Escribe un programa que sea capaz de generar contraseñas de forma aleatoria.
 * Podrás configurar generar contraseñas con los siguientes parámetros:
 * - Longitud: Entre 8 y 16.
 * - Con o sin letras mayúsculas.
 * - Con o sin números.
 * - Con o sin símbolos.
 * (Pudiendo combinar todos estos parámetros entre ellos)
"""

import sys
import getopt
import random

argumentList = sys.argv[1:]

options = "hl:cnso:z"
long_options = ["help","length","case","numbers","symbols","output"]

helpMenu = """Description:
    This script creates a random password.

    Options:
        -h,--help
            displays help menu
        -l,--length
            decide how long the password is - it has to be between 8 and 16
        -c,--ignore-case
            if this options is included, NO upper case will be included on the password
        -n,--numbers
            if this options is included, NO numbers will be included on the password
        -s,--symbols
            if this options is included, NO symbols will be included on the password
        -z,--surprise
            if this options is included, you'll be surpised!
        -o,--output
            output to a file

    Example usage:
        - no options: create a random password between 8 and 16 with upper and lower case letters, numbers, and symbols
            python3 jaliagag.py
"""

flags = {
    "l": 8,
    "c": True,
    "n": True,
    "s": True,
    "z": False,
}

try:
    # Parsing argument
    arguments, values = getopt.getopt(argumentList, options, long_options)

    # checking each argument
    for currentArgument, currentValue in arguments:

        if currentArgument in ("-h", "--help"):
            print(helpMenu)
            exit
        if currentArgument in ("-l", "--length"):
            if int(currentValue) < 8 or int(currentValue) > 16:
                print('ERROR: la contraseña tiene que tener un largo entre 8 y 16')
            else:
                flags["l"] = currentValue
        if currentArgument in ("-c", "--case"):
            flags["c"] = False
        if currentArgument in ("-n", "--numbers"):
            flags["n"] = False
        if currentArgument in ("-s", "--symbols"):
            flags["s"] = False
        if currentArgument in ("-z", "--surprise"):
            flags["z"] = True
        elif currentArgument in ("-o", "--output"):
            print (("Enabling special output mode (% s)") % (currentValue))

except getopt.error as err:
    # output error, and return with an error code
    print (str(err))

letters = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]
upper_letters = ["A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z"]
numbers = ["0","1","2","3","4","5","6","7","8","9"]
symbols = ["!","?","@","#","!","$","%","&","!",")","(","=","|"]


def create_password(diccionario):
    numero_uno = 0
    numero_dos = 0
    numero_tres = 0
    numero_cuatro = 0
    numero_cinco = 0
    numero_seis = 0
    # length
    if diccionario["z"] == True:
        numero_uno = random.randint(8, 16) # surprise mode - do it all for me
    else:
        numero_uno = int(diccionario["l"])
    # Q letras
    if numero_uno % 2 == 0:
        numero_dos = int(numero_uno * 0.65)
    else:
        numero_dos = int((numero_uno+1)* 0.65)

    # Q lower case
    if numero_dos % 2 == 0:
        if diccionario["c"] == True:
            numero_tres = int(numero_dos * 0.75)
            numero_cuatro = numero_dos - numero_tres
        else:
            numero_tres = int(numero_dos * 0.75)
    # Q upper case
    else:
        if diccionario["c"] == True:
            numero_tres = int((numero_dos-1) * 0.75)
            numero_cuatro = numero_dos - numero_tres
        else:
            numero_tres = int(numero_dos-1 * 0.75)
    # Q numeros
    if diccionario["n"] == True:
        numero_cinco = int((numero_uno - numero_dos) / 2)
    # Q simbolos
    if diccionario["s"] == True:
        numero_seis = numero_uno - numero_dos - numero_cinco

    make_random(numero_tres,numero_cuatro,numero_cinco,numero_seis)

def make_random(letras, mayus, numeros, simbolos):
    password = []
    # elijo una de las 4 categorías
    # de la categoría aleatoria agrego un item aleatorio a la contraseña
    # evaluo cuántos elementos quedan, si es igual a 0, saco la categoría
    largo = letras + mayus + numeros + simbolos

    for i in range(largo):
        n = random.randint(1, 4)
        #print(n)
        if n == 1:
            letra = random.randint(1,len(letters)-1)
            password.append(str(letters[letra]))
        elif n == 2:
            mayu = random.randint(1,len(upper_letters)-1)
            password.append(str(upper_letters[mayu]))
        elif n == 3:
            numero = random.randint(1,len(numbers)-1)
            password.append(str(numbers[numero]))
        elif n == 4:
            simbolo = random.randint(1,len(symbols)-1)
            password.append(str(symbols[simbolo]))
    p = ""
    print(p.join(password))

if __name__ == '__main__':
    create_password(flags)

