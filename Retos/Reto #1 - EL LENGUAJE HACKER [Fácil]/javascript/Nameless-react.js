const readline = require('readline');

const hackerLenguaje = (text) => {
    const replaceLetters = {
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
        "R": "|2",
        "S": "5",
        "T": "7",
        "U": "(_)",
        "V": "\\/",
        "W": "\\/\\/",
        "X": "><",
        "Y": "j",
        "Z": "2",
        " ": " ",        
        "1": "L",        
        "2": "R",        
        "3": "E",        
        "4": "A",        
        "5": "S",        
        "6": "b",        
        "7": "T",        
        "8": "B",        
        "9": "g",        
        "0": "o",        
    }
   
    const translation = Array.from(text).map(letter => replaceLetters[letter.toUpperCase()] || letter).join("");
    console.log(translation);
    rl.close();
}


const rl = readline.createInterface({
    input: process.stdin,
    output: process.stdout
});
rl.question("Digite un nombre o palabra: ", (word)  => hackerLenguaje(word));

