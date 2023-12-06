def tenis_game(secuencia):
  P1control=0
  P2control=0
  puntos=['Love','15','30','40']
  finished=False
  for i in secuencia:

    P1control+=1 if i == 'P1' else 0
    P2control+=1 if i == 'P2' else 0

    if P1control>=3 and P2control>=3:
      if abs(P1control-P2control)<=1 and not finished:
          print('Deuce' if P1control == P2control else 'Ventaja P1' if P1control>P2control else 'Ventaja P2')
      else:
        finished = True
    else:
      if P1control < 4 and P2control < 4:
        print(puntos[P1control], '-', puntos[P2control])
      else:
        finished=True
  print('Los puntos ingresados son incorrectos' if not finished else 'Ha ganado el P1' if P1control>P2control else 'Ha ganado el P2')

tenis_game(['P1', 'P1', 'P2', 'P2', 'P1', 'P2', 'P1', 'P1'])