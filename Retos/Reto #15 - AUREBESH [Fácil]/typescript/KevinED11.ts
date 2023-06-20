/*
 * Crea una función que sea capaz de transformar Español al lenguaje básico 
 * del universo Star Wars: el "Aurebesh".
 * - Puedes dejar sin transformar los caracteres que no existan en "Aurebesh".
 * - También tiene que ser capaz de traducir en sentido contrario.
 *  

 *
 * ¡Que la fuerza os acompañe!
 */

interface SpanToAure {
  [key: string]: string
}

interface AureToSpan {
  [key: string]: string;
}

const dictSpanishToAurebesh = (): SpanToAure => {

  const diccionary: SpanToAure = {
    A: "Aa",
    B: "Besh",
    C: "Cresh",
    D: "Dorn",
    E: "Een",
    F: "Forn",
    G: "Gree",
    H: "Herf",
    I: "Isk",
    J: "Jenth",
    K: "Krill",
    L: "Leth",
    M: "Mando",
    N: "Nern",
    Ñ: "Ñ",
    O: "Osk",
    P: "Pei",
    Q: "Qek",
    R: "Resh",
    S: "Senth",
    T: "Trill",
    U: "Usk",
    V: "Vev",
    W: "Wesk",
    X: "Xesh",
    Y: "Yirt",
    Z: "Zerek",
    
    
  }

  return diccionary

}

const dictAurebeshToSpanish = (): AureToSpan => {
  const diccionary: AureToSpan = {
  AA: "A",
  BESH: "B",
  CRESH: "C",
  DORN: "D",
  EEN: "E",
  FORN: "F",
  GREE: "G",
  HERF: "H",
  ISK: "I",
  JENTH: "J",
  KRILL: "K",
  LETH: "L",
  MANDO: "M",
  NERN: "N",
  Ñ: "Ñ",
  OSK: "O",
  PEI: "P",
  QEK: "Q",
  RESH: "R",
  SENTH: "S",
  TRILL: "T",
  USK: "U",
  VEV: "V",
  WESK: "W",
  XESH: "X",
  YIRT: "Y",
  ZEREK: "Z",
  

  }
  
  return diccionary
}

const transformSpanToAurebesh = (word: string, diccionary: SpanToAure): string => {
  const splitWord: string[] = word.toUpperCase().split("")

  const transformWord: string[] = []
  
  for (let letter of splitWord) {

    if (letter !== " ") {
      transformWord.push(diccionary[letter])

    }

  }

  return transformWord.join(" ")


}


const transformAureToSpan = (word: string, diccionary: AureToSpan): string => {
  const splitWord: string[] = word.toUpperCase().split(" ")
  console.log(splitWord)

  const transformWord: string[] = []
  
  for (let letter of splitWord) {
      transformWord.push(diccionary[letter])
    

  }

  return transformWord.join("").toLowerCase()

  
}

function mainF(wordSpanish: string = "hola", wordAurebesh: string = "Herf Osk Leth Aa" , aureToSpanish: boolean = true, spanToAurebesh: boolean = true): string {
  const dictSpanToAure: SpanToAure = dictSpanishToAurebesh()
  const dictAureToSpan: AureToSpan = dictAurebeshToSpanish()

  if (wordSpanish.length < 3 && wordAurebesh.length < 3) {
    console.error("Place 4 or more characters")
  }

  if (aureToSpanish && spanToAurebesh) {
    return `spanish to aurebesh: ${transformSpanToAurebesh(wordSpanish, dictSpanToAure)}, aurebesh to spanish: ${transformAureToSpan(wordAurebesh, dictAureToSpan)}`
  }

  if (aureToSpanish) {
    return transformAureToSpan(wordAurebesh, dictAureToSpan)
  } 


  return transformSpanToAurebesh(wordSpanish, dictSpanToAure)


}


console.log(mainF())