def get_dictionary():
  traditional_alphabet = list("ABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890 ")
  hacker_alphabet = ["4","I3","[",")","3","|=","&","#","1",",_|",">|","1","^^","^/","0","|*","(_,)","I2","5","7","(_)","\/","\/\/","><","j","2","L","R","E","A","S","b","T","B","g","o", " "]

  dictionary = { key: value for key, value in zip(traditional_alphabet, hacker_alphabet)}

  return dictionary


def translate(text):
  dictionary = get_dictionary()
  translated_text = ""
  for letter in text:
    translated_text += dictionary.get(letter) if dictionary.get(letter) else ""
  
  return translated_text


def clean_text(text):
  a,b = 'áéíóúüñ','aeiouun'
  trans = str.maketrans(a,b)

  new_text = text.replace("  ", " ").lower()
  new_text = new_text.translate(trans)

  return new_text.upper()


def run():
  user_text = input("Type some text and we'll translate into hacker language: ")
  cleaned_text = clean_text(user_text)
  translated = translate(cleaned_text)

  print(f"{user_text} = {translated}")
  print("NOTE: All special caracteres are deleted")


if __name__ == "__main__":
  run()


