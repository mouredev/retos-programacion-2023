function fizzbuzz( number ) {
    
    while ( number >= 1 ) {

        if ( number % 3 == 0 ) {
            console.log('fizz');
        }
        if ( number % 5 == 0 ) {
            console.log('buzz');
        }
        if ( number % 3 == 0 && number % 5 == 0 ) {
            console.log('fizzbuzz');
        }
    }
}