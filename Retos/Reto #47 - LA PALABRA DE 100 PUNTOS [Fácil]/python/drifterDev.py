def game():
  points = 0
  letters1 = "abcdefghijklmnñopqrstuvwxyz"
  letters2 = letters1.upper()
  try:
    word = input('Ingrese la palabra: ').split(' ')[0]
    for c in word:
      if not c in letters1 and not c in letters2:
        raise Exception('No es una palabra valida')
    for c in word:
      points+=letters1.index(c.lower())+1
  except Exception as e:
    print(e.args[0])
  return points


def main():
  print('#'*50)
  print('Bienvenido al juego de palabras')
  print('El objetivo es ingresar una palabra con 100 puntos')
  print('Cada letra tiene un valor de 1 a 27 dependiendo de su posicion en el alfabeto')
  print('Solo se tendra en cuenta la primera palabra ingresada')
  print('#'*50)
  while True:
    points = game()
    if points == 100:
      break
    print('Puntos: '+str(points)+', vuelve a intentarlo')
  print('Ganaste!')


if __name__ == '__main__':
  main()
