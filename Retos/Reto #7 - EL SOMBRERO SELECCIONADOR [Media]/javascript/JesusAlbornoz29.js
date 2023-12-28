/*
 * Crea un programa que simule el comportamiento del sombrero selccionador del
 * universo mágico de Harry Potter.
 * - De ser posible realizará 5 preguntas (como mínimo) a través de la terminal.
 * 
 * - Cada pregunta tendrá 4 respuestas posibles (también a selecciona una a través de terminal).
 * - En función de las respuestas a las 5 preguntas deberás diseñar un algoritmo que
 *   coloque al alumno en una de las 4 casas de Hogwarts (Gryffindor, Slytherin , Hufflepuff y Ravenclaw)
 * - Ten en cuenta los rasgos de cada casa para hacer las preguntas y crear el algoritmo seleccionador.
 *   Por ejemplo, en Slytherin se premia la ambición y la astucia.
 */



// 1) Para capturar datos desde la terminal en Node.js, puedes utilizar la API readline para heco la importamos
const readline = require('readline');

// 2) Creamos la interfaz de lectura
const rl = readline.createInterface({
  input: process.stdin,
  output: process.stdout
});

// funcion de hacer pregunta
function hacerPregunta (pregunta) {
    return new Promise ((resolve, reject) => {
        rl.question(pregunta, (respuesta) => {
            resolve(respuesta);
        })
    })
}

console.log ("!Bienvenido al sombrero seleccionador de Hogwarts!");

// Constantes
var grifindor = 0;
var huffepuff = 0;
var ravenclaw = 0;
var slytherin = 0;

// function devolve mayor 
function devolverMayor (p1,p2,p3,p4) {
    if (p1 > p2 && p1 > p3 && p1 > p4){
        return console.log("Mmmmmmm muy dificil, dificil.... Valiente pero imprudente lo veo! \n Grifindor!!!");
    } if (p2 > p1 && p2 > p3 && p2 > p4){
        return console.log("Mmmmmmm muy dificil, dificil.... Solidario y leal lo veo! \n Huffepuff!!!");
    } if (p3 > p1 && p3 > p2 && p3 > p4){
        return console.log("Mmmmmmm muy dificil, dificil.... Inteligente pero presumido lo veo! \n Ravenclaw!!!");
    } if (p4 > p1 && p4 > p3 && p4 > p2){
        return console.log("Mmmmmmm muy dificil, dificil.... Ambicioso y astuto lo veo! \n Slytherin!!!");
    }
}


// Hacer todas las preguntas 
async function hacerTodasLasPreguntas() {
    const pregunta1 = await hacerPregunta(" Como te definirias? \n 1) Valiente \n 2) Leal \n 3) Sabio \n 4) Ambicioso \n");
    if (parseInt(pregunta1) == 1){
        grifindor += 1;
    }if (parseInt(pregunta1) == 2){
        huffepuff += 1;
    }if (parseInt(pregunta1) == 3){
        ravenclaw += 1;
    }if (parseInt(pregunta1) == 4){
        slytherin += 1;
    }
    const pregunta2 = await hacerPregunta(" Donde pasarias mas tiempo? \n 1) Invernadero \n 2) Biblioteca \n 3) Sala comunal \n 4) Explorando \n ");
    if (parseInt(pregunta2) == 1){
        grifindor += 1;
    }if (parseInt(pregunta2) == 2){
        huffepuff += 1;
    }if (parseInt(pregunta2) == 3){
        ravenclaw += 1;
    }if (parseInt(pregunta2) == 4){
        slytherin += 1;
    }
    const pregunta3 = await hacerPregunta(" Cual seria tu clase favorita? \n 1) Vuelo \n 2) Pociones \n 3) Defensas contras las artes misticas \n 4) Animales fantasticos \n ");
    if (parseInt(pregunta3) == 1){
        grifindor += 1;
    }if (parseInt(pregunta3) == 2){
        huffepuff += 1;
    }if (parseInt(pregunta3) == 3){
        ravenclaw += 1;
    }if (parseInt(pregunta3) == 4){
        slytherin += 1;
    }
    const pregunta4 = await hacerPregunta(" Cual es tu color favorito? \n 1) Rojo \n 2) Azul \n 3) Negro \n 4) Verde \n ");
    if (parseInt(pregunta4) == 1){
        grifindor += 1;
    }if (parseInt(pregunta4) == 2){
        huffepuff += 1;
    }if (parseInt(pregunta4) == 3){
        ravenclaw += 1;
    }if (parseInt(pregunta4) == 4){
        slytherin += 1;
    }
    const pregunta5 = await hacerPregunta(" Si tuvieras que elegir una de las siguientes mascotas. Cual elegirias? \n 1) Lechuza \n 2) Gato \n 3) Sapo \n 4) Serpiente \n ");
    if (parseInt(pregunta5) == 1){
        grifindor += 1;
    }if (parseInt(pregunta5) == 2){
        huffepuff += 1;
    }if (parseInt(pregunta5) == 3){
        ravenclaw += 1;
    }if (parseInt(pregunta5) == 4){
        slytherin += 1;
    }
    rl.close();
    console.log(devolverMayor(grifindor, huffepuff, ravenclaw, slytherin));
}

console.log(hacerTodasLasPreguntas());


