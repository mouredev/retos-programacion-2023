// # Reto #1: EL "LENGUAJE HACKER"
// #### Dificultad: Fácil | Publicación: 02/01/23 | Corrección: 09/01/23

// ## Enunciado

// ```
// /*
//  * Escribe un programa que reciba un texto y transforme lenguaje natural a
//  * "lenguaje hacker" (conocido realmente como "leet" o "1337"). Este lenguaje
//  *  se caracteriza por sustituir caracteres alfanuméricos.
//  * - Utiliza esta tabla (https://www.gamehouse.com/blog/leet-speak-cheat-sheet/)
//  *   con el alfabeto y los números en "leet".
//  *   (Usa la primera opción de cada transformación. Por ejemplo "4" para la "a")
//  */
// ```

function leetSpeak(text) {
  const dictionary = {
    A: "4",
    B: "8",
    C: "(",
    D: "[)",
    E: "3",
    F: "|=",
    G: "6",
    H: "#",
    I: "1",
    J: "_|",
    K: "|<",
    L: "|_",
    M: "JVI",
    N: "||",
    O: "0",
    P: "|>",
    Q: "9",
    R: "|2",
    S: "5",
    T: "7",
    U: "|_|",
    V: "\\/",
    W: "\\/\\/",
    X: "><",
    Y: "`/",
    Z: "2",
    1: "I",
    2: "Z",
    3: "E",
    4: "A",
    5: "S",
    6: "G",
    7: "T",
    8: "B",
    9: "g",
    0: "O",
  };

  const textArray = text.toUpperCase().split("");
  const textHacker = textArray.map((letter) => {
    if (dictionary[letter]) {
      return dictionary[letter];
    } else {
      return letter;
    }
  });
  return textHacker.join("");
}

console.log(leetSpeak("Hola mundo! 2023"))
