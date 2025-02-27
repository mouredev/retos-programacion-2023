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

DICCIONARIO_AUREBESH = {
  'a': 'Aurek', 'b': 'Besh', 'c': 'Cresh', 'd': 'Dorn', 'e': 'Esk',
  'f': 'Forn', 'g': 'Grek', 'h': 'Herf', 'i': 'Isk', 'j': 'Jenth',
  'k': 'Krill', 'l': 'Leth', 'm': 'Mern', 'n': 'Nern', 'o': 'Osk',
  'p': 'Peth', 'q': 'Qek', 'r': 'Resh', 's': 'Senth', 't': 'Trill',
  'u': 'Usk', 'v': 'Vev', 'w': 'Wesk', 'x': 'Xesh', 'y': 'Yirt', 'z': 'Zerek'
}

DICCIONARIO_ESPANOL = {
  'Aurek': 'a', 'Besh': 'b', 'Cresh': 'c', 'Dorn': 'd', 'Esk': 'e',
  'Forn': 'f', 'Grek': 'g', 'Herf': 'h', 'Isk': 'i', 'Jenth': 'j',
  'Krill': 'k', 'Leth': 'l', 'Mern': 'm', 'Nern': 'n', 'Osk': 'o',
  'Peth': 'p', 'Qek': 'q', 'Resh': 'r', 'Senth': 's', 'Trill': 't',
  'Usk': 'u', 'Vev': 'v', 'Wesk': 'w', 'Xesh': 'x', 'Yirt': 'y', 'Zerek': 'z'
}

function encodeAurebesh(text) {
  text = text.toLowerCase()
  let newText = []
  for (let i = 0; i < text.length; i++) {
    let currentLetter = text[i];
    
    if (currentLetter in DICCIONARIO_AUREBESH) {
      newText.push(DICCIONARIO_AUREBESH[currentLetter]);
    } else {
      newText.push(currentLetter);
    }
  }
  newText = newText.join(' ');
  return newText;
}

function decodeAurebesh(text) {
  let newText = [];
  let words = text.split(' ');
  words.forEach(word => {
    if (word in DICCIONARIO_ESPANOL) {
      newText.push(DICCIONARIO_ESPANOL[word]);
    } else {
      newText.push(word);
    }
  });
  newText = newText.join(' ');
  return newText;
}

function translateAurebesh({ text, decode }) {
  // Validations
  if (typeof text !== 'string') {
    throw new Error("text parameter must be a string.");
  } else if (typeof decode !== 'boolean') {
    throw new Error("decode parameter must be boolean.");
  }

  if (decode === false) {
    let encodedText = encodeAurebesh(text);
    console.log(encodedText);
  }

  if (decode === true) {
    let decodedText = decodeAurebesh(text);
    console.log(decodedText);
  }

}

translateAurebesh({ text: 'hola ñoqui', decode: false })
translateAurebesh({ text: 'Herf Osk Leth Aurek   ñ Osk Qek Usk Isk', decode: true })
