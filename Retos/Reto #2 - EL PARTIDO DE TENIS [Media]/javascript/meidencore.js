const gameScore = (scoreArray) => {

let P1 = 0;
let P2 = 0;
let deuce = false;
let winingCondition = false;

const scoreList = ["love", 15, 30, 40, "deuce", "ventaja"]

for (let i = 0; i < scoreArray.length; i++) {
    const score = scoreArray[i];

    if (score === "P1") P1++
    if (score === "P2") P2++
    if (P1 === 3 && P2 === 3) deuce = true;

    if (!winingCondition) {
        if (deuce) {
            switch (P1 - P2) {
                case 0:
                    console.log("deuce")
                break;
                case 1:
                    console.log("Ventaja P1")
                break;
                case -1:
                    console.log("Ventaja P2")
                break;
                case 2:
                    console.log("Ha Ganado el P1");
                    winingCondition = true;
                break;
                case -2:
                    console.log("Ha Ganado el P2");
                    winingCondition = true;
                break;
                default:
                    console.log("no se que ha pasado")
            }
        } else {
            if (P1 === 4) {
                console.log("Ha Ganado el P1");
                winingCondition = true;
                break
            } else if (P2 === 4) {
                console.log("Ha Ganado el P2");
                winingCondition = true;
                break
            } else if (score === "P1") {
                console.log(scoreList[P1] + " - " + scoreList[P2])
            } else if (score === "P2") {
                console.log(scoreList[P1] + " - " + scoreList[P2])
            }
        }
    } else {
        break;
    }
}

}

gameScore(["P1", "P1", "P2", "P2", "P1", "P2", "P1", "P1"])