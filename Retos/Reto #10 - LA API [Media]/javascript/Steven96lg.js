
/*
 * Llamar a una API es una de las tareas más comunes en programación.
 *
 * Implementa una llamada HTTP a una API (la que tú quieras) y muestra su
 * resultado a través de la terminal. Por ejemplo: Pokémon, Marvel...
 *
 * Aquí tienes un listado de posibles APIs: 
 * https://github.com/public-apis/public-apis
 */

// Funcion para llamar la API


const getAPI = async (url) => {
    try{
      const response = await fetch(url)
      const characters = await response.json()
      console.log(characters)
    }catch(err){
      console.log(err)
    }
}

//Rick and Morty API
const api = "https://rickandmortyapi.com/api/character/"

getAPI(api)