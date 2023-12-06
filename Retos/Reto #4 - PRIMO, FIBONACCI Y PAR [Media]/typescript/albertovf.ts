const reto = (n: number) => {
	function isPrime(): boolean {
		if (n >= 0 && n <= 3) return true;

		for (let i = 3; i <= n / 2; i++) {
			if (n % i == 0) return false;
		}
		return true;
	}

	function isEven(): boolean {
		return n % 2 === 0;
	}

	function isFibonacci(): boolean {
		let fibonacciNumbers: number[] = [0, 1];
		while (fibonacciNumbers[1] <= n) {
			if (n === fibonacciNumbers[1]) {
				return true;
			}
			fibonacciNumbers.push(fibonacciNumbers[0] + fibonacciNumbers[1]);
			fibonacciNumbers.shift();
		}
		return false;
	};
	console.log(`${n} ${isPrime() ? 'es' : 'no es'} primo, ${isFibonacci() ? 'es' : 'no es'} Fibonacci y ${isEven() ? 'es par' : 'es impar'}`)
}

reto(2)
reto(7)
