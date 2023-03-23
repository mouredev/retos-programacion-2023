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

//Quizz and answer
const QUIZZ = {
    'query_1': '¿Qué cualidad valoras más en ti mismo/a?',
    'query_2': '¿Qué tipo de actividad disfrutas más?',
    'query_3': '¿Cuál es tu materia favorita en la escuela?',
    'query_4':'¿Qué animal te parece más interesante?',
    'query_5':'¿Cómo describirías tu personalidad en una palabra?',
    'query_6':'¿Cuál es tu mayor objetivo en la vida?',
    'query_7':'¿Qué cualidad te describe mejor?',
    'query_8':'¿Cuál de estas criaturas mágicas te gustaría tener como mascota?',
    'query_9':'¿Qué asignatura de Hogwarts te resulta más interesante?',
    'query_10':'¿Qué valoras más en una persona?',
  }
  
  const ANSWER = {
    answer_1: {
      'Valentía': 'Gryffindor',
      'Astucia': 'Slytherin',
      'Lealtad': 'Hufflepuff',
      'Inteligencia': 'Ravenclaw',
    },
    answer_2: {
      'Deportes y juegos de riesgo': 'Gryffindor',
      'Resolver acertijos y enigmas': 'Ravenclaw',
      'Ayudar a otros y trabajar en equipo': 'Hufflepuff',
      'Leer y aprender cosas nuevas': 'Ravenclaw',
    },
    answer_3: {
      'Defensa contra las artes oscuras': 'Gryffindor',
      'Pociones': 'Slytherin',
      'Cuidado de criaturas mágicas': 'Hufflepuff',
      'Encantamientos': 'Ravenclaw',
    },
    answer_4: {
      'León': 'Gryffindor',
      'Serpiente': 'Slytherin',
      'Tejón': 'Hufflepuff',
      'Águila': 'Ravenclaw',
    },
    answer_5: {
      'Valiente': 'Gryffindor',
      'Astuto/a': 'Slytherin',
      'Leal': 'Hufflepuff',
      'Inteligente': 'Ravenclaw',
    },
    answer_6: {
      'Ser un héroe o heroína': 'Gryffindor',
      'Ser poderoso/a y exitoso/a': 'Slytherin',
      'Tener una vida plena y feliz': 'Hufflepuff',
      'Ser conocido/a por tu sabiduría y conocimiento': 'Ravenclaw',
    },
    answer_7: {
      'Coraje': 'Gryffindor',
      'Ambición': 'Slytherin',
      'Paciencia': 'Hufflepuff',
      'Creatividad': 'Ravenclaw',
    },
    answer_8: {
      'Un fénix': 'Gryffindor',
      'Una serpiente': 'Slytherin',
      'Un perro mágico': 'Hufflepuff',
      'Un búho': 'Ravenclaw',
    },
    answer_9: {
      'Adivinación': 'Ravenclaw',
      'Historia de la Magia': 'Ravenclaw',
      'Herbología': 'Hufflepuff',
      'Transformaciones': 'Gryffindor',
    },
    answer_10: {
      'La honestidad': 'Hufflepuff',
      'La astucia': 'Slytherin',
      'La amistad': 'Gryffindor',
      'La inteligencia': 'Ravenclaw',
    },
  }
  
  function checkInput(expresionInput) {
    let numberCheck
    while (true) {
      numberCheck = prompt(expresionInput)
      if (numberCheck === null) {
        return null
      }
  
      if (
        parseInt(numberCheck) &&
        parseInt(numberCheck) > 0 &&
        parseInt(numberCheck) < 5
      ) {
        return parseInt(numberCheck)
      } else {
        console.log('>>> Por favor, use los numeros del 1 al 4.\n')
      }
    }
  }
  
  function quizz(name = 'Harry') {
    let playerResponses = []
  
    for (let i = 0; i < Object.keys(QUIZZ).length; i++) {
      let num_key = i + 1
      let query_key = 'query_' + num_key.toString()
      let answer_key = 'answer_' + num_key.toString()
  
      console.log('---------------------------------------------------------')
      let query = QUIZZ[query_key]
      let answers = Object.keys(ANSWER[answer_key])
      console.log(`>>> ${query}`)
      for (let i = 0; i < answers.length; i++) {
        console.log(`>>> ${i + 1} - ${answers[i]}`)
      }
  
      console.log('---------------------------------------------------------')
      console.log(`>>> Inserta tú respuesta ${name}`)
      player_input = checkInput(`>>> Inserta tú respuesta ${name}`)
  
      if (player_input === null) {
        console.log('>>> Cancelado por el usuario.')
        return
      }
  
      console.log(answers[player_input - 1])
      playerResponses.push(ANSWER[answer_key][answers[player_input - 1]])
    }
  
    return playerResponses
  }
  
  function check_results_quizz(answers) {
    const frecuencia = answers.reduce(
      (acumulador, valorActual) => (
        acumulador[valorActual]
          ? (acumulador[valorActual] += 1)
          : (acumulador[valorActual] = 1),
        acumulador
      ),
      {}
    )
  
    const masFrecuente = Object.entries(frecuencia).reduce(
      (acumulador, [clave, valor]) =>
        valor > acumulador[1] ? [clave, valor] : acumulador,
      ['', 0]
    )
  
    return masFrecuente[0]
  }
  
  function mainGame() {
    console.log('---------------------------------------------------------')
    console.log('Bienvenidos tod@s a la Ceremonia de Selección de Hogwarts')
    console.log('---------------------------------------------------------\n')
  
    console.log('>>> Que suba el siguiente aspirante, por favor.')
  
    let name = prompt('>>> ¿Cuál es su nombre?\n')
  
    console.log(
      `>>> Bueno ${name} le dejo con el Sombrero Seleccionador, responda sus preguntas sin miedo.\n`
    )
  
    console.log('---------------------------------------------------------\n')
    console.log(
      `>>> Hola ${name}, soy el Sombrero Seleccionador, empecemos con las preguntas.`
    )
    console.log('>>> Para marcar su respuesta use los números 1, 2, 3 o 4\n')
  
    let answers = quizz(name)
    console.log(`>>> ${name} has terminado de responder las preguntas.\n`)
    console.log(`>>> Ahora es mi turno para decidir ...\n`)
  
    let result = check_results_quizz(answers)
    console.log(`>>> Ehorabuena ${name} has sido seleccionado para ${result} !!\n`)
  }
  
  mainGame()
  