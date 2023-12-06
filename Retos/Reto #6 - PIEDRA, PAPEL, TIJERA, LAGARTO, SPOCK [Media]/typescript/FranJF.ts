/*
 * Crea un programa que calcule quien gana más partidas al piedra,
 * papel, tijera, lagarto, spock.
 * - El resultado puede ser: "Player 1", "Player 2", "Tie" (empate)
 * - La función recibe un listado que contiene pares, representando cada jugada.
 * - El par puede contener combinaciones de "🗿" (piedra), "📄" (papel),
 *   "✂️" (tijera), "🦎" (lagarto) o "🖖" (spock).
 * - Ejemplo. Entrada: [("🗿","✂️"), ("✂️","🗿"), ("📄","✂️")]. Resultado: "Player 2".
 * - Debes buscar información sobre cómo se juega con estas 5 posibilidades.
*/

const combinacionesGanadoras: object = {
    "piedra": ["tijeras", "lagarto"],
    "papel": ["piedra", "spock"],
    "tijeras": ["papel", "lagarto"],
    "lagarto": ["papel", "spock"],
    "spock": ["piedra", "tijeras"]
}

function juego(combinacion: Array<[string, string]>): string {
    let puntosPlayer1: number = 0;
    let puntosPlayer2: number = 0;

    combinacion.forEach(tupla => {
        let eleccionPlayer1: string = tupla[0];
        let eleccionPlayer2: string = tupla[1];
        let combinacionesGanadorasPlayer1: string[] = combinacionesGanadoras[eleccionPlayer1];

        let mismaEleccion = true ? eleccionPlayer1 == eleccionPlayer2 : false;
        if (!mismaEleccion) {
            let ganador: number = combinacionesGanadorasPlayer1.includes(eleccionPlayer2) ? 1 : 2;
            switch (ganador) {
                case 1:
                    puntosPlayer1++;
                    break;
                case 2:
                    puntosPlayer2++;
                    break
                default:
                    throw ("Esto no deberia pasar");
            }
        };

    });

    if (puntosPlayer1 > puntosPlayer2) {
        return "Player 1"
    } else if (puntosPlayer1 < puntosPlayer2) {
        return "Player 2"
    } else {
        return "Tie"
    }
}

console.info(juego([["tijeras", "papel"], ["lagarto", "spock"], ["papel", "piedra"]]))
console.info(juego([["piedra", "piedra"], ["spock", "spock"], ["tijeras", "tijeras"]]))
console.info(juego([["piedra", "papel"], ["spock", "lagarto"], ["tijeras", "piedra"]]))
