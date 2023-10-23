/*
 * Crea un programa que sea capaz de generar e imprimir todas las 
 * permutaciones disponibles formadas por las letras de una palabra.
 * - Las palabras generadas no tienen por qué existir.
 * - Deben usarse todas las letras en cada permutación.
 * - Ejemplo: sol, slo, ols, osl, los, lso 
 */

const permutar = (word) =>{
    
    if (word.length===1){
        return [word]
    }
    let permutations = []

    for(let i=0; i<word.length;i++){
        let char = word[i]
        let withoutChar = word.slice(0,i) + word.slice(i+1,word.length)
        for( let permutation of permutar(withoutChar)) {
            permutations.push(char+permutation)
        }
}
    return permutations
}

console.log(permutar('soles').length)
const setChar = new Set(permutar('soles'))
console.log('Sin repiticiones: '+setChar.size)