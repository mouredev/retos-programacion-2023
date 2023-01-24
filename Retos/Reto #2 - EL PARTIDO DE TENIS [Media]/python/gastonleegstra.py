def juego (secuencia):
  puntosP1 = 0
  puntosP2 = 0
  for jugada in secuencia:
    if jugada == 'P1':
      if puntosP1<30:
        puntosP1+=15
      else:
        puntosP1+=10
    elif jugada == 'P2':
      if puntosP2<30:
        puntosP2+=15
      else:
        puntosP2+=10

    if puntosP1 == 0 or puntosP2 == 0:
        if puntosP1 == 0:
          print("Love - "+str(puntosP2))
        else:
          print (str(puntosP1)+" - Love")
    elif (puntosP1 == puntosP2) and (puntosP1 == 40 and puntosP2 == 40):
      print("Deuce")
    elif(puntosP2 == 40 and puntosP1 == puntosP2 + 10):
      print("Ventaja P1")
    elif(puntosP1==40 and puntosP2 == puntosP1+10):
      print("Ventaja P2")
    elif(puntosP2 == 40 and puntosP1 == puntosP2 + 20):
      print("Ha ganado el P1")
    elif(puntosP1==40 and puntosP2 == puntosP1+10):  
      print("Ha ganado el P2")
    else:
      print(str(puntosP1)+" - "+str(puntosP2))

s = ['P1', 'P1', 'P2', 'P2', 'P1', 'P2', 'P1', 'P1']

juego(s)