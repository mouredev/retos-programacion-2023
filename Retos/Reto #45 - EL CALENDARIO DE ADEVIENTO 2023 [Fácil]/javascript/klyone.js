const readline = require('node:readline/promises');

const options = {
    add : { name : "add", func : addFunc },
    remove : { name : "remove", func : removeFunc },
    show : { name : "show", func : showFunc },
    raffle : { name : "raffle", func : raffleFunc },
    quit : { name: "quit", func: quitFunc },
};

let people = [];

function getRandomPerson() {
    obj = {};

    obj.index = Math.floor(Math.random() * people.length);
    obj.person = people[obj.index];

    return obj;
}

async function addFunc(prompt) {
    let name = await prompt.question("Name: ");

    if (people.includes(name)) {
        console.log("The person already exists");
    } else {
        people.push(name);
    }

    return false;
}

async function removeFunc(prompt) {
    let name = await prompt.question("Name: ");

    if (people.includes(name)) {
        const index = people.indexOf(name);
        people.splice(index, 1);
    } else {
        console.log("The person does not exist");
    }

    return false;
}

function showFunc() {
    console.log(people);
    return false;
}

function raffleFunc() {
    const {index, person} = getRandomPerson();
    console.log(`Selected: ${person}`);
    people.splice(index, 1);

    return false;
}

function quitFunc() {
    return true;
}

function handleFunction(func, prompt) {
    let exit = false;
    let name = "";

    for (const o in options) {
        if ( options[o].name === func ) {
            exit = options[o].func(prompt);
            break;
        }
    }

    return exit;
}

async function runAdeviento() {
    let exitProgram = false;
    const prompt = readline.createInterface({ input: process.stdin, output: process.stdout })

    while (!exitProgram) {
        console.log("");
        console.log("=============================");
        console.log("ADEViento options: ");
        console.log("");
        console.log("add: Add new person");
        console.log("remove: Remove a person");
        console.log("show: Show people");
        console.log("raffle: Perform a raffle with the existing people");
        console.log("quit: Exit the program");
        console.log("");
        console.log("=============================");
        console.log("");
        const answer = await prompt.question("Operation: ");
        exitProgram = await handleFunction(answer, prompt);
    }

    prompt.close();
}

runAdeviento();
