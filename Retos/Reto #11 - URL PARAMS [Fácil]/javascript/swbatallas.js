/*
 * Dada una URL con parámetros, crea una función que obtenga sus valores.
 * No se pueden usar operaciones del lenguaje que realicen esta tarea directamente.
 *
 * Ejemplo: En la url https://retosdeprogramacion.com?year=2023&challenge=0
 * los parámetros serían ["2023", "0"]
 */

const url = "https://retosdeprogramacion.com?year=2023&challenge=0"

function extractParams(url) {
    let urlArray = url.split("?")
    let paramsArray = urlArray[1]
    paramsArray = paramsArray.split("&")
    let paramObj = {}
    for (let param of paramsArray) {
        let getParam = param.split("=")
        console.log(getParam)
        paramObj[getParam[0]] = getParam[1]
    }
    return `en la url ${url}, estan los parametros ${Object.keys(paramObj)} y los valores ${Object.values(paramObj)}`
}

console.log(extractParams(url))