const texto = "Érase una vez una Vtuber muy kawaii cariñosa y graciosa. Le gustaba hacer chistes de gatetes y se partía el ojal de una manera impresionante. Ponía vocecillas para alegrar a sus fans."

let numPalabras = 0;
let longMediaPalabras = 0;
let numOraciones = 0;
let palabraMasLarga = "";

texto.split(' ').forEach((palabra) => { 
    // Se cuentan las oraciones que terminan con un punto.
    if (palabra.includes(".")) {
        numOraciones++;
    }

    // Si la palabra actual tiene un punto o una coma, se elimina de la palabra
    // actual para las siguientes comprobaciones.
    if (palabra.includes(".") || palabra.includes(",")) {
        palabra = palabra.substring(0, palabra.length - 1)
    }

    // Se obtiene la palabra más larga (con mayor longitud)
    if (palabra.length > palabraMasLarga.length) {
        palabraMasLarga = palabra;
    }

    // Se obtiene la longitud media de las palabras
    if ((palabra.length / texto.length) > longMediaPalabras) {
        longMediaPalabras = palabra.length;
    }
    numPalabras++;
    
    console.log(palabra);
});

console.log(`Número de palabras: ${numPalabras}`);
console.log(`Longitud media de palabras: ${longMediaPalabras}`);
console.log(`Número de oraciones: ${numOraciones}`);
console.log(`Palabra más larga: ${palabraMasLarga}`);
