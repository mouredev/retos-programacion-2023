/*
 * Llamar a una API es una de las tareas más comunes en programación.
 *
 * Implementa una llamada HTTP a una API (la que tú quieras) y muestra su
 * resultado a través de la terminal. Por ejemplo: Pokémon, Marvel...
 *
 * Aquí tienes un listado de posibles APIs:
 * https://github.com/public-apis/public-apis
 */

const myMethod = async () => {
  const request = await fetch('https://reqres.in/api/users?page=1', {
    method: 'GET',
  });
  return request;
};

const response = async () => {
  const response = await myMethod();
  const jsonData = await response.json();
  const data = jsonData.data;
  console.log(data);
};

const main = () => {
  response();
};

main();
