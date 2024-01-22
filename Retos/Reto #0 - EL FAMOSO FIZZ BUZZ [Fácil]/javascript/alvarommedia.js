function fizzBuzz() {
	for (let i = 1; i <= 100; i++) {
		const esMultiploTres = i % 3 === 0;
		const esMultiploCinco = i % 5 === 0;
		const esMultiploAmbos = i % 3 === 0 && i % 5 === 0;
		if (esMultiploAmbos) {
			console.log("fizzBuzz");
		} else if (esMultiploTres) {
			console.log("fizz");
		} else if (esMultiploCinco) {
			console.log("buzz");
		} else {
			console.log(i);
		}
	}
}
