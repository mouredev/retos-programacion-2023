/*
 * Crea una función que calcule el número de la columna de una hoja de Excel
 * teniendo en cuenta su nombre.
 * - Las columnas se designan por letras de la "A" a la "Z" de forma infinita.
 * - Ejemplos: A = 1, Z = 26, AA = 27, CA = 79.
 */

function columna_excel(letras_columna){

    const diccionario= "ABCDEFGHIJKLMN0PQRSTUVWXYZ"
    let aux= letras_columna.length
    let numero= 0

    for(let i= 0; i< letras_columna.length; i++){
        let indice= diccionario.indexOf(letras_columna[i])+1
        if(i < (letras_columna.length-1)){
            numero= numero + indice*26**(aux-1)
        }
        else{
            numero= numero + indice
        }
        aux--
    }
    return numero
}

console.log(columna_excel("A"))
console.log(columna_excel("Z"))
console.log(columna_excel("AA"))
console.log(columna_excel("CA"))
console.log(columna_excel("XFD")) 