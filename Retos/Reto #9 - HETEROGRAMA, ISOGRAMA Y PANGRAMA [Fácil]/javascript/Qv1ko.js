heterogram("the big dwarf only jumps")
isogram("copycopycopy")
pangram("Waxy and quivering, jocks fumble the pizza")

function heterogram(str) {
    let isHeterogram = true;
    Array.from(lettersCounter(str).values()).forEach(letterNumber => {
        if (letterNumber !== 1) {
            isHeterogram = false;
            return;
        }
    });
    console.log((isHeterogram) ? "The string \"" + str + "\" is a heterogram" : "The string \"" + str + "\" is not a heterogram");
}

function isogram(str) {
    let isIsogram = true;
    let lettersValue = 0;
    Array.from(lettersCounter(str).values()).forEach(letterNumber => {
        lettersValue = (lettersValue === 0) ? letterNumber : lettersValue;
        if (letterNumber !== lettersValue) {
            isIsogram = false;
            return;
        }
    });
    console.log((isIsogram) ? "The string \"" + str + "\" is an isogram" : "The string \"" + str + "\" is not an isogram");
}

function pangram(str) {
    let isPangram = (lettersCounter(str).size !== 26) ? false : true;
    console.log((isPangram) ? "The string \"" + str + "\" is a pangram" : "The string \"" + str + "\" is not a pangram");
}

function lettersCounter(str) {
    str = str.toLowerCase();
    let letters = new Map();
    for (let i = 0; i < str.length; i++) {
        if (isLetter(str.charAt(i))) {
            if (letters.has(str.charAt(i))) {
                letters.set(str.charAt(i), letters.get(str.charAt(i)) + 1);
            } else {
                letters.set(str.charAt(i), 1);
            }
        }
    }
    return letters;
}

function isLetter(char) {
    return char.match(/[a-z]/i);
}
