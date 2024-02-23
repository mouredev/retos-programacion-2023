const createTrifuerza = (n) => {
    let trifuerza = "";

	for (let i = 0; i < 2 * n; i++) {
		if (i < n) {
			trifuerza += " ".repeat(2 * n - 1 - i);
			trifuerza += "*".repeat(2 * (i + 1) - 1);
		} else {
			trifuerza += " ".repeat((2 * n) - 1 - i);
			trifuerza += "*".repeat(2 * (i - n + 1) - 1);
			trifuerza += " ".repeat(2 * (2 * n - i) - 1);
			trifuerza += "*".repeat(2 * (i - n + 1) - 1);
		}
		trifuerza += "\n";
	}

	return trifuerza;
}

console.log(createTrifuerza(3))