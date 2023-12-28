
const teclado_t9 = (bloque_pulsaciones) => {
    const dictionary = [
      [".", ",", "?", "!"],
      ["A", "B", "C"],
      ["D", "E", "F"],
      ["G", "H", "I"],
      ["J", "K", "L"],
      ["M", "N", "O"],
      ["P", "Q", "R", "S"],
      ["T", "U", "V"],
      ["W", "X", "Y", "Z"]
    ]
    const seccion_numeros = bloque_pulsaciones.split("-")
    let result = '';
    
    for (var i = 0; i < seccion_numeros.length; i++) {
      let num = seccion_numeros[i]
      let zone = num[0] -1 
      let howMany = num.length - 1
      result += dictionary[zone][howMany]
    }
    return result
  }
  
  
  
  teclado_t9("6-666-88-777-33-3-33-888")