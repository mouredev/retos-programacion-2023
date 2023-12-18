//*Utilizamos la estructura de datos hashSet, el cual guarda valores, unicos, si el valor existe en el set entonces no es Heterograma, por lo que se retorna false, si al finalizar de recorrer el string no se han encontrado valores duplicados, se retorna true.
const isHeterogram = (s) => {
	const set = new Set();
	for (char of s) {
		if (set.has(char)) return false;
		set.add(char);
	}
	return true;
};

//*Utilizando una estructura de datos HashMap, guardamos las letras como keys y recorremos el string, si encuentra letras  repetidas aumentara el valore de dichas keys dentro del HashMap, por ultimo se compara si todos los valores del HashMap son iguales, si no, no es un Isograma.
const isIsogram = (s) => {
	const hashMap = new Map();
	let sString = s.split(" ").join("");

	for (char of sString) {
		let charInMap = hashMap.has(char);
		if (charInMap) {
			let val = hashMap.get(char);
			hashMap.set(char, val + 1);
		} else {
			hashMap.set(char, 0);
		}
	}

	let vals = [];
	for (let val of hashMap.values()) {
		vals.push(val);
	}
	const allEqual = vals.every((val) => val === vals[0]);

	return allEqual;
};

//*Creamos el array del que contienen las letras del idioma.
//*creamos otro array que contiene el numero de veces que aparecen las letras en la cadena de texto, este array nos ayudara a determinar si el panagrama es valido.
//*Recorremos el texto verificando si el indice de la letra se encuentra dentro de nuestro array de letras, si es asi, incrementamos en esa posicion nuestro array count.
//*Al finalizar comprobamos si dentro de count todos los valores son mayores a 0, ya que esto nos indicaria que al menos todas las letras fueron usadas 1 vez.
const isPangram = (s) => {
	let letters = Array.from({ length: 26 }, (_i, index) =>
		String.fromCharCode(65 + index).toLowerCase()
	);
	let count = Array.from({ length: letters.length }).fill(0);

	for (let char of s.split(" ").join("").toLowerCase()) {
		let index = letters.indexOf(char);
		let isInLetters = index !== -1;

		if (!isInLetters) return false;
		count[index]++;
	}

	const hasAllLetters = count.every((val) => val > 0);

	return hasAllLetters;
};

console.log(isHeterogram("hola i a"));
console.log(isHeterogram("hola"));
console.log(isIsogram("hi javascript"));
console.log(isIsogram("hi hi hi"));
console.log(isPangram("abcd"));
console.log(isPangram("The quick brown fox jumps over a lazy dog"));
