/*
 * Crea un programa que sea capaz de solicitarte un número y se
 * encargue de imprimir su tabla de multiplicar entre el 1 y el 10.
 * - Debe visualizarse qué operación se realiza y su resultado.
 *   Ej: 1 x 1 = 1
 *       1 x 2 = 2
 *       1 x 3 = 3
 *       ... 
 */


const readline = require('readline')

function multiplicationTable(){
    console.log('Please enter a number:')

    const rl = readline.createInterface({
        input: process.stdin,
        output: process.stdout
    })
   
    rl.on('line', (input) => {
        if(isNaN(input)){
            console.log('Please enter a valid number')
        } else {
            for (let i = 1; i <= 10; i++) {
                console.log(`${input} x ${i} = ${input * i}`)            
        }
        rl.close()
        }
    })
}

multiplicationTable()