/*
 * Crea un programa que simule el comportamiento del sombrero seleccionador del
 * universo mágico de Harry Potter.
 * - De ser posible realizará 5 preguntas (como mínimo) a través de la terminal.
 * - Cada pregunta tendrá 4 respuestas posibles (también a selecciona una a través de terminal).
 * - En función de las respuestas a las 5 preguntas deberás diseñar un algoritmo que
 *   coloque al alumno en una de las 4 casas de Hogwarts (Gryffindor, Slytherin , Hufflepuff y Ravenclaw)
 * - Ten en cuenta los rasgos de cada casa para hacer las preguntas y crear el algoritmo seleccionador.
 *   Por ejemplo, en Slytherin se premia la ambición y la astucia.
 */

const readline = require('readline-sync');

let gryffindor = 0;
let hufflepuff = 0;
let slytherin = 0;
let ravenclaw = 0;


const preguntas = [
  {
    pregunta: "¿Amanecer o atardecer? ",
    respuestas: ["Amanecer", "Atardecer"],
    puntos: { gryffindor: 1, hufflepuff: 1, ravenclaw: 0, slytherin: 1 }
  },
  {
    pregunta: "¿Cuando muera, quiero que la gente me recuerde como? : ",
    respuestas: ["El Bueno", "El Grande", "El Sabio", "El Audaz"],
    puntos: { gryffindor: 1, hufflepuff: 2, ravenclaw: 1, slytherin: 2 }
  },
  {
    pregunta: "¿Qué tipo de instrumento te agrada más escuchar?: ",
    respuestas: ["El violín", "La trompeta", "El piano", "La batería"],
    puntos: { gryffindor: 1, hufflepuff: 1, ravenclaw: 1, slytherin: 2 }
  },
  {
    pregunta: "¿Cuál es tu asignatura favorita en la escuela?: ",
    respuestas: ["Defensa Contra las Artes Oscuras", "Herbología", "Pociones", "Adivinación"],
    puntos: { gryffindor: 1, hufflepuff: 1, ravenclaw: 2, slytherin: 1 }
  },
  {
    pregunta: "¿Qué cualidad valoras más en un amigo?: ",
    respuestas: ["Valentía", "Lealtad", "Inteligencia", "Ambición"],
    puntos: { gryffindor: 2, hufflepuff: 1, ravenclaw: 1, slytherin: 2 }
  }
];


const hacerPregunta = (pregunta, respuestas) => {
  console.log(pregunta);
  respuestas.forEach((respuesta, index) => {
    console.log(` ${index + 1}.) ${respuesta}`);
  });
  const respuestaIndex = parseInt(readline.question('Elige una respuesta (1 - 4): '));
  if (respuestaIndex >= 1 && respuestaIndex <= 4) {
    return respuestaIndex;
  } else {
    console.log('Respuesta incorrecta');
    return hacerPregunta(pregunta, respuestas);
  }
}

preguntas.forEach(pregunta => {
  const respuesta = hacerPregunta(pregunta.pregunta, pregunta.respuestas);
  comprobarRespuesta(respuesta, pregunta.puntos);
});


const comprobarRespuesta = (respuesta, puntos) => {
  if (respuesta === 1) {
    gryffindor += puntos.gryffindor;
  } else if (respuesta === 2) {
    hufflepuff += puntos.hufflepuff;
  } else if (respuesta === 3) {
    ravenclaw += puntos.ravenclaw;
  } else if (respuesta === 4) {
    slytherin += puntos.slytherin;
  }
}

console.log('===============');
console.log('El Sombrero Seleccionador');
console.log('===============');



console.log("Gryffindor: ", gryffindor);
console.log("Ravenclaw: ", ravenclaw);
console.log("Hufflepuff: ", hufflepuff);
console.log("Slytherin: ", slytherin);

const puntuacionMaxima = Math.max(gryffindor, ravenclaw, hufflepuff, slytherin);

if (gryffindor === puntuacionMaxima) {
  console.log('🦁 ¡Gryffindor!');
} else if (ravenclaw === puntuacionMaxima) {
  console.log('🦅 ¡Ravenclaw!');
} else if (hufflepuff === puntuacionMaxima) {
  console.log('🦡 ¡Hufflepuff!');
} else if (slytherin === puntuacionMaxima) {
  console.log('🐍 ¡Slytherin!');
}
