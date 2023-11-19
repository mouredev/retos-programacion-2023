const P1 = "P1";
const P2 = "P2";

function playTenis(...secuence) { 
    let printScore = function() {                
        let getValue = function(value) { 
            const values = { 0: 'Love', 1: '15', 2: '30', 3: '40' };
            if(value in values) return values[value];
        }
    
        if (score[0] == score[1] && score[0] >= 3)
            console.log('Deuce');
        else if (score[0] > score[1] && (score[0] - score[1]) == 1 && score[0] > 3)
            console.log('Ventaja P1');
        else if (score[1] > score[0] && (score[1] - score[0]) == 1 && score[1] > 3)
            console.log('Ventaja P2');
        else if (score[1] - score[0] > 1 && score[1] > 4)
            console.log('Ha ganado el P2');
        else if (score[0] - score[1] > 1 && score[0] > 4)
            console.log('Ha ganado el P1');            
        else {
            console.log(`${getValue(score[0])} - ${getValue(score[1])}`);   
        }
    }

    let score = [0, 0];     
   
    for (let index = 0; index < secuence.length; index++) {
        const element = secuence[index];
        if(element !== P1 && element !== P2) continue;

        if (element.length!=2) continue;        
        const player = parseInt(element[1]);            
        if (player!=1 && player!=2) continue;   
      
        score[player-1] += 1; 

        printScore();
    }   
}

playTenis('P1', 'P1', 'P2', 'P2', 'P1', 'P2', 'P1', 'P1');