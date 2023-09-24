/*
 * Crea las funciones capaces de transformar colores HEX
 * a RGB y viceversa.
 * Ejemplos:
 * RGB a HEX: r: 0, g: 0, b: 0 -> #000000
 * HEX a RGB: hex: #000000 -> (r: 0, g: 0, b: 0)
 */

function rgbToHex(r, g, b) {
    let rgbValues = [r, g, b]
    let hex = "#"

    rgbValues.forEach(element => {

        hex += parseInt((element / 16)).toString(16) + (element % 16).toString(16)        
    })

    return `r: ${r}, g: ${g}, b:${b} -> ${hex.toUpperCase()}`
}

function hexToRgb(hex) {
    let rgb = []

        for(let i = 1; i < hex.length-1; i+=2) {  
            
            rgb.push(((parseInt(hex.slice(i, i+1), 16)*16) + parseInt(hex.slice(i+1,i+2),16)))
        }

    return `${hex} -> (r:  ${rgb[0]}, g: ${rgb[1]}, b: ${rgb[2]})`
}
    
    
console.log(rgbToHex(23,150,228))
console.log(hexToRgb("#1796E4"))