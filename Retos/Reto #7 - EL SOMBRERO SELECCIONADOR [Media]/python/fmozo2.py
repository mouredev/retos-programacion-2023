'''
 * Crea un programa que simule el comportamiento del sombrero selccionador del
 * universo mágico de Harry Potter.
 * - De ser posible realizará 5 preguntas (como mínimo) a través de la terminal.
 * - Cada pregunta tendrá 4 respuestas posibles (también a selecciona una a través de terminal).
 * - En función de las respuestas a las 5 preguntas deberás diseñar un algoritmo que
 *   coloque al alumno en una de las 4 casas de Hogwarts (Gryffindor 🦁, Slytherin 🐍, Hufflepuff 🦡 y Ravenclaw 🦅 )
 * - Ten en cuenta los rasgos de cada casa para hacer las preguntas y crear el algoritmo seleccionador.
 *   Por ejemplo, en Slytherin se premia la ambición y la astucia.
'''

#Vamos a tener cinco preguntas, dependiendo la respuesta se le asigna una puntuación y en fución de ella, se le asignará a una casa u otra
#Creamos un diccionario de listas con preguntas - El valor de la lista [0] es la prengunta y los siguientes [1],[2],[3] y [4]
#las puntuaciones para cada respuesta, las puntuaciones de 0,5,15 a 20 y a boleo 😊
#Haremos que el usuario introduzca de 1 al 4 para que coincida con la posición dentro de la lista.

# Preguntas sacadas de https://www.gotoquiz.com/prueba_del_sombrero_seleccionador

my_dict_preguntas = {
1: ("¿Cuál de las siguientes opciones odiaría más que la gente lo llamara? \n 1:Ordinario \n 2:Ignorante \n 3:Cobarde \n 4:Egoista\n",5,10,15,20),
2: ("Después de su muerte ¿qué es lo que más le gustaría que hiciera la gente cuando escuche su nombre? \n 1:Te extraña, pero sonríe \n 2:Pide mas historias sobre tus aventuras \n 3:Piensa con admiración tus logros \n 4:No me importa lo que la gente piense de mí después de mi muerte, es lo que piensan de mi mientras estoy vivo lo que cuenta\n",10,5,15,20),
3: ("Dada la opción, preferirías inventar una poción que garantizara: \n 1:Gloria \n 2:Sabiduría \n 3:Amor \n 4:Poder\n",20,15,10,5),
4: ("¿Cómo le gustaría ser conocido en la historia? \n 1:El sabio \n 2:El bueno \n 3:El gran \n 4:El audaz\n",5,10,20,15),
5: ("Entras en un jardín encantado. ¿Qué sería lo más curioso de examinar primero? \n 1:El árbol de hojas de plata con manzanas doradas \n 2: Las setas rojas gordas que parecen estar hablando entre sí \n 3:El estanque burbujeante en cuyas profundidades se arremolina algo luminoso \n 4:La estatua del viejo mago con un extraño centelleo en los ojos\n",15,5,10,20)
}

def sombrero_seleccionador(pregunta,respuesta):
  return int((my_dict_preguntas[pregunta][respuesta]))

#Se puntua cada respuesta entre 0 y 20 puntos.
#Con esto la puntuación mínima será 5 y la máxima 100
#Del 5 al 25 --> Gryffindor
#Del 26 al 50 --> Slytherin
#Del 51 al 75 --> Hufflepuff222
#Del 76 a 100 --> Ravenclaw

def selecciona_casa(puntos):
  if puntos <= 25:
    print("Se te ha asignado la casa de 🦁 Gryffindor")
  elif puntos >=26 and puntos <=50:
    print("Se te ha asignado la casa de 🐍 Slytherin")
  elif puntos >=51 and puntos <=75:
    print("Se te ha asignado la casa de 🦡 Hufflepuff")
  else:
    print("Se te ha asignado la casa de 🦅 Ravenclaw")


puntos = 0 #Puntuación inicial
print("🎩🎩🎩 EL SOMBRERO SELECCIONADOR 🎩🎩🎩")

for clave in my_dict_preguntas:
  respuesta = input(my_dict_preguntas[clave][0])
  while respuesta not in ["1","2","3","4"]:
    if respuesta not in ["1","2","3","4"]:
      print("Por favor, tienes que elegir una opción entre 1 y 4...\n")
    respuesta = input(my_dict_preguntas[clave][0])
  puntos += sombrero_seleccionador(clave,int(respuesta))

selecciona_casa(puntos)