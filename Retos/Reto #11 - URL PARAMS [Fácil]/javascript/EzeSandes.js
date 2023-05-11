/*
 * Dada una URL con parámetros, crea una función que obtenga sus valores.
 * No se pueden usar operaciones del lenguaje que realicen esta tarea directamente.
 *
 * Ejemplo: En la url https://retosdeprogramacion.com?year=2023&challenge=0
 * los parámetros serían ["2023", "0"]
 */

const URL = 'https://retosdeprogramacion.com?year=2023&challenge=0';

/**
 *
 * @param {String} url
 */
function getValues(url) {
  const res = [];

  let paramStartIdx = url.indexOf('?');

  if (paramStartIdx === -1) return [];

  while (paramStartIdx < url.length) {
    while (paramStartIdx < url.length && url[paramStartIdx] != '=') {
      paramStartIdx++;
    }

    if (paramStartIdx === url.length) return res;

    let endParam = paramStartIdx;

    while (endParam < url.length && url[endParam] != '&') {
      endParam++;
    }

    res.push(url.slice(paramStartIdx + 1, endParam));

    paramStartIdx++;
  }

  return res;
}

console.log(getValues(URL)); // [ '2023', '0' ]
console.log(getValues('https://retosdeprogramacion.com')); // []
console.log(getValues('https://retosdeprogramacion.com?year=2023')); // [ '2023' ]
console.log(
  getValues('https://retosdeprogramacion.com?year=2023&age=18&name=Ezequiel') // [ '2023', '18', 'Ezequiel' ]
);
console.log(
  getValues('https://retosdeprogramacion.com?year=2023&age=18&name=john%20cena') // [ '2023', '18', 'john%20cena' ]
);
