/*
 * Crea un programa que simule la competición de dos coches en una pista.
 * - Los dos coches estarán representados por 🚙 y 🚗. Y la meta por 🏁.
 * - Cada pista tendrá entre 1 y 3 árboles 🌲 colocados de forma aleatoria.
 * - Las dos pistas tendrán una longitud configurable de guiones bajos "_".
 * - Los coches comenzarán en la parte derecha de las pistas. Ejemplo:
 *   🏁____🌲_____🚙
 *   🏁_🌲____🌲___🚗
 * 
 * El juego se desarrolla por turnos de forma automática, y cada segundo
 * se realiza una acción sobre los coches (moviéndose a la vez), hasta que
 * uno de ellos (o los dos a la vez) llega a la meta.
 * - Acciones:
 *   - Avanzar entre 1 a 3 posiciones hacia la meta.
 *   - Si al avanzar, el coche finaliza en la posición de un árbol,
 *     se muestra 💥 y no avanza durante un turno.
 *   - Cada turno se imprimen las pistas y sus elementos.
 *   - Cuando la carrera finalice, se muestra el coche ganador o el empate.
 *   
 */

const car1 = "🚙"
const car2 = "🚗"
const meta = "🏁"
const tree = "🌲"
const crash = "💥"
function raceCart(trace){
    let [trace1, trace2] =createRacetrace(trace)
    console.log(trace1)
    console.log(trace2)
    let carToMove = car1
   const interval = setInterval(() => {
        if (carToMove === car1) {
            trace1 = move(trace1, carToMove);
            carToMove = car2
        } else {
            trace2= move(trace2, carToMove);
            carToMove = car1
        }
        console.log('##################')
        console.log(trace1)
        console.log(trace2)
        anyWinner(trace1, trace2) && clearInterval(interval)
     
    }, 1000);
}


// Helper functions

function createRacetrace(trace){
    let trace1 = meta+ "_".repeat(trace)+ car1
    let trace2 = meta+"_".repeat(trace)+ car2
    trace1 = addTrees(trace1)
    trace2 = addTrees(trace2)
    return [trace1, trace2]
}

function addTrees(trace){
    const traceArray = [...trace]
    const trees = Math.floor(Math.random()*3) +1
    for (let i=1; i<=trees; i++){
        let treePosition
        do {
            treePosition = Math.floor(Math.random()*(traceArray.length -4))+2

        } while (traceArray[treePosition] === tree)
        traceArray[treePosition] = tree
    }
    return traceArray.join("")
}

function move(trace, car){
    const steps= Math.floor(Math.random()*3) +1
    const traceArray = [...trace]
    const crashPosition = traceArray.indexOf(crash)
    if (crashPosition !== -1) {
        traceArray[crashPosition] = car
        return traceArray.join("")
    } 
    const carPosition = traceArray.indexOf(car)
    const newCarPosition = carPosition - steps
    if (newCarPosition < 0){
        traceArray[0] = car
    } else if (traceArray[newCarPosition] === tree){
        traceArray[newCarPosition] = crash
    } else { 
        traceArray[newCarPosition] = car
    }
    traceArray[carPosition] = '_'
    return traceArray.join("")
}

function hasWin(currentTrace){
    return (!currentTrace.includes(meta) && !currentTrace.includes(crash))
}

function anyWinner(trace1, trace2){
    if (hasWin(trace1)){        
        console.log(`🎉 Winner: Car ${car1} 🎉`)
        return true
    }
    if (hasWin(trace2)){
        console.log(`🎉 Winner: Car ${car2} 🎉`) 
        return true   
    }
    return false
}

raceCart(12)