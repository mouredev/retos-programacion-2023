/*
 * Crea las funciones capaces de transformar colores HEX
 * a RGB y viceversa.
 * Ejemplos:
 * RGB a HEX: r: 0, g: 0, b: 0 -> #000000
 * HEX a RGB: hex: #000000 -> (r: 0, g: 0, b: 0)
 */



function isValidHex(color: string) {
    return /^#[A-Fa-f0-9]{6}$|^#[A-Fa-f0-9]{3}$/.test(color);
}
function isValidRgbColor(color: string) {
    return /^\((\s?)r:(\s?)(\d{1,3}),(\s?)g:(\s?)(\d{1,3}),(\s?)b:(\s?)(\d{1,3})\)/.test(color);
}

function convertHexToRgb(hexColor: string): string {
    const rHex =
         hexColor.length === 7 ? hexColor.substring(1, 3) : hexColor[1];
    const gHex =
         hexColor.length === 7 ? hexColor.substring(3, 5) : hexColor[2];
    const bHex =
         hexColor.length === 7 ? hexColor.substring(5) : hexColor[3];

    return `(r: ${Number.parseInt(rHex, 16)}, g: ${Number.parseInt(gHex,16)}, b: ${Number.parseInt(bHex, 16)})`;
}

function convertRgbToHex(rgbColor:string):string {
   
   const rValueIndex =  rgbColor.indexOf('r:')+2
   const gValueIndex = rgbColor.indexOf('g:')+2
   const bValueIndex = rgbColor.indexOf('b:')+2
    
   const red = rgbColor.substring(rValueIndex, rgbColor.indexOf(',', rValueIndex ))
   const green = rgbColor.substring(gValueIndex, rgbColor.indexOf(',', gValueIndex ))
   const blue = rgbColor.substring(bValueIndex, rgbColor.indexOf(')'))
      
   
   return `#${Number(red).toString(16)}${Number(green).toString(16)}${Number(blue).toString(16)}`
}


const convertColorFormat = (color: string): string => {
    if (!isValidHex(color) && !isValidRgbColor(color)) throw new Error('Invalid color format');
       return isValidHex(color) ? convertHexToRgb(color) :  convertRgbToHex(color)
    
};


console.log(convertColorFormat('(r: 85, g: 105, b: 108)'))