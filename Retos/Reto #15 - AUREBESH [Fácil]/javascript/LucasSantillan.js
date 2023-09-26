/* 
 * Reto #15: AUREBESH
 * FÁCIL | Publicación: 10/04/23 | Resolución: 17/04/23
 * 
 * Crea una función que sea capaz de transformar Español al lenguaje básico 
 * del universo Star Wars: el "Aurebesh".
 * - Puedes dejar sin transformar los caracteres que no existan en "Aurebesh".
 * - También tiene que ser capaz de traducir en sentido contrario.
 *  
 * ¿Lo has conseguido? Nómbrame en twitter.com/mouredev y escríbeme algo en Aurebesh.
 *
 * ¡Que la fuerza os acompañe!
 */

const transformar = {
  A: 'AUREK',
  'Á': 'AUREK',
  B: 'BESH',
  C: 'CRESH',
  D: 'DORN',
  E: 'ESK',
  'É': 'ESK',
  F: 'FORN',
  G: 'GREK',
  H: 'HERF',
  I: 'ISK',
  'Í': 'ISK',
  J: 'JENTH',
  K: 'KRILL',
  L: 'LETH',
  M: 'MERN',
  N: 'NERN',
  'Ñ': 'NEN',
  O: 'OSK',
  'Ó': 'OSK',
  P: 'PETH',
  Q: 'QEK',
  R: 'RESH',
  S: 'SENTH',
  T: 'TRILL',
  U: 'USK',
  'Ú': 'USK',
  'Ü': 'USK',
  V: 'VEV',
  W: 'WESK',
  X: 'XESH',
  Y: 'YIRT',
  Z: 'ZEREK',
  ' ': ' ',
  '.': '.',
  ',': ',',
  '\n': '\n'
}


function traducirEspanolAurebesh(texto, idioma) {
  idioma = idioma.toUpperCase();
  texto = texto.toUpperCase();
  let textoTransformado = '';

  if(idioma === 'ESPAÑOL') {
    for(let c of texto) {
      textoTransformado += transformar[c];
    }
    console.log(textoTransformado);
  } else {
    for(let c in transformar) {
      texto = texto.replaceAll(transformar[c], c);
    }
    console.log('\n' + texto);
  }

}
let texto1 = `La República Galáctica
está sumida en disturbios.
Hay protestas contra la tributación
de las rutas comerciales
a sistemas estelares.`;

let texto2 = `ESKSENTHPETHESKRESHAUREKNERNDORNOSK RESHESKSENTHOSKLETHVEVESKRESH ESKLETH PETHRESHOSKBESHLETHESKMERNAUREK 
CRESHOSKNERN USKNERN BESHLETHOSKQEKUSKESKOSK DORNESK MERNOSKRESHTRILLISKFORNESKRESHOSKSENTH CRESHRESHUSKCRESHESKRESHOSKSENTH,
LETHAUREK AUREKVEVAUREKRESHISKCRESHISKOSKSENTHAUREK FORNESKDORNESKRESHAUREKCRESHISKOSKNERN DORNESK CRESHOSKMERNESKRESHCRESHISKOSK
HERFAUREK DORNESKTRILLESKNERNISKDORNOSK TRILLOSKDORNOSKSENTH LETHOSKSENTH ESKNERNVEVISKOSKSENTH
AUREKLETH PETHESKQEKUSKESKNENOSK PETHLETHAUREKNERNESKTRILLAUREK DORNESK NERNAUREKBESHOSKOSK.`;

traducirEspanolAurebesh(texto1, 'español');
traducirEspanolAurebesh(texto2, 'Aurebesh');

/*
* Episodio I: La Amenaza Fantasma:
* 
* Texto 1
* La República Galáctica
* está sumida en disturbios.
* Hay protestas contra la tributación
* de las rutas comerciales
* a sistemas estelares.
* 
* Texto 2
* Esperando resolver el problema 
* con un bloqueo de mortíferos cruceros,
* la avariciosa Federación de Comercio
* ha detenido todos los envios
* al pequeño planeta de Naboo.
*/