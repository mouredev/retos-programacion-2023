function tennisGame(points: string[]) {
    const scores = ["Love", "15", "30", "40"];
    let p1Score = 0;
    let p2Score = 0;
    let winner:string = "";
    for (const point of points) {
        if (point === "P1") {
            p1Score++;
        } else if (point === "P2") {
            p2Score++;
        }
        if (p1Score < 4 && p2Score < 4) {
            console.log(`${scores[p1Score]} - ${scores[p2Score]}`);
        } else if (p1Score === p2Score) {
            console.log("Deuce");
        } else if (p1Score > p2Score) {
            if (p1Score - p2Score === 1) {
                console.log("Ventaja P1");
                winner = "P1";
            } else {
                winner = "P1";
            }
        } else {
            if (p2Score - p1Score === 1) {
                console.log("Ventaja P2");
                winner = "P2";
            } else {
                winner = "P2";
            }
        }
    }
    if (winner != ""){
        console.log(`Ha ganado el ${winner}`);
    }
}

// Example usage
const points = ["P1", "P1", "P2", "P2", "P1", "P2", "P1", "P1"];
tennisGame(points);
