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


function GuessWord2(originalWord: string): void {
    let word: string = HiddenWord2(originalWord)
    let attempts: number = Math.round((originalWord.length) / 2) + 1

    while (attempts > 0) {
        console.log("Número de intentos:", attempts)
        console.log("Palabra oculta:", word)
        let input: string | null = prompt("Introduce una letra: ")

        let found: boolean = false;

        for (let i = 0; i < originalWord.length; i++) {
            if (originalWord[i] === input && word[i] === "_") {
                word = word.substring(0, i) + input + word.substring(i + 1)
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

function HiddenWord2(word: string): string {
    let len: number = Math.round(word.length * 0.6)
    let arr: string[] = Array(word.length).fill("_")
    for (let i = 0; i < len; i++) {
        let index: number = Math.round(Math.random() * word.length)
        if (arr[index] === word[index]) {
            i--
        } else {
            arr[index] = word[index]
        }
    }
    return arr.join("")
}


console.log(GuessWord2("mouredev"))