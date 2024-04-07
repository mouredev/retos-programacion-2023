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

const readline = require('node:readline')

const rl = readline.createInterface({
    input: process.stdin,
    output: process.stdout
})

function wordCounter(word) {
    const alfabeto = 'abcdefghijklmnñopqrstuvwxyz';
    let sum = 0
    word.toLowerCase().split('').forEach(letra => {
        const contador = alfabeto.indexOf(letra) + 1
        console.log(`La letra ${letra} tiene un valor de ${contador}`)
        sum += contador
    })
    // const array = alfabeto.split('').findIndex(l => l === letra) + 1
    return sum
}
let sum = 0

function Question() {
    if (sum !== 100) {
        rl.question('Ingrese una palabra para conseguir los 100 puntos: ', (word) => {
            sum = wordCounter(word)
            Question()
        })
    }
    else {
        rl.close()
    }
}
Question()
