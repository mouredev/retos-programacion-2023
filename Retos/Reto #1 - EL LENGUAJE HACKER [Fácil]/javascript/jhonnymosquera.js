/*
 * Escribe un programa que reciba un texto y transforme lenguaje natural a
 * "lenguaje hacker" (conocido realmente como "leet" o "1337"). Este lenguaje
 *  se caracteriza por sustituir caracteres alfanuméricos.
 * - Utiliza esta tabla (https://www.gamehouse.com/blog/leet-speak-cheat-sheet/)
 *   con el alfabeto y los números en "leet".
 *   (Usa la primera opción de cada transformación. Por ejemplo "4" para la "a")
 */

let natural = [
	" ",
	"a",
	"b",
	"c",
	"d",
	"e",
	"f",
	"g",
	"h",
	"i",
	"j",
	"k",
	"l",
	"m",
	"n",
	"o",
	"p",
	"q",
	"r",
	"s",
	"t",
	"u",
	"v",
	"w",
	"x",
	"y",
	"z",
];
let leet = [
	" ",
	"4",
	"13",
	"]",
	")",
	"3",
	"|=",
	"&",
	"#",
	"1",
	",_|",
	">|",
	"1",
	"[]V[]",
	"^/",
	"0",
	"|*",
	"(_,)",
	"I2",
	"5",
	"7",
	"(_)",
	"/",
	"//",
	"><",
	"j",
	"2",
];

function transform(text) {
	text = text.toLowerCase();
	let naturalText = Array.from(text);
	let naturalTextInfex = [];

	naturalText.forEach(letter => {
		natural.filter((natural_letter, i) => {
			if (natural_letter == letter) {
				naturalTextInfex.push(leet[i]);
			}
		});
	});

	let leagueLeet = naturalTextInfex.join("");

	console.log(leagueLeet);
}

transform("parangacutirimicuaro");
transform("jeje se acabo");
transform("Muy interezante");
transform("viva JS");
transform("Agrege tambien los espacios y corregi el tema de las MAYUSCULAS");
