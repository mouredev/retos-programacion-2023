/*
 * Dada una URL con parámetros, crea una función que obtenga sus valores.
 * No se pueden usar operaciones del lenguaje que realicen esta tarea directamente.
 *
 * Ejemplo: En la url https://retosdeprogramacion.com?year=2023&challenge=0
 * los parámetros serían ["2023", "0"]
 */

// getting params using split and map
const getParams = (url) => {
  const params = url.split('?')[1]?.split('&');
  return params && params.every((param) => param.length > 0)
    ? params.map((param) => param.split('=')[1])
    : [];
};

// getting params using URL API
const getParamsAPI = (url) => {
  const paramsArray = [];
  const params = new URL(url).searchParams;
  params.forEach((param) => paramsArray.push(param));
  return paramsArray;
};

// Visita mi repo en GitHub para ver y correr los tests de este código --> https://github.com/marcode24/weekly-challenges
