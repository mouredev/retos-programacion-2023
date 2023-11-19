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
})

playGame()

function playGame(){
    console.log('Welcome to the math game!')
    console.log('You have 3 seconds to answer...')
    console.log('Good luck!!')
    game(0)
    
}

function game(points){
    const [number1,operation, number2] = getQuestion(points)
    const question = `${number1} ${operation} ${number2}`
    const result =getResult(number1, operation, number2)

    const timer = setTimeout(() => {
        console.log('\nTime is up! Game over :(');
        console.log(`You answered ${points} questions correctly`);
        rl.close();
    }, 3000)
      
    rl.question(`What is the result of the operation: ${question} = `, (answer) => {
         console.log(result)
         clearTimeout(timer);
        if (parseInt(answer) === result){
            console.log('Correct answer')
            points++
            console.log(`You have ${points} points`)
            game(points)
        }
        else {
            console.log('Game over :(')
            console.log(`You answered ${points} questions correctly`)
            rl.close()
        }
    })
    
}

// helper functions
function getOperator(){
    const operations = ['+','-','*','/'];
    return operations[Math.floor(Math.random()*operations.length)];
}

function getOneDigitNumber(){
    return Math.floor(Math.random()*10);
}

function getTwoDigitNumber(){
    return Math.floor(Math.random()*100);
}

function getThreeDigitNumber(){
    return Math.floor(Math.random()*1000);
}

function getQuestion(points){   
    let number1
    let number2
    if (points< 5 ){
     number1 = getOneDigitNumber()
     number2 = getOneDigitNumber()
    } else if (points< 10){
        number1 = getTwoDigitNumber()
        number2 = getOneDigitNumber()
    } else if (points< 15){
        number1 = getTwoDigitNumber()
        number2 = getTwoDigitNumber()
    } else if (points< 20){
        number1 = getThreeDigitNumber()
        number2 = getTwoDigitNumber()
    } else if (points< 25){
        number1 = getThreeDigitNumber()
        number2 = getThreeDigitNumber()
    }
    const operation = getOperator()
    return [number1, operation, number2]
}

function getResult(number1, operator, number2){
    if (operator === '+'){
        return number1 + number2
    } else if (operator === '-'){
        return number1 - number2
    } else if (operator === '*'){
        return number1 * number2
    } else if (operator === '/'){
        return Math.round(number1 / number2)
    }
}

