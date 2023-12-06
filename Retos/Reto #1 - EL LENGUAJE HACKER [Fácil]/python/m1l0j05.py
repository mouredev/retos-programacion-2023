
# Escribe un programa que reciba un texto y transforme lenguaje natural a
# "lenguaje hacker" (conocido realmente como "leet" o "1337"). Este lenguaje
# se caracteriza por sustituir caracteres alfanuméricos.
# - Utiliza esta tabla (https://www.gamehouse.com/blog/leet-speak-cheat-sheet/) 
# con el alfabeto y los números en "leet".
# (Usa la primera opción de cada transformación. Por ejemplo "4" para la "a")


leetCode = {
  'a': "4",
  'b': "I3",
  'c': "[",
  'd': ")",
  'e': "3",
  'f': "|=",
  'g': "&",
  'h': "#",
  'i': "1",
  'j': ",_|",
  'k': ">|",
  'l': "1",
  'm': "//\\",
  'n': "^/",
  'o': "0",
  'p': "|*",
  'q': "(_,)",
  'r': "I2",
  's': "5",
  't': "7",
  'u': "(_)",
  'v': "/",
  'w': "//",
  'x': "><",
  'y': "j",
  'z': "2",
  1: "L",
  2: "R",
  3: "E",
  4: "A",
  5: "S",
  6: "b",
  7: "T",
  8: "B",
  9: "g",
  0: "o",
}


def leetTraductor (text: str):
  letters = [i for i in text.lower()]
  
  leetTraduction = ''

  for j in letters:
    if j in leetCode:
      leetTraduction = leetTraduction + str(leetCode[j])
    else:
      leetTraduction = leetTraduction + str(j)

  return print(leetTraduction)  

leetTraductor('Hola ?? mundo ?? desde mi script de python')


# OpenAi

def leetTraductor(text: str) -> str:

  # Utilizamos una comprensión de listas para obtener una lista de los caracteres
  # en minúsculas del texto
  letters = [char.lower() for char in text]

  # Utilizamos el método join() para unir los caracteres de la lista en una cadena
  # de texto, reemplazando cada carácter por su correspondiente en el código leet
  # si existe en el diccionario
  leet_traduction = ''.join(
    str(leetCode.get(char, char)) for char in letters
  )

  return leet_traduction

print(leetTraductor('SOY OPEN_AI -- Hola mundo desde mi script de python'))

