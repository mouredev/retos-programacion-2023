/*
 * La última semana de 2021 comenzamos la actividad de retos de programación,
 * con la intención de resolver un ejercicio cada semana para mejorar
 * nuestra lógica... ¡Hemos llegado al EJERCICIO 100! Gracias 🙌
 *
 * Crea un programa que calcule los puntos de una palabra.
 * - Cada letra tiene un valor asignado. Por ejemplo, en el abecedario
 *   español de 27 letras, la A vale 1 y la Z 27.
 * - El programa muestra el valor de los puntos de cada palabra introducida.
 * - El programa finaliza si logras introducir una palabra de 100 puntos.
 * - Puedes usar la terminal para interactuar con el usuario y solicitarle
 *   cada palabra.
 */
const readline = require('readline')
const rl = readline.createInterface({
    input: process.stdin,
    output: process.stdout
})

console.log("Welcome to 100 points word!!")
game()    

function game(){
    let points = 0
    console.log("Try to find a word of 100 points:")
    rl.on('line', (input) => {
        for (let char of input.toLowerCase()){
            points += char.charCodeAt(0) - 96        
        }
        if(points == 100){
            console.log("Congratulations!! You found the word!!")
            rl.close()
        } else {
               console.log(`You get ${points} points,`)
            console.log("Try again!!")
            rl.removeAllListeners('line');
            game()
        }                
    })
}


