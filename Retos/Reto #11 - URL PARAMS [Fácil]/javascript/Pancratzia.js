/*
 * Dada una URL con parámetros, crea una función que obtenga sus valores.
 * No se pueden usar operaciones del lenguaje que realicen esta tarea directamente.
 *
 * Ejemplo: En la url https://retosdeprogramacion.com?year=2023&challenge=0
 * los parámetros serían ["2023", "0"]
 */

function getParameters(url) {
    const paramsString = url.split('?')[1];
    if (!paramsString) {
      return "No hay parámetros";
    }
  
    const paramPairs = paramsString.split('&');
  
    const result = [];
    for (const paramPair of paramPairs) {
      const [key, value] = paramPair.split('=');
      if (key !== "") {
        if (value !== undefined && value !== "") {
          result.push(value);
        }
      }
    }
  
    if (result.length === 0) {
      return "Los parámetros no están definidos";
    }
  
    return result;
  }
  
  // Ejemplos de uso
  console.log(getParameters("https://retosdeprogramacion.com?year=2023&challenge=0"));
  console.log(getParameters("https://retosdeprogramacion.com?year=2023&challenge=0&user=3"));
  console.log(getParameters("https://retosdeprogramacion.com?year=2023&challenge=0&user="));
  console.log(getParameters("https://retosdeprogramacion.com"));
  console.log(getParameters("https://retosdeprogramacion.com?"));
  console.log(getParameters("https://retosdeprogramacion.com?year=2023"));
  console.log(getParameters("https://retosdeprogramacion.com?year=2023&"));
  console.log(getParameters("https://retosdeprogramacion.com?year=&"));  