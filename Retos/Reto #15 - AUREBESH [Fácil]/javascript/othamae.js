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

const alfabetoAurebesh = {
    a: "aurek",
    b: "besh",
    c: "cresh",
    d: "dorn",
    e: "esseles",
    f: "forn",
    g: "grek",
    h: "herf",
    i: "isk",
    j: "jenth",
    k: "krill",
    l: "leth",
    m: "mern",
    n: "nern",
    ñ: "nerf",
    o: "osk",
    p: "pei",
    q: "qek",
    r: "resh",
    s: "senth",
    t: "trill",
    u: "ujeb",
    v: "vev",
    w: "wirch",
    x: "xesh",
    y: "yirt",
    z: "zerek",
    ch: "cherek",
    ae: "enth",
    eo: "onith",
    kh: "krenth",
    ng: "nen",
    oo: "orenth",
    sh: "shen",
    th: "thesh",
};

function spanishToAurebesh(text) {
    let translation = ''

    text.toLowerCase().split('').map(letter => {
        alfabetoAurebesh[letter]
            ? translation += alfabetoAurebesh[letter]
            : translation += letter
    })

    return translation
}

function AurebeshToSpanish(text) {
    let translation = ''
    let word = text[0].toLowerCase()
    text.toLowerCase().split('').slice(1).forEach(letter => {
        alfabetoAurebesh.hasOwnProperty(letter)
            ? word += letter
            : (translation += letter, word = '')

        const value = Object.entries(alfabetoAurebesh).find(([key, val]) => val === word)

        if (value !== undefined) {
            translation += value[0]
            word = ''
        }
    })

    return translation
}


console.log(spanishToAurebesh('Que la fuerza te acompañe!'))
// qekujebesseles lethaurek fornujebesselesreshzerekaurek trillesseles aurekcreshoskmernpeiaureknerfesseles!
console.log(AurebeshToSpanish('Qekujebesseles lethaurek fornujebesselesreshzerekaurek trillesseles aurekcreshoskmernpeiaureknerfesseles!'))
// que la fuerza te acompañe!