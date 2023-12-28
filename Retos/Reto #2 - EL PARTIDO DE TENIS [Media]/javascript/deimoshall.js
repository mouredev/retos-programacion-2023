const game = ['P1', 'P1', 'P2', 'P2', 'P1', 'P2', 'P1', 'P1'];
const game2 = ['P1', 'P1', 'P2', 'P2', 'P1', 'P2', 'P2', 'P2', 'P1', 'P1', 'P1'];
const game3 = ['P2', 'P2', 'P1', 'P1', 'P1', 'P1'];

let p1_score = 0;
let p2_score = 0;
let deuce = false;

const scores = new Map();
scores.set(0, "love");

for(let i = 15; i < 1000; i+=15) {
    if(i === 45) {
        scores.set(i, i - 5);
    } else {
        scores.set(i, i);
    }
}

game3.every(winner => {
    if(winner === 'P1') {
        p1_score += 15;
    } else {
        p2_score += 15;
    }
    
    if(p1_score === p2_score && p1_score === 45) {
        console.log('Deuce');
        deuce = true;
    } else if(deuce) {
        if(p1_score === p2_score + 15) {
            console.log('Ventaja P1');
        } else if(p1_score === p2_score + 30) {
            console.log('Ha ganado P1');
            return false; // break
        } else if(p2_score === p1_score + 15) {
            console.log('Ventaja P2');
        } else if(p2_score === p1_score + 30) {
            console.log('Ha ganado P2');
            return false; // break
        } else if(p1_score === p2_score) {
            console.log('All');
        }
    } else if(p1_score === 60 && p2_score <= 30) {
        console.log('Ha ganado P1');
        return false;
    } else if(p2_score === 60 && p1_score <= 30) {
        console.log('Ha ganado P2');
        return false;
    } else {
        console.log(`${scores.get(p1_score)} - ${scores.get(p2_score)}`);
    }
    return true;
});