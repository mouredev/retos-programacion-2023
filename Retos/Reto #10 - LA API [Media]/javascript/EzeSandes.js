/*
 * Llamar a una API es una de las tareas más comunes en programación.
 *
 * Implementa una llamada HTTP a una API (la que tú quieras) y muestra su
 * resultado a través de la terminal. Por ejemplo: Pokémon, Marvel...
 *
 * Aquí tienes un listado de posibles APIs:
 * https://github.com/public-apis/public-apis
 */

const API_URL = 'https://v2.jokeapi.dev/joke/Programming';

async function fetchData(url, options = undefined) {
  try {
    const res = await fetch(url, options);
    if (!res.ok) throw new Error('⛔ERROR RESPONSE DATA⛔');

    return await res.json();
  } catch (error) {
    console.log(error.message);
  }
}

fetchData(API_URL)
  .then(data => {
    if (data.error) throw new Error('⛔DATA ERROR⛔');

    console.log(data);
  })
  .catch(error => console.log(error.message));
