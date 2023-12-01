/*
 * Crea las funciones capaces de transformar colores HEX
 * a RGB y viceversa.
 * Ejemplos:
 * RGB a HEX: r: 0, g: 0, b: 0 -> #000000
 * HEX a RGB: hex: #000000 -> (r: 0, g: 0, b: 0)
 */


function hexToRgb(hex) {
    const num = hex.slice(1)
    const r = num.slice(0,2)
    const g = num.slice(2,4)
    const b = num.slice(4,6)
    return {r: fromHexaToDecimal(r), g: fromHexaToDecimal(g), b: fromHexaToDecimal(b)}
}

function rgbToHex(rgb) {
    const {r, g, b} = rgb
    return `#${fromDecimalToHexa(r)}${fromDecimalToHexa(g)}${fromDecimalToHexa(b)}`
}


function fromDecimalToHexa (decimalNumber){
    const numToletters = {
        10: 'A',
        11: 'B', 
        12: 'C',
        13: 'D',
        14: 'E',
        15: 'F'
    }
    let modules = []
    let div = decimalNumber
    while (div>16 ){        
        const mod = Math.floor(div)% 16
        modules.push(numToletters[mod]?? mod)
        div = Math.floor(div)/16
    }
    div = Math.floor(div)
    modules.push(numToletters[div]?? div)
    const res = modules.reverse().join('')
    return res    
}

function fromHexaToDecimal(hexaNumber){
    const lettersToNum = {
        'A':10,
        'B':11, 
        'C':12,
        'D':13,
        'E':14,
        'F':15
    }
    const num = hexaNumber.toUpperCase().split('')
    let res = lettersToNum[num[0]] ? lettersToNum[num[0]]*16 : Number(num[0])*16
    res += lettersToNum[num[1]] ?? Number(num[1])
    return res
}

console.log(rgbToHex({r: 255, g: 100, b: 22})) // Solution: #FF6416
console.log(hexToRgb('#ff6416')) // Solution: {r: 255, g: 100, b: 22}

console.log(rgbToHex({r: 142, g: 40, b: 176})) // Solution: #8E28B0
console.log(hexToRgb('#8E28B0')) // Solution: {r: 142, g: 40, b: 176}
