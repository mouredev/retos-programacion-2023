/*
 * Crea 3 funciones, cada una encargada de detectar si una cadena de
 * texto es un heterograma, un isograma o un pangrama.
 * - Debes buscar la definición de cada uno de estos términos.
 */

function isHeterograma(word) {
    let arrWords = []
    word.split('').map(e => {
        if (!arrWords.includes(e)) {
            arrWords.push(e)
        }
    })
    return arrWords.length === word.length
}

function isIsograma(word) {
    let objWords = {}
    word.split('').map(e => {
        if (objWords[e]) {
            objWords[e]++
        } else {
            objWords[e] = 1
        }
    })
    return Object.values(objWords).every(e => e % 2 === 0 || e === 1)
}

function isPangrama(word) {
    const alphabet = 'abcdefghijklmnñopqrstuvwxyz'
    let arrWords = []
    word.split('').map(e => {
        if (!arrWords.includes(e.toLowerCase()) && alphabet.split('').includes(e.toLowerCase())) {
            arrWords.push(e.toLowerCase())
        }
    })
    return arrWords.length === 27
}

console.log(isHeterograma('luteranismo'))
console.log(isIsograma('papelera'))
console.log(isPangrama('Benjamín pidió una bebida de kiwi y fresa. Noé, sin vergüenza, la más exquisita champaña del menú.'))