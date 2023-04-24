leet_dict = {
  'a': '4',
  'b': 'I3',
  'c': '[',
  'd': ')',
  'e': '3',
  'f': '|=',
  'g': '&',
  'h': '#',
  'i': '1',
  'j': ',_|',
  'k': '>|',
  'l': '|',
  'm': '/\/\\',
  'n': '^/',
  'o': '0',
  'p': '|*',
  'q': '(_,)',
  'r': 'I2',
  's': '5',
  't': '7',
  'u': '(_)',
  'v': '\/',
  'w': '\/\/',
  'x': '><',
  'y': 'j',
  'z': '2'
}

while True:
  text = input("Ingresa el texto a convertir a leet: ")
  text = text.lower()
  leet_text = ""
  for char in text:
    if char in leet_dict:
      leet_text += leet_dict[char]
    else:
      leet_text += char
  print(f"Texto en leet: {leet_text}")
