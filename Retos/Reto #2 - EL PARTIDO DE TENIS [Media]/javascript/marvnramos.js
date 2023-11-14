// P1 (player 1)
// P2 (player 2)

const show_score = (plays) =>{
    // initializing player's score
    let P1 = 0;
    let P2 = 0;

    // Iterate over each play in array plays
    for(let play in plays){
        if(play === "P1"){
            P1++;
        }
        else{
            P2++;
        }

        // logic to determinate the game status
        game_status = determinate_game_status(P1, P2)
        console.log(game_status);

        if(game_status === "Ganador"){
            break;
        }
    }
}

const determinate_game_status = (P1, P2) =>{
    // logica para determinar el estado del juego
    // devolver el estado del juego
    // (love, 15, 30, 40, Deuce, Ventaja, Ganador)
}

// Ej. de uso
let sequence_of_actions = ["P1", "P1", "P2", "P2", "P1", "P2", "P1", "P1"];
show_score(sequence_of_actions);
