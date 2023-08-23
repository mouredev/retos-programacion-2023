/*
 * Llamar a una API es una de las tareas más comunes en programación.
 *
 * Implementa una llamada HTTP a una API (la que tú quieras) y muestra su
 * resultado a través de la terminal. Por ejemplo: Pokémon, Marvel...
 *
 * Aquí tienes un listado de posibles APIs:
 * https://github.com/public-apis/public-apis
 */

async function apiCall() {
  const response = await fetch("https://techy-api.vercel.app/api/json");
  const jsonData = await response.json();
  console.log(jsonData?.message);
}

apiCall();
