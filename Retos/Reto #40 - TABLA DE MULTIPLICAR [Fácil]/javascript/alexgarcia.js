const prompt = require("prompt-sync")();

// Ask and validate whether is a number
function askAndValidateNumber() {
    let number = parseInt(prompt("Ingrese un valor para imprimir su tabla de multiplicar del 1 hasta el 10: "));

    if (typeof number === 'number' && !isNaN(number)) {
        generateMultiplicationTable(number);
    } else {
        console.log("Debes ingresar un numero.")
    }
}

// Generate multiplication table for entered number
function generateMultiplicationTable(number) {
    for (let i = 1; i <= 10; i++) {
        let multiplicationResult = number * i
        console.log(`${number} x ${i} = ${multiplicationResult}`)
    }
}

askAndValidateNumber()