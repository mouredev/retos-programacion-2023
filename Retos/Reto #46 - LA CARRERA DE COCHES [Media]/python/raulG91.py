from random import randint
from time import sleep

def init_circuit(length)->list:
  '''
  Initilize circuit with certain length 
  '''
  circuit = ["🏁"]  
  number_trees = randint(1,3)

  for step in range(0,length-1):
     circuit.append("_")

 #Set trees
  while number_trees > 0:
   position = randint(1,length-1)
   circuit[position] = "🌲"
   number_trees -=1
  return circuit

def array_2_string(array:list)->str:
  '''
  Convert list to string
  '''
  result = ""
  for element in array:
    result+= element
  return result  

def game(circuit_length):

    finish_game = False
    circuit1 = init_circuit(circuit_length)
    circuit2 = init_circuit(circuit_length)

    pos_car1 = circuit_length - 1
    pos_car2 = circuit_length - 1
    previous_value_circuit1 = "_"
    previous_value_circuit2 = "_"
    crash_car1 = False
    crash_car2 = False

    while not(finish_game):
 
        if circuit1[pos_car1] == "🏁" or circuit2[pos_car2] == "🏁": #Finish line
          finish_game = True
          ganador = ""
          if circuit1[pos_car1] == "🏁" and circuit2[pos_car2] == "🏁":
            ganador += "Empate"
          elif circuit1[pos_car1] == "🏁":
            ganador +="Ganador es "+"🚙"
          else:
            ganador+="Ganador es "+"🚗" 
          #Before print the car check if there is a colission
          if circuit1[pos_car1] == "🌲" or crash_car1:
            circuit1[pos_car1] = "💥"
          else:        
            circuit1[pos_car1] = "🚙"
          
          if circuit2[pos_car2] == "🌲" or crash_car2:
            circuit2[pos_car2] = "💥"
          else:    
            circuit2[pos_car2] = "🚗"
          print(array_2_string(circuit1))
          print(array_2_string(circuit2))  
          print(ganador)
        else: #Game has not finished
          # Bofore moving car, store previous value         
          previous_value_circuit1 = circuit1[pos_car1]
          previous_value_circuit2 = circuit2[pos_car2]
          #Move car 
          if circuit1[pos_car1] == "🌲": #Colission
            circuit1[pos_car1] = "💥"
            crash_car1 = True
          elif crash_car1: # There was a colission on previous turn
            crash_car1 = False  
            previous_value_circuit1 = "🌲"
          else:  
            circuit1[pos_car1] = "🚙"
            
          if circuit2[pos_car2] == "🌲": #Colission
            circuit2[pos_car2] = "💥"
            crash_car2 = True
          elif crash_car2: # There was a colission on previous turn
            crash_car2 = False
            previous_value_circuit2 = "🌲" 
          else:    
            circuit2[pos_car2] = "🚗"
            
          #Print the results  
          print(array_2_string(circuit1))
          print(array_2_string(circuit2))

          #Restore prvious value
          if not(crash_car1):
            circuit1[pos_car1] = previous_value_circuit1
          if not(crash_car2):
            circuit2[pos_car2] = previous_value_circuit2 

          #Let's decide how many positions car will advance, if the car doesn't crash
          if not(crash_car1):
            advance_car1 = randint(1,3)
          else:
            advance_car1 = 0  
          if not(crash_car2):
            advance_car2 = randint(1,3)
          else:
            advance_car2 = 0  

          if pos_car1 - advance_car1 < 0:
             pos_car1 = 0
          else:
              pos_car1 = pos_car1 - advance_car1   
          if pos_car2 - advance_car2< 0:
             pos_car2 =0  
          else:
              pos_car2 = pos_car2 - advance_car2   
              
          #Sleep the process for one second
          sleep(1.0)


game(10)
