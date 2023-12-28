class Jugador:
  def __init__(self, nombre):
    self.nombre = nombre
    self.opciones = ['🗿', '📄', '✂️', '🦎', '🖖']
    self.opcion = None
    self.puntos = 0

  def elegir_opcion(self):
    self.opcion = input(
        f'{self.nombre}, elige : {self.opciones}')
    if self.opcion == '🗿':
      print("Piedra")
    elif self.opcion == '📄':
      print("Papel")
    elif self.opcion == '✂️':
      print("Tijera")
    elif self.opcion == '🦎':
      print("Lagarto")
    else:
        print("Spock")


class Juego:
  def __init__(self, jugador1, jugador2):
    self.jugador1 = jugador1
    self.jugador2 = jugador2
    self.resultados = {"🗿": ["🦎", "✂️"],
                       "📄": ["🗿", "🖖"],
                       "✂️": ["📄", "🦎"],
                       "🦎": ["🖖", "📄"],
                       "🖖": ["✂️", "🗿"]
                       }

  def evaluar(self, opcion1, opcion2):
    if opcion1 == opcion2:
      return 'Empate'
    elif opcion2 in self.resultados[opcion1]:
      return f'Gana {self.jugador1.nombre}'
    else:
      return f'Gana {self.jugador2.nombre}'

  def jugar(self):
    self.jugador1.elegir_opcion()
    self.jugador2.elegir_opcion()
    resultado = self.evaluar(self.jugador1.opcion, self.jugador2.opcion)
    print(resultado)
    if resultado == f'Gana {self.jugador1.nombre}':
      self.jugador1.puntos += 1
    elif resultado == f'Gana {self.jugador2.nombre}':
      self.jugador2.puntos += 1

jugador1 = Jugador('Player 1')
jugador2 = Jugador('Player 2')
juego = Juego(jugador1, jugador2)

while True:
  juego.jugar()
  respuesta = input('Jugar de nuevo? (s/n): ')
  if respuesta == 'n':
    break

print(f'Puntos de {jugador1.nombre}: {jugador1.puntos}')
print(f'Puntos de {jugador2.nombre}: {jugador2.puntos}')
