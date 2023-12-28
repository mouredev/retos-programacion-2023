
/*
 * Reto #2: EL PARTIDO DE TENIS
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

const ordenMarcador = ["Love", "15", "30", "40"];

const partido = (secuencia) => {
    
    var puntosP1 = 0, puntosP2 = 0, ventaja = "";
    
    if (secuencia.find (item => item != "P1" && item != "P2") !== undefined) return console.log ("Hay un error en la entrada de los datos.");

    for (var i = 0; i < secuencia.length; i++) {
        
        if (puntosP1 === 3 && puntosP2 === 3) {

            if (ventaja === "") {
                
                ventaja = secuencia [i];
                console.log (`Ventaja ${secuencia [i]}`);
                continue;
            } else {
                if (ventaja === secuencia [i]) return console.log (`Ha ganado el ${secuencia [i]}`);
            }
        } else {

            if (secuencia [i] === "P1") puntosP1++;
            else puntosP2++;
    
            if (puntosP1 === 3 && puntosP2 === 3) {
                console.log ("Deuce");
            } else {
                console.log (`${ordenMarcador[puntosP1]} - ${ordenMarcador[puntosP2]}`);
            }
        }
        
        
        
        
        puntoAnterior = secuencia [i];
    }
}

const secuenciaPrueba0 = ["P1", "P1", "P2", "P2", "P1", "P2", "P3", "P1"];
const secuenciaPrueba1 = ["P1", "P1", "P2", "P2", "P1", "P2", "P1", "P1"];

console.log ("Este primer ejemplo contiene datos erróneos en la secuencia.");
partido (secuenciaPrueba0);
console.log ('')
console.log ("Este segundo ejemplo es el propuesto en el enunciado.");
partido (secuenciaPrueba1);
