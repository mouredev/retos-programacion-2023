const readLine = require('readline')

const rl = readLine.createInterface({
    input: process.stdin,
    output: process.stdout
});

rl.question("Introduce un número: ", (response: number) => {
    console.log(("El número " + response) + (esPrimo(response) ? " es primo, " : " no es primo, ") + (esFibonacci(response) ? "es fibonacci " :  "no es fibonacci ") + (esImpar(response) ? "y es impar" : "y es par"));
    process.exit();
});

function esPrimo(num: number): boolean {
    let esPrimo = true;
    // Un número siempre es divisible por 1 y por sí mismo, por lo que excluimos estos valores.
    for (let index = 2; index < num; index++){
        if (num % index == 0) {
            esPrimo = false;
            break;
        }
    }
    return esPrimo;
}

function esImpar(num: number): boolean {
    let esImpar = true;
    if (num % 2 == 0) {
        esImpar = false;
    }

    return esImpar;
}

function esFibonacci(num: number): boolean {
    let esFibonacci = false;
    let numeroAnterior = 1;
    let numeroActual = 1;
    let suma = 0;
    while (suma < num && !esFibonacci) {
        suma = numeroAnterior + numeroActual;
        if (suma == num) {
            esFibonacci = true;
            break;
        }
        numeroAnterior = numeroActual;
        numeroActual = suma;
    }
    return esFibonacci;
}
