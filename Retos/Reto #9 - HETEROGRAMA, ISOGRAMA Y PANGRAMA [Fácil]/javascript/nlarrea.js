/*
 * Crea 3 funciones, cada una encargada de detectar si una cadena de
 * texto es un heterograma, un isograma o un pangrama.
 * - Debes buscar la definición de cada uno de estos términos.
 */

function checkHeterogram(text){
    let textSet = new Set(text.toLowerCase());
    
    return textSet.size === text.length;
}


function checkIsogram(text){
    let prevNum;
    
    text = text.toLowerCase();

    for(let letter of text){
        let regex = new RegExp(`${letter}`, "g");
        let actualNum = text.match(regex).length;
        
        if(prevNum && prevNum !== actualNum){
            return false;
        }

        prevNum = actualNum;
    }

    return true;
}


function checkPangram(text){
    let isPangram = true;
    const alphabet = "abcdefghijklmnopqrtsuvwxyz";

    text = text.toLowerCase();
    text = text.normalize('NFD').replace(/[\u0300-\u036f]/g, '');
    text = text.replace(/[\d\W\s]/g, '');

    alphabet.split("").forEach(letter => {
        if(!text.includes(letter)) isPangram = false;
    });

    return isPangram;
}


// heterograma = texto que no contiene letras repetidas
console.log(checkHeterogram("Hola"));                           // true
console.log(checkHeterogram("Hello"));                          // false
console.log(checkHeterogram("abcdefghijklmnopqrstuvwxyz"));     // true


// isograma = texto donde cada letra aparece el mismo número de veces
console.log(checkIsogram("hola"));          	// true -> todas se repiten 1 vez
console.log(checkIsogram("Hhoollaa"));      	// true -> se repiten 2 veces
console.log(checkIsogram("Hholla"));        	// false
console.log()


// pangrama = texto que usa todas las letras del alfabeto de un idioma determinado
// panagram examples
const str1 = "the quick brown fox jumps over the lazy dog";
const str2 = "When zombies arrive quickly fax judge pat";
const str3 = "Sixty zippers were quickly picked from the woven jute bag.";
const str4 = "El veloz murciélago hindú comía feliz cardillo y kiwi, la cigüeña tocaba el saxofón detrás del palenque de paja";

console.log(checkPangram(str1));        // true
console.log(checkPangram(str2));        // true
console.log(checkPangram(str3));        // true
console.log(checkPangram(str4));        // true
console.log(checkPangram("This is not a pangram"));             // false
console.log(checkPangram("abcdefghijklmnopqrstuvwxyz"));        // true
console.log(checkPangram("abcdefghijklmnñopqrstuvwxyz"));       // true