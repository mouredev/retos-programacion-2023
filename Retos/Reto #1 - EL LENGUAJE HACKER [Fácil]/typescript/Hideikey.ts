/*
 * Escribe un programa que reciba un texto y transforme lenguaje natural a
 * "lenguaje hacker" (conocido realmente como "leet" o "1337"). Este lenguaje
 *  se caracteriza por sustituir caracteres alfanuméricos.
 * - Utiliza esta tabla (https://www.gamehouse.com/blog/leet-speak-cheat-sheet/)
 *   con el alfabeto y los números en "leet".
 *   (Usa la primera opción de cada transformación. Por ejemplo "4" para la "a")
 */
const LEETALPHABET = [
	"4",
	"I3",
	"[",
	")",
	"3",
	"|=",
	"&",
	"#",
	"1",
	",_|",
	">|",
	"1",
	"//'",
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
	"L",
	"R",
	"E",
	"A",
	"S",
	"b",
	"T",
	"B",
	"g",
	"o",
	" ",
];
const ALPHABET = [
	"A",
	"B",
	"C",
	"D",
	"E",
	"F",
	"G",
	"H",
	"I",
	"J",
	"K",
	"L",
	"M",
	"N",
	"O",
	"P",
	"Q",
	"R",
	"S",
	"T",
	"U",
	"V",
	"W",
	"X",
	"Y",
	"Z",
	"1",
	"2",
	"3",
	"4",
	"5",
	"6",
	"7",
	"8",
	"9",
	"0",
	" ",
];

function replaceFunction(letter: string): string {
	let index = ALPHABET.indexOf(letter);
	return LEETALPHABET[index];
}

function leetConverter(text: string): string {
	let newText: string = "";
	let arrayText: Array<string> = text.toUpperCase().split("");
	for (let i = 0; i < arrayText.length; i++) {
		const letter: string = arrayText[i];
		newText = newText + replaceFunction(letter);
	}
	return newText;
}

let textToConvert = "This is a test";
console.log(leetConverter(textToConvert));
