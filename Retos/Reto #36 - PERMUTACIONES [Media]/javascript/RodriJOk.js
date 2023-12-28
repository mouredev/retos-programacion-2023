// ## Enunciado
/*
 * Crea un programa que sea capaz de generar e imprimir todas las 
 * permutaciones disponibles formadas por las letras de una palabra.
 * - Las palabras generadas no tienen por qué existir.
 * - Deben usarse todas las letras en cada permutación.
 * - Ejemplo: sol, slo, ols, osl, los, lso 
 */

function generatePermutations(word) {
    const result = [];
  
    function permute(current, remaining) {
      if (remaining.length === 0) {
        result.push(current);
        return;
      }
  
      for (let i = 0; i < remaining.length; i++) {
        const nextChar = remaining[i];
        const rest = remaining.slice(0, i) + remaining.slice(i + 1);
        permute(current + nextChar, rest);
      }
    }
  
    permute('', word);
    return [...new Set(result)];
  }
  
  console.log(generatePermutations("sol"))
  console.log(generatePermutations("hola"))
  console.log(generatePermutations("devs"))
  console.log(generatePermutations("rodri"))
  