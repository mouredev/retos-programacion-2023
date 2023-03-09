/*
 Llamar a una API es una de las tareas más comunes en programación.

  Implementa una llamada HTTP a una API (la que tú quieras) y muestra su
  resultado a través de la terminal. Por ejemplo: Pokémon, Marvel...

  Aquí tienes un listado de posibles APIs:
  https://github.com/public-apis/public-apis

*/

const fetch = require('node-fetch');

// API de Star Wars
const URL_API = 'https://swapi.dev/api/people/1/';

const getLuke = async () => {
  const response = await fetch(URL_API);
  const data = await response.json();
  return data;
};

// Visita mi repo en GitHub para ver y correr los tests de este código --> https://github.com/marcode24/weekly-challenges
