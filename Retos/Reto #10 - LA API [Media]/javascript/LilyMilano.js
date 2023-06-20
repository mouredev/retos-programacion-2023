/*
 * Llamar a una API es una de las tareas más comunes en programación.
 *
 * Implementa una llamada HTTP a una API (la que tú quieras) y muestra su
 * resultado a través de la terminal. Por ejemplo: Pokémon, Marvel...
 *
 * Aquí tienes un listado de posibles APIs:
 * https://github.com/public-apis/public-apis
 */

//? About Catboys.com:
//? Started by a Catboy named Kristian (aka Beyondtoshi), our goal is to create a website and community dedicated to catboys, catboy lovers, and enthusiasts! Nya~
//? API: https://api.catboys.com/img

//? GET/img Returns a random image of a catboy and the artist's data.

// ::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::

const getCatboyImageUrl = 'https://api.catboys.com/img';

fetch(getCatboyImageUrl)
	.then(async (response) => await response.json())
	.then((response) => {
		console.log(response);
	})
    .catch((error)=>(console.log(error)))

// ::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::

//   Log:
// { url: 'https://cdn.catboys.com/images/image_136.jpg',
//   artist: 'Heidi',
//   artist_url: 'https://www.pixiv.net/en/users/19044504',
//   source_url: 'https://www.pixiv.net/en/artworks/92283998',
//   error: 'none' }
