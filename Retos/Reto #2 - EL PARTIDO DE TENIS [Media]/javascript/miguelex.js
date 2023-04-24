function TennisMatch(players) {
    
    let p1Points = 0;
    let p2Points = 0;

    players.forEach(element => {
        if (element.toUpperCase() === "P1") {
            p1Points++;
        }
        else if (element.toUpperCase() === "P2") {
            p2Points++;
        }
        else {
            console.log("Error en el tanteo ")
            return;
        }
    
        if (p1Points === 4 && p2Points === 4) {
            p1Points = 3;
            p2Points = 3;
        }

        PrintScore(p1Points, p2Points);
    });
}

function PrintScore(P1, P2) {

    const score = ["Love", "15", "30", "40"];

    if ((P1 === P2) && (P1 === 3)) {
        console.log("\tDeuce")
    } else if ((P1 == 4) && (P2 == 3)) {
        console.log("\tVentaja P1")
    } else if ((P2 == 4) && (P1 == 3)) {
        console.log("\tVentaja P2")
    } else if ((P1 == 5) && (P1 - P2 == 2)) {
        console.log("\tGana P1")
    } else if ((P2 == 5) && (P2 - P1 == 2)) {
        console.log("\tGana P2")
    } else {
        console.log("P1:\t " + score[P1] + " - " + score[P2] + "\t:P2")
    }
}

TennisMatch(["P1", "P1", "P2", "P2", "P1", "P2", "P1", "P1"]);
TennisMatch(["P1", "P1", "P1", "P2", "P2", "P2", "P1", "P2", "P1", "P2", "P2", "P2"]);
