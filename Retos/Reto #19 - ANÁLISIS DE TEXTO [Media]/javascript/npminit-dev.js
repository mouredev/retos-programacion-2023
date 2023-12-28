/*
 * Crea un programa que analice texto y obtenga:
 * - Número total de palabras.
 * - Longitud media de las palabras.
 * - Número de oraciones del texto (cada vez que aparecen un punto).
 * - Encuentre la palabra más larga.
 *
 * Todo esto utilizando un único bucle.
 */

const text = `Nos encontramos en un periodo de guerra civil. Las naves espaciales rebeldes, atacando desde una base oculta, han logrado su primera victoria contra el malvado Imperio Galáctico. Durante la batalla, los espías rebeldes han conseguido apoderarse de los planos secretos del arma total y definitiva del Imperio, la ESTRELLA DE LA MUERTE, una estación espacial acorazada, llevando en sí potencia suficiente para destruir a un planeta entero. Perseguida por los siniestros agentes del Imperio, la Princesa Leia vuela hacia su patria, a bordo de su nave espacial, llevando consigo los planos robados, que pueden salvar a su pueblo y devolver la libertad a la galaxia.`

const getTextData = (text) => {
  if(text.length === 0) return [null]
  let wordsCant = 0;
  let wordsLetterSum = 0;
  let avgLettersPerWord = 0
  let prayers = 1;
  let longestWord = '';
  let longestwordaux = '';
  text = text.replace('\n', ' ')
  text = text.replace('\n', '')
  for(let i = 0; i < text.length; i++){
    if(text[i] !== '.' && text[i] !== ' ' && text[i] !== '\n') {
      wordsLetterSum++;
      longestwordaux += text[i];
    }
    if(text[i] === '.' || text[i] === ' ') {
      wordsCant++
      if(text[i] === ' ') {
        if(longestwordaux.length > longestWord.length) longestWord = longestwordaux + '';
        longestwordaux = '';
      }
      if(text[i] === '.' && text[i + 1] !== undefined && text[i + 1] !== '.') prayers++
    }
  }

  avgLettersPerWord = (wordsLetterSum / wordsCant).toFixed(2)
  return [wordsCant, avgLettersPerWord, prayers, longestWord]
}

console.log(...getTextData(text))