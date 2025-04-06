/*
 * Dada una URL con parámetros, crea una función que obtenga sus valores.
 * No se pueden usar operaciones del lenguaje que realicen esta tarea directamente.
 *
 * Ejemplo: En la url https://retosdeprogramacion.com?year=2023&challenge=0
 * los parámetros serían ["2023", "0"]
 */
const url = "https://retosdeprogramacion.com?year=2023&challenge=0"

function getParamUrl(url: string){
    let arParam: Array<string> = []
    if(!url.includes("?")) return [] //Valida que la URL si tenga parametros (?)

    let parametros = (url.split("?")[1].split("&"))
    for (const item of parametros) {
        arParam.push(item.split("=")[1])
    }
    return arParam
}

function getParamUrlv2(url: string) {
    if(!url.includes("?")) return [] //Valida que la URL si tenga parametros (?)
    const [, parametros] = url.split("?");
    return parametros.split("&").map(par => par.split("=")[1]);
}

console.log(getParamUrlv2(url))