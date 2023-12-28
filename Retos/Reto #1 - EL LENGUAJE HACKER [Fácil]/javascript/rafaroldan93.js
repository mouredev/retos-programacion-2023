let text = "¡Hola, mundo 2023!";
let translate = "";
const dic = {
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
    "m": "/\\/\\",
    "n": "^/",
    "o": "0",
    "p": "|*",
    "q": "(_,)",
    "r": "I2",
    "s": "5",
    "t": "7",
    "u": "(_)",
    "v": "\/",
    "w": "\/\/",
    "x": "><",
    "y": "j",
    "z": "2",
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
};

for (i = 0; i < text.length; i++) {
    let letter = text.charAt(i).toLowerCase();
    if (letter.match(/[a-z0-9]/)) {
        letter = dic[letter];
    }
    translate += letter;
}

console.log(text);
console.log(translate);
