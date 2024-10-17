/*
 * Crea un programa que analice texto y obtenga:
 * - Número total de palabras.
 * - Longitud media de las palabras.
 * - Número de oraciones del texto (cada vez que aparecen un punto).
 * - Encuentre la palabra más larga.
 *
 * Todo esto utilizando un único bucle.
 */

const text =
  'La vida es bella. la vida. es linda. y llego la pandemia y todos para la casa en cuarentena';

let totalPalabras = [];
let totalCaracteres = [];
let data;
let filtering;
let media;
let numeroOraciones;

const textValidation = (text) => {
  text.split(' ').forEach((x) => {
    totalPalabras.push(x);
    totalCaracteres.push(x.length);
    data = Math.max(...totalCaracteres);
    filtering = totalPalabras.filter((x) => x.length === data).join();
    media = totalPalabras.reduce((a, b) => a + b, 0);
    numeroOraciones = `${text.split('. ').length}`;
  });
};

textValidation(text);

console.log(
  `- Total Palabras: ${totalPalabras.length}\n`,
  '- Longitud media:',
  media.length / totalPalabras.length,
  '\n',
  `- Número de oraciones: ${numeroOraciones}\n`,
  `- Palabra más larga ${filtering} con ${data} caracteres.\n`
);
