/**
 * Generador de cadenas de carácteres
 * @returns objeto con tres cadenas de carácteres: letras, digitos y símbolos
 */
const getChars = () => {
    const letters = Array.from({ length: 26 }, (_, i) => String.fromCharCode(i + 65)).join('')
    const digits = Array.from({ length: 10 }, (_, i) => i).join("")
    const symbols = `!"#$%&'()*+,-./:;<=>?@[\\]^_\`{|}~`
    return {
        letters,
        digits,
        symbols
    }
}
/**
 * Concatena y devuelve una serie de carácteres de acuerdo a los parametros
 * @param {Boolean} up Permite mayúsculas
 * @param {Boolean} dig Permite digitos del 0 al 9
 * @param {Boolean} sym Permite símbolos
 * @returns conjunto de carácteres
 */
const validChars = (up, dig, sym) => {
    const { letters, digits, symbols } = getChars()
    const chars =
        letters.toLowerCase() +
        (up ? letters : '') +
        (dig ? digits : '') +
        (sym ? symbols : '')
    return chars
}
/**
 * Devuelve un elemento aleatorio de un array
 * @param {Array} Array array desde donde se toma el elemento 
 * @returns elemento del arreglo
 */
const randomInArray = (Array) => {
    const randomIndex = Math.floor(Math.random() * Array.length)
    return Array[randomIndex]
}
/**
 * Genera una contraseña
 * @param {*} len Tamaño de contraseña (8-16)
 * @param {*} options opciones para la generación
 * @returns contraseña
 */
const getPassword = (len = 8, { up = false, dig = false, sym = false }) => {
    if (len < 8 || len > 16) {
        console.log('solo se permiten longitudes de 8 a 16 carácteres')
    }
    len = len > 16 ? 16 : len
    len = len < 8 ? 8 : len
    const chars = validChars(up, dig, sym)
    const password = Array.from({ length: len }, () => randomInArray(chars)).join('')
    return password
}

console.log(getPassword(16, { up: 1, dig: 1, sym: 1 }))