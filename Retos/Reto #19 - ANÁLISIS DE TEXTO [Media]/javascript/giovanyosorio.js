/*
 * Crea un programa que analice texto y obtenga:
 * - Número total de palabras.
 * - Longitud media de las palabras.
 * - Número de oraciones del texto (cada vez que aparecen un punto).
 * - Encuentre la palabra más larga.
 *
 * Todo esto utilizando un único bucle.
 */

function analizar(texto){
    const palabras=texto.split(" ")
    let sentences=texto.split(".")
    let mayor=palabras[0]
    
   for(let i=0;i<palabras.length;i++){
    // console.log(palabras[i])
      if(palabras[i].length>mayor.length){
         mayor=palabras[i]
      }
   }  
    //console.log(palabras)
    //console.log(palabras.join("").length)
    //console.log(palabras.length)
    let average=palabras.join("").length/palabras.length
    console.log("Longitud media de palabras: "+average)
    console.log("Numero total de palabras: "+texto.split(" ").length)
     console.log("letra mayor: "+mayor)
    console.log("numero de oraciones del texto: "+sentences.length)
  }
  
  analizar("Crea un programa que analice texto y obtenga:  Número total de palabras.  Longitud media de las palabras.  Número de oraciones del texto(cada vez que aparecen un punto). Encuentre la palabra más larga (Supercalifragilisticoespialidoso). Todo esto utilizando un único bucle.")
  
  