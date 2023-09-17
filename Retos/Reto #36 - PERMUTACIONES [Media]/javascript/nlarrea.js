/*
 * Crea un programa que sea capaz de generar e imprimir todas las 
 * permutaciones disponibles formadas por las letras de una palabra.
 * - Las palabras generadas no tienen por qué existir.
 * - Deben usarse todas las letras en cada permutación.
 * - Ejemplo: sol, slo, ols, osl, los, lso 
*/


function getPermutationQuantity(word){
    // Formula to get the number of permutations:
    //   factorial(n) / multiplication of the factorial of how many times is repeated each char
    
    const factorial = number => {
        if (number === 1) return 1;
        return number * factorial(number-1);
    }

    // Get how many times is repeated each char (without repetition)
    const charsQtyObj = {}
    for (let char of word) {
        if (!charsQtyObj[char]) {
            charsQtyObj[char] = [...word].filter(c => c === char).length;
        }
    }

    const charsQty = Object.entries(charsQtyObj);
    
    const n = word.length;
    const factOfCharsQty = charsQty.reduce((total, current) => total * factorial(current[1]), 1);

    return parseInt(factorial(n) / factOfCharsQty);
}


function wordPermutations(word){
    // Get the quantity of permutations
    const permutationsQty = getPermutationQuantity(word);

    // Generate the permutations
    const permutations = new Set();
    while (permutations.size < permutationsQty) {
        let originalWord = [...word];
        let newWord = '';

        for (let _ in word) {
            const randomIndex = Math.floor(Math.random() * originalWord.length);
            newWord += originalWord.splice(randomIndex, 1);
        }
        
        if (!permutations.has(newWord)) {
            permutations.add(newWord);
        }
    }

    // Print the results
    console.log(`\nPermutaciones de '${word}':`);
    [...permutations].forEach((permutation, index) => {
        console.log(`${index + 1}. ${permutation}`);
    });
}


wordPermutations("sol");