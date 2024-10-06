/*
 * Dada una URL con parámetros, crea una función que obtenga sus valores.
 * No se pueden usar operaciones del lenguaje que realicen esta tarea directamente.
 *
 * Ejemplo: En la url https://retosdeprogramacion.com?year=2023&challenge=0
 * los parámetros serían ["2023", "0"]
 */

const url =
  'https://retosdeprogramacion.com?year=2023&challenge=11&language=javascript&posted=true';

const myData = () => {
  let final = [];

  const data = url.split('?');
  const data2 = data[1].split('&');
  const doingMap = data2.map((x) => x.split('='));
  doingMap.map((x) => {
    final.push(x[1]);
  });
  console.log(final);
};

myData();
