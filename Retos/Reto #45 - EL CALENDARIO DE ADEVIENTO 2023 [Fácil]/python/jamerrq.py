import random as rd
import sys
from time import sleep

def clear():
    sys.stdout.write("\033c")

"""
stackoverflow.com/questions/287871/how-do-i-print-colored-text-to-the-terminal
"""
class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

class Participation:

  def __init__(self):

    self.participants = set([])
    self.cursor = f'{bcolors.BOLD}{bcolors.HEADER}→'
    self.prompt = f'{bcolors.OKBLUE}Inserta el nombre' + \
        f' del participante\n{self.cursor} '
    self.index = 0
    self.heading = f"{bcolors.OKGREEN}🎄 CALENDARIO DE ADEVIENTO 🎁"

  def ask_prompt(self):

    name = input(self.prompt)
    return name

  def add_participant(self):

    name = self.ask_prompt()

    if name in self.participants:

      print(f'{bcolors.FAIL}🛑 Error: este participante ya se encuentra' + \
             ' registrado!\n')
      # sleep(1)

    else:

      self.participants.add(name)
      print(f'{bcolors.OKCYAN}El participante ha sido agregado' + \
            ' correctamente!\n')

  def delete_participant(self):

    name = self.ask_prompt()

    if name in self.participants:

      self.participants.remove(name)
      print(f'{bcolors.OKCYAN}El participante ha sido borrado exitosamente!\n')

    else:

      print(f'{bcolors.FAIL}🛑 Error: no ha sido encontrado un participante' +\
             f' con nombre ⚠️ {name} ⚠️\n')

  def show_participants(self):

    print(f'{bcolors.OKGREEN}********** Lista de participantes **********')

    for (index, participant) in enumerate(self.participants):

      color = bcolors.FAIL if index % 2 == 0 else bcolors.OKGREEN
      print(f'{color}{index + 1} {participant}')

    plural = 's' if len(self.participants) != 1 else ''
    color = bcolors.FAIL if len(self.participants) % 2 == 0 else bcolors.OKGREEN
    print(f'{color}' + \
          f'Hay un total de {len(self.participants)} ' + \
          f'participante{plural} registrado{plural}!\n')

  def giveaway(self):

    if not len(self.participants):

      print(f'{bcolors.FAIL}Error: no hay participantes registrados todavía!\n')

    else:

      winner = rd.choice(list(self.participants))

      print(f'{bcolors.OKCYAN}Resultado: El ganador es 🎉 {winner} 🥳\n')
      self.participants.remove(winner)


  def show_menu(self):

    print(self.heading)
    print(f'{bcolors.FAIL}1. Añadir participante.')
    print(f'{bcolors.OKGREEN}2. Remover participante.')
    print(f'{bcolors.FAIL}3. Listar participantes.')
    print(f'{bcolors.OKGREEN}4. Realizar sorteo')
    print(f'{bcolors.FAIL}5. Salir')

    while True:

      option = input(self.cursor + ' ')

      try:

        option = int(option)

        if 0 >= option or option > 5:
          print(f'{bcolors.FAIL}Error. Opción fuera de rango')
          print(option, type(option), 0 <= option or option > 5)
          continue

      except ValueError:

        print(f'{bcolors.FAIL}Error: Opción inválida')
        continue

      return option

  def welcome_message(self):

    clear()
    print(f'{bcolors.OKGREEN}Bienvenido al calendario de aDEViento')
    print(f'{bcolors.FAIL}24 días, 24 regalos sorpresa relacionados' + \
          ' con desarrollo de software')
    print(f'{bcolors.OKGREEN}Desde el 1 al 24 de diciembre.')
    print(f'{bcolors.FAIL}¿Estás listo para participar?')

    print(f'{bcolors.OKCYAN}\nPresiona enter para continuar')

    input(f'{self.cursor} ')
    clear()

  def start(self):

    self.welcome_message()

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
        print(f'{bcolors.OKCYAN}Saliendo 🕺...')
        sleep(1)
        clear()
        break


if __name__ == '__main__':
  calendar = Participation()
  calendar.start()
