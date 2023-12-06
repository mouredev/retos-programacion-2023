const fizzBuzz = () => {
    for ( let index=1; index<=100; index++ ) {
        let output = ( index % 3 ==0 ? "fizz" : "" ) + ( index % 5 ==0 ? "buzz" : "" );
        console.log( output ? output : index )
    }
}

fizzBuzz();