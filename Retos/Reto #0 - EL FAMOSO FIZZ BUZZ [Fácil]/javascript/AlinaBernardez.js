let contador = 0;

function fizzBuzz(n) {
    while(n < 101) {
        n++;
        if(n % 3 === 0) {
            console.log('fizz');
        }
        else if(n % 5 === 0) {
            console.log('buzz');
        }
        else if(n % 3 === 0 && n % 5 === 0) {
            console.log('fizzbuzz');
        }
        else {
            console.log(n);
        }
    }
}

fizzBuzz(contador);

