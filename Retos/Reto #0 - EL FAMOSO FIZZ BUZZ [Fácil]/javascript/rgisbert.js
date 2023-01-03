const fizzBuzz = ( num ) => {
    const isMultipleOf3 = num % 3 === 0;
    const isMultipleOf5 = num % 5 === 0;

    if( isMultipleOf3 && isMultipleOf5 ) return 'fizzbuzz';
    if( isMultipleOf3 ) return 'fizz';
    if( isMultipleOf5 ) return 'buzz';
    return num;
}

for(let num = 1; num <= 100; num++) {
    console.log( fizzBuzz( num ) );
}