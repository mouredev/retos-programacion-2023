/*
  Crea un programa que simule el comportamiento del sombrero selccionador del
  universo mágico de Harry Potter.
  - De ser posible realizará 5 preguntas (como mínimo) a través de la terminal.
  - Cada pregunta tendrá 4 respuestas posibles (también a selecciona una a través de terminal).
  - En función de las respuestas a las 5 preguntas deberás diseñar un algoritmo que
    coloque al alumno en una de las 4 casas de Hogwarts (Gryffindor, Slytherin , Hufflepuff y Ravenclaw)
  - Ten en cuenta los rasgos de cada casa para hacer las preguntas y crear el algoritmo seleccionador.
    Por ejemplo, en Slytherin se premia la ambición y la astucia.
*/


const readLine = require('readline').createInterface({
  input: process.stdin,
  output: process.stdout,
});

const houses = ['Gryffindor', 'Slytherin', 'Ravenclaw', 'Hufflepuff'];

const questions = [
  {
    question: 'Digamos que tiene un exámen la próxima semana, ¿como se va a preparar?',
    answers: [
      'Reviso mis apuntes y estudio solo en mi casa',
      'Dejo todo para última hora y el día antes me trasnocho estudiando con uno '
      + 'o dos amigos',
      'Estudio un poquito cada día de la semana pero no me estreso porque sé que '
      + 'he parado bolas en clase entonces me va a ir bien',
      'Le digo a mis compañeros que nos reunamos a estudiar juntos en la biblioteca',
    ],
  },
  {
    question: 'Si su habitación en Hogwarts se está quemando y pudiera rescatar '
    + 'solo una cosa, ¿cuál sería?',
    answers: [
      'Su libro favorito o su computador',
      'Las fotos que tiene con sus amigos',
      'Una reliquia familiar que ha pasado de generación en generación',
      'A su mascota',
    ],
  },
  {
    question: '¿Cuál de estas cosas lo pone más nervioso?',
    answers: [
      'Hablar en público',
      'Fracasar',
      'Los espacios cerrados',
      'La soledad',
    ],
  },
  {
    question: 'Si le dan un pedazo de papel, ¿qué hace con él?',
    answers: [
      'Dibuja',
      'Escribe',
      'Un avioncito de papel',
      'Lo rompe en muchos pedacitos',
    ],
  },
  {
    question: 'Si en una clase los ponen a hacer un trabajo en grupo, ¿usted qué hace?',
    answers: [
      'Investiga y escribe gran parte del trabajo pero deja que alguien más en el'
      + ' grupo lo decore y haga la presentación',
      'Lo mínimo posible. En los grupos siempre hay alguien que se va a encargar '
      + 'de hacerlo todo y eso es lo chévere',
      'Hace de todo un poquito: ayuda con la investigación, organiza, escribe',
      'Se pone a cargo de todo, organiza, asigna roles y termina casi haciéndolo '
      + 'todo usted. Prefiere eso porque si no lo hace usted, no va a quedar bien hecho',
    ],
  },
  {
    question: '¿Haría trampa en un examen?',
    answers: [
      'Si ayudar a sus amigos que no estudiaron es hacer trampa, entonces sí',
      'Pues, trata de no hacerlo siempre pero hay veces en las que toca',
      'Nunca',
      'Sí, todo el mundo hace trampa. De hecho, hacer trampa sin ser '
      + 'pillado es muy inteligente',
    ],
  },
  {
    question: '¿Qué cosa le fastidia más?',
    answers: [
      'Que la gente se indigne por cualquier cosa',
      'Que la gente no sea leal',
      'Que la gente confunda ay, hay y ahí',
      'Que la gente se aproveche de otra gente',
    ],
  },
  {
    question: 'Es fin de semana y está tratando de decidir dónde comer '
    + 'con un amigo. ¿Qué hace?',
    answers: [
      'Busca restaurantes en google y le cuenta las mejores opciones que '
      + 'encontró para que su amigo escoja',
      'Le dice “vamos a ir a tal lado”. Es mejor que usted escoja de una '
      + 'para evitar perder tiempo',
      'Analizan cuál es el restaurante que más le gusta a los dos y van a ese',
      'Le dice que vayan a probar algún sitio en el que ninguno de '
      + 'los dos haya estado antes',
    ],
  },
  {
    question: 'Y por último, si un grupo de magos malvados atrapó a su mejor '
    + 'amigo y lo tiene escondido en un sótano, ¿qué haría para rescatarlo?',
    answers: [
      'Conseguiría planos del sitio y excavaría un túnel. Puede que le tome '
      + 'más de un mes hacerlo pero es la forma más segura y menos sospechosa '
      + 'de recuperar a su amigo',
      'Usaría una poción o un encantamiento para disfrazarse como alguno de '
      + 'los captores y sacar a su amigo sin que nadie sospeche',
      'Llamaría a alguno de los contactos de sus papás que tienen cargos '
      + 'altos para que ellos planeen una misión de rescate',
      'Reuniría a sus demás amigos y planearía una misión de rescate',
    ],
  },
];


const printResult = (total) => {
  let result = 'Tu casa es: ';
  if (total <= 10) {
    result += houses[0];
  } else if (total <= 16) {
    result += houses[1];
  } else if (total <= 22) {
    result += houses[2];
  } else {
    result += houses[3];
  }
  return result;
};

let counter = 0;

const start = () => {
  const askQuestion = (i) => {
    console.log(`\n${questions[i].question}\n`);
    for (let j = 0; j < questions[i].answers.length; j++) {
      console.log(`${j + 1}. ${questions[i].answers[j]}`);
    }
    readLine.question('\nSeleccione una opcion:', (answer) => {
      const answerTemp = parseInt(answer, 10) || 0;
      counter += answerTemp > 0 && answerTemp <= 4 ? answerTemp : 0;

      if (i < questions.length - 1) {
        askQuestion(i + 1);
      } else {
        readLine.close();
        console.log(printResult(counter));
      }
    });
  };
  askQuestion(0);
};

start();

// Visita mi repo en GitHub para ver y correr los tests de este código --> https://github.com/marcode24/weekly-challenges
