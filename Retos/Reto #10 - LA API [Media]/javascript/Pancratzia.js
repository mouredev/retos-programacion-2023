/*
 * Llamar a una API es una de las tareas más comunes en programación.
 *
 * Implementa una llamada HTTP a una API (la que tú quieras) y muestra su
 * resultado a través de la terminal. Por ejemplo: Pokémon, Marvel...
 *
 * Aquí tienes un listado de posibles APIs: 
 * https://github.com/public-apis/public-apis
 * 
 * 
 * Realizado por Laura Ortega - 27/08/2023
 */


async function isEven(number) {
    try {
        const response = await fetch(`https://api.isevenapi.xyz/api/iseven/${number}/`);
        const data = await response.json();
        console.log(`BEFORE KNOWING WE HAVE AN AD: ${data.ad}\nAFTER THAT, THE NUMBER ${number} IS EVEN: ${data.iseven}`);
    } catch (error) {
        console.log(error);
    }
}

isEven(Math.floor(Math.random() * 1000000));