/*
 * Crea 3 funciones, cada una encargada de detectar si una cadena de
 * texto es un heterograma, un isograma o un pangrama.
 * - Debes buscar la definición de cada uno de estos términos.
 */

function heterograma(str){
    for(let i = 0; i < str.length - 1; i++){
        for(let j = i + 1; j < str.length; j++){
            if(str[i] == str[j]){
                return false;
            }else{
                bandera = 1;
            }
        }
    }
    return bandera == 1 ? true : false;
}

function isograma(str){
    let arreglo = [];
    for(let i = 0; i < str.length; i++){
        arreglo[i] = 0;
    }
    for(let i = 0; i < str.length; i++){
        for(let j = 0; j < str.length; j++){
            if(str[i] == str[j]){
                arreglo[i]++;
            }else{

            }
        }
    }
    for(let i = 0; i < arreglo.length; i++){
        for(let j = 0; j < arreglo.length; j++){
            if(arreglo[i] != arreglo[j]){
                return false;
            }else{
                bandera = 1;
            }
        }
    }
    return bandera == 1 ? true : false;
}

function pangrama(str){
    let abc = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z'];
    for(let i = 0; i < str.length; i++){
        for(let j = 0; j < abc.length; j++){
            if(str[i] == abc[j]){
                abc.splice(j, 1);
            }
        }
    }
    return abc.length == 0 ? true : false;
}

console.log(heterograma('hola'));
console.log(isograma('neuqquen'));
console.log(pangrama('the quick brown fox jumps over the lazy dog'));




//...x pibelanzallamas n.nv
