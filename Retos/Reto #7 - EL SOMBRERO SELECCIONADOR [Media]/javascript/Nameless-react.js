const readlinePromises = require('node:readline/promises');

class createQuestion {   
     constructor(question, answer) {
        this.question = question;
        this.answer = answer;
    }
}

const selectionHouse = async (rl) => {
    console.log("Bienvenido(a) yo soy el sombrero seleccionador, a continuación voy a hacer unas preguntas para saber a que casa perteneces");

    const hatQuestions = [new createQuestion("¿Cómo te definirías?", [
                            ["1. Valiente", "gryffindor"],
                            ["2. Leal", "hufflepuff"],
                            ["3. Sabio", "ravenclaw"],
                            ["4. Ambicioso", "slytherin"]]),
                 new createQuestion("¿Cuál es tu clase favorita?", [
                            ["1. Vuelo", "gryffindor"],
                            ["2. Pociones", "ravenclaw"],
                            ["3. Defensa contra las artes oscuras", "slytherin"],
                            ["4. Animales fantásticos", "hufflepuff"]]),
                 new createQuestion("¿Dónde pasarías más tiempo?", [
                            ["1. Invernadero", "hufflepuff"],
                            ["2. Biblioteca", "ravenclaw"],
                            ["3. En la sala común", "slytherin"],
                            ["4. Explorando", "gryffindor"]]),
                 new createQuestion("¿Cuál es tu color favorito?", [
                            ["1. Rojo", "gryffindor"],
                            ["2. Azul", "ravenclaw"],
                            ["3. Verde", "slytherin"],
                            ["4. Amarillo", "hufflepuff"]]),
                 new createQuestion("¿Cuál es tu mascota?", [
                            ["1. Sapo", "ravenclaw"],
                            ["2. Lechuza", "gryffindor"],
                            ["3. Gato", "hufflepuff"],
                            ["4. Serpiente", "slytherin"]])
            ];
    const houses = {
        "gryffindor": 0,
        "hufflepuff": 0,
        "ravenclaw": 0,
        "slytherin": 0
    }
    
    

    for (let question of hatQuestions) {
        let answer = "";

        do  {
            answer = await rl.question(question.question + question.answer.map(answer =>  "\n" + answer[0]).join("") + "\n");
            answer = parseInt(answer);
            
        } while ([1, 2 ,3, 4].every(option => option != answer));
        for (let i = 0; i < question.answer.length; i++) {
            if (i + 1 == answer) houses[question.answer[i][1]] += 1;
        }            
    }         
    console.log("Hmmmmm....");
    console.log("Creo...");
    console.log("Que podrias encajar en....");
    const house = Math.max(...Object.values(houses));


    console.log(`\n${'#'.repeat(20)} ${Object.entries(houses).find(elements => elements[1] == house)[0]} ${'#'.repeat(20)}`);
    rl.close();
}


const rl = readlinePromises.createInterface({
    input: process.stdin,
    output: process.stdout
});


selectionHouse(rl);