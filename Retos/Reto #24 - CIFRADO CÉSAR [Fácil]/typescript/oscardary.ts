/*
 * Crea un programa que realize el cifrado César de un texto y lo imprima.
 * También debe ser capaz de descifrarlo cuando así se lo indiquemos.
 *
 * Te recomiendo que busques información para conocer en profundidad cómo
 * realizar el cifrado. Esto también forma parte del reto.
 */

const abc = "ABCDEFGHIJKLMNÑOPQRSTUVWXYZ"

function cifradoCesar(texto: string): string{
    const texto_temp = texto.toUpperCase().split("")
    let cifrado = ""
    for (const char of texto_temp) {
        const index1 = abc.indexOf(char)
        const index2 = (index1 + 3) < abc.length ? (index1 + 3) : (index1 + 3 - abc.length)
        cifrado = cifrado + (abc[index2] || char)
    }
    return cifrado
}

function cifradoCesarV2(texto: string): string{
    return texto.toUpperCase().split("")
        .map(char => {
            const index1 = abc.indexOf(char)
            if(index1 === -1) return char
            return abc[(index1 + 3) % abc.length]
        })
        .join("")
}

function descifradoCesar(texto: string): string{
    return texto.toUpperCase().split("")
        .map(char => {
            const index1 = abc.indexOf(char)
            if(index1 === -1) return char
            const index2 = (index1 + abc.length - 3) % abc.length
            return abc[index2]
        })
        .join("")
}

const miTexto = "OSCAR.XYZ"
console.log(miTexto)
console.log(cifradoCesar(miTexto))
console.log(cifradoCesarV2(miTexto))
console.log(descifradoCesar("RVFDU.ABC"))