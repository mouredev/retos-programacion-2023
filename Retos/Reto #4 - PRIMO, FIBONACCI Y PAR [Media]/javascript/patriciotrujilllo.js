
/*
# Reto #4: PRIMO, FIBONACCI Y PAR
 * Escribe un programa que, dado un número, compruebe y muestre si es primo, fibonacci y par.
 * Ejemplos:
 * - Con el número 2, nos dirá: "2 es primo, fibonacci y es par"
 * - Con el número 7, nos dirá: "7 es primo, no es fibonacci y es impar"
 */

function primo(x) {
    if (x <= 1) return `${x} No es primo`

    let cont = 0
    for (let i = x; i > 1; i--) {
        if (x % i === 0) {
            cont += 1
        }
    }
    if (cont > 2) return `${x} No es primo`
    return `${x} Es primo`
}
function fibonacci(x) {
    let num1 = 0
    let num2 = 1
    let numActual = num2

    while (x > numActual) {

        numActual = num1 + num2
        num1 = num2
        num2 = numActual
    }
    if (x === numActual) return `, es fibonacci`
    console.log(`el numero actual es ${numActual}`)
    return `, No es fibonacci`
}
function par_impar(x) {
    if (x % 2 === 0) return ", es par"
    return ", es impar"
}

function prifipar(x) {
    return primo(x) + fibonacci(x) + par_impar(x)
}
console.log(prifipar(16))
console.log(prifipar(5))
console.log(prifipar(2))
console.log(prifipar(1))