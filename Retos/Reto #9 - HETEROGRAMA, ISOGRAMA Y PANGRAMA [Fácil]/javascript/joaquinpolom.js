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
// Isogramas con una repetición o de segundo orden: abdomen, escritura (9), intestinos (10), papelera (8)...
// Pangrama: Benjamín pidió una bebida de kiwi y fresa. Noé, sin vergüenza, la más exquisita champaña del menú.

function isHeterograma(word) {
  console.log("isHeterograma word: " + word);
  var letters = [];
  for (let i = 0; i < word.length; i++) {
    let letter = word[i];
    if (isInArray(letter,letters)) {
      // Is not Heterograma
      console.log("No es un Heterograma");
      return false;
    } else {
      // Add the leter to the array
      letters = letters + letter;
    }
  }
  // Es un Heterograma
  console.log("Es un Heterograma");
  return true;
}

function isIsograma(word) {
  console.log("isIsograma word: " + word);
  var letters = new Map();
  for (let i = 0; i < word.length; i++) {
    let letter = word[i];
    if (letters.has(letter)) {
      // If the letter has already appeared, increase the account
      letters.set(letter, (letters.get(letter) + 1));
    } else {
      // if the letter has not appeared include in the array
      letters.set(letter, 1);
    }
  }
  // Check if letters appears the same qty
  let a = 0;
  for (const value of letters.values()) {
    if (a == 0) {
      // Is the first value
      a = value;
    }
    if (a != value) {
      // Is diferent. Is not Isograma
      console.log("No es un Isograma");
      return false;
    }
  } 
  // Is a Isograma
  console.log("Es un Isograma");
  return true;
}

function isPangrama(word) {
  console.log("isPangrama word: " + word);
  var letters = new Map();
  // Count the letters
  for (let i = 0; i < word.length; i++) {
    let letter = word[i];
    if (letters.has(letter)) {
      // If the letter has already appeared, increase the account
      letters.set(letter, (letters.get(letter) + 1));
    } else {
      // if the letter has not appeared include in the array
      letters.set(letter, 1);
    }
  }
  // Alphabet
  const alphabet = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"];
  // Check if all the letter of the alphabet are in the map with the letters of the word
  for (const l of alphabet) {
    // if l is in letters
    if (!letters.get(l)) {
      console.log("No es un Pangrama");
      return false
    }
  }
  // is a Pangrama
  console.log("Es un pangrama");
  return true;
}

function isInArray(element, array) {
  for (let i = 0; i < array.length; i++) {
    if (element === array[i]) return true;
  }
  return false
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
isIsograma("abdomen");
isPangrama("acondicionar");
isHeterograma("escritura");
isIsograma("escritura");
isPangrama("escritura");
isHeterograma("Benjamín pidió una bebida de kiwi y fresa. Noé, sin vergüenza, la más exquisita champaña del menú.");
isIsograma("Benjamín pidió una bebida de kiwi y fresa. Noé, sin vergüenza, la más exquisita champaña del menú.");
isPangrama("Benjamín pidió una bebida de kiwi y fresa. Noé, sin vergüenza, la más exquisita champaña del menú.");
