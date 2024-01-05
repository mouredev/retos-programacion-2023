### Reto 44 Python ###

"""
   Crea un juego interactivo por terminal en el que tendrás que adivinar 
   el resultado de diferentes
   operaciones matemáticas aleatorias (suma, resta, multiplicación 
   o división de dos números enteros).
  - Tendrás 3 segundos para responder correctamente.
  - El juego finaliza si no se logra responder en ese tiempo.
  - Al finalizar el juego debes mostrar cuántos cálculos has acertado.
  - Cada 5 aciertos debes aumentar en uno el posible número de cifras 
     de la operación (cada vez en un operando):
  - Preguntas 1 a 5: X (entre 0 y 9) operación Y (entre 0 y 9)
  - Preguntas 6 a 10: XX (entre 0 y 99) operación Y (entre 0 y 9)
  - Preguntas 11 a 15: XX operación YY
  - Preguntas 16 a 20: XXX (entre 0 y 999) operación YY
 
 """
import random
from inputimeout import inputimeout, TimeoutOccurred

operacion=["+","-","*","/"]

def request (result_operator,num_one,num_two):
    if result_operator== 1:
        op= operacion[0]
    elif result_operator==2:
        op=operacion[1]
    elif result_operator==3:
        op=operacion[2] 
    else:
        op=operacion[3]      
    while True:
        try:
            valor = (int(inputimeout(prompt=f"{num_one} {op} {num_two}: ",timeout=3)))
            break
        except TimeoutOccurred:
            print ("Tiempo Agotado  PERDISTE")
            valor=None 
            break
    return valor

def operation(question):
    num_one=0
    num_two=0
    if question<5: 
        x=9
        y=9
    elif question<10:
        x=99
        y=9
    elif question<15:
        x=99
        y=99
    else:
        x=999
        y=99
    operator=random.randint(1,4)
    num_one=random.randint(0,x)
    if operator==4:
        num_two=random.randint(1,y)
    else:
        num_two=random.randint(0,y)
    return operator,num_one,num_two

print (input("Para comenzar presione cualquier tecla"))
try:     
    def interactive_game ():
            error=0
            question=0
            while error == 0:
                if question<20:
                    operator = operation(question)
                    result_operator=operator[0]
                    num_one =operator[1]
                    num_two = operator[2]
                    valor=request(result_operator,num_one,num_two)
                    if valor is None:
                        break
                    if operator[0] == 1:

                        if valor == num_one + num_two:
                            print ("Correcto")
                            question += 1
                        else:
                            print("Incorrecto")
                    elif operator[0] == 2:
                        if valor == num_one-num_two:
                            print ("Correcto")
                            question += 1
                        else:
                            print("Incorrecto")
                    elif operator[0] == 3:
                        if valor == num_one*num_two:
                            print ("Correcto")
                            question += 1
                        else:
                            print("Incorrecto")
                    else:
                        if valor == num_one//num_two:
                                print ("Correcto")
                                question += 1
                        else:
                            print("Incorrecto")
                            
                else:
                    error=1                
            print(f"Ha respondido {question} respuesta/s correcta/s")

    interactive_game()  
except ValueError:
    print ("Error en la ejecución")
finally:
    print("Ha finalizado el juego")
