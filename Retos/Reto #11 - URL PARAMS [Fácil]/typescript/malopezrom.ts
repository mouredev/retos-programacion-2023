/*
 * Dada una URL con parámetros, crea una función que obtenga sus valores.
 * No se pueden usar operaciones del lenguaje que realicen esta tarea directamente.
 *
 * Ejemplo: En la url https://retosdeprogramacion.com?year=2023&challenge=0
 * los parámetros serían ["2023", "0"]
 */


/**
 * Función que obtiene los parámetros de una URL usando expresiones regulares
 * @param url
 * @returns {string[][]} Array de arrays con los parámetros y sus valores
 */
function getParams(url: string): string[][] {
    const urlRegex = new RegExp("^(https?:\\/\\/)?([\\da-z\\.-]+)\\.([a-z\\.]{2,6})([\\/\\w\\.-]*)*\\/?\\?(.*)$");
    if (urlRegex.test(url)) {
        const paramsRegex = /([?&])([^=]+)=([^&]+)/g;

        const params = url.match(paramsRegex)

        if(params){

            return params.map(param =>  [param.substring(1).split("=")[0],param.split("=")[1]])
        }
        else{
            return []
        }

    }
    else{
        return []
    }

}

/**
 * Ejemplo de uso
 */
console.log(getParams("https://retosdeprogramacion.com?year=2023&challenge=0"))