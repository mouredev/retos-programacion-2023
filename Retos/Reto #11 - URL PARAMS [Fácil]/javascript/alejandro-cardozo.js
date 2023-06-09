/*
 * Dada una URL con parámetros, crea una función que obtenga sus valores.
 * No se pueden usar operaciones del lenguaje que realicen esta tarea directamente.
 *
 * Ejemplo: En la url https://retosdeprogramacion.com?year=2023&challenge=0
 * los parámetros serían ["2023", "0"]
 */

/**
 * This function returns an array containing the values of the parameters in an url
 * @param  {String} url the url to analyze
 * @return {Array}     an array with the values of the parameters in the passed url
 */
function getParams(url) {
  if (url.indexOf('?') === -1) return [];
  const params = url.slice(url.indexOf('?') + 1).split('&');
  return params?.map((el) => el.slice(el.indexOf('=') + 1));
}

// Tests
console.log(getParams('https://retosdeprogramacion.com'));
console.log(getParams('https://retosdeprogramacion.com?year=2023&challenge=0'));
console.log(getParams('https://www.patreon.com/artechnaut/posts?filters%5Btag%5D=Battle'));
console.log(getParams('https://www.youtube.com/results?search_query=mouradev'));
console.log(getParams('https://www.youtube.com/watch?v=4Azc4Gs2nlU&t=334s'));
