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
 */

function race(large, red_pos_p, green_pos_p, tree_red_p, tree_green_p, red_crash_p, green_crash_p){
    const red_car = "🚗"
    const green_car = "🚙"
    const tree = "🌲"
    const crash = "💥"

    let red_track = "🏁"
    let green_track = "🏁"

    let tree_red_track = []
    let tree_green_track = []

    let red_pos = 0
    let green_pos = 0

    let red_crash = false
    let green_crash = false
    if (red_pos_p === undefined && green_pos_p === undefined){
        red_pos = large + 1
        green_pos = large + 1
        tree_red_track = set_tree_pos(large)
        tree_green_track = set_tree_pos(large)
    }
    else{
        red_pos = red_pos_p
        green_pos = green_pos_p
        tree_red_track = tree_red_p
        tree_green_track = tree_green_p  
        red_crash = red_crash_p
        green_crash = green_crash_p      
    }


    for (let i=0; i <= large+1; i++){
        if(tree_red_track.includes(i) && i == red_pos){
            red_track += crash
            red_crash = true
        }
        else if (tree_red_track.includes(i)){
            red_track += tree
        }
        else if (i == red_pos){    
            red_track += red_car
        }
        else{
            red_track += "_"
        }
    }

    for (let i=0; i <= large+1; i++){
        if(tree_green_track.includes(i) && i == green_pos){
            green_track += crash
            green_crash = true
        }
        else if (tree_green_track.includes(i)){
            green_track += tree
        }
        else if (i == green_pos){
            green_track += green_car
        }
        else{
            green_track += "_"
        }
    }
    
    console.log(red_track)
    console.log(green_track)
    
    if(green_pos == 0){
        console.log("Ha ganado el coche verde")
    }
    else if(red_pos == 0)    {
        console.log("Ha ganado el coche rojo")
    }
    else if (red_pos == 0 && green_pos == 0){
        console.log("Los dos coches han llegado a la vez")
    }
    else{
        //if(!green_crash){
            green_pos = set_new_car_pos(green_pos)
        //}
        //if(!red_crash){
            red_pos= set_new_car_pos(red_pos)
        //}
        race(large, red_pos, green_pos, tree_red_track, tree_green_track, red_crash, green_crash)
    }
}

function set_new_car_pos(actual_pos){
    let random = Math.floor(Math.random() * 3)

    let result = actual_pos - random
    if(result < 0){
        result = 0
    }

    return result
}

function set_tree_pos(large){
    let tree_pos = []
    let random = Math.floor(Math.random() * 3)
    
    if(random > 1){
        for(let i=0; i<random; i++){
            let pos = Math.floor(Math.random() * large)
            while (tree_pos.includes(pos)){
               let pos = Math.floor(Math.random() * large)
            }
            tree_pos.push(pos)
        }
    }
    else{
        tree_pos.push(Math.floor(Math.random() * large))
    }    
    return tree_pos
   
}

race(15)