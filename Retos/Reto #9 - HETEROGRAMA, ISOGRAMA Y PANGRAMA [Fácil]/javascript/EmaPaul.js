/*
 Crea 3 funciones, cada una encargada de detectar si una cadena de
 texto es un heterograma, un isograma o un pangrama.
 - Debes buscar la definición de cada uno de estos términos.
*/

function heterograma(str) {
  let palabra = str.toLowerCase().replace(/\s+/g, '');
  let arr = palabra.split("")
  let glifos = {};
  let letras = [];

    for (let i = 0; i < palabra.length; i++) {
        let letra = palabra[i];
        let glifo = palabra[i];

        if(letra === "á" || letra === "é" || letra === "í" || letra === "ó" || letra === "ú"){
            glifo = letra.normalize('NFKD').replace(/[\u0300-\u036f]/g, "")
            return "No es un heterograma";
        }
        glifos[letra] = glifo;
    }

    for(let i = 0;i<arr.length;i++){
        let letra1 = arr[i];
        if(letras.indexOf(letra1) === -1){
            letras.push(letra1)
        }
    }

    if(letras.length === palabra.length){
        return "Heterograma"
    }else{
        return "No es un heterograma"
    }

  
}
console.log(heterograma("mundo"));
console.log(heterograma("murcielago"))
console.log(heterograma("subcomité"))

function isograma(str) {
    let palabra1 = str.toLowerCase().replace(/\s+/g, '');
    let arr = palabra1.split("");
    let glifos = {};
    let letras = [];
  
    for (let i = 0; i < palabra1.length; i++) {
        let letra = palabra1[i];
        let glifo = palabra1[i];

        if(letra === "á" || letra === "é" || letra === "í" || letra === "ó" || letra === "ú"){
            glifo = letra.normalize('NFKD').replace(/[\u0300-\u036f]/g, "")
            return "Isograma";
        }
        glifos[letra] = glifo;
        
        for (let i = 0; i < arr.length; i++) {
            let letra = arr[i];
            if (letras.indexOf(letra) === -1) {
            letras.push(letra);
            } 
        }
        
        if(letras.length === palabra1.length){
            return "Isograma"
        }else{
            return "No es un Isograma"
        }

    }
}
console.log(isograma("murcielago"));
console.log(isograma("subcomité"));
console.log(isograma("murciélago"))


function pangrama (str) {
    let alfabeto = 'abcdefghijklmnopqrstuvwxyz'; 
    let alf = alfabeto.toLowerCase().replace(/\s+/g, '')
    let texto = str.toLowerCase().replace(/[^a-z]/g, '')
    let letras2 = []

    for(let i = 0; i < texto.length; i++) {
        if(texto[i].match(/[a-z]/) && alf.includes(texto[i])) {
            letras2.push(texto[i]);
        }
    }

    let resultado = letras2.filter((item,index)=>{
        return letras2.indexOf(item) === index;
    })

    if(resultado.length === alfabeto.length){
       return "Pangrama"
    }else{
       return "No es un pangrama"
    }
}

console.log(pangrama("The quick brown fox jumps over the lazy dog"))
