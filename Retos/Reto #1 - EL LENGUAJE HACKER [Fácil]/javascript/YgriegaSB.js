// Alfabeto Leet
const leetAlphabet = {
    "a": "4",
    "b": "I3",
    "c": "[",
    "d": ")",
    "e": "3",
    "f": "|=",
    "g": "&",
    "h": "#",
    "i": "1",
    "j": ",_|",
    "k": ">|",
    "l": "1",
    "m": "JVI",
    "n": "^/",
    "o": "0",
    "p": "|*",
    "q": "(_,)",
    "r": "|2",
    "s": "5",
    "t": "7",
    "u": "(_)",
    "v": "\\/",
    "w": "\\/\\/",
    "x": "><",
    "y": "`/",
    "z": "2",
    "0": "o",
    "1": "L",
    "2": "R",
    "3": "E",
    "4": "A",
    "5": "S",
    "6": "b",
    "7": "T",
    "8": "B",
    "9": "g",
};
// Texto objetivo
let txt = "Este texto se transforma a alfabeto leet - 1337 1337 1337 1337";
// Texto output
let leettxt = "";
for(let i = 0; i < txt.length; i++) {
    // Variable char para encontrar la letra en el alfabeto 
    let char = txt.charAt(i).toLowerCase();
    // Si la letra no se encuentra en el alfabeto, se añade la letra
    if(!leetAlphabet[char]) {
        leettxt += char
    }else {
        leettxt += leetAlphabet[char];
    }
}
console.log(leettxt);