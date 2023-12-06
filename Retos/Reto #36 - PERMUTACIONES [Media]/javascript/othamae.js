/*
 * Crea un programa que sea capaz de generar e imprimir todas las 
 * permutaciones disponibles formadas por las letras de una palabra.
 * - Las palabras generadas no tienen por qué existir.
 * - Deben usarse todas las letras en cada permutación.
 * - Ejemplo: sol, slo, ols, osl, los, lso 
 */

function permutations(word){
    let result = []
    const swaps = (prefix, suffix)=>{
        suffix.length === 0 && result.push(prefix)
        for (let i=0; i<suffix.length; i++){
            swaps(prefix+suffix[i], suffix.slice(0, i)+suffix.slice(i+1))
        }    
    }
    swaps('', word)
    return result
}


console.log(permutations('sol')) // [ 'sol', 'slo', 'osl', 'ols', 'lso', 'los' ]
console.log(permutations('pan')) // [ 'pan', 'pna', 'apn', 'anp', 'npa', 'nap' ]
console.log(permutations('hola')) /* [
                                     'hola', 'hoal', 'hloa',
                                     'hlao', 'haol', 'halo',
                                     'ohla', 'ohal', 'olha',
                                     'olah', 'oahl', 'oalh',
                                     'lhoa', 'lhao', 'loha',
                                     'loah', 'laho', 'laoh',
                                     'ahol', 'ahlo', 'aohl',
                                     'aolh', 'alho', 'aloh'
                                     ]
                                    */