const readline = require("readline");

const rl = readline.createInterface({
	input: process.stdin,
	output: process.stdout,
});

function askQuestion(question, options) {
	return new Promise((resolve) => {
		const formattedOptions = options
			.map((option, index) => `${index + 1}. ${option}`)
			.join("\n");
		rl.question(
			`${question}\n${formattedOptions}\nRespuesta: `,
			(answer) => {
				const selectedOption = parseInt(answer);
				if (
					isNaN(selectedOption) ||
					selectedOption < 1 ||
					selectedOption > options.length
				) {
					console.log(
						"Respuesta no válida. Por favor, selecciona una opción válida."
					);
					resolve(askQuestion(question, options));
				} else {
					resolve(selectedOption);
				}
			}
		);
	});
}

async function sortingHat() {
	const questions = [
		"¿Qué cualidad valoras más?",
		"En una situación difícil, ¿qué harías?",
		"¿Qué tipo de amigos prefieres?",
		"Elige una criatura mágica:",
		"¿Cuál es tu materia favorita en Hogwarts?",
	];

	const options = [
		["Coraje", "Astucia", "Lealtad", "Intelecto"],
		[
			"Enfrentarlo directamente",
			"Analizar la situación",
			"Pedir ayuda",
			"Evitar el problema",
		],
		[
			"Ambiciosos y decididos",
			"Inteligentes y creativos",
			"Leales y amigables",
			"Honestos y sabios",
		],
		["Dragón", "Serpiente", "Hippogrifo", "Elfo doméstico"],
		[
			"Defensa contra las artes oscuras",
			"Adivinación",
			"Herbología",
			"Transformaciones",
		],
	];

	let housePoints = [0, 0, 0, 0];

	for (let i = 0; i < questions.length; i++) {
		const answer = await askQuestion(questions[i], options[i]);
		housePoints[answer - 1]++;
	}

	const maxPointsIndex = housePoints.indexOf(Math.max(...housePoints));
	const houses = ["Gryffindor", "Slytherin", "Hufflepuff", "Ravenclaw"];
	console.log(`¡Bienvenido a ${houses[maxPointsIndex]}!`);

	rl.close();
}

sortingHat();
