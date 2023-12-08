enum Dificultad {
	MUY_FACIL = 1,
	FACIL = 2,
	PRIMARIA = 3,
	SECUNDARIA = 4,
	DIFICIL = 5,
	UNIVERSIDAD = 6,
	MUY_DIFICIL = 7,
	IMPOSIBLE = 8,
	GENIO = 9,
	TRAMPAS = 10,
	OREDENADOR = 11
}
const TIEMPO_PREGUNTA = 5
const DIFICULTAD_MAXIMA: Dificultad = Dificultad.OREDENADOR
const PREGUNTAS_DIFICULTAD = 10

const operacion = (dificultad: Dificultad) => {
	const operando = (): String => {
		let simbolos = ["+", "-", "/", "*"]
		const indiceAleatorio = Math.floor(Math.random() * simbolos.length)
		return simbolos[indiceAleatorio]
	}

	const obtenerNumero = (dificultad: Dificultad): number => {
		let maximo = Number.parseInt('9'.repeat(dificultad).toString())
		let numero = Math.floor(Math.random() * (maximo + 1)) + 1
		return numero
	}

	let n1 = obtenerNumero(dificultad)
	let sim = operando()
	let n2 = obtenerNumero(dificultad)
	let cuenta = `${n1} ${sim} ${n2}`
	return { cuenta, resultado: eval(cuenta) }
}

const time = (): number => Math.round(new Date().getTime() / 1000)

const reto = (): void => {
	let dificultad = 1
	let valido = true
	let pregunta = 1
	while (valido) {
		let a = time()
		let { cuenta, resultado } = operacion(dificultad)
		let respuesta = prompt(`[OPERACION]: ${cuenta} = `)
		// let respuesta = resultado
		let b = time()
		console.log({ pregunta, cuenta: `[OPERACION]: ${cuenta} = `, respuesta, resultado, tiempo: b - a })

		if (resultado != respuesta || (b - a) > TIEMPO_PREGUNTA) {
			valido = false
			console.log(`HAS FALLADO. Has acertado un total de ${pregunta - 1} preguntas`)
		}

		if (pregunta % PREGUNTAS_DIFICULTAD == 0 && dificultad < DIFICULTAD_MAXIMA) {
			dificultad++
		}
		pregunta++
	}
}

reto()