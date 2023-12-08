const getRandomInt      = ( max ) => Math.floor( Math.random() * max );
const getFactorial      = ( num ) => num===0 ? 1 : num * getFactorial( num - 1 );

const getRepeatedLetters= ( string ) => {
    let letters         = [];
    let repeatedLetters = 1;

    string.trim().toLowerCase().split('').forEach( (letter) => letters.includes(letter) ? repeatedLetters++ : letters.push(letter) );

    return repeatedLetters;
}

const shuffledString = ( string ) => {
    const array = string.split("");
    const size  = array.length - 1;

    for ( let index=size; index>0; index-- ) {
        const random    = getRandomInt( index + 1 );
        const tmp       = array[ index ];
        array[ index ]  = array[ random ];
        array[ random ] = tmp;
    }

    return array.join("");
}

const Permutation = ( string, array, permutation ) => {
    if ( permutation === 0 ) {
        return array;
    }

    if ( !array.includes(string) ) {
        array.push( string );
        permutation--;
    }

    return Permutation( shuffledString(string), array, permutation );
}

const getPermutations = ( string ) => {
    const permutations = getFactorial( string.length ) / getFactorial( getRepeatedLetters(string) );
    return Permutation( string, [], permutations );
}

const permutations = getPermutations( 'casa' );
console.log( permutations );