/*
 * Crea un programa que simule el comportamiento del sombrero selccionador del
 * universo mágico de Harry Potter.
 * - De ser posible realizará 5 preguntas (como mínimo) a través de la terminal.
 * - Cada pregunta tendrá 4 respuestas posibles (también a selecciona una a través de terminal).
 * - En función de las respuestas a las 5 preguntas deberás diseñar un algoritmo que
 *   coloque al alumno en una de las 4 casas de Hogwarts (Gryffindor, Slytherin , Hufflepuff y Ravenclaw)
 * - Ten en cuenta los rasgos de cada casa para hacer las preguntas y crear el algoritmo seleccionador.
 *   Por ejemplo, en Slytherin se premia la ambición y la astucia.
 *
 * Creador por Pancratzia - 25/08/2023
 */

const readline = require("readline");

const rl = readline.createInterface({
  input: process.stdin,
  output: process.stdout,
});

const houses = ["Gryffindor", "Slytherin", "Ravenclaw", "Hufflepuff"];

let data = [
  {
    question: "¿Qué cualidad valoras más en ti mismo?",
    answers: {
      1: "Valentía",
      2: "Astucia",
      3: "Inteligencia",
      4: "Lealtad",
    },
  },
  {
    question: "¿Cuál es tu materia favorita en Hogwarts?",
    answers: {
      1: "Defensa contra las artes oscuras",
      2: "Pociones",
      3: "Encantamientos",
      4: "Cuidado de Criaturas Mágicas",
    },
  },
  {
    question:
      "¿Qué harías si tuvieras la oportunidad de conseguir un gran poder?",
    answers: {
      1: "Usarlo para ayudar a los demás",
      2: "Usarlo para lograr mis objetivos",
      3: "Usarlo para aprender más",
      4: "Usarlo para cuidar de mi familia y amigos",
    },
  },
  {
    question: "¿Qué tipo de animal te gustaría tener como mascota?",
    answers: {
      1: "León",
      2: "Serpiente",
      3: "Búho",
      4: "Tejón",
    },
  },
  {
    question: "¿Qué lugar te gustaría visitar en el mundo mágico?",
    answers: {
      1: "Torre de Gryffindor",
      2: "Bosque Prohibido",
      3: "Biblioteca de Hogwarts",
      4: "Cabaña de Hagrid",
    },
  },
  {
    question: "¿Cuál es tu hechizo favorito?",
    answers: {
      1: "Expecto Patronum",
      2: "Wingardium Leviosa",
      3: "Expelliarmus",
      4: "Lumos",
    },
  },
];

data = data.sort(() => Math.random() - 0.5);

let name = "";
let answersCount = [0, 0, 0, 0]; 

console.log("¡Bienvenido a Hogwarts!");

rl.question("¿Cuál es tu nombre? ", (answer) => {
  name = answer;
  console.log(
    `¡Hola, ${name}! Seguramente serás un mago o bruja maravilloso. Pero antes, necesitas saber a qué casa perteneces...\nPara ello, responde las siguientes preguntas:`);

  
    function askQuestion(questionData, index) {
        console.log(`\n${questionData.question}`);
        for (const [key, value] of Object.entries(questionData.answers)) {
          console.log(`${key}: ${value}`);
        }
      
        rl.question("Respuesta: ", (answer) => {
          const choice = parseInt(answer);
          if (choice >= 1 && choice <= 4) {
            answersCount[choice - 1]++;
            if (index < data.length - 1) {
              askQuestion(data[index + 1], index + 1);
            } else {
              
              const maxCount = Math.max(...answersCount);
              const maxIndex = answersCount.indexOf(maxCount);
              const duplicateMax = answersCount.lastIndexOf(maxCount);
      
              if (duplicateMax !== maxIndex) {
                console.log("\nCurioso... Es díficil encontrar una casa para ti... ¿Dónde quisieras estar?");
                const validHouses = houses.filter((_, index) => answersCount[index] === maxCount);
                console.log(`Casas ideales para ti: ${validHouses.join(", ")}`);
                
                rl.question(`Elige tu casa (${validHouses.map((house, index) => `${index + 1}: ${house}`).join(", ")}): `, (choice) => {
                  const chosenHouse = validHouses[parseInt(choice) - 1];
                  console.log(`¡En ese caso felicidades, ${name}! ¡Perteneces a ${chosenHouse}!`);
                  rl.close();
                });
              } else {
                const chosenHouse = houses[maxIndex];
                console.log(`¡Felicidades, ${name}! ¡Perteneces a ${chosenHouse}!`);
                rl.close();
              }
            }
          } else {
            console.log("Respuesta inválida. Por favor, elige una respuesta válida.");
            askQuestion(questionData, index);
          }
        });
      }
      
      askQuestion(data[0], 0); 
});


