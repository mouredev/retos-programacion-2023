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
    for (var i = 0; i < seccion_numeros.length; i++) {
      let num = seccion_numeros[i]
      let howMany = num.length
      console.log(howMany)
      console.log(dictionary[howMany][0])
      
    }
  }
  
  
  
  teclado_t9("6-666-88-777-33-3-33-888")