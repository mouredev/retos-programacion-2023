
/*
 * Crea las funciones capaces de transformar colores HEX
 * a RGB y viceversa.
 * Ejemplos:
 * RGB a HEX: r: 0, g: 0, b: 0 -> #000000
 * HEX a RGB: hex: #000000 -> (r: 0, g: 0, b: 0)
 */

const HexToRgb = (hex) =>{
    
    const array = hex.slice('')
    let arrayCopy = new Array(array.length)
    let flag = false

    for(let i=0; i<array.length;i++){

        switch(array[i]){
            case '0': case '1': case '2': case '3': case '4': case '5': case '6': case '7': case '8': case '9':
                arrayCopy[i] = parseInt(array[i])
                break
            case 'A':
                arrayCopy[i] = 10
                break
            case 'B':
                arrayCopy[i] = 11
                break
            case 'C':
                arrayCopy[i] = 12
                break
            case 'D':
                arrayCopy[i] = 13
                break
            case 'E':
                arrayCopy[i] = 14
                break
            case 'F':
                arrayCopy[i] = 15
                break
            default:
                flag = true
                break
        }
    }

    const R =arrayCopy.slice(0,2)
    const G = arrayCopy.slice(2,4)
    const B = arrayCopy.slice(4,6)

    // let suma = 100*(centena[0]*16 + centena[1]*1) + 10*(centena[0]*16 + centena[1]*1) + (centena[0]*16 + centena[1]*1)
    const RGB = new Array(3)

    RGB[0] = 16*R[0]+R[1]
    RGB[1] = 16*G[0]+G[1]
    RGB[2] = 16*B[0]+B[1]

    if(flag){
        return 'El valor hexadecimal no es correcto, pruebe nuevamente'
    }
    return RGB
}
const RgbToHex = (r,g,b) =>{//255,255,255
    let all = [r,g,b]
    let RGB = []
    for(let i=0;i<all.length;i++){
        let resto
        let resultado = all[i]
        if(all[i]>255) return 'No se puede agregar valores mayores a 255'
        let RGBLocal = []

        while(resto!==0){
            resto = resultado % 16
            resultado = Math.floor(resultado/16)
            if(resto !== 0) RGBLocal.push(resto)
        }
        RGB.push(RGBLocal.reverse())
    }
    
    for(let i=0; i<RGB.length;i++){
    
        for(let j=0;j<2;j++){

            switch(RGB[i][j]){
                case 10:
                    RGB[i][j] = 'A'
                    break
                case 11:
                    RGB[i][j] = 'B'
                    break
                case 12:
                    RGB[i][j] = 'C'
                    break
                case 13:
                    RGB[i][j] = 'D'
                    break
                case 14:
                    RGB[i][j] = 'E'
                    break
                case 15:
                    RGB[i][j] = 'F'
                    break
                default:
                
            }
        }
    }
    const newRGB = '#'+RGB.join().replace(/,/g, '')
    return newRGB
    
}
console.log(HexToRgb('000000'))
console.log(HexToRgb('FFFFFF'))
console.log(HexToRgb('FFAA22'))
console.log(HexToRgb('1122HH'))//valor no valido

console.log(RgbToHex(255,100,50))
console.log(RgbToHex(255,150,200))
console.log(RgbToHex(300,150,200))//valor no valido