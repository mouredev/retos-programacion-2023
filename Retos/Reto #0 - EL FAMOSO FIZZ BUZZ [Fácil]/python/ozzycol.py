# -*- coding: utf-8 -*-
"""
Created on Sat Jan  7 18:57:31 2023

@author: oardila
"""

numero=1
while numero <=100:
    if (numero % 3==0 and numero%5==0):
        print("fizzbuzz")
    elif numero%3==0:
        print("fizz")
    elif numero%5==0:
        print("buzz")
    else:
        print(numero)  
    numero+=1
    

