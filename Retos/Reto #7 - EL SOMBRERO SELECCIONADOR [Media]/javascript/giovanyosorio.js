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

const readline = require('readline');
let puntajeGryffindor = 0;
let puntajeSlytherin = 0;
let puntajeHufflepuff = 0;
let puntajeRavenclaw = 0;

let rl = readline.createInterface(
                    process.stdin, process.stdout);

                    
rl.question('What is your name? ', (nombre) => {
    console.log(`\n${nombre}, responde las siguientes preguntas:`);
    rl.question("Cual cualidad valoras mas\n"+
    "   a) Valentía\n" +
    "   b) Ambición\n" +
    "   c) Lealtad\n" +
    "   d) Inteligencia\n" +
    "Respuesta: ",(respuesta1)=>{
        respuesta1.toLowerCase=="a" ? puntajeGryffindor++  : respuesta1.toLowerCase=="b" ? puntajeSlytherin++ :respuesta1.toLowerCase=="c" ? puntajeHufflepuff++ :puntajeRavenclaw++
    
    
        rl.question("Qué tipo de mascota preferirías tener?\n"+
        "a) Lechuza\n "+
        "b) Serpiente \n"+
        "C) Perro \n"+
        "D)Gato \n"+
        "Respuesta: ",(respuesta2)=>{
            respuesta2.toLowerCase=="a" ? puntajeGryffindor++  : respuesta2.toLowerCase=="b" ? puntajeSlytherin++ :respuesta2.toLowerCase=="c" ? puntajeHufflepuff++ :puntajeRavenclaw++
    
            rl.question("Cual es tu clase favorita\n "+
            "a) Vuelo\n "+
            "b) Pociones \n"+
            "C) Defensa contra las artes oscuras \n"+
            "D)Animales fantasticos \n"+
            "Respuesta: ",(respuesta3)=>{
                respuesta3.toLowerCase=="a" ? puntajeGryffindor++  : respuesta3.toLowerCase=="b" ? puntajeSlytherin++ :respuesta3.toLowerCase=="c" ? puntajeHufflepuff++ :puntajeRavenclaw++
       
     
        console.log("\nEl Sombrero está pensando...");
        console.log("Tu casa es...");

        if (puntajeGryffindor=>puntajeSlytherin && puntajeGryffindor>puntajeHufflepuff && puntajeGryffindor>puntajeRavenclaw) {
            console.log("¡Gryffindor!");
        }else if(puntajeSlytherin=>puntajeGryffindor && puntajeSlytherin>puntajeHufflepuff && puntajeSlytherin>puntajeRavenclaw){
            console.log("puntajeSlytherin!");
        }
        else if(puntajeGryffindor=>puntajeSlytherin && puntajeGryffindor>puntajeHufflepuff && puntajeGryffindor>puntajeRavenclaw){
            console.log("puntajeSlytherin!");
        }
        else{
            console.log("ravenclaw")
        }
        console.log(`¡Bienvenido a tu nueva casa en Hogwarts, ${nombre}!`);
        rl.close();
    })
    })
})
});