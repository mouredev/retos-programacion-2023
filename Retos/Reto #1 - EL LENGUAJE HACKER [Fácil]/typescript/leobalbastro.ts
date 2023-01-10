let leetAlphabet ={
    'A' : "4",
    'B' : "l3",
    'C' : "[",
    'D' : ")",
    'E' : "3",
    'F' : "|=",
    'G' : "&",
    'H' : "#",
    'I' : "1",
    'J' : ",_|",
    'K' : ">|",
    'L' : "1",
    'M' : "JVI",
    'N' : "^/",
    'O' : "0",
    'P' : "|*",
    'Q' : "(_,)",
    'R' : "I2",
    'S' : "5",
    'T' : "7",
    'U' : "(_)",
    'V' : "\/",
    'W' : "VV",
    'X' : "><",
    'Y' : "j",
    'Z' : "2",
    ' ' : " ",
    1 : "1",
    2 : "2",
    3 : "3",
    4 : "4",
    5 : "5",
    6 : "6",
    7 : "7",
    8 : "8",
    9 : "9",
    0 : "0",
}

function leetString(chain : string){
    let originChain = chain;
    let origin = chain.toUpperCase();
    let tempResult = [];
    let arrayString = origin.split("");
    for (let i in arrayString) {
        let letter = arrayString[i];
        let replaceLetter = leetAlphabet[letter as keyof typeof leetAlphabet]
        tempResult.push(replaceLetter);
    }
    let finalResult = tempResult.join("");
    console.log(`la cadena original es: ${originChain}`);
    console.log(`La cadena en formato 1337 es: ${finalResult}`);
}

leetString("anonLeet645");
