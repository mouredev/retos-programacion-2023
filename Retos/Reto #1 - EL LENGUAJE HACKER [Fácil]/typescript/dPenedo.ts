// Escribe un programa que reciba un texto y transforme lenguaje natural a
// "lenguaje hacker" (conocido realmente como "leet" o "1337"). Este lenguaje
//  se caracteriza por sustituir caracteres alfanuméricos.
// - Utiliza esta tabla (https://www.gamehouse.com/blog/leet-speak-cheat-sheet/)
//   con el alfabeto y los números en "leet".
//   (Usa la primera opción de cada transformación. Por ejemplo "4" para la "a")

const leetDictionary = {
    A: "4",
    B: "|3",
    C: "[",
    D: ")",
    E: "3",
    F: "|=",
    G: "&",
    H: "#",
    I: "1",
    J: ",_|",
    K: ">|",
    L: "1",
    M: "/\\/\\",
    N: "^/",
    O: "0",
    P: "|*",
    Q: "(_,)",
    R: "I2",
    S: "5",
    T: "7",
    U: "(_)",
    V: "\\/",
    W: "\\/\\/",
    X: "><",
    Y: "j",
    Z: "2",
    0: "o",
    1: "L",
    2: "R",
    3: "E",
    4: "A",
    5: "S",
    6: "b",
    7: "T",
    8: "B",
    9: "g",
};

function convert_text(normal_text: string): string {
    let new_text = "";
    for (let char of normal_text) {
        const upperChar = char.toUpperCase();
        if (upperChar in leetDictionary) {
            new_text += leetDictionary[upperChar];
        } else {
            new_text += char;
        }
    }
    return new_text;
}
const originalText =
    "Un texto de prueba para ver si funciona el diccionario Leet";
const convertedText = convert_text(originalText);
console.log(convertedText);
