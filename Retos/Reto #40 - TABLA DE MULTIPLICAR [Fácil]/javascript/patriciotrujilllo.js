/*
 * Crea un programa que sea capaz de solicitarte un número y se
 * encargue de imprimir su tabla de multiplicar entre el 1 y el 10.
 * - Debe visualizarse qué operación se realiza y su resultado.
 *   Ej: 1 x 1 = 1
 *       1 x 2 = 2
 *       1 x 3 = 3
 *       ... 
 */

const multi = (a) =>{
    let result = []
    for(let i = 0; i < 10 ; i++){
        result.push(`${a} x ${i+1} = ${a*(i+1)}`)
    }
    return result
}
console.log(multi(9))