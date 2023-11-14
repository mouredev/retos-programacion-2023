const texto = `El fichero de código`
/**
 * Transforma un normal a lenguaje hacker
 * @param {String} text 
 */
const hackerTranslator = (text) => {
    const datamap = {
        "a": '4',
        "b": 'ß',
        "c": '©',
        "d": 'cl',
        "e": '€',
        "f": 'ƒ',
        "g": '6',
        "h": '#',
        "i": '!',
        "j": ']',
        "k": '|c',
        "l": '£',
        "m": 'nn',
        "n": 'И',
        "o": '0',
        "p": '|º',
        "q": '&',
        "r": 'Я',
        "s": '$',
        "t": '7',
        "u": 'บ',
        "v": '\/',
        "w": 'Ш',
        "x": 'Ж',
        "y": 'Ч',
        "z": '2',
        "1": "L",
        "2": "R",
        "3": "E",
        "4": "A",
        "5": "S",
        "6": "b",
        "7": "T",
        "8": "B",
        "9": "g",
        "0": "o",
        " ": " "
    }
    const result = text.toLowerCase().split('').map(e => datamap[e]).join('')
    return result
}
/**
 * Transforma un normal a lenguaje hacker con expresiones regulares
 * @param {String} text 
 */
const Translator = (text) => {
    const datamap = [[/0/gi, "o"], [/1/gi, "L"], [/2/gi, "R"], [/3/gi, "E"], [/4/gi, "A"], [/5/gi, "S"], [/6/gi, "b"], [/7/gi, "T"], [/8/gi, "B"], [/9/gi, "g"], [/a/gi, "4"], [/b/gi, "ß"], [/c/gi, "©"], [/d/gi, "cl"], [/e/gi, "€"], [/f/gi, "ƒ"], [/g/gi, "6"], [/h/gi, "#"], [/i/gi, "!"], [/j/gi, "]"], [/k/gi, "|c"], [/l/gi, "£"], [/m/gi, "nn"], [/n/gi, "И"], [/o/gi, "0"], [/p/gi, "|º"], [/q/gi, "&"], [/r/gi, "Я"], [/s/gi, "$"], [/t/gi, "7"], [/u/gi, "บ"], [/v/gi, '\/'], [/w/gi, "Ш"], [/x/gi, "Ж"], [/y/gi, "Ч"], [/z/gi, "2"], [/ /gi, " "]]
    datamap.forEach(e => text = text.replace(...e))
    return text
}

console.log(hackerTranslator(texto))