/*
Escribe un programa que muestre por consola (con un print) los
números de 1 a 100 (ambos incluidos y con un salto de línea entre
cada impresión), sustituyendo los siguientes:
Múltiplos de 3 por la palabra "fizz".
Múltiplos de 5 por la palabra "buzz".
Múltiplos de 3 y de 5 a la vez por la palabra "fizzbuzz"
 */

const PrintFizzBuzzByNumber2 = () => {
    for (let index = 1; index <= 100; index++) {
        let text = '';
        if (index % 3 === 0) text += "fizz";
        if (index % 5 === 0) text += "buzz";
        if (text === '') text += `${index}`
        console.log(text);
    }
}

PrintFizzBuzzByNumber2();
