/*
 * Crea 3 funciones, cada una encargada de detectar si una cadena de
 * texto es un heterograma, un isograma o un pangrama.
 * - Debes buscar la definición de cada uno de estos términos.
 */
// Un heterograma es una palabra que no contiene ninguna letra repetida.
// Un isograma es una palabra en la que cada letra aparece el mismo número de veces.
// Un pangrama es una frase en la que aparecen todas las letras del abecedario.
// Ejemplos
// Heterogramas: yuxtaponer (10), centrifugado (12), luteranismo (11), adulterinos (11), hiperblanduzcos (15)...
// Isogramas con una repetición o de segundo orden: acondicionar (11), escritura (9), intestinos (10), papelera (8)...
// Pangrama: Benjamín pidió una bebida de kiwi y fresa. Noé, sin vergüenza, la más exquisita champaña del menú.

function isHeterograma(word) {
  var letters = [];
  for (let i = 0; i < word.Length; i++) {
    let letter = word[i];
    console.log(letter);
}

function isIsograma(word) {
  var letters = [];
}

function isPangrama(word) {
  var letters = [];
}

isHeterograma("yuxtaponer");
isIsograma("yuxtaponer");
isPangrama("yuxtaponer");
isHeterograma("centrifugado");
isIsograma("centrifugado");
isPangrama("centrifugado");
isHeterograma("luteranismo");
isIsograma("luteranismo");
isPangrama("luteranismo");
isHeterograma("acondicionar");
isIsograma("acondicionar");
isPangrama("acondicionar");
isHeterograma("escritura");
isIsograma("escritura");
isPangrama("escritura");
isHeterograma("Benjamín pidió una bebida de kiwi y fresa");
isIsograma("Benjamín pidió una bebida de kiwi y fresa");
isPangrama("Benjamín pidió una bebida de kiwi y fresa");
