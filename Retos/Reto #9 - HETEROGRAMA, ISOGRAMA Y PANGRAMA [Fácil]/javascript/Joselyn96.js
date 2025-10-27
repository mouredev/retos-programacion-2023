
/*
 * Crea 3 funciones, cada una encargada de detectar si una cadena de
 * texto es un heterograma, un isograma o un pangrama.
 * - Debes buscar la definición de cada uno de estos términos.
 */

let word = "brickfade";

function isHeterogram(text) {
    //tenemos que eliminar los espacios en blanco
    text = text.toLowerCase().replace(/[^a-z]/g, '');
    for (let i = 0; i < text.length; i++) {
        for (let j = i + 1; j < text.length; j++) {
            if (text[i] === text[j]) {
                return false;
            }
        }
    }
    return true;
}


function isIsogram(text) {
    //tenemos que eliminar los espacios en blanco porque for y set lo cuentan
    text = text.toLowerCase().replace(/[^a-z]/g, '');
    let referenceCount = 1;
    const lettersSet = new Set();
    for (let i = 0; i < text.length; i++) {
        if (lettersSet.has(text[i])) {
            continue;
        } else {
            lettersSet.add(text[i]);
        }
        let repeatedCount = 1;
        for (let j = i + 1; j < text.length; j++) {
            if (text[i] === text[j]) {
                if (i === 0) {
                    referenceCount++;
                } else {
                    repeatedCount++;
                }
            }
        }
        if (i > 0 && referenceCount != repeatedCount) {
            return false;
        }
    }
    return true;
}

function isPangram(text) {
    let alphabet = 'abcdefghijklmnopqrstuvwxyz';
    let alphabet_size = alphabet.length;
    if (text.length >= alphabet_size) {
        const alphabet_set = new Set((text.toLowerCase()).replace(/[^a-z]/g, ''));
        // console.log(alphabet_set);
        // console.log(alphabet_set.size);
        if (alphabet_set.size === alphabet_size) {
            return true;
        }
    }
    return false;
}


console.log(isHeterogram(word) ? "es un heterograma" : "no es heterograma");
console.log(isIsogram(word) ? "es un isograma" : "no es isograma");
console.log(isPangram(word) ? "es un pangrama" : "no es pangrama");



