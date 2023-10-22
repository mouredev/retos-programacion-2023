# -*- coding: utf-8 -*-
"""
Created on Sat Oct 14 19:19:05 2023

@author: Jarkillo
"""

# Challengue FizzBuzz

# Escribe un programa que muestre por consola ( con un print)
# Los numeros de 1 a 100 (ambos incluidos y con un salto de linea entre cada impresion)
# sustituyendo los siguientes:

# - Multiplos de 3 por la palabra fizz
# - Multiplos de 5 por la palabra buzz
# - Multiplos de 3 y de 5 a la vez por la palabra fizzbuzz


def fizzbuzz():
    
    for i in range (1,101):
    
        if i%3 == 0:
            print ("fizz")
    
        elif i%5 == 0:
            print ("buzz")
        
        elif i%3 == 0 and i%5 == 0:
        
            print ("fizzbuzz")
        
        else:
            print (i)

















         
         