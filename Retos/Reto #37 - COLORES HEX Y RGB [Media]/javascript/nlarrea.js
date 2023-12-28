/*
 * Crea las funciones capaces de transformar colores HEX
 * a RGB y viceversa.
 * Ejemplos:
 * RGB a HEX: r: 0, g: 0, b: 0 -> #000000
 * HEX a RGB: hex: #000000 -> (r: 0, g: 0, b: 0)
 */

function fromHexaToRGB(color) {
    // Check if given color is in hexadecimal
    if (
        !typeof color === 'string' ||
        !color.includes('#') ||
        (color.length !== 4 && color.length !== 7)
    ) {
        return 'This is not in a correct hexadecimal format.';
    } else if (color.toLowerCase().match(/[^#0-9a-f]/g)) {
        return 'Hexadecimal only contains digits from 0-9 and A-F.';
    }

    // Get the RGB value
    const hexaToInt = (hexa) => parseInt(hexa, 16);
    const [r, g, b] = color.slice(1).match(/.{2}/g).map(item => hexaToInt(item));
    
    return {r, g, b};
}


function fromRGBToHexa({ r, g, b }) {
    // Check if given color is RGB
    const inRange = (number) => number >= 0 && number <= 255;

    if ((!r && r !== 0) || (!g && g !== 0) || (!b && b !== 0)) {
        return 'You must enter values for all RGB colors.';
    } else if (!inRange(r) || !inRange(g) || !inRange(b)) {
        return 'Numbers must be between 0-255.';
    }

    // Get the hexadecimal value
    const intToHexa = (integer) => {
        if (integer.toString(16).length < 2) {
            return '0' + integer.toString(16);
        } else {
            return integer.toString(16);
        }
    }

    return `#${intToHexa(r)}${intToHexa(g)}${intToHexa(b)}`;
}


console.log(fromHexaToRGB('#000000'));                  // { r: 0, g: 0, b: 0 }
console.log(fromHexaToRGB('#ffd486'));                  // { r: 255, g: 212, b: 134 }
console.log(fromRGBToHexa({r: 0, g: 0, b: 0}));         // #000000
console.log(fromRGBToHexa({r: 110, g: 235, b: 131}));   // #6eeb83