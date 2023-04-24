/*

  Dada una URL con parámetros, crea una función que obtenga sus valores.
  No se pueden usar operaciones del lenguaje que realicen esta tarea directamente.
 
  Ejemplo: En la url https://retosdeprogramacion.com?year=2023&challenge=0
  los parámetros serían ["2023", "0"] 

*/


function urlParametros(url){
    let arrParametros = []
    let urlS = url.indexOf("?")

    if(urlS === -1){
      return arrParametros
    }

    let subUrl = url.substring(urlS+1)
    let arrSub = subUrl.split("&")
    
    arrSub.map((el)=>{
      let dib = el.split("=")
      arrParametros.push(dib[1])
    })

    return arrParametros
}

console.log(urlParametros("https://retosdeprogramacion.com?year=2023&challenge=0"))
console.log(urlParametros("https://www.youtube.com/watch?v=zj14pKjAETw"))
console.log(urlParametros("https://swapi.dev/api/people/?search=r2"))
console.log(urlParametros("https://fonts.google.com/icons?icon.query=s"))