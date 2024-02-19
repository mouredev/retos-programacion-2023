/*
 * Crea un juego interactivo por terminal en el que tendrás que adivinar 
 * el resultado de diferentes
 * operaciones matemáticas aleatorias (suma, resta, multiplicación 
 * o división de dos números enteros).
 * - Tendrás 3 segundos para responder correctamente.
 * - El juego finaliza si no se logra responder en ese tiempo.
 * - Al finalizar el juego debes mostrar cuántos cálculos has acertado.
 * - Cada 5 aciertos debes aumentar en uno el posible número de cifras 
 *   de la operación (cada vez en un operando):
 *   - Preguntas 1 a 5: X (entre 0 y 9) operación Y (entre 0 y 9)
 *   - Preguntas 6 a 10: XX (entre 0 y 99) operación Y (entre 0 y 9)
 *   - Preguntas 11 a 15: XX operación YY
 *   - Preguntas 16 a 20: XXX (entre 0 y 999) operación YY
 *   ...
 */
const readline = require('readline')
const rl = readline.createInterface({
    input: process.stdin,
    output: process.stdout
});

let contador = 0, X = 1, Y = 1

const tribia = () => {

    const OPERACIONES = ['+', '-', '*', '/']
    let a, b, resultado

    const operacion = OPERACIONES[Math.floor(Math.random() * 4)]
    a = Math.floor(Math.random() * (10 ** X))
    b = Math.floor(Math.random() * (10 ** Y))

    if (operacion === '+') resultado = a + b
    if (operacion === '-') resultado = a - b
    if (operacion === '*') resultado = a * b
    if (operacion === '/') resultado = a / b

    console.log(`Resuelva ${a}${operacion}${b}`)

    let timeoutId = setTimeout(() => {
        console.log('Tiempo agotado')
        rl.close()
    }, 3000)

    rl.question('Ingrese su respuesta: ', (userInput) => {
        clearTimeout(timeoutId)
        console.log(`la respuesta es ${userInput == resultado ? 'Correcta' : 'Incorrecta'}`)
        contador += 1
        if (contador % 5 === 0) {
            X <= Y ? X += 1 : Y += 1
        }
        console.log(`X:${X} e Y:${Y}`)
        tribia()
    })
}
tribia()
