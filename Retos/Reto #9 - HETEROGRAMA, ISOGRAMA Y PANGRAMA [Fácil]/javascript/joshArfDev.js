
// Heterograma: es una palabra que no tiene letras repetidas.
const heterograma = ( string ) => {
  
    let stringInput = string.toLowerCase().split('')
    stringInput = stringInput.map( char => char.replace(' ', '') )
    stringInput = [...new Set(string)] //copying our "string" with ...

    return stringInput.length == string.length
}

// Isograma: es una palabra o frase en la que cada letra aparece el mismo número de veces
const isograma = ( string ) => {

    let size;

    string  = string.toLowerCase()

    for( let char of string ) {
        let regex = new RegExp(`${char}`, 'g')
        let actualSize = string.match(regex).length

        if( size && size !== actualSize ) {
            return false
        }

        size = actualSize
    }

    return true
}

// Pangrama: es una frase que contiene todas las letras del abecedario.

const pangrama = ( string ) => {

    const abc = [ "a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "ñ", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z" ]
    let stringInput = string.toLowerCase().split('')
    stringInput = stringInput.map( char => char.replace(' ', '') )
    stringInput = [...new Set(string)] //copying our "string" with ...

    return stringInput.length == abc.length

}

console.log(heterograma('ahjkl'))
console.log(isograma('aahhjjkkll'))
console.log(pangrama('abcdefghijklmnñopqrstuvwxy'))
