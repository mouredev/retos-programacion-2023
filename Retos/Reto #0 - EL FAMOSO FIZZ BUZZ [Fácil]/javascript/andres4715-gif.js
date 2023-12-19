/*
 * Escribe un programa que muestre por consola (con un print) los
 * números de 1 a 100 (ambos incluidos y con un salto de línea entre
 * cada impresión), sustituyendo los siguientes:
 * - Múltiplos de 3 por la palabra "fizz".
 * - Múltiplos de 5 por la palabra "buzz".
 * - Múltiplos de 3 y de 5 a la vez por la palabra "fizzbuzz".
 */

const execution = () => {
    let dataObtained = data(1, 100); 
    return dataObtained;
}

const data = (startNumber, finalNumber) => {
    for (let i = startNumber ; i <= finalNumber; i++) {
        for (let i = startNumber; i <= finalNumber; i++) {
            if (i % 3 == 0 && i % 5 == 0) {
                console.log("fizzbuzz")
            }
            else if (i % 3 == 0) {
                console.log("fizz")
            } else if (i % 5 == 0) {
                console.log("buzz")
            } else {
                console.log(i)
            }
        }
        console.log(i)
    }
}


console.log(execution()); 
