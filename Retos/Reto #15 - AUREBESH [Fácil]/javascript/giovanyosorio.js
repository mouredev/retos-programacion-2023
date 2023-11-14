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

const aurebesh = {
    'A': 'Aurek',
    'B': 'Besh',
    'C': 'Cresh',
    'D': 'Dorn',
    'E': 'Esk',
    'F': 'Forn',
    'G': 'Grek',
    'H': 'Herf',
    'I': 'Isk',
    'J': 'Jenth',
    'K': 'Krill',
    'L': 'Leth',
    'M': 'Mern',
    'N': 'Nern',
    'O': 'Osk',
    'P': 'Peth',
    'Q': 'Qek',
    'R': 'Resh',
    'S': 'Senth',
    'T': 'Trill',
    'U': 'Usk',
    'V': 'Vev',
    'W': 'Wesk',
    'X': 'Xesh',
    'Y': 'Yirt',
    'Z': 'Zerek'
}


function translateToAurebesh(text) {
    return text.split('').map(char => aurebesh[char.toUpperCase()] || char).join('');
}



console.log(translateToAurebesh('Hola Mundo'));

