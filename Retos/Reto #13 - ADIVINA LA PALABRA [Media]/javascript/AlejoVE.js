import * as readline from 'node:readline';
import util from 'util';

const rl = readline.createInterface({
	input: process.stdin,
	output: process.stdout,
});

const questionAsync = util.promisify(rl.question).bind(rl);
// prettier-ignore
const words = ['juguete','familia','persona','ludo','esfera','restaurante','colegio','sisterna','camion','mascota'];

const main = async () => {
	let lives = 5;
	const randomIndex = Math.floor(Math.random() * words.length);
	const randomWord = words[randomIndex];
	const randomWordArray = [...randomWord];
	let { encryptedWord, lettersToGuess } = encryptWord(randomWord);

	console.log('Here is the world you have to guess: ');
	displayWord(encryptedWord);

	while (lives > 0 && lettersToGuess.length > 0) {
		// User response
		const answer = await questionAsync('Please type a letter or sentence: ');

		// Evaluates complete sentence
		if (answer.length === randomWord.length) {
			if (answer === randomWord) {
				console.log('You won!');
				rl.close();
				return;
			} else {
				lives--;
				console.log(`Wrong answer, you have ${lives} left`);
				continue;
			}
		}

		if (!lettersToGuess.includes(answer)) {
			lives--;
			console.log(`Wrong answer, you have ${lives} left`);
			continue;
		}

		lettersToGuess = lettersToGuess.filter((value) => value !== answer);

		const indices = [];
		let idx = randomWordArray.indexOf(answer);

		// In case the word has repeated letters
		while (idx != -1) {
			indices.push(idx);
			idx = randomWordArray.indexOf(answer, idx + 1);
		}

		indices.forEach((index) => (encryptedWord[index] = answer));

		displayWord(encryptedWord);

		if (lettersToGuess.length === 0) {
			console.log('You won!');
			rl.close();
			return;
		}
	}

	if (lives > 0) {
		displayWord(encryptedWord);
		console.log('You won!');
		rl.close();
	} else {
		console.log('Game Over!');
		console.log(`The word was: ${randomWord}`);

		rl.close();
	}
};

const encryptWord = (word) => {
	const chartsToRest = Math.floor(word.length * 0.6);
	let wordCopy = [...word];
	const lettersToGuess = [];

	for (let i = 0; i <= chartsToRest; i++) {
		const randomIndex = Math.floor(Math.random() * word.length);
		const letterToHide = wordCopy[randomIndex];
		if (letterToHide !== '_') {
			lettersToGuess.push(letterToHide);
			wordCopy[randomIndex] = '_';
		}
	}

	return {
		encryptedWord: wordCopy,
		lettersToGuess,
	};
};

const displayWord = (array) => {
	console.log(array.join(' '));
};

main();
