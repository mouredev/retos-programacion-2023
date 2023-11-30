const ReadLine = require('readline');

const readLine = ReadLine.createInterface({
    input: process.stdin,
    output: process.stdout,
});



const guessWord = (word, attempts) => {
    const words = ["javascript", "developer", "website", "marvnramos", "mauredev"];
    
    readLine.question("Enter a word: ", (answer) => {
        console.log(`Your word is: ${answer}\n`);
    });
};

