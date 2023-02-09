/*
 * Escribe un programa que reciba un texto y transforme lenguaje natural a
 * "lenguaje hacker" (conocido realmente como "leet" o "1337"). Este lenguaje
 *  se caracteriza por sustituir caracteres alfanuméricos.
 * - Utiliza esta tabla (https://www.gamehouse.com/blog/leet-speak-cheat-sheet/) 
 *   con el alfabeto y los números en "leet".
 *   (Usa la primera opción de cada transformación. Por ejemplo "4" para la "a")
 */



var cadena="hola mundo";
var letra="";
let abc_a=["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]
let abc_h=["4","l3","[",")","3","|=","&","#","1",",_l",">l","1","/\\/\\","^/","0","l*","(_,)","12","5","7","(_)","\/","\/\/","><","j","2"]
let traduccion="";

for (i=0;i<cadena.length;i++) {
    letra=cadena.substring(i,i+1);
    if(letra==" "){
        traduccion=traduccion+" "
    }
    for (h=0;h<abc_a.length;h++){
        if(abc_a[h]==letra){
            traduccion=traduccion+abc_h[h]
            break 
        }
    }

}

console.log(traduccion)



