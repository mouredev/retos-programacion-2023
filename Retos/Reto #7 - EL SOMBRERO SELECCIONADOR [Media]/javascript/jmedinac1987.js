const questions = [
  "A. Si invitan al Quidditch un día festivo, que harías?: \n1. Me rio de la persona que me invita y no voy  \n2. Simplemente ignoro la ivitación  \n3. Vas pero solo a ver \n4. Vas y juegas sin dudarlo \nRespuesta: ",
  "B. Con cual profesor te gustaría ver la clase de defensa contra las artes oscuras? \n1. Quirinus Quirrell \n2. Gilderoy Lockhart \n3. Severus Snape \n4. Remus Lupin \nRespuesta: ",
  "C. Cual es tu clase preferida? \n1. Transformaciones  \n2. Pociones \n3. Defensa contra las artes oscuras \n4. Encantamientos \nRespuesta: ",
  "D. Si el que no debe ser nombrado te invita a unirte a su ejercito, que harías? \n1. Me tatúo su marca, me uno sin dudarlo y le soy fiel por la eternidad \n2. Solo me uno para que no me haga daño  \n3. Hago un encantamiento de desaparición y huyo  \n4. Me niego y lo enfrento \nRespuesta: ",
  "E. Cual crees que sea el mejor hechizo de todos los tiempos? \n1. Avada Kedavra \n2. Cruciatus \n3. Expelliarmus \n4. Expecto Patronum \nRespuesta: ",
];

let answers = [];

function ask(index) {
  process.stdout.write(questions[index]);
}

function getHouse(responsesForAverage) {
  let houses = ["Gryffindor", "Slytherin", "Hufflepuff", "Ravenclaw"];
  let sum = 0;

  responsesForAverage.forEach((answer) => {
    sum += answer;
  });

  if (sum >= 16 && sum <= 20) return houses[0];
  if (sum >= 11 && sum <= 15) return houses[3];
  if (sum >= 6 && sum <= 10) return houses[2];
  if (sum >= 1 && sum <= 5) return houses[1];
}

process.stdin.on("data", (data) => {
  let answer = parseInt(data.toString().trim());

  if (answer < 1 || answer > 4 || isNaN(answer)) {
    console.log("Lo siento, pero debes ingresar un número de respuesta válido");
    process.exit();
    return;
  }

  answers.push(answer);

  if (answers.length < questions.length) {
    ask(answers.length);
  } else {
    console.log("Tu casa es:", getHouse(answers));
    process.exit();
  }
});

ask(0);