function cifrar(palabra, clave){
  let letra,respuesta=""
  let alfabeto = 'abcdefghijklmnopqrstuvwxyz';
  let cifrado=alfabeto.slice(-clave)
  console.log(cifrado)
  cifrado+=alfabeto.slice(0,alfabeto.length-clave)
   console.log("cifrado "+ cifrado)
  console.log(palabra.length)
  
  for(let i=0;i<palabra.length;i++){
    letra=palabra[i].toLowerCase()
 console.log(letra)
    if(letra==" "){
      letra = ""
    }else{
    //  letra=cifrado[alfabeto.indexOf(letra)]
      letra=cifrado[alfabeto.indexOf(letra)]
          console.log(letra)
    }
    respuesta+=letra
  }
  console.log(respuesta)


  
}



function descifrar(palabra, clave){
  
  let letra,respuesta=""
      let alfabeto = 'abcdefghijklmnopqrstuvwxyz'
    let cifrado  = alfabeto.slice(-clave);
    cifrado += alfabeto.slice(0, alfabeto.length - clave)
    for(let i=0; i< palabra.length; i++) { 
        letra = palabra[i].toLowerCase();
        if(letra == ' '){
            letra =' ';
         }   else{
            letra = alfabeto[cifrado.indexOf(letra)];
            }
              respuesta += letra;
    }
console.log(respuesta)


}
cifrar("hola",3)
descifrar("elix",3)