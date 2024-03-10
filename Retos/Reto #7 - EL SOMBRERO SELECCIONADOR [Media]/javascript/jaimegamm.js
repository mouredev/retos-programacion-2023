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

const readlineSync = require('readline-sync');

function hacerPregunta(pregunta, opciones){
    console.log("-----------------------------------------------------------------")
    console.log(pregunta)
    console.log("-----------------------------------------------------------------")
    for (let i = 0; i < opciones.length; i++) {
        const opcion = opciones[i];
        console.log((i+1) + ". " + opcion);  
    }
    const respuesta = readlineSync.questionInt('Selecciona una opcion (1-4): ');
    if (respuesta >= 1 && respuesta <= 4) {
        return respuesta
    } else {
        console.log("Por favor, ingresa un número válido.")
        return hacerPregunta(pregunta, opciones);
    }
}

function sombrero_seleccionador(){
    preguntas = [
        "¿Qué cualidad valoras más en un amigo?",
        "¿Qué tipo de magia prefieres?",
        "En una situación difícil, ¿eres?",
        "¿Qué animal mágico te gustaría tener como mascota?",
        "¿Cuál es tu asignatura favorita en Hogwarts?"
    ]

    respuestas_casas = {
        "Gryffindor": 0,
        "Slytherin": 0,
        "Hufflepuff": 0,
        "Ravenclaw": 0
    }

    lista_opciones = [
    [
        "Valiente", 
        "Ambicioso", 
        "Leal", 
        "Inteligente"
    ],
    [
        'Encantamientos',
        'Transformaciones',
        'Defensa Contra las Artes Oscuras',
        'Pociones',
    ],
    [
        "Valentía", 
        "Ambición", 
        "Lealtad", 
        "Inteligencia"
    ],
    [
        "Hippogriff",
        "Thestral",
        "Niffler",
        "Blast-Ended Skrewt"
    ],
    [
        'Defensa Contra las Artes Oscuras',
        'Pociones',
        'Transformaciones',
        'Astronomía'
    ]
    ]

    numero_lista = 0;
    preguntas.forEach(pregunta => {
        respuesta = hacerPregunta(pregunta, lista_opciones[numero_lista]);
        numero_lista += 1;
        if (respuesta === 1){
            respuestas_casas["Gryffindor"] += 1
        }else if (respuesta === 2){
            respuestas_casas["Slytherin"] += 1
        }else if (respuesta === 3){
            respuestas_casas["Hufflepuff"] += 1
        }else{
            respuestas_casas["Ravenclaw"] += 1
        }
    });

    let maxpuntuacion = 0;
    let casa_seleccionada;
    for(const casa in respuestas_casas){
        const puntuacion = respuestas_casas[casa]
        if(puntuacion > maxpuntuacion){
            maxpuntuacion = puntuacion;
            casa_seleccionada = casa;
        }
    }
    console.log("-----------------------------------------------------------------")
    console.log("-----------------------------------------------------------------")
    console.log(`Casa seleccionada: ${casa_seleccionada}`);
    console.log("-----------------------------------------------------------------")
    console.log("-----------------------------------------------------------------")
}


sombrero_seleccionador()