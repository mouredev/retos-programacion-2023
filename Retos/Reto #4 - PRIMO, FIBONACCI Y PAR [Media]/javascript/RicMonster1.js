function analyzeNumber(num) {
	let answer = `\n${num} `;

	function checkPrime(num) {
		let prime = true;

		for (let i = 2; i < num; i++) {
			if (num % i === 0) {
				prime = false;
				break;
			}
		}

		prime
			? (answer = answer + 'es primo')
			: (answer = answer + 'no es primo');
	}

	function checkFibonacci(num) {
		let fibonacci = false;
		let num1 = 1;
		let num2 = 1;

		for (let i = 0; i < num; i++) {
			[num1, num2] = [num1 + num2, num1];

			if (num1 === num) {
				fibonacci = true;
				break;
			}
		}

		fibonacci || num === 1
			? (answer = answer + ', es fibonacci')
			: (answer = answer + ', no es fibonacci');
	}

	function checkEven(num) {
		num % 2 === 0
			? (answer = answer + ' y es par')
			: (answer = answer + ' y es impar');
	}

	if (typeof num === 'number') {
		checkPrime(num);
		checkFibonacci(num);
		checkEven(num);
		console.log(answer);
	} else {
		console.log('\nEsta función solo admite números enteros como parámetro');
	}
}

analyzeNumber(2);

analyzeNumber(7);

analyzeNumber(10);

analyzeNumber(13);

analyzeNumber('R');
