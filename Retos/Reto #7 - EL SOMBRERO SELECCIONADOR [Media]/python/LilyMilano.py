# * Crea un programa que simule el comportamiento del sombrero selccionador del
#  universo mágico de Harry Potter.
#  - De ser posible realizará 5 preguntas (como mínimo) a través de la terminal.
#  - Cada pregunta tendrá 4 respuestas posibles (también a selecciona una a través de terminal).
#  - En función de las respuestas a las 5 preguntas deberás diseñar un algoritmo que
#  coloque al alumno en una de las 4 casas de Hogwarts (Gryffindor, Slytherin , Hufflepuff y Ravenclaw)
#  - Ten en cuenta los rasgos de cada casa para hacer las preguntas y crear el algoritmo seleccionador.
# Por ejemplo, en Slytherin se premia la ambición y la astucia.

# :::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::

# * VARIABLES:
gryffindor = 0
ravenclaw = 0
hufflepuff = 0
slytherin = 0

# :::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::

# * INPUTS:
# * Quiz:
# * Hogwarts Sorting Hat:

# ______________________________________________________________________________

q1_answer = input("When I make decisions, I... \na) Take chances and pick the risky choise. \nb) Consider every option carefully. \nc) Think about how it will affect others. \nd) Make sure it works out for me. \n")

if q1_answer == "a":
  gryffindor += 1
elif q1_answer == "b":
  ravenclaw += 1
elif q1_answer == "c":
  hufflepuff += 1
elif q1_answer == "d":
  slytherin += 1
else:
  print("Sorry, I don't understand that answer.")

# ______________________________________________________________________________

q2_answer = input("What can you be found doing on the weekends? \na) Going on adventures \nb) Doing my homework \nc) Spending time with family or friends \nd) Plotting revenge on my enemies \n")

if q2_answer == 'a':
  gryffindor += 1
elif q2_answer == 'b':
  ravenclaw += 1
elif q2_answer == 'c':
  hufflepuff +=1
elif q2_answer == 'd':
  slytherin +=1
else:
  print("Sorry, I don't understand that response.")

# ______________________________________________________________________________

q3_answer = input("What would you do if the Dark Lord was going to invade your school? \na) Fight him \nb) Look up some good defensive curses in a book \nc) Stand by my friends no matter what. \nd) Help the Dark Lord invade the school. \n")

if q3_answer == 'a':
  gryffindor += 1
elif q3_answer == 'b':
  ravenclaw += 1
elif q3_answer == 'c':
  hufflepuff +=1
elif q3_answer == 'd':
  slytherin +=1
else:
  print("Sorry, I don't understand that response.")

# ______________________________________________________________________________

q4_answer = input("I like to spend time with people who...\na) Are different and creative. \nb) Are smart. \nc) Are kind. \nd) Are the same as me.\n")

if q4_answer == 'a':
  gryffindor += 1
elif q4_answer == 'b':
  ravenclaw += 1
elif q4_answer == 'c':
  hufflepuff +=1
elif q4_answer == 'd':
  slytherin +=1
else:
  print("Sorry, I don't understand that response.")

# ______________________________________________________________________________

q5_answer = input("Which of the Hogwarts ghosts would you ask for advice? \na) Headless Nick. \nb) The Grey Lady. \nc) The Fat Friar \nd) The Bloody Baron \n")

if q5_answer == 'a':
  gryffindor += 1
elif q5_answer == 'b':
  ravenclaw += 1
elif q5_answer == 'c':
  hufflepuff +=1
elif q5_answer == 'd':
  slytherin +=1
else:
  print("Sorry, I don't understand that response.")

# ::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::

#* SORTING:

if gryffindor > ravenclaw and gryffindor > hufflepuff and gryffindor > slytherin:
  print("GRYFFINDOR!!!!!!")
elif ravenclaw > gryffindor and ravenclaw > hufflepuff and ravenclaw > slytherin:
  print("RAVENCLAW!!!!!!")
elif hufflepuff > gryffindor and hufflepuff > ravenclaw and hufflepuff > slytherin:
  print("HUFFLEPUFF!!!!!!")
elif slytherin > gryffindor and slytherin > ravenclaw and slytherin > hufflepuff:
  print("SLYTHERIN!!!!!!")

# ::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::

# * DESKTOP TESTING:

# ? When I make decisions, I... 
# a) Take chances and pick the risky choise. 
# b) Consider every option carefully. 
# c) Think about how it will affect others. 
# d) Make sure it works out for me. 
# !a
# ? What can you be found doing on the weekends? 
# a) Going on adventures 
# b) Doing my homework 
# c) Spending time with family or friends 
# d) Plotting revenge on my enemies 
# !b
# ? What would you do if the Dark Lord was going to invade your school? 
# a) Fight him
# b) Look up some good defensive curses in a book
# c) Stand by my friends no matter what.
# d) Help the Dark Lord invade the school.
# !a
# ?I like to spend time with people who...
# a) Are different and creative.
# b) Are smart.
# c) Are kind.
# d) Are the same as me.
# !c
# ?Which of the Hogwarts ghosts would you ask for advice?
# a) Headless Nick.
# b) The Grey Lady.
# c) The Fat Friar
# d) The Bloody Baron
# !a
# * GRYFFINDOR!!!!!!
