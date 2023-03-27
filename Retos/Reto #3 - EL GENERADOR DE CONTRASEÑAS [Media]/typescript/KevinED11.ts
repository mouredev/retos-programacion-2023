  /*
  * Escribe un programa que sea capaz de generar contraseñas de forma aleatoria.
  * Podrás configurar generar contraseñas con los siguientes parámetros:
  * - Longitud: Entre 8 y 16.
  * - Con o sin letras mayúsculas.
  * - Con o sin números.
  * - Con o sin símbolos.
  * (Pudiendo combinar todos estos parámetros entre ellos)
  */




  const passwordGenerator = (longitud: number = 10, uppercase: boolean = true, 
      numeros: boolean = true, simbols: boolean= true): string => {

    if (longitud > 8 && longitud <= 16) {

      let password: string = ""
      let characters = "abcdefghijklmnopqrstuvwxyz"
      
      characters += (numeros ? "0123456789" : "") 
      + (simbols ? "!@#$%^&*()_+-={}[]|\\:;\\\">,.?/": "") 
      + (uppercase ? "ABCDEFGHIJKLMNOPQRSTUVWXYZ" : "")
    
      for (let i = 0; i < longitud; i++ ) {
        password += characters.charAt(Math.floor(Math.random() * characters.length))
        

    } 
      return password

    } 

    return "Coloca entre 8 y 16 caracteres de longitud"

  }

  console.log(passwordGenerator(15))