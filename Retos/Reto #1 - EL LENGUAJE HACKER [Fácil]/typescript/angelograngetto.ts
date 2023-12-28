
const letters:{
  [index: string]: string;
} = {
  "A": "4",
  "B": "I3",
  "C": "[",
  "D": ")",
  "E": "3",
  "F": "|=",
  "G": "&",
  "H": "#",
  "I": "1",
  "J": ",_|",
  "K": ">|",
  "L": "1",
  "M": "/\\/\\",
  "N": "^/",
  "O": "0",
  "P": "|*",
  "Q": "(_,)",
  "R": "I2",
  "S": "5",
  "T": "7",
  "U": "(_)",
  "V": "\/",
  "W": "\/\/",
  "X": "><",
  "Y": "j",
  "Z": "2",
};

function encrypt(text:string):string {
  return text.toLocaleUpperCase().split("").reduce((acc, letter) => {
    if(letter === " ") return acc + " ";
    return acc + (letters[letter] || "")
  }, "");
}

console.log(encrypt("hola que tal"));
