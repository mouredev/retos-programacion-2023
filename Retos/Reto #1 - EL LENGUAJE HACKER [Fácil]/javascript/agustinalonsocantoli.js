/*
 * Escribe un programa que reciba un texto y transforme lenguaje natural a
 * "lenguaje hacker" (conocido realmente como "leet" o "1337"). Este lenguaje
 *  se caracteriza por sustituir caracteres alfanuméricos.
 * - Utiliza esta tabla (https://www.gamehouse.com/blog/leet-speak-cheat-sheet/) 
 *   con el alfabeto y los números en "leet".
 *   (Usa la primera opción de cada transformación. Por ejemplo "4" para la "a")
 */

function transformarLenguaje(texto = "Reto de programacion, lenguaje hacker") {
  
    texto = texto.replace(/a/gi, '4');
    texto = texto.replace(/b/gi, 'ß');
    texto = texto.replace(/c/gi, '©');
    texto = texto.replace(/d/gi, 'cl');
    texto = texto.replace(/e/gi, '€');
    texto = texto.replace(/f/gi, 'ƒ');
    texto = texto.replace(/g/gi, '6');
    texto = texto.replace(/h/gi, '#');
    texto = texto.replace(/i/gi, '!');
    texto = texto.replace(/j/gi, ']');
    texto = texto.replace(/k/gi, '|c');
    texto = texto.replace(/l/gi, '£');
    texto = texto.replace(/m/gi, 'nn');
    texto = texto.replace(/n/gi, 'И');
    texto = texto.replace(/o/gi, '0');
    texto = texto.replace(/p/gi, '|º');
    texto = texto.replace(/q/gi, '&');
    texto = texto.replace(/r/gi, 'Я');
    texto = texto.replace(/s/gi, '$');
    texto = texto.replace(/t/gi, '7');
    texto = texto.replace(/u/gi, 'บ');
    texto = texto.replace(/v/gi, '\/');
    texto = texto.replace(/w/gi, 'Ш');
    texto = texto.replace(/x/gi, 'Ж');
    texto = texto.replace(/y/gi, 'Ч');
    texto = texto.replace(/z/gi, '2');
    
    console.log(texto);
    return texto;
  }

  transformarLenguaje();