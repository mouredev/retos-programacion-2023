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

import * as readline from 'readline';


/**
 * Interface que representa una pregunta y sus respuestas
 */
interface Question {

question: string;
answers: Answer[];

}

/**
 * Interface que representa una respuesta y sus puntos
 */
interface Answer {
    answer :string
    points:Points[]
}


/**
 * Interface que representa los puntos de cada equipo
 */
interface Points {
    name:Teams;
    points: number;

}


/**
 * Enumerado que representa los equipos
 */
export enum Teams {
    GranadaCF = 'Granada CF',
    RMadrid = 'Real Madrid',
    Farsa = 'Farsa, el equipo de los culerdos',
    Celtic = 'Celtic de Pulianas'

}

/**
 * Array de preguntas y respuestas y sus puntos correspondientes a cada equipo
 */
const questions: Question[] = [
    {   question: 'Se acerca la fecha del próximo partido de tu equipo, ¿cómo te sientes?',
        answers: [
            {answer: 'Nervioso/a, todos los partidos de mi equipo los siento con pasión.', points: [{name: Teams.Celtic, points: 10}, {name: Teams.Farsa, points: 0}, {name: Teams.GranadaCF, points: 9},{name: Teams.RMadrid, points: 2}]},
            {answer: 'No es relevante, cuando llegue la hora ya me sentaré a verlo tranquilamente.',points :[{name: Teams.Celtic, points: 0}, {name: Teams.Farsa, points: 7}, {name: Teams.GranadaCF, points: 2},{name: Teams.RMadrid, points: 7}]},
            {answer: 'Los vecinos hablan sobre el partido los días previos, se nota el ambiente en la calle.',points: [{name: Teams.Celtic, points: 4}, {name: Teams.Farsa, points:10}, {name: Teams.GranadaCF, points: 1},{name: Teams.RMadrid, points: 9}]},
            {answer: 'No como ni duermo los días previos de los nervios. Da igual que sean dieciseisavos de Copa o la última jornada de Liga, lo vivo.' , points: [{name: Teams.Celtic, points: 8}, {name: Teams.Farsa, points: 1}, {name: Teams.GranadaCF, points:10},{name: Teams.RMadrid, points: 0}]},
        ]
    },
    {   question: 'Estás en un bar y te das cuenta de que nadie es del mismo equipo que tú, ¿qué piensas?',
        answers: [
            {answer:'Joder, mira que es raro.',points:[{name: Teams.Celtic, points: 10}, {name: Teams.Farsa, points: 0}, {name: Teams.GranadaCF, points: 3},{name: Teams.RMadrid, points: 2}]},
            {answer:'Ya está esto lleno de borregos, míralos, todos viendo el Chirincirco.',points: [{name: Teams.Celtic, points: 1}, {name: Teams.Farsa, points: 7}, {name: Teams.GranadaCF, points: 4},{name: Teams.RMadrid, points: 9}]},
            {answer:'Normal, si somos 4 gatos. Eh, pero con orgullo, coño.',points: [{name: Teams.Celtic, points: 2}, {name: Teams.Farsa, points:10}, {name: Teams.GranadaCF, points: 1},{name: Teams.RMadrid, points: 2}]},
            {answer:'Ups, igual tenía que haber ido al de dos calles más abajo...',points: [{name: Teams.Celtic, points: 10}, {name: Teams.Farsa, points: 1}, {name: Teams.GranadaCF, points:4},{name: Teams.RMadrid, points: 1}]},
        ]
    },
    {   question: 'Penalti a favor del Madrid/Barcelona. En la repetición se ve que no era. ¿Cómo reaccionas?',
        answers: [
            {answer:'Ya están robando estos perros.',points:[{name: Teams.Celtic, points: 10}, {name: Teams.Farsa, points: 0}, {name: Teams.GranadaCF, points: 9},{name: Teams.RMadrid, points: 2}]},
            {answer:'Esto es una puta vergüenza! Soy el entrenador y los saco del campo, que se rían de su madre.',points: [{name: Teams.Celtic, points: 3}, {name: Teams.Farsa, points: 10}, {name: Teams.GranadaCF, points: 3},{name: Teams.RMadrid, points: 9}]},
            {answer:'Ya la tenemos liada, ahora a aguantar a la prensa toda la semana...',points: [{name: Teams.Celtic, points: 4}, {name: Teams.Farsa, points: 0}, {name: Teams.GranadaCF, points: 9},{name: Teams.RMadrid, points: 2}]},
            {answer:'Ya estamos con la prensa mamadora del movimiento',points: [{name: Teams.Celtic, points: 10}, {name: Teams.Farsa, points: 0}, {name: Teams.GranadaCF, points: 9},{name: Teams.RMadrid, points: 2}]},
        ]
    },
    {   question: ' Caso contrario: última jornada de liga y una victoria de tu equipo hace que supere el objetivo marcado al principio del año.',
        answers: [
            {answer: 'Coño, coño, coño, coño, coño, coño. Como les dé por ganar me desnudo en la fuente del pueblo.',points:[{name: Teams.Celtic, points: 10}, {name: Teams.Farsa, points: 0}, {name: Teams.GranadaCF, points: 9},{name: Teams.RMadrid, points: 2}]},
            {answer:'Yaya, enséñame unos rezos de esos, que es para una cosa del finde.',points: [{name: Teams.Celtic, points: 1}, {name: Teams.Farsa, points: 9}, {name: Teams.GranadaCF, points: 2},{name: Teams.RMadrid, points: 6}]},
            {answer:'Pase lo que pase ha sido un temporadón, ¡qué orgullo de equipo!',points: [{name: Teams.Celtic, points:6}, {name: Teams.Farsa, points: 5}, {name: Teams.GranadaCF, points:4},{name: Teams.RMadrid, points: 4}]},
            {answer:'Con lo bien que vivía yo cuando éramos mediocres, qué ganas de matarnos con los nervios.',points: [{name: Teams.Celtic, points: 10}, {name: Teams.Farsa, points: 1}, {name: Teams.GranadaCF, points: 9},{name: Teams.RMadrid, points: 4}]},
        ]
    },
    {   question: 'Final de la temporada, tu equipo desciende a Segunda División. Vaya veranito te vas a pegar...',
        answers: [
            {answer: 'JAJAJAJAJAJAJAJAJA EN SEGUNDA DICE, ¡QUE SOY DEL MADRID/BARÇA, TOLAI!',points:[{name: Teams.Celtic, points: 0}, {name: Teams.Farsa, points: 10}, {name: Teams.GranadaCF, points: 0},{name: Teams.RMadrid, points: 10}]},
            {answer:'Lloro, me enfado, durante las primeras semanas va a ser una auténtica pesadilla. No puede pasarnos a nosotros...',points: [{name: Teams.Celtic, points: 5}, {name: Teams.Farsa, points: 7}, {name: Teams.GranadaCF, points: 3},{name: Teams.RMadrid, points: 4}]},
            {answer:'No pudo ser, nos vino grande la categoría. Volveremos con más fuerza, ¡seguro!',points: [{name: Teams.Celtic, points: 7}, {name: Teams.Farsa, points: 2}, {name: Teams.GranadaCF, points: 9},{name: Teams.RMadrid, points: 2}]},
            {answer:'Otra vez al hoyo. El año que viene mi abono se lo pueden meter por el...',points: [{name: Teams.Celtic, points: 4}, {name: Teams.Farsa, points: 0}, {name: Teams.GranadaCF, points: 9},{name: Teams.RMadrid, points: 0}]},
        ]
    }
]

