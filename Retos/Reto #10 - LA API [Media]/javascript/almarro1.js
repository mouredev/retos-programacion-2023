/*
 * Llamar a una API es una de las tareas más comunes en programación.
 *
 * Implementa una llamada HTTP a una API (la que tú quieras) y muestra su
 * resultado a través de la terminal. Por ejemplo: Pokémon, Marvel...
 *
 * Aquí tienes un listado de posibles APIs:
 * https://github.com/public-apis/public-apis
 */

const SERVICE_URL = 'https://www.dnd5eapi.co/api/monsters';
fetch(SERVICE_URL).then(async (response) => {
  console.log(await response.json());
});
