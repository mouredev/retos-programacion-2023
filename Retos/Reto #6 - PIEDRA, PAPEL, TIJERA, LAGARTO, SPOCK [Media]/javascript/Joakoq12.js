const model = {
    'Rock': ['Liz', 'Sis'],
    'Papper': ['Rock', 'Spock'],
    'Sis': ['Papper', 'Lizz'],
    'Lizz': ['Spock', 'Papper'],
    'Spock': ['Papper', 'Sis'],
  }

  let player1_points = 0;
  let player2_points = 0;


function freshStart(games) {

    player1_points = 0;
    player2_points = 0;

    games.forEach(playgame);
    if(player1_points === player2_points){
        return 'TIE';
    }
    else if (player1_points > player2_points) {
        return 'Player_1 Wins';
    }
    else  
        return 'Player_2 Wins'
    }


function playgame ([player1, player2]) {
    if (model[player1].indexOf(player2) > -1) {
        player1_points += 1
    } 
     else if (model[player2].indexOf(player1) > -1) {
        player2_points += 1 
    }
}

console.log(freshStart([['Rock', 'Spock'], ['Sis', 'Lizz'], ['Spock', 'Spock']]));
console.log(freshStart([['Rock', 'Sis'], ['Sis', 'Rock'], ['Sis', 'Rock']]));
console.log(freshStart([['Rock', 'Rock'], ['Sis', 'Sis'], ['Sis', 'Sis']]));






// buscar estructura de objeto para comprobar las reglas 

// hacer un for y derivar ifs 