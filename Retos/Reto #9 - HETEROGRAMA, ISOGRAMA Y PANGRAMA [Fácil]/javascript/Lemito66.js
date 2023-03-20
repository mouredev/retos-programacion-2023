/*

 * Crea 3 funciones, cada una encargada de detectar si una cadena de
 * texto es un isHeterogram, un isHeterogram o un isPangram+.
 * - Debes buscar la definición de cada uno de estos términos.

*/

const replaceAccents = (word) => {
  toReplace = {
    á: "a",
    é: "e",
    í: "i",
    ó: "o",
    ú: "u",
  };
  for (const words in toReplace) {
    word = word.replace(words, toReplace[words]);
  }
  return word.toLowerCase();
};

// Un heterograma es una palabra o frase que no contiene ninguna letra repetida.
const isHeterogram = (word) => {
  word = replaceAccents(word).toLowerCase();
  objectOfLetters = {};
  response = "";
  for (let index = 0; index < word.length; index++) {
    if (word[index] in objectOfLetters) {
      response += "No es un heterograma";
      return response;
    } else {
      objectOfLetters[word[index]] = 1;
    }
  }
  response += "Es un heterograma";
  return response;
};

const isIsogram = (word) => {
  word = replaceAccents(word).toLowerCase();
  objectOfLetters = {};
  response = "";
  for (let index = 0; index < word.length; index++) {
    if (word[index] in objectOfLetters) {
      objectOfLetters[word[index]] += 1;
    } else {
      objectOfLetters[word[index]] = 1;
    }
  }
  for (const letter in objectOfLetters) {
    if (objectOfLetters[letter] > 1) {
      response += "No es un isHeterogram";
      return response;
    }
  }
  response += "Es un isHeterogram";
  return response;
};

const isPangram = (word) => {
  word = replaceAccents(word).toLowerCase();
  alphabet = {
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
    ñ: 0,
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
  response = "";
  for (let index = 0; index < word.length; index++) {
    if (word[index] in alphabet) {
      alphabet[word[index]] += 1;
    }
  }
  for (const letter in alphabet) {
    if (alphabet[letter] == 0) {
      response += "No es un pangrama";
      return response;
    }
  }
  response += "Es un pangrama";
  return response;
};

console.log(isHeterogram("Víctima"))
console.log(isHeterogram("Wágner"))
console.log(isHeterogram("Queso"))
console.log(isHeterogram("Néctar"))
console.log(isHeterogram("Lánguido"))


console.log(isHeterogram("Víctima"))
console.log(isHeterogram("Políglota"))
console.log(isHeterogram("Abstemio"))
console.log(isHeterogram("Desoxirribonucleico"))
console.log(isHeterogram("Hipopótamo"))
console.log(isHeterogram("Benzodiacepina"))

console.log(
  isPangram(
    "El veloz murciélago hindú comía feliz cardillo y kiwi. La cigüeña tocaba el saxofón detrás del palenque de paja"
  )
);
console.log(
  isPangram(
    "Jovencillo emponzoñado de whisky, qué figurota exhibe. Cadáveres de ñus, paz y asombro, ¿qué más añadir?"
  )
);
console.log(
  isPangram(
    "El pingüino Wenceslao hizo kilómetros bajo exhaustiva lluvia y frío, añoraba a su querido cachorro"
  )
);

console.log(isPangram("pajarito"));
