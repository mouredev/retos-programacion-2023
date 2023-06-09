/*
 * Crea un programa que simule el comportamiento del sombrero selccionador del
 * universo mágico de Harry Potter.
 * - De ser posible realizará 5 preguntas (como mínimo) a través de la terminal.
 * - Cada pregunta tendrá 4 respuestas posibles (también a selecciona una a través de terminal).
 * - En función de las respuestas a las 5 preguntas deberás diseñar un algoritmo que
 *   coloque al alumno en una de las 4 casas de Hogwarts:
 *   (Gryffindor, Slytherin , Hufflepuff y Ravenclaw)
 * - Ten en cuenta los rasgos de cada casa para hacer las preguntas
 *   y crear el algoritmo seleccionador:
 *   Por ejemplo, en Slytherin se premia la ambición y la astucia.
 */
const readline = require('readline').createInterface({
	input: process.stdin,
	output: process.stdout,
});

let respuesta = 0;

const pregunta1 = `Digamos que tiene un examen la próxima semana, ¿cómo se va a preparar?\n
1. Reviso mis apuntes y estudio solo en mi casa\n
2. Dejo todo para última hora y el día antes me trasnocho estudiando con uno o dos amigos\n
3. Estudio un poquito cada día de la semana pero no me estreso porque sé que he parado bolas en clase entonces me va a ir bien\n
4. Le digo a mis compañeros que nos reunamos a estudiar juntos en la biblioteca\n
Elija una respuesta:
`;
const pregunta2 = `Si su habitación en Hogwarts se está quemando y pudiera rescatar solo una cosa, ¿cuál sería?\n
1. Una reliquia familiar que ha pasado de generación en generación\n
2. Las fotos que tiene con sus amigos\n
3. A su mascota\n
4. Su libro favorito o su computador\n
Elija una respuesta:
`;
const pregunta3 = `¿Cuál de estas cosas lo pone más nervioso?\n
1. Fracasar\n
2. Los espacios cerrados\n
3. La soledad\n
4. Hablar en público\n
Elija una respuesta:
`;
const pregunta4 = `Si le dan un pedazo de papel, ¿qué hace con él?\n
1. Lo rompe en muchos pedacitos\n
2. Un avioncito de papel\n
3. Dibuja\n
4. Escribe\n
Elija una respuesta:
`;
const pregunta5 = `Si en una clase los ponen a hacer un trabajo en grupo, ¿usted qué hace?\n
1. Se pone a cargo de todo porque si no lo hace usted, no va a quedar bien hecho\n
2. Lo mínimo posible. En los grupos siempre hay alguien que se va a encargar de hacerlo todo\n
3. Hace de todo un poquito: ayuda con la investigación, organiza, escribe\n
4. Investiga y escribe gran parte del trabajo pero deja que alguien más en el grupo lo decore y haga la presentación\n
Elija una respuesta:
`;

readline.question(pregunta1, respuestaTerminal => {
	respuesta += parseInt(respuestaTerminal);
	readline.question(pregunta2, respuestaTerminal => {
		respuesta += parseInt(respuestaTerminal);
		readline.question(pregunta3, respuestaTerminal => {
			respuesta += parseInt(respuestaTerminal);
			readline.question(pregunta4, respuestaTerminal => {
				respuesta += parseInt(respuestaTerminal);
				readline.question(pregunta5, respuestaTerminal => {
					respuesta += parseInt(respuestaTerminal);
					obtenerCasaHogwarts();
					readline.close();
				});
			});
		});
	});
});

function obtenerCasaHogwarts() {
	let casa = '';
	if (respuesta <= 8) {
		casa = 'Slytherin';
	} else if (respuesta <= 12) {
		casa = 'Gryffindor';
	}
	else if (respuesta <= 16) {
		casa = 'Hufflepuff';
	}
	else {
		casa = 'Ravenclaw';
	}
	console.log(`Enhorabuena! Su casa es ${casa}`);
}