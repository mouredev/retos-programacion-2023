import java.util.*

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
data class AurebeshMap(val map: Map<String,String>)

/**
 * Enumerado que representa el tipo de traducción
 */
enum class AurebeshTraslation{
    AUREBESH2SPANISH,
    SPANISH2AUREBESH
}
/**
 * Función que traduce de español a aurebesh y viceversa
 * @param text Texto a traducir
 * @param translation Tipo de traducción
 */
fun translate(text:String,traslation: AurebeshTraslation):String {
    val aurebeshMap = AurebeshMap(mapOf(
            "a" to "aurek",
            "b" to "besh",
            "c" to "cresh",
            "d" to "dorn",
            "e" to "esseles",
            "f" to "forn",
            "g" to "grek",
            "h" to "herf",
            "i" to "isk",
            "j" to "jenth",
            "k" to "krill",
            "l" to "leth",
            "m" to "mern",
            "n" to "nern",
            "ñ" to "nerf",
            "o" to "osk",
            "p" to "pei",
            "q" to "qek",
            "r" to "resh",
            "s" to "senth",
            "t" to "trill",
            "u" to "ujeb",
            "v" to "vev",
            "w" to "wirch",
            "x" to "xesh",
            "y" to "yirt",
            "z" to "zerek",
            "ch" to "cherek",
            "ae" to "enth",
            "eo" to "onith",
            "kh" to "krenth",
            "ng" to "nen",
            "oo" to "orenth",
            "sh" to "shen",
            "th" to "thesh"
    ))
    return when (traslation) {
        AurebeshTraslation.SPANISH2AUREBESH -> {
            val regexSpanish = aurebeshMap.map.keys.joinToString(separator = "|").toRegex(setOf(RegexOption.IGNORE_CASE))
            text.lowercase(Locale.getDefault()).replace(regexSpanish) {
                aurebeshMap.map[it.value.lowercase(Locale.getDefault())] ?: it.value
            }
        }

        AurebeshTraslation.AUREBESH2SPANISH -> {
            val spanishMap = aurebeshMap.map.entries.associate { (key, value) -> value to key.toString() }
            val regexAurebesh = spanishMap.keys.joinToString(separator = "|").toRegex(setOf(RegexOption.IGNORE_CASE))
            text.lowercase(Locale.getDefault()).replace(regexAurebesh) {
                spanishMap[it.value] ?: it.value
            }
        }
    }
}


/**
 * Función que traduce de español a aurebesh
 * @param text Texto a traducir
 */
fun spanishToAurebesh(text: String): String {
    return translate(text, AurebeshTraslation.SPANISH2AUREBESH)
}

/**
 * Función que traduce de aurebesh a español
 * @param text Texto a traducir
 */
fun aurebeshToSpanish(text: String): String {
    return translate(text, AurebeshTraslation.AUREBESH2SPANISH)
}

/** Casos de prueba */
fun main() {

    println(spanishToAurebesh("Que la fuerza te acompañe"))
    println(aurebeshToSpanish("""lethaurek lethujebnernaurek aureksenthoskmernaurek : fornesselesdornesselesreshiskcreshosk grekaurekreshcreshíaurek lethoskreshcreshaurek
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
                senthosklethlethoskzerekaurek esselesnern esselesleth beshosklethsenthisklethlethosk."""))// Prueba a traducirlo a ver que sale ;)
}


