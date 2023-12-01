const ReadLine = require('readline');

const readLine = ReadLine.createInterface({
    input: process.stdin,
    output: process.stdout,
});

const getRandomWord = () => {
    const words = ["javascript", "developer", "website", "marvnramos", "mauredev"];
    const randomWord = words[Math.floor(Math.random() * words.length)];
    
    let incompleteWord = "";

    for(let i = 0; i < 5; i++) {
        let index = Math.floor(Math.random() * randomWord.length);
        incompleteWord = randomWord.split(randomWord[index]).join("_");
    }

    return incompleteWord;
};

console.log(getRandomWord());

const guessWord = (word, attempts) => {
    
    readLine.question("Enter a word: ", (answer) => {
        console.log(`Your word is: ${answer}\n`);
    });
};

