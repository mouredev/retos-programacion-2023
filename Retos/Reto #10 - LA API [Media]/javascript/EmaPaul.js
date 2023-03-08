/*
 Llamar a una API es una de las tareas más comunes en programación.
 
  Implementa una llamada HTTP a una API (la que tú quieras) y muestra su
  resultado a través de la terminal. Por ejemplo: Pokémon, Marvel...
 
  Aquí tienes un listado de posibles APIs: 
  https://github.com/public-apis/public-apis

*/

import fetch from "node-fetch";

/*Trae los personajes de star wars y los filtra por id y nombre*/
async function personajes(id = null, name = null) {
  try {
    let url 
    if(id){
        url = `https://swapi.dev/api/people/${id}`
    }else{
        url = 'https://swapi.dev/api/people/'
        if (name) {
            url += `?search=${name}`;
        }
    }
    const res = await fetch(url);
    const data = await res.json();
    let resultados
    if(id){
        resultados = {
            name: data.name,
            height: data.height,
            mass: data.mass,
        };
    }else{
        resultados = data.results.map((person) => ({
            name: person.name,
            height: person.height,
            mass: person.mass,
          }));
    }
    console.log(resultados);
  } catch (error) {
    console.error(error);
  }
}

personajes(); // trae todos los personajes
personajes(2) // tare un personaje por id
personajes(null,"Skywalker") // trae los personajes que coincidan con el nombre