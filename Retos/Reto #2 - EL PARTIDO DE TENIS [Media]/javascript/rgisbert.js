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

const gameStructure = {
    states: ['Love', '15', '30', '40', 'Deuce', 'Ventaja', 'Gana'],
    advantage: 5,
    deuce: 4,
    gamePointIndex: 3,
    win: 6,
}

const getNameLeader = points => {
    const [nombre] = Object.entries(points).sort( (a, b) => b[1] - a[1])[0];
    return nombre;
};

const pointNamed = i => gameStructure.states[i] ?? '???';

const adaptPoints = (playerWinPoint, points) => {

    if (Math.max(...Object.values(points)) < gameStructure.win)
        points[playerWinPoint]++;

    const maxPoint = Math.max(...Object.values(points));
    const difPoints = maxPoint - Math.min(...Object.values(points));
    // ¿Ya hay ganador?
    if (maxPoint === gameStructure.win || (maxPoint > gameStructure.gamePointIndex && difPoints >= 2)) {
        // Puede ganar desde 40, en lugar de Advantage, en ese caso lo igual a Ganador
        const winner = getNameLeader(points);
        points[winner] = gameStructure.win;
        return `${gameStructure.states[gameStructure.win]} ${winner}`
    }
    
    const playerLosePoint = Object.keys(points)
        .filter( player => player !== playerWinPoint )[0];

    if (maxPoint > gameStructure.gamePointIndex && difPoints > 0)
        return `${pointNamed(gameStructure.advantage)} ${getNameLeader(points)}`;

    if (difPoints === 0 && maxPoint >= gameStructure.gamePointIndex) {
        // Si están igualados a "Advantage", igualar a "Deuce"
        if (points[playerWinPoint] === gameStructure.advantage) {
            points[playerWinPoint] = gameStructure.deuce;
            points[playerLosePoint] = gameStructure.deuce;
        }
        return `${pointNamed(gameStructure.deuce)}`
    }

    const [p1, p2] = Object.keys(points);
    return `${pointNamed(points[p1])} - ${pointNamed(points[p2])}`;
}

function game(points = []) {
    try {
        if (points.length === 0)
            throw new Error('El array de los puntos está vacío')

        const players = [...new Set(points)]
        if (players.length > 2)
            throw new Error('El juego es para dos jugadores')

        const pointsByPlayer = {
            [players[0]]: 0,
            [players[1] ?? `** Empty **`]: 0,
        }
        
        return points
            .map(pointFor => adaptPoints(pointFor, pointsByPlayer))
            .join('\n');

    } catch (error) {
        return error.message
    }
}

// console.log(game(['P1', 'P1', 'P2', 'P2', 'P1', 'P2', 'P1', 'P2', 'P2', 'P1', 'P1', 'P1']))
console.log( game( ['Federer', 'Federer', 'Nadal', 'Federer', 'Nadal', 'Nadal', 'Federer', 'Nadal', 'Nadal', 'Nadal'] ))
