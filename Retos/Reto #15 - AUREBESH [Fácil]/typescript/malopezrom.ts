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


/**
 * Interface que representa el mapeo de caracteres
 */
interface AurebeshMap {
    [key: string]: string;
}

/**
 * Enumerado que representa el tipo de traducción
 */
enum AurebeshTranslation {
    AUREBESH2SPANISH,
    SPANISH2AUREBESH
}


/**
 * Función que traduce de español a aurebesh y viceversa
 * @param text Texto a traducir
 * @param translation Tipo de traducción
 */

function translate(text: string,translation:AurebeshTranslation): string {

    const aurebeshMap:AurebeshMap = {
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


    switch (translation) {
        case AurebeshTranslation.SPANISH2AUREBESH:
            const regexSpanish = new RegExp(Object.keys(aurebeshMap).join('|'), 'gi');
            return text.toLowerCase().replace(regexSpanish, match => aurebeshMap[match.toLowerCase()] || match);
        case AurebeshTranslation.AUREBESH2SPANISH:
            const spanishMap:AurebeshMap = {};
                Object.entries(aurebeshMap).map(([key, value]) => {
                spanishMap[value] = key
            })
            const regexAurebesh = new RegExp(Object.keys(spanishMap).join('|'), 'gi');
                let cadena = text.toLowerCase()
            return cadena.toLowerCase().replace(regexAurebesh, match => spanishMap[match] || match);

    }

}

/**
 * Función que traduce de español a aurebesh
 * @param text Texto a traducir
 */
function spanishToAurebesh(text: string): string {
    return translate(text,AurebeshTranslation.SPANISH2AUREBESH);
}


/**
 * Función que traduce de aurebesh a español
 * @param text Texto a traducir
 */
function aurebeshToSpanish(text: string): string {
    return translate(text,AurebeshTranslation.AUREBESH2SPANISH);
}


/** Casos de prueba */

const spanish2AurebeshText ='Que la fuerza te acompañe'

console.log(spanishToAurebesh(spanish2AurebeshText))

const aurebesh2SpanishText =
   `lethaurek lethujebnernaurek aureksenthoskmernaurek : fornesselesdornesselesreshiskcreshosk grekaurekreshcreshíaurek lethoskreshcreshaurek 
    creshujebaureknerndornosk senthaureklethesseles lethaurek lethujebnernaurek
    senthesseles peiiskesselesreshdornesselesnern lethaureksenth creshaurekmernpeiaureknernaureksenth
    yirt aurekpeiaurekreshesselescreshesselesnern lethaureksenth senthesselesnerndornaureksenth
    iskmernpeiesselesnernesselestrillreshaurekbeshlethesselessenth.
    creshujebaureknerndornosk senthaureklethesseles lethaurek lethujebnernaurek,
    esselesleth mernaurekresh creshujebbeshreshesseles lethaurek trilliskesselesreshreshaurek
    yirt esselesleth creshoskreshaurekzerekónern senthesseles senthiskesselesnerntrillesseles
    isksenthlethaurek esselesnern esselesleth isknernfornisknernisktrillosk.
    nernaurekdorniskesseles creshoskmernesseles nernaurekreshaureknernjenthaureksenth
    beshaurekjenthosk lethaurek lethujebnernaurek lethlethesselesnernaurek.
    esselessenth peireshesselescreshisksenthosk creshoskmernesselesresh
    fornreshujebtrillaurek vevesselesreshdornesseles yirt herfesseleslethaurekdornaurek.
    creshujebaureknerndornosk senthaureklethesseles lethaurek lethujebnernaurek
    dornesseles creshiskesselesnern reshosksenthtrillreshosksenth iskgrekujebaureklethesselessenth,
    lethaurek mernosknernesselesdornaurek dornesseles peilethaurektrillaurek
    senthosklethlethoskzerekaurek esselesnern esselesleth beshosklethsenthisklethlethosk.`

console.log(aurebeshToSpanish(aurebesh2SpanishText)); // Prueba a traducirlo a ver que sale ;)


