const removeDiacritics = (cadena) => {
  const diacriticos = {
    'á': 'a', 'é': 'e', 'í': 'i', 'ó': 'o', 'ú': 'u',
    'à': 'a', 'è': 'e', 'ì': 'i', 'ò': 'o', 'ù': 'u',
    'ä': 'a', 'ë': 'e', 'ï': 'i', 'ö': 'o', 'ü': 'u',
    'â': 'a', 'ê': 'e', 'î': 'i', 'ô': 'o', 'û': 'u',
    'ã': 'a', 'ñ': 'n', 'õ': 'o',
    'ç': 'c'
  };

  return cadena.split('')
    .map(caracter => diacriticos[caracter] || caracter)
    .join('');
}

const isHeterogram = (cadena) => cadena.length === new Set(removeDiacritics(cadena)).size;

const isIsogram = (cadena) => {
  const letras_vistas = new Set();
  return !Array.from(removeDiacritics(cadena), letra => {
    if (letras_vistas.has(letra)) {
      return false;
    } else {
      letras_vistas.add(letra);
      return true;
    }
  }).includes(false);
}

const isPangram = (cadena) => {
  const alfabeto = new Set('abcdefghijklmnopqrstuvwxyz');
  return Array.from(removeDiacritics(cadena.toLowerCase()), letra => {
    if (alfabeto.has(letra)) {
      alfabeto.delete(letra);
    }
    return alfabeto.size === 0;
  }).includes(true);
}

const string1 = "murcielago";
const string2 = "esdrújula";
const string3 = "El veloz murciélago hindú comía feliz cardillo y kiwi. La cigüeña tocaba el saxofón detrás del palenque de paja";

console.log(isHeterogram(string1)); // true
console.log(isHeterogram(string2)); // false
console.log(isIsogram(string1)); // true
console.log(isIsogram(string2)); // false
console.log(isPangram(string3)); // true
