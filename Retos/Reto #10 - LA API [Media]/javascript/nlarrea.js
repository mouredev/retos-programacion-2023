/*
 * Llamar a una API es una de las tareas más comunes en programación.
 *
 * Implementa una llamada HTTP a una API (la que tú quieras) y muestra su
 * resultado a través de la terminal. Por ejemplo: Pokémon, Marvel...
 *
 * Aquí tienes un listado de posibles APIs: 
 * https://github.com/public-apis/public-apis
 */

let pokemonName = prompt("Enter a Pokemon name: ");

const getData = fetch(`https://pokeapi.co/api/v2/pokemon/${pokemonName.toLowerCase()}`);

getData
    .then(data => data.json())
    .then(data => {
        console.log(data);
    })
    .catch(err => {
        console.error(err);
    });