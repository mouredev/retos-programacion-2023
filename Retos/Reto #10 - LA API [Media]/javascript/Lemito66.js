/*
 * Llamar a una API es una de las tareas más comunes en programación.
 *
 * Implementa una llamada HTTP a una API (la que tú quieras) y muestra su
 * resultado a través de la terminal. Por ejemplo: Pokémon, Marvel...
 *
 * Aquí tienes un listado de posibles APIs:
 * https://github.com/public-apis/public-apis
 */

const url = "https://jsonplaceholder.typicode.com/posts";

const api = async (id) => {
  if (id > 100)
    return "Lo sentimos, el id no existe, ingrese un id entre 1 y 100";
  try {
    const response = await fetch(`${url}/${id}`);
    const data = await response.json();
    return `Usuario Id: ${data.userId}\nId: ${data.id}\nTítulo: ${data.title} \nCuerpo: ${data.body}`;
  } catch (error) {
    return error;
  }
};

(async () => {

  console.log(await api(5));
  
})();
