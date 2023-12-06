function cifrado_cesar(text,key){
  let cesar_text = "";
  let cesar_text_ascii = [];
  for(let suma=0; suma<text.length;suma++){
    cesar_text_ascii[suma] = text.charCodeAt(suma);
    if(cesar_text_ascii[suma]>=65 && cesar_text_ascii[suma]<=90){
      cesar_text_ascii[suma]=cesar_text_ascii[suma]+key;
      if(cesar_text_ascii[suma]>90){
        cesar_text_ascii[suma] = 64+(cesar_text_ascii[suma]-90)
      }
    }
    else if(cesar_text_ascii[suma]>=97 && cesar_text_ascii[suma]<=122){
      cesar_text_ascii[suma]=cesar_text_ascii[suma]+key;
      if(cesar_text_ascii[suma]>122){
        cesar_text_ascii[suma] = 96+(cesar_text_ascii[suma]-122)
      }
    }
  }
  for(let suma=0; suma<text.length;suma++){
    cesar_text=cesar_text+String.fromCharCode(cesar_text_ascii[suma])
  }
  return cesar_text
}

function descifrado_cesar(cesar_text,key){
  let text = "";
  let cesar_text_ascii = [];
  for(let suma=0; suma<cesar_text.length;suma++){
    cesar_text_ascii[suma] = cesar_text.charCodeAt(suma);
    if(cesar_text_ascii[suma]>=65 && cesar_text_ascii[suma]<=90){
      cesar_text_ascii[suma]=cesar_text_ascii[suma]-key;
      if(cesar_text_ascii[suma]<65){
        cesar_text_ascii[suma] = 91+(cesar_text_ascii[suma]-65)
      }
    }
    else if(cesar_text_ascii[suma]>=97 && cesar_text_ascii[suma]<=122){
      cesar_text_ascii[suma]=cesar_text_ascii[suma]-key;
      if(cesar_text_ascii[suma]<97){
        cesar_text_ascii[suma] = 123+(cesar_text_ascii[suma]-97)
      }
    }
  }
  for(let suma=0; suma<cesar_text.length;suma++){
    text=text+String.fromCharCode(cesar_text_ascii[suma])
  }
  return text
}
let texto = "Hola Mundo, que tal todoZ?";
let key = 5;
console.log("Texto para cifrar: "+texto);
console.log("Cifrado Cesar: " + cifrado_cesar(texto,key));
console.log("Descifrado Cesar: " + descifrado_cesar(cifrado_cesar(texto,key),key));