/* 

* Crea una función que sea capaz de transformar Español al lenguaje básico del universo
 * Star Wars: el "Aurebesh".
 * - Puedes dejar sin transformar los caracteres que no existan en "Aurebesh".
 * - También tiene que ser capaz de traducir en sentido contrario.
 *  
 * ¿Lo has conseguido? Nómbrame en twitter.com/mouredev y escríbeme algo en Aurebesh.
 *
 * ¡Que la fuerza os acompañe!
*/

function aurebesh(text) {
  let response = "";
  const doubleAurebesh = {
    ch: "cherek",
    ae: "enth",
    eo: "onith",
    kh: "krenth",
    ng: "nen",
    oo: "orenth",
    sh: "shen",
    th: "thesh",
  };
  const dictionaryAurebesh = {
    a: "aurek",
    b: "besh",
    c: "cresh",
    d: "dorn",
    e: "esk",
    f: "forn",
    g: "grek",
    h: "herf",
    i: "isk",
    j: "jenth",
    k: "krill",
    l: "leth",
    m: "mern",
    n: "nern",
    o: "osk",
    p: "peth",
    q: "qek",
    r: "resh",
    s: "senth",
    t: "trill",
    u: "usk",
    v: "vev",
    w: "wesk",
    x: "xesh",
    y: "yirt",
    z: "zerek",
  };
  let positionOfWord = 0;
  textToLowerCase = text.toLowerCase();
  while (positionOfWord < textToLowerCase.length) {
    if (
      positionOfWord < textToLowerCase.length - 1 &&
      textToLowerCase.substr(positionOfWord, 2) in doubleAurebesh
    ) {
      response += doubleAurebesh[textToLowerCase.substr(positionOfWord, 2)];
      positionOfWord += 2;
    }
    // Si no, verifica si el carácter actual está en el diccionario dictionary_aurebesh y agrega su valor a la respuesta
    else if (textToLowerCase[positionOfWord] in dictionaryAurebesh) {
      response += dictionaryAurebesh[textToLowerCase[positionOfWord]];
      positionOfWord += 1;
    }
    // Si no, agrega el carácter original a la respuesta
    else {
      response += textToLowerCase[positionOfWord];
      positionOfWord += 1;
    }
  }
  return response;
}

console.log(aurebesh("Lemito66"));
