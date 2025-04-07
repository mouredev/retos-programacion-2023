/*
 * Crea una función que reciba un número decimal y lo trasforme a Octal
 * y Hexadecimal.
 * - No está permitido usar funciones propias del lenguaje de programación que
 * realicen esas operaciones directamente.
 */

function fnBaseOctal(numero: number) {
    let numOctal = ""
    let numTemp = numero
    do {
        const cociente = ~~(numTemp / 8)  //Retorna solo el numero entero de una división, tambien se puede usar  = Math.floor(numTemp / 8)
        const residuo = numTemp % 8
        numTemp = cociente
        console.log("cociente: " + numTemp + ", residuo: " + residuo)
        numOctal = residuo + numOctal
    } while(numTemp !== 0)
    console.log(numOctal)
    return numOctal
}

function fnBaseHexadecimal(numero: number) {
    const mapHexa: Map<number, string> = new Map([[10,"A"],[11,"B"],[12,"C"],[13,"D"],[14,"E"],[15,"F"]])
    let numHexa: string = ""
    let numTemp = numero
    do {
        const cociente = ~~(numTemp / 16) //Retorna solo el numero entero de una división, tambien se puede usar  = Math.floor(numTemp / 8)
        const residuo = numTemp % 16
        numTemp = cociente
        console.log("cociente: " + numTemp + ", residuo: " + residuo)
        numHexa = (residuo >= 10 ? mapHexa.get(residuo) : residuo ) + numHexa
    } while(numTemp !== 0)
    console.log(numHexa)
    return numHexa
}

function fnBaseHexadecimalv2(numero: number) {
    const arrHexa = "0123456789ABCDEF"
    let numHexa: string = ""
    let numTemp = numero
    do {
        const cociente = ~~(numTemp / 16) //Retorna solo el numero entero de una división, tambien se puede usar  = Math.floor(numTemp / 8)
        const residuo = numTemp % 16
        numTemp = cociente
        console.log("cociente: " + numTemp + ", residuo: " + residuo)
        numHexa = (arrHexa[residuo]) + numHexa
    } while(numTemp !== 0)
    console.log(numHexa)
    return numHexa
}

let numero_r14: number = 920

fnBaseOctal(numero_r14)
console.log("\n")
fnBaseHexadecimal(numero_r14)
console.log("\n")
fnBaseHexadecimalv2(numero_r14)
console.log("\n")