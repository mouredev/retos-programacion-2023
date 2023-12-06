/*
 * Dada una URL con parámetros, crea una función que obtenga sus valores.
 * No se pueden usar operaciones del lenguaje que realicen esta tarea directamente.
 *
 * Ejemplo: En la url https://retosdeprogramacion.com?year=2023&challenge=0
 * los parámetros serían ["2023", "0"]
 */

const queryParamParser = (url: string, onlyValues: boolean = false) => {
  const urlParts = url.split('?');
  const queryParams = urlParts[1].split('&');
  const params: Record<string, string> = {};
  queryParams.forEach((param) => {
    const [key, value] = param.split('=');
    params[key] = value;
  })

  if (onlyValues) {
    return Object.values(params);
  }

  return params;
}



const url = 'https://www.google.com/search?q=typescript&oq=typescript&aqs=chrome..69i57j0l5.1009j0j7&sourceid=chrome&ie=UTF-8';

console.log(queryParamParser(url));
console.log(queryParamParser(url, true));