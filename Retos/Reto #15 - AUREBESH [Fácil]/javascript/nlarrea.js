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

const dictionaryAurebesh = {
    'a': 'aurek',
    'b': 'besh',
    'c': 'cresh',
    'd': 'dorn',
    'e': 'esk',
    'f': 'forn',
    'g': 'grek',
    'h': 'herf',
    'i': 'isk',
    'j': 'jenth',
    'k': 'krill',
    'l': 'leth',
    'm': 'mern',
    'n': 'nern',
    'o': 'osk',
    'p': 'peth',
    'q': 'qek',
    'r': 'resh',
    's': 'senth',
    't': 'trill',
    'u': 'usk',
    'v': 'vev',
    'w': 'wesk',
    'x': 'xesh',
    'y': 'yirt',
    'z': 'zerek'
};

const doubleAurebesh = {
    'ch': 'cherek',
    'ae': 'enth',
    'eo': 'onith',
    'kh': 'krenth',
    'ng': 'nen',
    'oo': 'orenth',
    'sh': 'sen',
    'th': 'thesh'
}


function translateAurebesh(text) {
    text = text.toLowerCase();
    let result = '';

    let idx = 0;
    while (idx < text.length) {
        if (Object.keys(doubleAurebesh).includes(text[idx] + text[idx + 1])) {
            result += doubleAurebesh[text[idx] + text[idx + 1]];
            idx++;
        } else if (Object.keys(dictionaryAurebesh).includes(text[idx])) {
            result += dictionaryAurebesh[text[idx]];
        } else {
            result += text[idx];
        }
        idx++;
    }

    return result;
}


console.log(translateAurebesh('Hola mundo!'));
// herfosklethaurek mernusknerndornosk!

console.log(translateAurebesh('Mucho gusto conocerte'));
// mernuskcherekosk grekusksenthtrillosk creshosknernoskcresheskreshtrillesk