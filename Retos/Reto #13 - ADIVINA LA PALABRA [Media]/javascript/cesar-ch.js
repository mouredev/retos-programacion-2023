/*
 * Crea un pequeño juego que consista en adivinar palabras en un número máximo de intentos:
 * - El juego comienza proponiendo una palabra aleatoria incompleta
 *   - Por ejemplo "m_ur_d_v", y el número de intentos que le quedan
 * - El usuario puede introducir únicamente una letra o una palabra (de la misma longitud que
 *   la palabra a adivinar)
 *   - Si escribe una letra y acierta, se muestra esa letra en la palabra. Si falla, se resta
 *     uno al número de intentos
 *   - Si escribe una resolución y acierta, finaliza el juego, en caso contrario, se resta uno
 *     al número de intentos
 *   - Si el contador de intentos llega a 0, el jugador pierde
 * - La palabra debe ocultar de forma aleatoria letras, y nunca puede comenzar
 *   ocultando más del 60%
 * - Puedes utilizar las palabras que quieras y el número de intentos que consideres
 */


function GuessWord(originalWord) {
    let word = HiddenWord(originalWord)
    let attempts = Math.round((originalWord.length) / 2) + 1

    while (attempts > 0) {
        console.log("Número de intentos:", attempts)
        console.log("Palabra oculta:", word)
        let input = prompt("Introduce una letra: ")

        let found = false;

        for (let i = 0; i < originalWord.length; i++) {
            if (originalWord[i] === input && word[i] === "_") {
                word = word.split("");
                word[i] = input;
                word = word.join("");
                found = true;
                console.log(word)
            }
        }
        if (word === originalWord) {
            break;
        }

        if (!found) {
            attempts--;
        }

    }

    if (word === originalWord) {
        console.log("Has ganado");
    } else {
        console.log("Has perdido");
    }

}

function HiddenWord(word) {
    let len = Math.round(word.length * 0.6)
    let arr = Array(word.length).fill("_")
    for (let i = 0; i < len; i++) {
        let index = Math.round(Math.random() * word.length)
        if (arr[index] === word[index]) {
            i--
        } else {
            arr[index] = word[index]
        }
    }
    return arr.join("")
}


console.log(GuessWord("mouredev"))