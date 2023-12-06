/*
 * Dada una URL con parámetros, crea una función que obtenga sus valores.
 * No se pueden usar operaciones del lenguaje que realicen esta tarea directamente.
 *
 * Ejemplo: En la url https://retosdeprogramacion.com?year=2023&challenge=0
 * los parámetros serían ["2023", "0"]
 */

type UrlParams = (url: string) => string[]

const urlParams: UrlParams = (url: string): string[] | [] => {
  try {
    const value: string = url.split("?")[1]
    if (!value) return []


    const queryParams: string[] = value.split("&")



    const valuesOfQuery: string[] = []  
    
    for (let valueQuery of queryParams) {
      const valueParam: string = valueQuery.split("=")[1] 
      valuesOfQuery.push(valueParam)
    }

    return valuesOfQuery

  } catch(err) {
    console.error(err)
    return []
  }





}

console.log(urlParams("https://retosdeprogramacion.com?year=2023&challenge=0&dinero=45"))

console.log(urlParams("https://retosdeprogramacion.com"))