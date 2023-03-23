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

const secuencia = ["P1", "P1", "P2", "P2", "P1", "P2", "P1", "P2","P2","p1","p1","p1"]
/*
Se espera:
P1: 15 --- P2: Love
P1: 30 --- P2: Love
P1: 30 --- P2: 15
P1: 30 --- P2: 30
P1: 40 --- P2: 30
Deuce
Ventaja P1
Deuce
Ventaja P2
Deuce
Ventaja P1
Ha ganado P1
*/

let puntuacion = {
    P1: 0,
    P2: 0
}

const puntos = {
    0: "Love",
    1: 15,
    2: 30,
    3: 40,
    4: "Deuce",
    5: "Ventaja",
    6: "Ha ganado"
}

let resultado = ""
for (let i = 0; i < secuencia.length; i++) {
    const player = secuencia[i].toUpperCase();

    if (player === "P1") {
        puntuacion.P1++
    } else if (player === "P2") {
        puntuacion.P2++
    } else {
        resultado = "No es un jugador válido."
        break
    }


    // Comprobar si hay empate
    if (puntuacion.P1 === puntuacion.P2 && puntuacion.P1 >= 3) {
        puntuacion.P1 = 4
        puntuacion.P2 = 4
        resultado += `${ puntos[4] } player \n`
    } else if(puntuacion.P1 === 5 || puntuacion.P2 === 5) {
        //Hay ventaja para uno de los dos
        resultado += `${ puntos[5] } player \n`
    } else if (puntuacion.P1 === 6 || puntuacion.P2 === 6) {
        //Hay ganador
        resultado += `${ puntos[6] } player \n`

        //Generar error si hay mas elementos en la secuencia y el juego ya ha terminado
        if (i < secuencia.length - 1) {
            resultado = "Error: El juego ya habia terminado."
            break
        }
    } else {
        //No hay ventaja ni ganador
        resultado += `P1: ${ puntos[puntuacion.P1] } --- P2: ${ puntos[puntuacion.P2] } \n`
    }
}

console.log(resultado)

