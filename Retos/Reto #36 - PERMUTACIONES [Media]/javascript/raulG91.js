
function permutaciones(cadena,subcadena){

    if(cadena.length == 0){
        console.log(subcadena)
    }
    else{

        for(let i=0;i<cadena.length;i++){

            permutaciones(cadena.slice(0,i)+cadena.slice(i+1),subcadena+cadena.slice(i,i+1));

        }
    }
}


let word = "sol"

permutaciones(word,'');