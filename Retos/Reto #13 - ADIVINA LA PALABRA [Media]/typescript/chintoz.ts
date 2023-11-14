import readLine from "readline-sync";

let attempts = 10

function selectWordToPlay(): string {
    // This dictionary could be retrieved from any API
    let dictionary = ["computacion", "lenguaje", "bucle", "iterador", "patron", "incidente"]
    let index = Math.ceil(Math.random() * 10000 % dictionary.length) - 1
    return dictionary[index];
}

function readInput(): string {
    return readLine.question("Numero de intentos restantes: " + attempts + ". Que valor quieres introducir: ")
}

function manageWordSelection(word: string, playerInput: string): boolean {
    if (playerInput === word) {
        console.log("Has ganado la partida. La palabra seleccionada es la correcta: " + playerInput)
        return true;
    } else {
        console.log("La palabra introducida no es la correcta. Intentalo de nuevo. Número de intentos restantes " + attempts)
        return false;
    }
}

export function playGame() {
    let word: string = selectWordToPlay()
    let playerWord = word.split("").map(c => Math.random() <= 0.4 ? c : "*").join("")
    console.log("Comienza el juego. Tienes " + attempts + " intentos para averiguar la palabra: " + playerWord);

    while (attempts > 0) {
        // Introduce un caracter o una palabra
        let playerInput = readInput();
        if (playerInput.length > 1) {
            if (manageWordSelection(word, playerInput)) {
                break
            }
        } else {
            playerWord = word.split("")
                .map((c: string, index: number) => c === playerInput || playerWord[index] !== "*" ? c : "*")
                .join("")
            if (playerWord.indexOf("*") < 0) {
                console.log("Has ganado. Has completado la palabra: " + word)
                break
            } else {
                console.log("Sigue intentandolo. Tienes " + attempts + " intentos para completar la palabra:" + playerWord)
            }
        }
        attempts--
    }
    if (attempts == 0) {
        console.log("Has perdido. Vuelve a intentarlo cuando quieras.")
    }
}


playGame()




