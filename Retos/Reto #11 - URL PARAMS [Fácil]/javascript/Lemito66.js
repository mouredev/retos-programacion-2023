/*
 * Dada una URL con parámetros, crea una función que obtenga sus valores.
 * No se pueden usar operaciones del lenguaje que realicen esta tarea directamente.
 *
 * Ejemplo: En la url https://retosdeprogramacion.com?year=2023&challenge=0
 * los parámetros serían ["2023", "0"]
 */

const detectParameters = (url) => {
  let parameters = [];
  let urlParams = url.split("&");
  for (urlParam of urlParams) {
        if (urlParam.includes("=")) {
            urlParameter = urlParam.split('=');
            if (urlParameter.length  == 2 && urlParameter[1] !== "") {
                parameters.push(urlParameter[1]);
            }
        }
        
    }
  return parameters;
};

console.log(
  detectParameters(
    "https://retosdeprogramacion.com?year=2023&challenge=0&Lemito66=Fantastic&5="
  )
);
