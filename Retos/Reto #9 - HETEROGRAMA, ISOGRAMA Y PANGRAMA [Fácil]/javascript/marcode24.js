/*
 * Crea 3 funciones, cada una encargada de detectar si una cadena de
 * texto es un heterograma, un isograma o un pangrama.
 * - Debes buscar la definición de cada uno de estos términos.
 */

const isHeterogram = (str) => {
  const strArr = [...str.trim().toLowerCase().replace(/\s/g, '')];
  const strSet = new Set(strArr);
  return strArr.length === strSet.size;
};

const isIsogram = (str) => isHeterogram(str);

const isPangram = (str) => {
  str = str.normalize('NFD').replace(/[\u0300-\u036f]/g, '');
  str = str.replace(/[\d\W]/g, '').trim();
  const strArr = [...str.trim().toLowerCase().replace(/\s/g, '')];
  const strSet = new Set(strArr);
  return strSet.size === 26;
};

// Visita mi repo en GitHub para ver y correr los tests de este código --> https://github.com/marcode24/weekly-challenges
