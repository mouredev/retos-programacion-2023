const leetAlphabet = {
  "a": "4",
  "b": "8",
  "c": "[",
  "d": ")",
  "e": "3",
  "f": "/=",
  "g": "6",
  "h": "#",
  "i": "1",
  "j": "]",
  "k": "1<",
  "l": "|",
  "m": "|v|",
  "n": "/v",
  "o": "[]",
  "p": "?",
  "q": "9",
  "r": "|9",
  "s": "$",
  "t": "/",
  "u": "(_)",
  "v": "|/",
  "w": "2u",
  "x": ")(",
  "y": "7",
  "z": "7_",
  " ": " "
}

const conversorLeet = text => {
  let leetText = ''
  for (char in text){
    let alphabetChar = text[char].toLowerCase()
    leetChar = leetAlphabet[alphabetChar]
    leetText +=  leetChar
  }
  console.log(leetText)
}

conversorLeet("Hola mundo soy Poncho Ramos")
