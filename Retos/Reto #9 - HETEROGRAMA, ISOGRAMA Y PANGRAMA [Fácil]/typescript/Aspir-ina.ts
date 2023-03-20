/*
 * Crea 3 funciones, cada una encargada de detectar si una cadena de
 * texto es un heterograma, un isograma o un pangrama.
 * - Debes buscar la definición de cada uno de estos términos.
 */

const isHeterogram = (text: string): boolean => {
  const letters = text.toLowerCase().split('');
  const uniqueLetters = new Set(letters);
  return letters.length === uniqueLetters.size;
}

const isIsogram = (text: string) => {
  const letters = text.toLowerCase().split('');
  type Isogram = {
    [key: string]: number;
  }
  const lettersCounter: Isogram = letters.reduce((acc: Isogram, letter: string): Isogram => {
    if (letter === ' ' || letter === '-' || letter === '.' || letter === ',') {
      return acc;
    }
    acc[letter] = (acc[letter] && acc[letter] + 1) || 1;
    return acc;
  }, {});
  const letterCounterValues = Object.values(lettersCounter).filter((value: number) => value > 1);
  const isIsogram = Math.min(...letterCounterValues) === Math.max(...letterCounterValues);
  return {isogramStatus: isIsogram, isogramLevel: (isIsogram && Math.min(...letterCounterValues)) || 0};
}

const isPangram = (text: string): boolean => {
  const abecedario = 'abcdefghijklmnñopqrstuvwxyz';
  const letters = text.toLowerCase().replace(/[^a-z|ñ]+/gi, '').split('');
  const uniqueLetters = new Set(letters);

  return uniqueLetters.size === abecedario.length;
}

const textEvaluation = (text: string): string => {
  const isHeterogramResult = isHeterogram(text);
  const {isogramStatus, isogramLevel} = isIsogram(text);
  const isPangramResult = isPangram(text);
  let result = '';

  result += isHeterogramResult ? 'Heterograma ' : '';
  result += isogramStatus ? `Isograma de nivel ${isogramLevel}` : '';
  result += isPangramResult ? 'Pangrama ' : '';

  return result;
}

const ej: string = 'abcdefghijklmnñopqrstuvwxyz';
const ej1: string = 'yuxtaponer';
const ej2: string = 'acondicionar';
const ej3: string = 'Fabio me exige, sin tapujos, que añada cerveza al whisky';

console.log(`${ej}: ${textEvaluation(ej)}`);
console.log(`${ej1}: ${textEvaluation(ej1)}`);
console.log(`${ej2}: ${textEvaluation(ej2)}`);
console.log(`${ej3}: ${textEvaluation(ej3)}`);