let frase = prompt("Introduce el texto a traducir");

let alphabet = "abcdefghijklmnopqrstuvwxyz ,.ABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890";

let leet = new Array("4","|3","[",")","3","|=","&","#","1",",_|",">|","1","/\\/\\","^/","0","|*","(_,)","I2","5","7","(_)","\\/","\\/\\/","><","j","2"," ",",",".","4","|3","[",")","3","|=","&","#","1",",_|",">|","1","/\\/\\","^/","0","|*","(_,)","I2","5","7","(_)","\\/","\\/\\/","><","j","2","L","R","E","A","S","b","T","B","g","o");

let index;
let arrTraduccion = new Array();
for (let i = 0; i < frase.length; i++){
    index = alphabet.indexOf(frase[i]);
    arrTraduccion[i] = leet[index];
    if (alphabet.indexOf(frase[i]) == -1){
      arrTraduccion[i] = frase[i];
    }
}

let traduccion = arrTraduccion.join("");
console.log(traduccion);
