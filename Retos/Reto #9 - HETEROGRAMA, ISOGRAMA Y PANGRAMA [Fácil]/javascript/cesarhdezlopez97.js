// string que no tiene ninguna letra repetida
function isHeterograma(texto) {
    const lettersTexto = texto.split('');
    var comprobador = []
    for (i in lettersTexto) {
        if (comprobador.includes(lettersTexto[i])) {
            return false
        }
        comprobador.push(lettersTexto[i])
    }
    return true
}

// texto que emplea todas las letras posibles del alfabeto de una lengua
function isPangrama(texto) {
    const alphabet = 'abcdefghijklmnopqrstuvwxyz'
    const lettersAlphabet = [...alphabet];
    const lettersTexto = texto.split('');
    for (i in lettersAlphabet) {
        if (!lettersTexto.includes(lettersAlphabet[i])) {
            return false
        }
    }
    return true
}

// string que todas sus letras se repiten el mismo numero de veces
function isIstogram(texto) {
    const lettersTexto = texto.split('');
    var dict = {}

    for (i in lettersTexto) {
        if (!(lettersTexto[i] in dict)) {
            dict[lettersTexto[i]] = 1
        } else {
            dict[lettersTexto[i]] += 1
        }
    }
    var comprobador = '0'
    for (var key in dict) {
        if (comprobador == '0' || comprobador == String(dict[key])) {
            comprobador = String(dict[key])
        } else {
            return false
        }
    }
    return true
}

// console.log(isHeterograma('cesar')) // true
// console.log(isHeterograma('papa')) // false
// console.log(isIstogram('cesare')) // false
// console.log(isIstogram('papa')) // true
// console.log(isPangrama('abcdefghijklmnopqrstuvwxyz')) // true
// console.log(isPangrama('cesar')) // false
