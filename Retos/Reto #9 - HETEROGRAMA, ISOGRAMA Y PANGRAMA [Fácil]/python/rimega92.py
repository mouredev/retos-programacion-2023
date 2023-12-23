#Crea 3 funciones, cada una encargada de detectar si una cadena de
#texto es un heterograma, un isograma o un pangrama.
#- Debes buscar la definición de cada uno de estos términos.




def heterograma(cadena):
      cadena = cadena.lower()
      for i in cadena:
         if cadena.count(i) > 1:
               return False
      return True

def isograma(cadena):
      cadena = cadena.lower()
      for i in cadena:
         if cadena.count(i) > 1:
               return False
      return True

def pangrama(cadena):
      cadena = cadena.lower()
      for i in "abcdefghijklmnopqrstuvwxyz":
         if i not in cadena:
               return False
      return True

print(heterograma("luteranismo"))
print(isograma("papelera"))
print(pangrama("Benjamín pidió una bebida de kiwi y fresa. Noé, sin vergüenza, la más exquisita champaña del menú."))

