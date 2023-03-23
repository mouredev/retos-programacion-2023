/*
 * Dada una URL con parámetros, crea una función que obtenga sus valores.
 * No se pueden usar operaciones del lenguaje que realicen esta tarea directamente.
 *
 * Ejemplo: En la url https://retosdeprogramacion.com?year=2023&challenge=0
 * los parámetros serían ["2023", "0"]
 */
const url = 'https://retosdeprogramacion.com?year=2023&challenge=0'

function onlyParam(url) {
  const paramsStr = url.split('?')[1]
  const params = paramsStr.split('&')
  return params.map((param) => param.split('=')[1])
}

console.log(onlyParam(url))
