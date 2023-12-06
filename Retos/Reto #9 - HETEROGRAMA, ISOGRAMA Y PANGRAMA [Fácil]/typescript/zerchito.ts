/*
 * Crea 3 funciones, cada una encargada de detectar si una cadena de
 * texto es un heterograma, un isograma o un pangrama.
 * - Debes buscar la definición de cada uno de estos términos.
 */

class StringChecker {
  /**
   * Heterograma: does not repeat a letter
   * @param phrase 
   */
  isHeterograma(phrase: string): boolean {
    phrase = phrase.toLowerCase();
    const lettersSet = new Set();
    let isHeterogram = true;
    for(let index = 0; index < phrase.length; index++){
      const letter = phrase.charAt(index);
      if(lettersSet.has(letter)){
        isHeterogram = false;
        break;
      }
      lettersSet.add(letter);
    }
    return isHeterogram;
  }
  /**
   * Isograma: All letters are repeated the same amount
   * @param phrase 
   */
  isIsograma(phrase: string) {
    phrase = phrase.toLowerCase();
    let hashMap = {}
    for(let index = 0; index < phrase.length; index++){
      const letter = phrase.charAt(index);
      if(!hashMap[letter]) {
        hashMap[letter] = 0;
      }
      hashMap[letter]++;
    }
    const keys = Object.keys(hashMap);
    const quantity = hashMap[keys[0]];
    const total = keys.reduce(
      (prev, curr, i) => { return prev + hashMap[curr] }, 
      0
    );
    return quantity === (total/keys.length);
  }
  /**
    * Pangrama: contains all letters of the alphabet
    * @param phrase 
  */
  isPangrama(phrase: string) {
    phrase = phrase.toLowerCase();
    const spanishAlphabet = new Set('abcdefghijklmnñopqrstuvwxyz')
    const letters = new Set(phrase.toLowerCase());
    let isPangram = true;
    for (const letter of spanishAlphabet) {
      if (!letters.has(letter)) { 
        isPangram = false;
        break;
      }
    }
    return isPangram
  }
}

const checker = new StringChecker();

console.log('Check heterograma', checker.isHeterograma('jumped'));
console.log('Check heterograma', checker.isHeterograma('banana'));
console.log('Check isograma', checker.isHeterograma('ambidextrous'));
console.log('Check isograma', checker.isHeterograma('mississippi'));
console.log('Check pangrama', checker.isHeterograma('El veloz murciélago hindú comía feliz cardillo y kiwi. La cigüeña tocaba el saxofón detrás del palenque de paja.'));
console.log('Check pangrama', checker.isHeterograma('La casa es grande y luminosa.'));