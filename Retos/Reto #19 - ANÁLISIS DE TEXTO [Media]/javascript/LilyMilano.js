const text = `It is a truth universally acknowledged that a single man in possession of a good fortune, must be in want of a wife.`;

let wordCount = 0;
let totalChars = 0;
let sentenceCount = 0;
let longestWord = '';

for (let i = 0; i < text.length; i++) {
	if (text[i] === ' ') {
		wordCount++;
	} else if (text[i] === '.') {
		sentenceCount++;
	} else {
		if (text[i - 1] === ' ' || i === 0) {
			let word = '';

			while (i < text.length && text[i] !== ' ' && text[i] !== '.') {
				word += text[i];
				i++;
			}
			i--;

			totalChars += word.length;

			if (word.length > longestWord.length) {
				longestWord = word;
			}
		}
	}
}

wordCount++;

const avgWordLength = totalChars / wordCount;

console.log(`Total words: ${wordCount}`);   // Total words: 23
console.log(`Average word length: ${avgWordLength}`);   // Average word length: 4.043478260869565
console.log(`Total sentences: ${sentenceCount}`);   // Total sentences: 1
console.log(`Longest word: ${longestWord}`);    // Longest word: acknowledged
