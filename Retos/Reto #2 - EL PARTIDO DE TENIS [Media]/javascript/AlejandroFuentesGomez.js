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

const possiblePoints = [15, 30, 40]
const sequence = ['P1', 'P1', 'P2', 'P2', 'P1', 'P2', 'P1', 'P2', 'P1', 'P2', 'P2', 'P2']
const sequence2 = ['P1', 'P1', 'P1', 'P1']

decideTennisMatch(sequence1);
function decideTennisMatch(sequence) {
    let initialResult = {
        "P1": 'Love',
        "P2": 'Love',
        "AUX": '',
    }
    let participant1 = 0;
    let participant2 = 0;
    let log = '';
    sequence.forEach(element => {
        if (initialResult['P1'] != 40 && initialResult['P2'] != 40) {
            switch (element) {
                case 'P1':
                    initialResult[element] = possiblePoints[participant1];
                    participant1 = participant1 + 1;
                    break;
                case 'P2':
                    initialResult[element] = possiblePoints[participant2];
                    participant2 = participant2 + 1;
                    break;
                default:
                    break;
            }
            
            log = initialResult['P1'] + ' - ' + initialResult['P2'];
            console.log(log);
        }
        else {
            switch (initialResult['AUX']) {
                case '':
                    if(initialResult['P1'] === 40 && element === 'P1'){
                        initialResult['AUX'] = 'Ha ganado P1';
                    }
                    if(initialResult['P2'] === 40 && element === 'P2'){
                        initialResult['AUX'] = 'Ha ganado P2';
                    }
                    else{
                        initialResult['AUX'] = 'Deuce';
                    }
                    break;
                case 'Ventaja P1':
                    initialResult['AUX'] = element === 'P1' ? 'Ha ganado P1' : 'Deuce' ;
                    break;
                case 'Ventaja P2':
                    initialResult['AUX'] = element === 'P1' ? 'Deuce' : 'Ha ganado P2' ;
                    break;
                case 'Deuce':
                    initialResult['AUX'] = element === 'P1' ? 'Ventaja P1' : 'Ventaja P2' ;
                    break;
                default:
                    break;
            }
            log = initialResult['AUX'];
            console.log(log);
        }

    }
    );
}