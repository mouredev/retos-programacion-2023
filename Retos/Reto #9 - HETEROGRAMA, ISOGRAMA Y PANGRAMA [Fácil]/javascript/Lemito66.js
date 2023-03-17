/*

 * Crea 3 funciones, cada una encargada de detectar si una cadena de
 * texto es un isHeterogram, un isograma o un pangrama.
 * - Debes buscar la definición de cada uno de estos términos.

*/

const replaceAccents = (word) => {
    toReplace = {
        'á': 'a',
        'é': 'e',
        'í': 'i',
        'ó': 'o',
        'ú': 'u',
    }
    for (const words in toReplace) {
        word = word.replace(words, toReplace[words])
    }
    return word.toLowerCase()
}


// Un heterograma es una palabra o frase que no contiene ninguna letra repetida.
const isHeterogram = (word) => {
    word = replaceAccents(word).toLowerCase();
    objectOfLetters = {}
    response = ""
    for (let index = 0; index < word.length; index++) {
        if (word[index] in objectOfLetters) {
            response += "No es un heterograma"
            return response
        }
        else{
            objectOfLetters[word[index]] = 1
            
        }
        
    }
    response += "Es un heterograma"
    return response
}

const isIsogram = (word) => {
    word = replaceAccents(word).toLowerCase();
    objectOfLetters = {}
    response = ""
    for (let index = 0; index < word.length; index++) {
        if (word[index] in objectOfLetters) {
            objectOfLetters[word[index]] += 1
        }
        else{
            objectOfLetters[word[index]] = 1
        }
    }
    for (const letter in objectOfLetters) {
        if (objectOfLetters[letter] > 1) {
            response += "No es un isograma"
            return response
        }
    }
    response += "Es un isograma"
    return response
}



console.log(isHeterogram("Víctima"))
console.log(isHeterogram("Wágner"))
console.log(isHeterogram("Queso"))
console.log(isHeterogram("Néctar"))
console.log(isHeterogram("Lánguido"))