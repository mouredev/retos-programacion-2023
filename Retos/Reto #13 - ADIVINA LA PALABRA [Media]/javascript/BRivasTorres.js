const words = ["psicoanalisis", "electroencefalografia", "biotecnologia", "constitucionalizacion", "hola"];

let randomWord = words[Math.floor(Math.random() * words.length)];
let hiddenWord = hideWord(randomWord);

let attempts = 5;

function hideWord(s) {
	let hideWord = "";
	for (let i = 0; i < s.length; i++) {
        let hide = Math.random() < 0.5
		if (hide) {
			hideWord += "_";
		} else {
			hideWord += s[i];
		}
	}
	return hideWord;
}

function showGame() {
	console.log(
		"Palabra a adivinar: " +
			hiddenWord +
			" - " +
			"Intentos restantes: " +
			attempts
	);
}

function checkVictory() {
	return randomWord === hiddenWord;
}

function updateWord(char) {
    const arr = randomWord.split("").map((letter, i) => letter === char ? char : hiddenWord[i])
    hiddenWord = arr.join("")
}

async function play() {
	const readline = require("readline").createInterface({
		input: process.stdin,
		output: process.stdout,
	});

	while (attempts > 0 && !checkVictory()) {
		showGame();
		const res = await pregunta("Enter a letter or a word: ");
		if (res.length === 1) {
            randomWord.includes(res) ? updateWord(res) : attempts -= 1
		} else {
            res === randomWord ? hiddenWord = randomWord : attempts -= 1
		}
	}

	if (checkVictory()) {
		console.log(`Contragulations you win, the word was ${randomWord}.`);
	} else {
		console.log(`Sorry! you lose, the word was ${randomWord}.`);
	}

	readline.close();
}

function pregunta(pregunta) {
	return new Promise((resolve) => {
		const readline = require("readline").createInterface({
			input: process.stdin,
			output: process.stdout,
			terminal: false,
		});
		readline.question(pregunta, (res) => {
			resolve(res.toLowerCase());
			readline.close();
		});
	});
}

play();
