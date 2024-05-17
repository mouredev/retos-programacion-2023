const alphabet = [
  "A",  "B",  "C",  "D",  "E",  "F",  "G",  "H",  "I",  "J",  "K",  "L",  "M",  "N",  "O",  "P",  "Q",  "R",  "S",  "T",  "U",  "V",  "W",  "X",  "Y",  "Z",
];

const leet = [
  "4",  "I3",  "[",  ")",  "3",  "|=",  "&",  "#",  "1",  ",_|",  ">|",  "1",  "/\\/\\",  "^/",  "0",  "|*",  "(_,)",  "I2",  "5",  "7",  "(_)",  "/",  "//",  "><",  "j",  "2",
];

function characterConverter(character) {
  const index = alphabet.indexOf(character.toUpperCase());
  if (index !== -1) {
    return leet[index];
  } else {
    return character;
  }
}

function textConverter(text) {
  let convertedText = "";
  for (let i = 0; i < text.length; i++) {
    convertedText += characterConverter(text[i]);
    console.log(convertedText)
  }
  return convertedText;
}

console.log(textConverter("1. Estoy cansado jefe"));

//  Otra version sugerida por Gemini

function textConverter(text) {
  const leetMap = { // Combine alphabet and leet into a single object
    "A": "4", "B": "I3", "C": "[", "D": ")", "E": "3", "F": "|=",
    "G": "&", "H": "#", "I": "1", "J": ",_|", "K": ">|", "L": "1",
    "M": "/\\/\\", "N": "^/", "O": "0", "P": "|*", "Q": "(_,)",
    "R": "I2", "S": "5", "T": "7", "U": "(_)", "V": "/", "W": "//",
    "X": "><", "Y": "j", "Z": "2"
  };
  return text.replace(/\w/g, (char) => leetMap[char.toUpperCase()] || char); // Use replace with regular expression
}

console.log(textConverter("2. Estoy cansado jefe")); // Call the function
