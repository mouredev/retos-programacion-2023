/*
 * Crea 3 funciones, cada una encargada de detectar si una cadena de
 * texto es un heterograma, un isograma o un pangrama.
 * - Debes buscar la definición de cada uno de estos términos.
 */

let abecedario = {
  a: 0,
  b: 0,
  c: 0,
  d: 0,
  e: 0,
  f: 0,
  g: 0,
  h: 0,
  i: 0,
  j: 0,
  k: 0,
  l: 0,
  m: 0,
  n: 0,
  o: 0,
  p: 0,
  q: 0,
  r: 0,
  s: 0,
  t: 0,
  u: 0,
  v: 0,
  w: 0,
  x: 0,
  y: 0,
  z: 0,
};

function isHeterogram(word) {
  word = word.toLowerCase();
  abc = abecedario;
  lettersInWord = "";
  for (let i = 0; i < word.length; i++) {
    if (word[i] in abc) {
      var currentLetter = word[i];

      if (lettersInWord.includes(currentLetter)) {
        return false;
      } else {
        lettersInWord += currentLetter;
      }
    }
  }

  return true;
}

function isIsogram(word) {
  word = word.toLowerCase();
  abc = abecedario;
  lettersInWord = "";
  for (let i = 0; i < word.length; i++) {
    if (word[i] in abc) {
      var currentLetter = word[i];

      abc[currentLetter]++;

      if (!lettersInWord.includes(currentLetter)) {
        lettersInWord += currentLetter;
      }
    }
  }

  const lttr1 = lettersInWord[0];

  for (let i = 0; i < lettersInWord.length; i++) {
    var currentLetter = lettersInWord[i];

    if (abc[lttr1] !== abc[currentLetter]) {
      return false;
    }
  }

  return true;
}

function isPangram(word) {
  word = word.toLowerCase();

  let abc = new Set("abcdefghijklmnopqrstuvwxyz");

  for (let i = 0; i < word.length; i++) {
    if (abc.has(word[i])) {
      abc.delete(word[i]);
    }
  }

  return abc.size === 0;
}

if (isHeterogram("pasolin ex ??24")) {
  console.log("es heterograma");
} else {
  console.log("no es heterograma");
}

if (isIsogram("pa pa")) {
  console.log("es isograma");
} else {
  console.log("no es isograma");
}

if (isPangram("The quick brown fox jumps over the lazy dog")) {
  console.log("es heterograma");
} else {
  console.log("no es heterograma");
}
