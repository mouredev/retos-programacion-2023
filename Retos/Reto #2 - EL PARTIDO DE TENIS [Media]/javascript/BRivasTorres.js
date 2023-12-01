const points = {
	0: "Love",
	1: 15,
	2: 30,
	3: 40,
};

const showGame = (arr) => {
	let results = "";
	let [currPointsP1, currPointsP2] = [0, 0];

	for (let i = 0; i < arr.length; i++) {
		let currPoint = arr[i];

		switch (currPoint) {
			case "P1":
				currPointsP1++;
				break;
			case "P2":
				currPointsP2++;
				break;
			default:
				break;
		}

		if (currPointsP1 >= 4 && currPointsP1 - currPointsP2 >= 2) {
			results += "Ha ganado P1\n";
			break;
		} else if (currPointsP2 >= 4 && currPointsP2 - currPointsP1 >= 2) {
			results += "Ha ganado P2\n";
			break;
		}

		if (currPointsP1 >= 3 && currPointsP2 >= 3) {
			if (currPointsP1 === currPointsP2) {
				results += "Deuce\n";
			} else if (currPointsP1 - currPointsP2 === 1) {
				results += "Ventaja P1\n";
			} else if (currPointsP2 - currPointsP1 === 1) {
				results += "Ventaja P2\n";
			}
		} else {
			results += `${points[currPointsP1] || currPointsP1} - ${
				points[currPointsP2] || currPointsP2
			}\n`;
		}
	}
	return results;
};

console.log(showGame(["P1", "P1", "P2", "P2", "P1", "P2", "P1", "P1"]));
