# Lista que representa el juego
juego = []

# Bucle para ingresar cada punto
while True:
  punto = input("Introduce el ganador del punto (P1 o P2 o termina): ")
  if punto == "termina":
    break
  elif punto == "P1" or punto == "P2":
    juego.append(punto)
  else:
    print("Entrada no válida, intenta de nuevo")

# Variables para llevar la puntuación
p1 = 0
p2 = 0

# Bucle para mostrar la puntuación
for punto in juego:
  if punto == "P1":
    p1 += 1
  else:
    p2 += 1

  # Mostrar puntuación
  if p1 == 0:
    p1_puntos = "Love"
  elif p1 == 1:
    p1_puntos = "15"
  elif p1 == 2:
    p1_puntos = "30"
  elif p1 == 3:
    p1_puntos = "40"
  else:
    p1_puntos = "Ha ganado el P1"

  if p2 == 0:
    p2_puntos = "Love"
  elif p2 == 1:
    p2_puntos = "15"
  elif p2 == 2:
    p2_puntos = "30"
  elif p2 == 3:
    p2_puntos = "40"
  else:
    p2_puntos = "Ha ganado el P2"

  if p1 >= 4 and p2 >= 0 and (p1-p2) >= 2:
    print("Ha ganado el P1")
    break
  elif p2 >= 4 and p1 >= 0 and (p2-p1) >= 2:
    print("Ha ganado el P2")
    break
  elif p1 == p2:
    print("Deuce")
  elif p1 >= 3 and p2 >= 3:
    if p1 > p2:
      print("Ventaja P1")
    else:
      print("Ventaja P2")
  else:
    print(f"{p1_puntos} - {p2_puntos}")