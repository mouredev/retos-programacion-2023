"use strict";
const abecedarioHacker=["4","8","¢","[)","3","ph","6","#","1","]","|{","£","nn","nh","0", "|*","9","Я","5","7","µ","v","Ш","ecks","Ч","2"," "]; 
const abecedario=["a","b","c","d","e","f","g","h","i","j","k","l","n","ñ","o","p","q","r","s","t","u","v","w","x","y","z"," "];
let palabra=prompt("Dame una palabra"); //Hola 
let palabraFinal=""; 
let letra1=""; 

function separar(){ //separa palabras por letras
    for (let key of palabra){
        //document.write(`La letra es ${key} <br>`);
        recorrer1(key);
        
    }
    
}
function comparar(letra,corredor,corredor2){//compara la letra separada con el abecedario normal
    if(letra==corredor){
        //document.write(`Cuando entra en comparar: ${letra} <br>`);
        letra1=letra.replace(letra,corredor2);
        palabraFinal+=letra1;
        //document.write(`Despues del cambio: ${palabraFinal} <br>`)
    }
}
function recorrer1(letra){//recorre el array de abecedario, casilla por casilla voto pot voto
    for(let i=0; i<=abecedario.length;i++){
        
        comparar(letra,abecedario[i],abecedarioHacker[i])

    }    
}
/*function recorrer2(){ //recorre el array de abecedarioHacker, casilla por casilla
    for(let key of abecedarioHacker){
         
    }
}
*/
separar();
document.write(palabraFinal);

//////
