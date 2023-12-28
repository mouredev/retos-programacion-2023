import select from '@inquirer/select';

const main = async () => {
	const housesPoints = {
		Gryffindor: 0,
		Hufflepuff: 0,
		Ravenclaw: 0,
		Slytherin: 0,
	};

	const answers = await doQuestions();

	for (const answer of answers) {
		housesPoints[answer] += 1;
	}

	const selectedHouse = selectHouse(housesPoints);

	console.log(` You will go to ${selectedHouse}!`);
};

const selectHouse = (housesPoints) => {
	let currentValue = 0;
	let winningHouses = [];
	const housesArray = Object.entries(housesPoints).sort((a, b) => b[1] - a[1]);

	for (const houseElement of housesArray) {
		const [house, points] = houseElement;

		if (points === 0) continue;
		if (points > currentValue) {
			currentValue = points;
			winningHouses.push(house);
		} else if (points === currentValue) {
			winningHouses.push(house);
		}
	}

	// If there is a tie
	const randomIndex = Math.floor(Math.random() * winningHouses.length);

	return winningHouses.length > 1 ? winningHouses[randomIndex] : winningHouses[0];
};

const doQuestions = async () => {
	const answers = [];
	const questions = [
		{
			message: 'What is your favorite color',
			choices: [
				{
					name: 'Scarlet red',
					value: 'Gryffindor',
				},
				{
					name: 'Canary yellow',
					value: 'Hufflepuff',
				},
				{
					name: 'Blue',
					value: 'Ravenclaw',
				},
				{
					name: 'Emerald green',
					value: 'Slytherin',
				},
			],
		},
		{
			message: 'When faced with an important decision, what guides you the most?',
			choices: [
				{
					name: 'Momentum',
					value: 'Gryffindor',
				},
				{
					name: "What's best for my friends and loved ones",
					value: 'Hufflepuff',
				},
				{
					name: 'Logic and reasoning',
					value: 'Ravenclaw',
				},
				{
					name: 'My personal goals and desires',
					value: 'Slytherin',
				},
			],
		},
		{
			message: 'What type of environment appeals to you most?',
			choices: [
				{
					name: 'Adventure and emotion',
					value: 'Gryffindor',
				},
				{
					name: 'Friendship and companionship',
					value: 'Hufflepuff',
				},
				{
					name: 'Knowledge and learning',
					value: 'Ravenclaw',
				},
				{
					name: 'Ambition and achievements',
					value: 'Slytherin',
				},
			],
		},
		{
			message:
				'If you were faced with a dangerous situation and could only carry one item with you, which one would you choose?',
			choices: [
				{
					name: 'A brave and shining sword',
					value: 'Gryffindor',
				},
				{
					name: 'A lucky charm that belonged to your grandmother',
					value: 'Hufflepuff',
				},
				{
					name: 'An ancient book full of magical knowledge',
					value: 'Ravenclaw',
				},
				{
					name: 'A secret potion that could give you special abilities',
					value: 'Slytherin',
				},
			],
		},
		{
			message: 'What quality do you value most in yourself?',
			choices: [
				{
					name: ' Courage',
					value: 'Gryffindor',
				},
				{
					name: 'Loyalty',
					value: 'Hufflepuff',
				},
				{
					name: 'Wisdom',
					value: 'Ravenclaw',
				},
				{
					name: 'Cunning',
					value: 'Slytherin',
				},
			],
		},
	];

	for (const question of questions) {
		const { message, choices } = question;
		const answer = await select({ message, choices });
		answers.push(answer);
	}
	return answers;
};

main();
