/*
    Escribe un programa que muestre por consola (con un print) los
    números de 1 a 100 (ambos incluidos y con un salto de línea entre
    cada impresión), sustituyendo los siguientes:
        - Múltiplos de 3 por la palabra "fizz".
        - Múltiplos de 5 por la palabra "buzz".
        - Múltiplos de 3 y de 5 a la vez por la palabra "fizzbuzz".
*/

for (let number = 1; number <= 100; number++) {
    const multipleOf3 = number % 3 === 0;
    const multipleOf5 = number % 5 === 0;

    if (multipleOf3)
        console.log("fizz");
    else if (multipleOf5)
        console.log("buzz");
    else if (multipleOf3 && multipleOf5)
        console.log("fizzbuzz");
    else
        console.log(number);
}