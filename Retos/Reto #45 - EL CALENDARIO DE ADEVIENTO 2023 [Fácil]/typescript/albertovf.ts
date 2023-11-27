let participantes: String[] = ["Anonimo", "1", "2", "3", "4"]

const add = (participante: String) => {
	if (participantes.indexOf(participante) != -1) {
		participantes.push(participante)
	} else {
		console.log(`El participante ${participante} ya existe`);
	}
}

const del = (participante: String) => {
	let l = participantes.findIndex(i => i == participante)
	if (l == -1) {
		console.log(`El participante ${participante} no existe`);
	} else {
		participantes.splice(l, 1);
	}
}

const mostrar = () => {
	console.log(participantes);
}

const sortear = () => {
	let numero = Math.floor(Math.random() * participantes.length)
	console.log(`El ganador es Nº${numero} ${participantes[numero]}`);
	participantes.splice(numero, 1)
}

const reto = () => {

	while (true) {
		const accion = prompt('Selecciona una opcion [A]ñadir, [S]ortear, [B]orrar, [M]ostrar, [E]xit')

		switch (accion) {
			case 'A':
				add(prompt('Introduce el nombre que quieres agregar:') || "")
				break;
			case 'S':
				sortear()
				break;
			case 'B':
				del(prompt('Introduce el nombre que quieres borrar: ') || "")
				break;
			case 'M':
				mostrar();
				break;
			case 'E':
				return false;
			default:
				mostrar()
				break;
		}
	}
}
reto()