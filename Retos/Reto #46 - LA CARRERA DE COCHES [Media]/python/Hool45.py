

"""
* Crea un programa que simule la competición de dos coches en una pista.
 * - Los dos coches estarán representados por 🚙 y 🚗. Y la meta por 🏁.
 * - Cada pista tendrá entre 1 y 3 árboles 🌲 colocados de forma aleatoria.
 * - Las dos pistas tendrán una longitud configurable de guiones bajos "_".
 * - Los coches comenzarán en la parte derecha de las pistas. Ejemplo:
 *   🏁____🌲_____🚙
 *   🏁_🌲____🌲___🚗
 * 
 * El juego se desarrolla por turnos de forma automática, y cada segundo
 * se realiza una acción sobre los coches (moviéndose a la vez), hasta que
 * uno de ellos (o los dos a la vez) llega a la meta.
 * - Acciones:
 *   - Avanzar entre 1 a 3 posiciones hacia la meta.
 *   - Si al avanzar, el coche finaliza en la posición de un árbol,
 *     se muestra 💥 y no avanza durante un turno.
 *   - Cada turno se imprimen las pistas y sus elementos.
 *   - Cuando la carrera finalice, se muestra el coche ganador o el empate.
"""

import random

global pos_tree_1
global pos_tree_2
global pos_tree_3



def car_path(emoji_car):
    global x1, x2, x3
    global x4, x5, x6
    global ct1, ct2
    global  car_1
    global cant_turnos
    
    cant_turnos = 1  

    if emoji_car == "🚙":
        car_1 = 1
    if emoji_car == "🚗":
        car_1 = 2
    
    cant_trees = random.randint(1,3)
   
    for i in range(0, cant_trees + 1):
        if i == 1:
            pos_tree_1 = random.randint(1,guiones)
        elif i == 2:
            pos_tree_2 = random.randint(1,guiones)
            if pos_tree_2 == pos_tree_1:
                pos_tree_2 = random.randint(1,guiones)
        elif i == 3:
            pos_tree_3 = random.randint(1,guiones)
            if pos_tree_3 == pos_tree_2 or pos_tree_3 == pos_tree_1:
                pos_tree_3 = random.randint(1, guiones)
                if pos_tree_3 == pos_tree_2 or pos_tree_3 == pos_tree_1:
                   pos_tree_3 = random.randint(1, guiones)
        else: 
            pos_tree_1 = -27
            pos_tree_2 = -27
            pos_tree_3 = -27

    if car_1 == 1:
        x1 = pos_tree_1
        x2 = pos_tree_2
        x3 = pos_tree_3
        ct1 = cant_trees
        car_1 =+ 1
        
    if car_1 == 2:
        x4 = pos_tree_1
        x5 = pos_tree_2
        x6 = pos_tree_3
        ct2 = cant_trees
        car_1 = 1 
    
    print("🏁", end="")
    for i in range(1,guiones + 1):
        if i == pos_tree_1 or i == pos_tree_2 or i == pos_tree_3 and cant_trees != 0:
            print("🌲", end="")
            cant_trees = cant_trees - 1
        else:
            print("_", end="")

    print(emoji_car)

def car_game(emoji_car1, emoji_car2):
    
 global ct1, ct2
 global x1, x2, x3
 global x4, x5, x6
 ct3 = 0
 if ct1 < ct2:
     ct3 = ct2
 elif ct1 == ct2:
      ct3 = ct1
 else:
     ct3 = ct1
   
 turno1 = 0
 turno2 = 0

 for e in range(0, 11 + ct3):
     turno1+= random.randint(1,3)
     turno2+= random.randint(1,3)
    

     if guiones - turno1 > 0:
         print("🏁", end="")
 
     for i in range(1, guiones + 1 - turno1):
         
         if i == x1 or i == x2 or i == x3 and ct1 != 0:
             print("🌲", end="")
             ct1 = ct1 - 1
         else:
             print("_", end="")
        
     if guiones + 1 - turno1 == 1:
         i = 1
         if i == x1 or i == x2 or i == x3 and ct1 != 0:
             print("🌲", end="")
             ct1 = ct1 - 1
         else:
             print("_", end="")



     
        
     if (i + 1 == x1 or i + 1 == x2 or i + 1 == x3 or i - 1 < 0 == x1 - 1 or i -1 < 0 == x2 - 1 or i - 1 < 0 == x3 - 1) and turno1 < 10:
          print("💥", end="")
          turno1-=1
          if x1 <= x3 and x2 <= x3:
             x3 = -27
          elif x1 >= x2  and x1 >= x3:
             x1 = -27
          elif x1 <= x2 and x2 >= x3:
             x2 = -27   
     if i < x1:
          x1 = -27
     elif i < x2:
         x2 = -27
     elif i < x3:
         x3 = -27 

      

     print(emoji_car1)
     print(i, turno1)
     print(x1, x2, x3)
     #turno segundo auto
     if guiones - turno2 > 0:
         print("🏁", end="")

     for i in range(1, guiones + 1 - turno2):
        
        if i == x4 or i == x5 or i == x6 and ct2 != 0:
             print("🌲", end="")
             ct2 = ct2 - 1
        else:
            print("_", end="")
        
     if guiones + 1 - turno2 == 1:
         i = 1
         if i == x4 or i == x5 or i == x6 and ct2 != 0:
             print("🌲", end="")
             ct2 = ct2 - 1
         else:
             print("_", end="")

     if (i + 1 == x4 or i + 1 == x5 or i + 1 == x6 or i - 1 < 0 == x4 - 1 or i - 1 < 0 == x5 - 1 or i - 1 < 0 == x6 - 1) and turno2 < 10:
         print("💥", end="")
         turno2-=1
         if x4 <= x6 and x5 <= x6:
              x6 = -27
         elif x4 >= x5 and x4 >= x6:
             x4 = -27
         elif x4 <= x5 and x5 >= x6:
             x5 = -27  
     
     if i < x4:
        x4 = -27
     elif i < x5:
         x5 = -27
     elif i < x6:
         x6 = 27

     print(emoji_car2)
     print(i, turno2)
     print(x4, x5, x6)

     if guiones - turno1 <= 0 and guiones - turno2 <= 0:
         print("EMPATE")
         start_game()
     elif guiones - turno2 <= 0:
         print(f"GANADOR: {emoji_car2}")
         start_game()
     elif guiones - turno1 <= 0:
         print(f"GANADOR: {emoji_car1}")
         start_game() 
    
     next_turn = input("siguiente turno?(y/n) ")
     if next_turn == "n":
         break

def start_game():
    global guiones
    guiones = int(input("cuantas casillas quieres? "))

    car_path("🚙")
    car_path("🚗")

    start_gm = input("start the game? (y/n) ")
    

    if start_gm == "y":
      car_game("🚙", "🚗")
    elif start_gm == "n":
      print("idc your opinion bruda")
      car_game("🚙", "🚗")
    else:
      print("its not that complicated, Y or N")
      car_game("🚙", "🚗")

try:
  start_game()
except ValueError as error:
    print(error)
