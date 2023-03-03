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
    if (isInArray(letter,letters)) {
      // Is not Heterograma
      console.log("No es un Heterograma");
      return FALSE;
    } else {
      // Add the leter to the array
      letters = letters + letter;
      console.log(letters);
    }
  }
  // Es un Heterograma
  console.log("Es un Heterograma");
  return TRUE;
}

function isIsograma(word) {
  var letters = new Map();
  for (let i = 0; i < word.Length; i++) {
    let letter = word[i];
    console.log(letter);
    if (letters.has(letter)) {
      // If the letter has already appeared, increase the account
      letters.set(letter, (letters.get(letter) + 1));
    } else {
      // if the letter has not appeared include in the array
      letters.set(letter, 1);
    }
  }
  // Check if letters appears the same qty
  const iterator = letters.values();
  let a = iterator.next().value;
  console.log("isIsograma a: " + a);
  for (iterator) {
    console.log("isIsograma iterator: " + iterator);
    if (iterator.value !== a) {
      // Is diferent. Is not Isograma
      console.log("No es un Isograma");
      return FALSE
    let a = iterator.value;
    console.log("isIsograma a: " + a);
  }
  // Is a Isograma
}

function isPangrama(word) {
  var letters = [];
}

function isInArray(element, array) {
  for (let i = 0; i < array.length; i++) {
    if (element === array[i]) return TRUE;
  }
  return FALSE;
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
