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

var puntuaciones = {
    "P1": "Love",
    "P2": "Love"
};

var resultados = [];
// var resultados = ['P1', 'P1', 'P2', 'P2', 'P1', 'P2', 'P1', 'P1'];

while (Object.values(puntuaciones).indexOf('Ganador')  === -1) {
    if (resultados.length) {
        for (var i = 0; i < resultados.length; i++) {
            var partida = {
                ganador: resultados[i],
                perdedor: resultados[i] == "P1" ? "P2" : "P1"
            }

            resultadoPartida(partida);
        }
    } else {
        // Partida con puntuaciones aleatorias
        var partida = ganadorPartida(2);

        resultadoPartida(partida);
    }
}

function resultadoPartida(partida) {
    if (puntuaciones[partida.ganador] == "Love") {
        puntuaciones[partida.ganador] = 15;
    } else if (puntuaciones[partida.ganador] == 15) {
        puntuaciones[partida.ganador] = 30;
    } else if (puntuaciones[partida.ganador] == 30) {
        if (puntuaciones[partida.perdedor] == 40) {
            puntuaciones[partida.ganador] = "Deuce";
            puntuaciones[partida.perdedor] = "Deuce";
        } else {
            puntuaciones[partida.ganador] = 40;
        }
    } else if (puntuaciones[partida.ganador] == 40 || puntuaciones[partida.ganador] == "Ventaja") {
        puntuaciones[partida.ganador] = "Ganador";
    } else if (puntuaciones[partida.ganador] == "Deuce" && puntuaciones[partida.perdedor] == "Ventaja") {
        puntuaciones[partida.ganador] = "Deuce";
        puntuaciones[partida.perdedor] = "Deuce";
    } else if (puntuaciones[partida.ganador] == "Deuce") {
        puntuaciones[partida.ganador] = "Ventaja";
        puntuaciones[partida.perdedor] = "Deuce";
    }

    if (Object.values(puntuaciones).indexOf('Ganador') > -1) {
        console.log("Ha ganado el " + partida.ganador);
    } else if (Object.values(puntuaciones).indexOf('Ventaja') > -1) { 
        console.log("Ventaja " + partida.ganador);
    } else if (Object.values(puntuaciones).indexOf('Deuce') > -1) { 
        console.log("Deuce");
    } else {
        console.log(puntuaciones["P1"] + " - " + puntuaciones["P2"]);
    }
}

function ganadorPartida(max) {
    if (Math.floor(Math.random() * max) == 1) {
        return {"ganador": "P2", "perdedor": "P1"};
    } else {
        return {"ganador": "P1", "perdedor": "P2"};
    }
}

function getKeyByValue(object, value) {
    return Object.keys(object).find(key => object[key] === value);
}