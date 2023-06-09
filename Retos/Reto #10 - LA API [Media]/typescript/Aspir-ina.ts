/*
 * Llamar a una API es una de las tareas más comunes en programación.
 *
 * Implementa una llamada HTTP a una API (la que tú quieras) y muestra su
 * resultado a través de la terminal. Por ejemplo: Pokémon, Marvel...
 *
 * Aquí tienes un listado de posibles APIs:
 * https://github.com/public-apis/public-apis
 *
 * Se ha escogido: https://api.chucknorris.io/
 */

import https from 'https';
import fetch from 'node-fetch';

const RANDOM_JOKE_URL = 'https://api.chucknorris.io/jokes/random';
const chuckNorrisJokes = () => {
  https.get(RANDOM_JOKE_URL, (res) => {
    let data = '';
    res.on('data', (chunk) => {
      data += chunk;
    });
    res.on('end', () => {
      const joke = JSON.parse(data);
      console.log(joke.value);
    });
  }).on('error', (err) => {
    console.log('Error: ' + err.message);
  });
}

const chuckNorrisJokes2 = async () => {
  const response= await fetch(RANDOM_JOKE_URL);
  const data: any = await response.json();
  console.log(data.value);
}

chuckNorrisJokes();
chuckNorrisJokes2();