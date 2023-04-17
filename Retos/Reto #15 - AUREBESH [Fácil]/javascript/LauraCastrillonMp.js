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

const aurebeshAlfabeto = {
    a: 'aurek',
    b: 'besh',
    c: 'cresh',
    d: 'dorn', 
    e: 'esk',
    f: 'forn',
    g: 'grek',
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
    th: "thesh"
}

function traduccionAurebesh(lenguaje, text) {
    let textoTraducido = '';

    if (lenguaje === 'español') {
        text.toLowerCase().split('').map(letter => {
            aurebeshAlfabeto[letter] 
                ? textoTraducido += aurebeshAlfabeto[letter]
                : textoTraducido += letter
        })
        console.log(textoTraducido)
    } else if (lenguaje === 'aurebesh') {
        let palabra = text[0].toLowerCase()
        text.toLowerCase().split('').slice(1).forEach(letter => {
            aurebeshAlfabeto[letter]
                ? palabra += letter
                : (textoTraducido += letter, palabra = '')

            const value = Object.entries(aurebeshAlfabeto).find(([key, value]) => value === palabra)

            if (value !== undefined) {
                textoTraducido += value[0]
                palabra = ''
            }
        })
        console.log(textoTraducido)
    }
}

traduccionAurebesh('español', 'mouredev') // Salida: 'mernoskujebresheskdorneskvev'
traduccionAurebesh('aurebesh', 'mernoskujebresheskdorneskvev') // Salida: 'mouredev
