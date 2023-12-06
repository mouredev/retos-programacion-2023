/*
 * Dada una URL con parámetros, crea una función que obtenga sus valores.
 * No se pueden usar operaciones del lenguaje que realicen esta tarea directamente.
 *
 * Ejemplo: En la url https://retosdeprogramacion.com?year=2023&challenge=0
 * los parámetros serían ["2023", "0"]
 */



function getParams(url) {

    let params = []
    let urlParams = url.split("?")[1].split("&")
    urlParams.forEach((item) => {
        params.push(item.split("=")[1])
        console.log("params " + params)
        console.log("item " + item)
    })
    console.log(params)

}

console.log(getParams('https://retosdeprogramacion.com?year=2023&challenge=0'))
console.log(getParams('https://retosdeprogramacion.com?year=2023&challenge=0&name=giovany'))
console.log(getParams('https://retosdeprogramacion.com?year=2023&challenge=0&name=giovany&lastname=osorio'))