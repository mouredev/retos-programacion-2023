/*
 * Dada una URL con parámetros, crea una función que obtenga sus valores.
 * No se pueden usar operaciones del lenguaje que realicen esta tarea directamente.
 *
 * Ejemplo: En la url https://retosdeprogramacion.com?year=2023&challenge=0
 * los parámetros serían ["2023", "0"]
 */

// I created a new scope with the { } because of duplicated param name Error
{
  function getParams(url: string): string[] {
    const urlSplited = url.split('?');
    const queryParams = urlSplited[1]?? '';
    const paramsList = queryParams.split('&');
    const paramsValues = paramsList.map((param: string) => {
      const paramParts = param.split('=');
      return paramParts[1] ?? '';
    });
    return paramsValues;
  } 

  const url = 'https://retosdeprogramacion.com?year=2023&challenge=0';
  const params = getParams(url);
  console.log(params);
}