/**
 * Equipos participantes en el quiz
 */
const teams: Points[] = [
    {name: Teams.Celtic, points: 0},
    {name: Teams.Farsa, points: 0},
    {name: Teams.GranadaCF, points: 0},
    {name: Teams.RMadrid, points: 0}
];


/**
 * Interfaz para la entrada de datos por consola
 */
let input = readline.createInterface({
    input: process.stdin,
    output: process.stdout
})


/**
 * Función que calcula el equipo al que perteneces
 */
function yourTeamIs(){
    const team = teams.reduce((prev, current) => (prev.points > current.points) ? prev : current).name
    console.log(`\nEnhorabuena!! Eres del ${team} hasta la muerte! \n`)
}

/**
 * Función que suma los puntos a cada equipo en función de la respuesta
 * @param points información de los puntos a sumar
 */
function addPoints(points: Points[]) {
    for (let i = 0; i < points.length; i++) {
        const point = points[i];
        teams.find((t) => t.name === point.name)!!.points+=point.points;
    }
}

/**
 * Función que muestra la pregunta y las respuestas y el control de la entrada de datos
 * @param q pregunta y respuestas
 * @param index índice de la pregunta
 * @constructor
 */
function Quiz(q: Question,index:number) : Promise<void> {
    return new Promise((resolve, reject) => {
        const quest = q.question;
        const answers = q.answers;
        let answerIndex = 0;
        let validInput = false;
        const value = quest + "\n\n\n" + answers.map((answer, i) => (i + 1) + "-" + answer.answer).join('\n')+ "\n"

        input.question(value,
            (answer) => {
                if(!/^\d+$/.test(answer) || Number(answer) > answers.length || Number(answer) < 1) {
                    console.log('\nIntroduce un número válido\n')
                    return Quiz(q, index).then(() => { validInput = true })
                } else {
                    console.log('\n')
                    answerIndex = parseInt(answer)
                    addPoints(answers[answerIndex - 1].points)
                    validInput = true
                }
            })
        function checkInput() {
            if (validInput) {
                resolve()
            } else {
                setTimeout(checkInput, 100)
            }
        }
        checkInput()
    })
}

/**
 * Función principal que llama a la función que muestra las preguntas
 */
async function futbolQuiz() {
    console.log('Bienvenido al test de fútbol. Responde a las siguientes preguntas y averigua qué equipo eres.\n')
    for (const q of questions) {1
        await Quiz(q, questions.indexOf(q))
    }
    input.close()
    yourTeamIs()

}

/**
 * Llamada a la función principal
 */
futbolQuiz()





