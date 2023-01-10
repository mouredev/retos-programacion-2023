/*
 * Escribe un programa que reciba un texto y transforme lenguaje natural a
 * "lenguaje hacker" (conocido realmente como "leet" o "1337"). Este lenguaje
 *  se caracteriza por sustituir caracteres alfanuméricos.
 * - Utiliza esta tabla (https://www.gamehouse.com/blog/leet-speak-cheat-sheet/)
 *   con el alfabeto y los números en "leet".
 *   (Usa la primera opción de cada transformación. Por ejemplo "4" para la "a")
 */

function leetSpeakTranslator(text: string): string {

    const leetSpeakMap:{[key:string]:string} = {
        "a" : "4",
        "b" : "I3",
        "c" :"[",
        "d" :")",
        "e" :"3",
        "f" : "|=",
        "g" : "&",
        "h" : "#",
        "i" : "1",
        "j" : ",_|",
        "k" : ">|",
        "l" : "1",
        "m" : "/\\/\\",
        "n" : "^/",
        "o" : "0",
        "p" : "|*",
        "q" : "(_,)",
        "r" : "I2",
        "s" : "5",
        "t" : "7",
        "u" : "(_)",
        "v" : "\\/",
        "w" : "\\/\\/",
        "x" : "><",
        "y" : "j",
        "z" : "2",
        "0" : "o",
        "1" : "L",
        "2" : "R",
        "3" : "E",
        "4" : "A",
        "5" : "S",
        "6" : "b",
        "7" : "T",
        "8" : "B",
        "9" : "g"

    }



  let textArray = text.toLowerCase().split('');
  let leetSpeakArray:string[] = []

  textArray.forEach((letter) => {
    if (leetSpeakMap[letter]) {
      leetSpeakArray.push(leetSpeakMap[letter]);
    } else {
      leetSpeakArray.push(letter);
    }
  })

  return leetSpeakArray.join('');

}

console.log(leetSpeakTranslator('Feliz 2023'));
console.log(leetSpeakTranslator('La Luma asoma : Federico García Lorca'));
console.log(leetSpeakTranslator('Cuando sale la luna\n' +
                                    'se pierden las campanas\n' +
                                    'y aparecen las sendas\n' +
                                    'impenetrables.\n' +
                                    'Cuando sale la luna,\n' +
                                    'el mar cubre la tierra\n' +
                                    'y el corazón se siente\n' +
                                    'isla en el infinito.\n' +
                                    'Nadie come naranjas\n' +
                                    'bajo la luna llena.\n' +
                                    'Es preciso comer\n' +
                                    'fruta verde y helada.\n' +
                                    'Cuando sale la luna\n' +
                                    'de cien rostros iguales,\n' +
                                    'la moneda de plata\n' +
                                    'solloza en el bolsillo.'));
