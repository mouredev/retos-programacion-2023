import { createInterface } from 'readline/promises'

// ===================================
// Evaluator
// ===================================
type EvaluatorMap = { [char: string]: number }

const wordEvaluator = (lang: 'es' | 'en') => {
	const alphabet = {
		es: Array(26)
			.fill(0)
			.map((_, i) => String.fromCharCode(65 + i))
			.toSpliced(14, 0, 'Ñ'),
		en: Array(26)
			.fill(0)
			.map((_, i) => String.fromCharCode(65 + i))
	}

	const evaluatorMap = alphabet[lang].reduce((map, char, i) => {
		map[char] = i + 1
		return map
	}, {} as EvaluatorMap)

	return (word: string) => {
		const normalizedWord = word
			.normalize('NFD')
			.replace(/[\u0300-\u036f]/g, '')
			.toUpperCase()

		return [...normalizedWord].reduce((punctuation, char) => punctuation + (evaluatorMap?.[char] || 0), 0)
	}
}

// ===================================
// Game
// ===================================
;(async () => {
	const communicator = createInterface({
		input: process.stdin,
		output: process.stdout
	})

	console.clear()
	console.log('Bienvenido al juego de las palabras!')
	console.log('El objetivo es conseguir el valor deseado con la suma de las letras de la palabra introducida.')

	let lang = ''
	let punctuationToWin = 0
	let lastTry = { punctuation: 0, word: '' }

	while (lang !== 'es' && lang !== 'en') {
		lang = await communicator.question('\nEn que idioma vas a introducir las palabras? (es/en): ')
	}

	while (punctuationToWin < 1 || Number.isNaN(punctuationToWin)) {
		punctuationToWin = Number(await communicator.question('\nQue valor quieres conseguir? (1-100): '))
	}

	const evaluator = wordEvaluator(lang)

	while (punctuationToWin !== lastTry.punctuation) {
		console.clear()
		console.log(`🏁 Valor esperado: ${punctuationToWin} 🏁 \n`)

		if (lastTry.word)
			console.log(
				`Ups... el valor de la palabra '${lastTry.word}' es ${lastTry.punctuation}, sigue intentándolo!\n`
			)
		const word = await communicator.question('Introduce una palabra: ')
		const punctuation = evaluator(word)

		lastTry = { punctuation, word }
	}

	console.clear()
	console.log(`🥳 Enhorabuena! has conseguido un valor de ${punctuationToWin} con '${lastTry.word}'!`)

	communicator.close()
})()

// ===================================
// Manual testing
// ===================================
// const runTests = () => {
// 	const expectEqual = (a: any, b: any) => {
// 		console.log(a === b ? `${a} OK` : `${a} KO, recived ${a} but expected ${b}`)
// 	}

// 	// Esp
// 	const espEvaluator = wordEvaluator('es')
// 	expectEqual(espEvaluator('HOLA'), 37) // H + O + L + A = 8 + 16 + 12 + 1 = 37
// 	expectEqual(espEvaluator('MUNDO'), 69) // M + U + N + D + O = 13 + 22 + 14 + 4 + 16 = 69
// 	expectEqual(espEvaluator('PROGRAMACIÓN'), 135) // P + R + O + G + R + A + M + A + C + I + Ó + N = 17 + 19 + 16 + 7 + 19 + 1 + 13 + 1 + 3 + 9 + 16 + 14 = 135
// 	expectEqual(espEvaluator('MoUreDev'), 107) // M + O + U + R + E + D + E + V = 13 + 16 + 22 + 19 + 5 + 4 + 5 + 23 = 107

// 	// Eng
// 	const engEvaluator = wordEvaluator('en')
// 	expectEqual(engEvaluator('HELLO'), 52) // H + E + L + L + O = 8 + 5 + 12 + 12 + 15 = 52
// 	expectEqual(engEvaluator('WORLD'), 72) // W + O + R + L + D = 23 + 15 + 18 + 12 + 4 = 72
// 	expectEqual(engEvaluator('PROGRAMMING'), 131) // P + R + O + G + R + A + M + M + I + N + G = 16 + 18 + 15 + 7 + 18 + 1 + 13 + 13 + 9 + 14 + 7 = 131
// 	expectEqual(engEvaluator('MoUreDev'), 103) // M + O + U + R + E + D + E + V = 13 + 15 + 21 + 18 + 5 + 4 + 5 + 22 = 103
// }

// runTests()
