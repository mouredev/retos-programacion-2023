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

console.log("Bienvenidos a hogwarts")
console.log("Porfavor para ser ubicados en una de las 4 casas responda a las siguientes preguntas que le hara el sombrero seleccionador:\n")

var preguntas_sombrero = [ 
    "Dime tu nombre: ",
    "\n¿Qué cualidad valoras más en ti mismo?\n A) Valentía\n B) Astucia\n C) Inteligencia\n D) Lealtad\n R: ",
    "\n¿Cuál es tu materia favorita en Hogwarts?\n A) Defensa contra las artes oscuras\n B) Pociones\n C) Encantamientos\n D) Cuidado de Criaturas Mágicas\n R: ",
    "\n¿Qué harías si tuvieras la oportunidad de conseguir un gran poder?\n A) Usarlo para ayudar a los demás\n B) Usarlo para lograr mis objetivos\n C) Usarlo para aprender más\n D) Usarlo para cuidar de mi familia y amigos\n R: ",
    "\n¿Qué tipo de animal te gustaría tener como mascota?\n A) León\n B) Serpiente\n C) Búho\n D) Tejón\n R: ",
    "\n¿Qué lugar te gustaría visitar en el mundo mágico?\n A) Torre de Gryffindor\n B) Bosque Prohibido\n C) Biblioteca de Hogwarts\n D) Cabaña de Hagrid\n R: ",
]


function recorrer_preguntas(i){
    process.stdout.write(preguntas_sombrero[i])
}


var respuestas = []
process.stdin.on('data', function(data){
    var gryffindor = 0
    var slytherin = 0
    var ravenclaw = 0 
    var hufflepuff = 0
    var nombre = ""
    respuestas.push(data.toString().trim())
    
    for(let i=0; i<respuestas.length; i++){
        if(respuestas[i]==="A"){
            gryffindor = gryffindor + 0.157
        }else if(respuestas[i]==="B"){
            slytherin = slytherin + 0.181
        }else if(respuestas[i]==="C"){
            ravenclaw = ravenclaw + 0.119
        }else if(respuestas[i]==="D"){
            hufflepuff = hufflepuff + 0.067
        }else if(respuestas[0]!=="A" || respuestas[0]!=="B" || respuestas[0]!=="C" || respuestas[0]!=="D"){
            nombre = nombre + respuestas[0]
        }else if(respuestas[i]!=="A" || respuestas[i]!=="B" || respuestas[i]!=="C" || respuestas[i]!=="D"){
            console.log("Error opcion no valida")
            process.exit()
        }
    }

    if(respuestas.length<preguntas_sombrero.length){
        recorrer_preguntas(respuestas.length)
    }else{
        if(gryffindor>slytherin && gryffindor>ravenclaw && gryffindor>hufflepuff ){
            console.log("\nFelicidades "+nombre+" iras a la casa gryffindor!!")
        }else if(slytherin>gryffindor && slytherin>ravenclaw && slytherin>hufflepuff ){
            console.log("\nFelicidades "+nombre+" iras a la casa slytherin!!")
        }else if(ravenclaw>gryffindor && ravenclaw>slytherin && ravenclaw>hufflepuff){
            console.log("\nFelicidades "+nombre+" iras a la casa ravenclaw!!")
        }else if(hufflepuff>gryffindor && hufflepuff>slytherin && hufflepuff>ravenclaw ){
            console.log("\nFelicidades "+nombre+" iras a hufflepuff!! ")
        }
        process.exit()
    }

})


recorrer_preguntas(0)