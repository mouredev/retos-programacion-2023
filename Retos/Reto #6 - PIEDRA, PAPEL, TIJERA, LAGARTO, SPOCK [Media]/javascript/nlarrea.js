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

const winsOver = {
    "🗿": ["✂️", "🦎"],
    "📄": ["🗿", "🖖"],
    "✂️": ["📄", "🦎"],
    "🦎": ["📄", "🖖"],
    "🖖": ["🗿", "✂️"]
};

function checkWinner(lists){
    let p1Counter = 0, p2Counter = 0;
    
    for(let list of lists){
        if(list.length !== 2) return "Falta alguno de los datos";

        if(list[0] !== list[1]){
            if(winsOver[list[0]].includes(list[1])){
                p1Counter++;
            } else{
                p2Counter++;
            }
        }
    }

    if(p1Counter !== p2Counter){
        if(p1Counter > p2Counter) return "Player 1";
        else return "Player 2";
    } else return "Tie";
}


console.log(checkWinner([["🗿","✂️"], ["✂️","🗿"], ["📄","✂️"]]));      // Player 2
console.log(checkWinner([["🗿","✂️"], ["📄","✂️"]]));                   // Tie
console.log(checkWinner([["🗿","🗿"], ["✂️", "📄"]]));                  // Player 1
console.log(checkWinner([["🦎","✂️"], ["🖖","🗿"], ["🖖","✂️"]]));      // Player 1