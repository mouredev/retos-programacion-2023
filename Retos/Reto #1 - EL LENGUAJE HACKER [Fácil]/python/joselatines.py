

leet = {"A": "4", "B": "I3", "C": "[", "D": ")", "E": "3", "F": "|=", "G": "&", "H": "#", "I": "1",

            "J": ",_|", "K": ">|", "L": "1", "M": "/\/\\", "N": " ^/", "O": "0", "P": " |*", "Q": "(_,)",
            "R": "I2", "S": "5", "T": "7", "U": "(_)", "V": "\/", "W": "\/\/", "X": "><", "Y": "j", "Z": "2",
            "1": "L", "2": "R", "3": "E", "4": "A", "5": "S", "6": "b", "7": "T", "8": "B", "9": "g", "0": "o"}

def text_to_leet(text):
  text = text.upper()
  new_text = ''

  for character in text:
    if character in leet.keys():
      new_text += character.replace(character, leet[character])

    else:
      new_text += character

  return new_text

text = input('Insert a text: ')
print(text_to_leet(text))
