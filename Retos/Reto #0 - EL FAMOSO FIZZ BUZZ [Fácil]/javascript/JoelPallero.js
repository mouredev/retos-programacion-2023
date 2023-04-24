// FIZZ BUZZ

function FizzBuzz(){
    //creo un bucle recorriendo desde el 1 al 100 )incluidos
    for(let i = 1; i < 101; i++){

        if(i % 3 === 0 && i % 5 === 0){
            console.log('FizzBuzz');
        }
        else{
            if(i % 3 === 0){
                console.log('Fizz');
            }
            else{
                if(i % 5 === 0){
                    console.log('Buzz');
                }
                else{
                    //si no es divisible por 3 ni 5, se muestra el numero
                    console.log(i)
                }
            }
        }
    }
}

FizzBuzz();
