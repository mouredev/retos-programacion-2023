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
 * Enumerado que representa el tipo de traducción
 */
enum AurebeshTraslation{
  toAureBesh,
  toSpanish
}

/**
 * Interface que representa el mapeo de caracteres
 */
class AurebeshMap{
  static const Map<String, String> dictionary = {
    'a': 'aurek',
    'b': 'besh',
    'c': 'cresh',
    'd': 'dorn',
    'e': 'esseles',
    'f': 'forn',
    'g': 'grek',
    'h': 'herf',
    'i': 'isk',
    'j': 'jenth',
    'k': 'krill',
    'l': 'leth',
    'm': 'mern',
    'n': 'nern',
    'ñ': 'nerf',
    'o': 'osk',
    'p': 'pei',
    'q': 'qek',
    'r': 'resh',
    's': 'senth',
    't': 'trill',
    'u': 'ujeb',
    'v': 'vev',
    'w': 'wirch',
    'x': 'xesh',
    'y': 'yirt',
    'z': 'zerek',
    'ch': 'cherek',
    'ae': 'enth',
    'eo': 'onith',
    'kh': 'krenth',
    'ng': 'nen',
    'oo': 'orenth',
    'sh': 'shen',
    'th': 'thesh',
  };

}
/**
 * Enumerado que representa el tipo de traducción
 */
String translate(String text,AurebeshTraslation translation){
  switch (translation) {
    case AurebeshTraslation.toAureBesh:
      final regexSpanish = RegExp(AurebeshMap.dictionary.keys.map((e) => e.toString()).join('|'), multiLine: true, caseSensitive: false);
      return text.toLowerCase().replaceAllMapped(regexSpanish, (match) => AurebeshMap.dictionary[match.group(0).toString().toLowerCase()] ?? match.group(0).toString());
    case AurebeshTraslation.toSpanish:
      final spanishMap = Map<String, String>.fromEntries(AurebeshMap.dictionary.entries.map((e) => MapEntry(e.value, e.key)));
      final regexAurebesh = RegExp(spanishMap.keys.map((e) => e.toString()).join('|'), multiLine: true, caseSensitive: false);
      return text.toLowerCase().replaceAllMapped(regexAurebesh, (match) => spanishMap[match.group(0).toString()] ?? match.group(0).toString());
  }
}
/**
 * Función que traduce de español a aurebesh
 * @param text Texto a traducir
 */
String spanishToAurebesh(String text) {
  return translate(text, AurebeshTraslation.toAureBesh);
}
/**
 * Función que traduce de aurebesh a español
 * @param text Texto a traducir
 */
String aurebeshToSpanish(String text) {
  return translate(text, AurebeshTraslation.toSpanish);
}
/** Casos de prueba */

void main() {
  final String spanish2AurebeshText = 'Que la fuerza te acompañe';

  print(spanishToAurebesh(spanish2AurebeshText));

  final String aurebesh2SpanishText =
  '''lethaurek lethujebnernaurek aureksenthoskmernaurek : fornesselesdornesselesreshiskcreshosk grekaurekreshcreshíaurek lethoskreshcreshaurek
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
senthosklethlethoskzerekaurek esselesnern esselesleth beshosklethsenthisklethlethosk.''';


  print(aurebeshToSpanish(aurebesh2SpanishText)); // Prueba a copiar y pegar el codigo en https://dartpad.dev/?  a ver que te sale ;)



}