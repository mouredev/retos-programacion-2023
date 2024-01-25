import random

class App:
  def __init__(self):
    self.persons = []

  def add(self, person):
    if person not in self.persons:
      self.persons.append(person)
      return True
    else:
      return False

  def delete(self, person):
    if person in self.persons:
      self.persons.remove(person)
      return True
    else:
      return False
  
  def lottery(self):
    if len(self.persons) == 0:
      return None
    choice = random.choice(self.persons)
    self.persons.remove(choice)
    return choice
  
  def show(self):
    if len(self.persons) == 0:
      print("No hay participantes")
      return
    print("Participantes:")
    for p in self.persons:
      print(p)

def main():
  app = App()
  menu = """
  Selecciona una opcion:
  1. Anadir participante
  2. Eliminar participante
  3. Mostrar participantes
  4. Realizar sorteo
  5. Salir
  """
  while True:
    print(menu)
    try:
      option = int(input("Opcion: "))
      if option == 1:
        name = input("Participante: ")
        result = app.add(name)
        if result:
          print("Anadido")
        else:
          print("Paricipante ya existe")
      elif option == 2:
        name = input("Participante: ")
        result = app.delete(name)
        if result:
          print("Eliminado")
        else:
          print("Participante no existe")
      elif option == 3:
        app.show()
      elif option == 4:
        result = app.lottery()
        if result == None:
          print("No hay participantes")
        else:
          print("El ganador del sorteo es:", result)
      elif option == 5:
        print("Adios")
        break
      else:
        print("Opcion invalida")
    except:
      print("Opcion invalida")
    

if __name__ == "__main__":
  main()
