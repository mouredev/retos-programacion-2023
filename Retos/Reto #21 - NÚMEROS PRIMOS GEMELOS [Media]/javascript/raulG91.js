
function es_primo(number){

    let es_primo = true;
    for(let i = 2;i<number;i++){
        if(number%i==0){
            es_primo = false;
            break;
        }

    }
    return es_primo;
}

function primos_gemelos(range){

    let actual_primo;
    let prev_primo
    let result = [];


    for(let i = 2; i<=range;i++){
        if(es_primo(i)){

            actual_primo = i;
            if (prev_primo == null){

                prev_primo = i;
            }

            let distancia = actual_primo - prev_primo;

            if(distancia == 2){
               result.push(`(${prev_primo},${actual_primo})`)
            }
          
            prev_primo = i;
        }

    }
    return result;


}

let range = 50;

console.log(primos_gemelos(range));
