/*
 * Enunciado
 * Crea 3 funciones, cada una encargada de detectar si una cadena de
 * texto es un heterograma, un isograma o un pangrama.
 * - Debes buscar la definición de cada uno de estos términos.
 */

function heterograma(cadena) {
    // Heterograma: es una palabra que no tiene letras repetidas.
    let string = cadena.toLowerCase().split("")
    string = string.map(letra => letra.replace(" ", ""))
    string = [...new Set(string)]
    return string.length == cadena.length
}

function isograma(cadena) {
    // Isograma: es una palabra o frase en la que cada letra aparece el mismo número de veces
    let string = cadena.toLowerCase().split("")
    let letras_usadas = {}
    for (let i = 0; i < string.length; i++) {
        if (string[i] != " ") {
            if (letras_usadas[string[i]]) letras_usadas[string[i]] += 1
            else letras_usadas[string[i]] = 1
        }
    }
    let valor_maximo = Math.max(...Object.values(letras_usadas))
    return Object.values(letras_usadas).every(valor => valor == valor_maximo)
}

function pangrama(cadena) {
    // Pangrama: es una frase que contiene todas las letras del abecedario.
    let abecedario = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "ñ", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]
    let string = cadena.toLowerCase().split("")
    string = string.map(letra => letra.replace(" ", ""))
    string = string.filter(letra => abecedario.includes(letra))
    string = [...new Set(string)]
    return string.length == abecedario.length
}

console.log(heterograma("hola")); // true
console.log(isograma("hoaa")); // false
console.log(heterograma("aaaaaaaaaa")); // false
console.log(isograma("hola")); // true
console.log(pangrama("Abcde fghijkl mnñopq rstuvwx yz")); // true
console.log(pangrama("cde fghijkl mnñopq rstuvwx yz")); // false
