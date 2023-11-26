//hecho por: Cesarpinagon
function tennisGame(points) {
    let scoreP1 = 0;
    let scoreP2 = 0;
    const scoreNames = ["Love", "15", "30", "40"];

    for (let point of points) {
        if (point === "P1") scoreP1++;
        else scoreP2++;

        if (scoreP1 >= 3 && scoreP2 >= 3) {
            if (scoreP1 === scoreP2) console.log("Deuce");
            else if (scoreP1 === scoreP2 + 1) console.log("Ventaja P1");
            else if (scoreP2 === scoreP1 + 1) console.log("Ventaja P2");
            else if (scoreP1 > scoreP2 + 1) {
                console.log("Ha ganado el P1");
                return;
            } else {
                console.log("Ha ganado el P2");
                return;
            }
        } else {
            console.log(scoreNames[scoreP1] + " - " + scoreNames[scoreP2]);
        }
    }
}

tennisGame(["P1", "P1", "P2", "P2", "P1", "P2", "P1", "P1"]);