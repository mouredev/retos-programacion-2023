import random as rd
import sys


def clear():
    sys.stdout.write("\033c")


class Participation:

  def __init__(self):

    self.participants = set([])
    self.cursor = '→'
    self.prompt = f'Inserta el nombre del participante\n{self.cursor} '

  def ask_prompt(self):

    name = input(self.prompt)
    return name

  def add_participant(self):

    name = self.ask_prompt()

    if name in self.participants:

      print('Error: este personaje ya existe')

    else:

      self.participants.add(name)
      print('El participante ha sido agregado correctamente!')

  def delete_participant(self):

    name = self.ask_prompt()

    if name in self.participants:

      self.participants.remove(name)
      print('El participante ha sido borrado exitosamente!')

    else:

      print(f'Error: no ha sido encontrado un particante con nombre: {name}')

  def show_participants(self):

    print('***** Lista de participantes *****')

    for (index, participant) in enumerate(self.participants):

      print(index + 1, participant)

    print(f'Hay un total de {len(self.participants)} {"participantes" if len(self.participants) != 1 else "participante"} registrado{"s" if len(self.participants) != 1 else ""}!\n')

  def giveaway(self):

    if not len(self.participants):

      print('Error: no hay participantes registrados todavía!')

    else:

      winner = rd.choice(list(self.participants))

      print(f'The winner is: {winner}')
      self.participants.remove(winner)


  def show_menu(self):

    print('1. Añadir participante.')
    print('2. Remover participante.')
    print('3. Listar participantes.')
    print('4. Realizar sorteo')
    print('5. Salir')

    while True:

      option = input(self.cursor + ' ')

      try:

        option = int(option)

        if 0 <= option or option > 5:
          print('Error. Opción fuera de rango')
          print(option)

      except ValueError:

        print('Error: Opción inválida')
        print(option)
        continue

      return option


  def start(self):

    print('Bienvenido al calendario de aDEViento')
    print('24 días, 24 regalos sorpresa relacionados con desarrollo de software')
    print('Desde el 1 al 24 de diciembre.')

    while True:


      option = self.show_menu()
      clear()

      if option == 1:
        self.add_participant()

      if option == 2:
        self.delete_participant()

      if option == 3:
        self.show_participants()

      if option == 4:
        self.giveaway()

      if option == 5:
        print('Saliendo...')
        break


if __name__ == '__main__':
  calendar = Participation()
  calendar.start()
