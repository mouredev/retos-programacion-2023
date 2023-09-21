/*
 * Crea las funciones capaces de transformar colores HEX
 * a RGB y viceversa.
 * Ejemplos:
 * RGB a HEX: r: 0, g: 0, b: 0 -> #000000
 * HEX a RGB: hex: #000000 -> (r: 0, g: 0, b: 0)
 */

/*
    0123456789ABCDEF
 */
const diccionario = "0123456789ABCDEF"

function hex_to_rgb(color){
    color = color.split("#")[1]
    let array = [color.slice(0,2), color.slice(2,4), color.slice(4,6)]
    let rgb = []

    for(let i=0; i<array.length; i++){
        let num_rgb = diccionario.indexOf(array[i][0])*16 + diccionario.indexOf(array[i][1])
        rgb.push(num_rgb)
    }
    return "(r: "+rgb[0]+", g: "+rgb[1]+", b: "+rgb[2]+")"
}

function rgb_to_hex(color){
    color = color.split(",")
    let array = [color[0].split(":"), color[1].split(":"), color[2].split(":")]
    let array2 = [array[0][1].trim(), array[1][1].trim(), array[1][1].trim()]
    let hex = "#"

    for(let i=0; i < array2.length; i++){
        let resto = 17
        let cociente = 0
        while (resto > 16){
            if(i == 0){
                cociente = parseInt(array2[i]) / 16
                resto = parseInt(array2[i]) % 16
            }
            else{
                cociente = cociente / 16
                resto = cociente % 16
            }
        }
        hex += cociente+""+resto
    }
    return hex
}