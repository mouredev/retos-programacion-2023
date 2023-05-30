/*
 * Crea una función que sea capaz de transformar Español al lenguaje básico 
 * del universo Star Wars: el "Aurebesh".
 * - Puedes dejar sin transformar los caracteres que no existan en "Aurebesh".
 * - También tiene que ser capaz de traducir en sentido contrario.
 *  
 * ¿Lo has conseguido? Nómbrame en twitter.com/mouredev y escríbeme algo en Aurebesh.
 *
 * ¡Que la fuerza os acompañe!
 */

const basicAlphabet2: { [key: string]: string } = {
    "a": "aurek", "b": "besh", "c": "cresh", "d": "dorn", "e": "esk", "f": "forn", "g": "grek", "h": "herf",
    "i": "isk", "j": "jenth", "k": "krill", "l": "leth", "m": "merm", "n": "nern", "o": "osk", "p": "peth", "q": "qek",
    "r": "resh", "s": "senth", "t": "trill", "u": "usk", "v": "vev", "w": "wesk", "x": "xesh", "y": "yirt", "z": "zerek",
    "ae": "enth", "eo": "onith", "kh": "krenth", "ng": "nen", "oo": "orenth", "sh": "sen", "th": "thesh"
}

function translate2(text: string): string {
    let translated_text: string = "";
    let i: number = 0;
    while (i < text.length) {
        if (basicAlphabet2[text.slice(i, i + 2)]) {
            translated_text += basicAlphabet2[text.slice(i, i + 2)];
            i += 2;
        } else {
            translated_text += basicAlphabet2[text[i].toLowerCase()] || text[i];
            i += 1;
        }
    }
    return translated_text;
}

console.log(translate2("Brais"))
console.log(translate2("Mouredev"))

