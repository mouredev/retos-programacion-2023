/*
 * Dada una URL con parámetros, crea una función que obtenga sus valores.
 * No se pueden usar operaciones del lenguaje que realicen esta tarea directamente.
 *
 * Ejemplo: En la url https://retosdeprogramacion.com?year=2023&challenge=0
 * los parámetros serían ["2023", "0"]
 */


function getQueryParams(param_url) {
  if(!param_url.includes("?")) return "No hay parámetros en la URL";
  let parts = param_url.split("?")[1].split("&");
  let url_params = parts.map(param => param.split("=")[1]);
  return url_params;
}

console.log(getQueryParams("https://retosdeprogramacion.com?year=2023&challenge=0"));