// P1 (player 1)
// P2 (player 2)

const show_score = (plays) =>{
    // initializing player's score
    let P1 = 0;
    let P2 = 0;

    // Iterate over each play in array plays
    for(let play in plays){
        if(plays[play] === "P1"){
            P1++;
        }
        else{
            P2++;
        }

        // logic to determinate the game status
        let game_status = determinate_game_status(P1, P2);
        console.log(game_status);

        if(game_status === "Ganador"){
            break;
        }
    }
}

const determinate_game_status = (P1, P2) =>{
    if(P1 == 1 && P2 == 0){
        return "15 - Love";
    }
    else if(P1 == 2 && P2 == 0){
        return "30 - Love";
    }
    else if(P1 == 2 && P2 == 1){
        return "30 - 15";
    }
    else if(P1 ==  2 && P2 == 2){
        return "30 - 30";
    }
    else if(P1 == 3 && P2 == 2){
        return "40 - 30";
    }
    else if(P1 == P2){
        return "Deuce";
    }else if (P1 == 4) {
        return "Ventaja P1";
    }else if (P1 > 4) {
        return "Ha ganado el P1";
    }
}


let sequence_of_actions = ["P1", "P1", "P2", "P2", "P1", "P2", "P1", "P1"];
show_score(sequence_of_actions);
