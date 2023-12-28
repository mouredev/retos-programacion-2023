/*
 * Crea un programa que simule el comportamiento del sombrero selccionador del
 * universo mágico de Harry Potter.
 * - De ser posible realizará 5 preguntas (como mínimo) a través de la terminal.
 * - Cada pregunta tendrá 4 respuestas posibles (también a selecciona una a través de terminal).
 * - En función de las respuestas a las 5 preguntas deberás diseñar un algoritmo que
 *   coloque al alumno en una de las 4 casas de Hogwarts (Gryffindor, Slytherin , Hufflepuff y Ravenclaw)
 * - Ten en cuenta los rasgos de cada casa para hacer las preguntas y crear el algoritmo seleccionador.
 *   Por ejemplo, en Slytherin se premia la ambición y la astucia.
 */

const preguntasYRespuestas = {
  preguntas: [
    {
      pregunta: "¿Qué cualidad valoras más en un alumno?",
      opciones: {
        a: { respuesta: "Coraje", casa: "Gryffindor" },
        b: { respuesta: "Inteligencia", casa: "Ravenclaw" },
        c: { respuesta: "Lealtad", casa: "Hufflepuff" },
        d: { respuesta: "Astucia", casa: "Slytherin" },
      },
    },
    {
      pregunta: "¿Qué criatura mágica te gustaría tener como mascota?",
      opciones: {
        a: { respuesta: "Búho", casa: "Ravenclaw" },
        b: { respuesta: "Gato", casa: "Gryffindor" },
        c: { respuesta: "Rata", casa: "Hufflepuff" },
        d: { respuesta: "Lechuza", casa: "Slytherin" },
      },
    },
    {
      pregunta: "¿Cuál es tu asignatura favorita en Hogwarts?",
      opciones: {
        a: { respuesta: "Pociones", casa: "Slytherin" },
        b: { respuesta: "Transformaciones", casa: "Ravenclaw" },
        c: { respuesta: "Herbología", casa: "Hufflepuff" },
        d: {
          respuesta: "Defensa contra las Artes Oscuras",
          casa: "Gryffindor",
        },
      },
    },
    {
      pregunta: "¿Cuál es tu lugar favorito en el castillo de Hogwarts?",
      opciones: {
        a: { respuesta: "La Sala Común de mi casa", casa: "Slytherin" },
        b: { respuesta: "El Gran Comedor", casa: "Gryffindor" },
        c: { respuesta: "La Biblioteca", casa: "Ravenclaw" },
        d: { respuesta: "Los terrenos del castillo", casa: "Hufflepuff" },
      },
    },
    {
      pregunta: "¿Cuál es tu hechizo favorito?",
      opciones: {
        a: { respuesta: "Expecto Patronum", casa: "Gryffindor" },
        b: { respuesta: "Wingardium Leviosa", casa: "Ravenclaw" },
        c: { respuesta: "Alohomora", casa: "Hufflepuff" },
        d: { respuesta: "Expelliarmus", casa: "Slytherin" },
      },
    },
  ],
};

function startQuestions() {
  // prompt para hacer cada pregunta y guardar la respuesta
  // guardar la respuesta en un array
  // llamar a la función que evalúa las respuestas
  const respuestaUserArray = [];
  preguntasYRespuestas.preguntas.forEach((element) => {
    console.log(element);
    const respuestas = returnAnswers(element.opciones);
    const respuestaUser = prompt(
      "Selecciona una opción: " + element.pregunta + respuestas
    );
    respuestaUserArray.push(element.opciones[respuestaUser].casa);
  });
  casas(respuestaUserArray);
}

/**
 * funcion helper para mostrar las respuestas en el propmt
 * @param {*} answers
 * @returns
 */
function returnAnswers(answers) {
  let opcionesTexto = "";
  for (const opcion in answers) {
    opcionesTexto += opcion + ": " + answers[opcion].respuesta + ", ";
  }
  return opcionesTexto.slice(0, -2);
}

/**
 * busqueda de que casa aparece mas veces
 * @param {*} casas
 */
function casas(casas) {
  const registro = {};
  let casaMasFrecuente = "";
  let frecuenciaMasAlta = 0;

  // Recorremos el array y contamos las apariciones de cada elemento
  casas.forEach((casa) => {
    if (!registro[casa]) {
      registro[casa] = 1;
    } else {
      registro[casa]++;
    }
  });

  // Buscamos la casa con la frecuencia más alta
  for (const casa in registro) {
    if (registro[casa] > frecuenciaMasAlta) {
      casaMasFrecuente = casa;
      frecuenciaMasAlta = registro[casa];
    }
  }

  console.log(
    `La casa más frecuente es ${casaMasFrecuente}, aparece ${frecuenciaMasAlta} veces.`
  );
}

startQuestions();
