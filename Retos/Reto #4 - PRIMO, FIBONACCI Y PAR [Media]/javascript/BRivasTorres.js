const testNum = (num) => {
	if (typeof num !== "number") return "Ingrese solo numeros";
	let isPrime = false;
	let isPar = false;
	let isFibonacci = false;
	let res = "";

	//*Si el residuo de un numero divido entre 2 es === 0, este es par.
	if (num % 2 === 0) {
		isPar = true;
	}

	//*Si un numero es divisible por otro numero que no sea el mismo o 1, este no es primo
	if (isPrimeFun(num) === true) {
		isPrime = true;
	}

	//*Si 5 * x^2 + 4 === cuadrado perfecto || 5 * x^2 - 4 === cuadrado perfecto, en donde x representa el número que deseamos probar,
	//*entoneces ese numero es fibonacci.
	if (isFibonacciFun(num) === true) {
		isFibonacci = true;
	}

	isPrime = isPrime ? num + " es primo" : num + " no es primo";
	isPar = isPar ? " es par" : " is impar";
	isFibonacci = isFibonacci ? " es fibonnacci" : " no es fibonncci";

	res += `${isPrime}, ${isFibonacci} y ${isPar} `;

	return res;
};

// A number x is a Fibonacci number if and only if one of the following conditions is true:
// 5 * x^2 + 4 is a perfect square (e.g., 9, 16, 25).
// 5 * x^2 - 4 is a perfect square.
//*Siguiendo esta ecuacion determinamos si un numero es fibonacci o no.

const isPerfect = (num) => {
	const sqrt = Math.sqrt(num);
	return sqrt === Math.floor(sqrt);
};
const isFibonacciFun = (num) => {
	return isPerfect(5 * num * num + 4) || isPerfect(5 * num * num - 4);
};

const isPrimeFun = (num) => {
	if (num <= 2) return false;
	let i = 2;
	while (i * i <= num) {
		if (num % i === 0) return false;
		i++;
	}
	return true;
};

console.log(testNum(6));
