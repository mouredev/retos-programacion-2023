// ## Enunciado

/*
 * Escribe un programa que muestre cómo transcurre un juego de tenis y quién lo ha ganado.
 * El programa recibirá una secuencia formada por "P1" (Player 1) o "P2" (Player 2), según quien
 * gane cada punto del juego.
 *
 * - Las puntuaciones de un juego son "Love" (cero), 15, 30, 40, "Deuce" (empate), ventaja.
 * - Ante la secuencia [P1, P1, P2, P2, P1, P2, P1, P1], el programa mostraría lo siguiente:
 *   15 - Love
 *   30 - Love
 *   30 - 15
 *   30 - 30
 *   40 - 30
 *   Deuce
 *   Ventaja P1
 *   Ha ganado el P1
 * - Si quieres, puedes controlar errores en la entrada de datos.
 * - Consulta las reglas del juego si tienes dudas sobre el sistema de puntos.
 */

async function playGame() {
    const GAME = ["P1", "P1", "P2", "P2", "P1", "P2", "P1", "P1"];
    let play_a = 0;
    let play_b = 0;
    for (const i in GAME) {
        let status = GAME[i];
        if (status == "P1") {
            if (play_a == 0) {
                play_a = 15;
            } else if (play_a == 15) {
                play_a = 30
            } else if (play_a == 30) {
                play_a += 10
            } else if (play_a >= 40) {
                play_a += 10
            }
        } else {
            if (play_b == 0) {
                play_b = 15;
            } else if (play_b == 15) {
                play_b = 30
            } else if (play_b == 30) {
                play_b += 10
            } else if (play_b >= 40) {
                play_b += 10
            } else {
                play_b += 10
            }
        }
        if (play_a <= 40 && play_b < 40 || play_a < 40 && play_b <= 40) {
            console.log(`${play_a} - ${play_b == 0 ? 'Love' : play_b}`)
        } else {
            if (play_a == play_b) {
                console.log('Deuce')
            } else {
                if (play_a > 40) {
                    console.log(`${play_a == 50 ? 'Ventaja P1' : 'Ha ganado el P1'}`);
                } else if (play_b > 40) {
                    console.log(console.log(`${play_b == 50 ? 'Ventaja P2' : 'Ha ganado el P2'}`));
                }
            }
        }
    }
}

(async function () {
    await playGame();
})();