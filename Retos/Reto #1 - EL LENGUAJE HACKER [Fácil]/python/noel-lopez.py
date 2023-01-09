# same as ../javascript/noel-lopez.js but in python

hackerLettersDict = {
  'a': '4',
  'b': 'I3',
  'c': '[',
  'd': ')',
  'e': '3',
  'f': '|=',
  'g': '&',
  'h': '#',
  'i': '1',
  'j': ",_|",
  'k': ">|",
  'l': "1",
  'm': "/\\/\\",
  'n': "^/",
  'o': "0",
  'p': "|*",
  'q': "(_,)",
  'r': "I2",
  's': "5",
  't': "7",
  'u': "(_)",
  'v': "\\/",
  'w': "\\/\\/",
  'x': "><",
  'y': "j",
  'z': "2",
  '1': "L",
  '2': "R",
  '3': "E",
  '4': "A",
  '5': "S",
  '6': "b",
  '7': "T",
  '8': "B",
  '9': "g",
  '0': "o",
}

def hackerLetters(word):
  word = word.lower()
  hackerWord = ""
  for letter in word:
    if letter in hackerLettersDict:
      hackerWord += hackerLettersDict[letter]
    else:
      hackerWord += letter
  return hackerWord

output = hackerLetters("Hola mundo! 2023")
print(output)