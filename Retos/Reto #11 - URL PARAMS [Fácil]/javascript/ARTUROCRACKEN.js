/*
 * Dada una URL con parámetros, crea una función que obtenga sus valores.
 * No se pueden usar operaciones del lenguaje que realicen esta tarea directamente.
 *
 * Ejemplo: En la url https://retosdeprogramacion.com?year=2023&challenge=0
 * los parámetros serían ["2023", "0"]
 */

const url = "https://retosdeprogramacion.com?year=2023&challenge=0";

function getParams(url) {
  let params = [];
  const regex = /[?&]([^=#&]+)=([^&#]*)/g;
  let coincidencias;

  while ((coincidencias = regex.exec(url)) !== null) {
    let clave = decodeURIComponent(coincidencias[1]);
    let valor = decodeURIComponent(coincidencias[2]);
    params.push(valor);
  }

  return console.log(params);
}

getParams(url);
