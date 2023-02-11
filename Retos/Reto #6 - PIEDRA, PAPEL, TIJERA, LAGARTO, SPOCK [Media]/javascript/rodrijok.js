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


function piedraPapelTijeraLagartoSpock(lists){
    let formas_ganar = {
        "🗿": ["🦎", "✂️"],
        "📄": ["🗿", "🖖"],
        "✂️": ["📄", "🦎"],
        "🦎": ["🖖", "📄"],
        "🖖": ["✂️", "🗿"]
    };

    let p1Counter = 0, p2Counter = 0;
    for(let i = 0; i < lists.length; i++){
        if(lists[i][0] != lists[i][1]){
            if(formas_ganar[lists[i][0]].includes(lists[i][1])){
                p1Counter++;
            }else{
                p2Counter++;
            }
        }else{
            p1Counter++;
            p2Counter++;
        }
    }

    if(p1Counter > p2Counter){
        return "Player 1";
    }else if(p2Counter > p1Counter){
        return "Player 2";
    }else{
        return "Tie";
    }
}

console.log(piedraPapelTijeraLagartoSpock([[("🗿","✂️"), ("✂️","🗿"), ("📄","✂️")]]));
console.log(piedraPapelTijeraLagartoSpock([[("🗿","🗿"), ("✂️","✂️"), ("🦎","🦎")]])); 
console.log(piedraPapelTijeraLagartoSpock([[("✂️","✂️"), ("🦎","🖖"), ("🦎","✂️")]]));
console.log(piedraPapelTijeraLagartoSpock([[("✂️","✂️"), ("🦎","🖖"), ("🗿","✂️")]]));
console.log(piedraPapelTijeraLagartoSpock([[("🗿","🗿"), ("✂️","✂️"), ("🦎","🦎")]]));
console.log(piedraPapelTijeraLagartoSpock([["🗿", "🗿"], ["✂️", "✂️"], ["🦎", "🦎"]]))
console.log(piedraPapelTijeraLagartoSpock([["✂️", "✂️"], ["🦎", "🖖"], ["🦎", "✂️"]]))