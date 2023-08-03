/*
Escribe un programa que muestre por consola (con un print) los
números de 1 a 100 (ambos incluidos y con un salto de línea entre
cada impresión), sustituyendo los siguientes:
Múltiplos de 3 por la palabra "fizz".
Múltiplos de 5 por la palabra "buzz".
Múltiplos de 3 y de 5 a la vez por la palabra "fizzbuzz"
 */
function fizz_buzz_junior() {
    for (let number = 1; number <= 100; number++) {
        if (number % 3 == 0 && number % 5 == 0) {
            console.log("fizzbuzz");
        } else if (number % 3 == 0) {
            console.log("fizz");
        } else if (number % 5 == 0) {
            console.log("buzz");
        } else {
            console.log(number);
        }
    }
}
//* Solucion junior
fizz_buzz_junior();

const fizz_buzz_senior = () => {
    for (let number = 1; number <= 100; number++) {
        const output = (number % 3 === 0 ? "fizz" : "") + (number % 5 === 0 ? "buzz" : "");
        console.log(output || number);
    }
}
//* Solucion senior
fizz_buzz_senior();

const fizz_buzz_chatgpt = () => Array(100).fill().forEach((_, n) => {
    const output = (n % 3 === 0 ? "fizz" : "") + (n % 5 === 0 ? "buzz" : "");
    console.log(output || n);
});
//* Solucion chatgpt 👀
fizz_buzz_chatgpt();
