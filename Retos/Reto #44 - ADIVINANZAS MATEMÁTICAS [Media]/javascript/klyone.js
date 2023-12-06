
const readline = require('node:readline/promises');

const SUM = 0;
const SUB = 1;
const MUL = 2;
const DIV = 3;
const TIMEOUTMS = 3000;

function getOperation() {
    return Math.floor(Math.random() * 4);
}

function getRandom(digits) {
    return Math.floor(Math.random() * (10**digits));
}

async function playGame() {
    let aDigits = 1;
    let bDigits = 1;
    let endGame = false;
    let answeredQuestions = 0;
    let aToBeUpdated = true;

    const prompt = readline.createInterface({ input: process.stdin, output: process.stdout })

    while (!endGame) {
        let a = getRandom(aDigits);
        let b = getRandom(bDigits);
        let op = getOperation();
        let opStr = "";
        let res = 0;

        switch (op) {
        case SUM:
            res = parseInt(Math.floor(a + b));
            opStr = "+";
            break;
        case SUB:
            res = parseInt(Math.floor(a - b));
            opStr = "-";
            break;
        case MUL:
            res = parseInt(Math.floor(a * b));
            opStr = "*";
            break;
        case DIV:
            if (b == 0) {
                b++;
            }
            res = parseInt(Math.floor(a / b));
            opStr = "/";
            break;
        default:
            throw new Error("Unexpected operation");
            break;
        }

        console.log(`${a} ${opStr} ${b} = ?`);

        try {
            const answer = parseInt(await prompt.question("Result: ", { signal: AbortSignal.timeout(TIMEOUTMS)}));

            if (res !== answer) {
                console.log(`Wrong answer, correct is ${res}`);
                endGame = true;
            }
            else {
                answeredQuestions++;

                if (answeredQuestions % 5 == 0) {
                    if (aToBeUpdated) {
                        aDigits++;
                        aToBeUpdated = false;
                    } else {
                        bDigits++;
                        aToBeUpdated = true;
                    }
                }
            }
        } catch(error) {
            endGame = true;
        }

    }

    prompt.close();

    console.log(`You have answered ${answeredQuestions}`);
}

playGame();
