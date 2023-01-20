//Bucle que muestra los números de 1 a 100 ambos inclusivos
for (let i = 1; i <= 100; i++) {
    //Si el número es múltiplo de 3 y de 5 a la vez muestra "fizzbuzz"
    if (i % 3 === 0 && i % 5 === 0) {
        console.log("fizzbuzz");
        //Si solo es múltiplo de 3 muestra la palabra "fizz"
    } else if (i % 3 === 0) {
        console.log("fizz");
        //Si solo es múltiplo de 5 muestra la palabra "buzz"
    } else if (i % 5 === 0) {
        console.log("buzz");
        //Si no es múltiplo de 3 o de 5 muestra el número
    } else {
        console.log(i);
    }
}