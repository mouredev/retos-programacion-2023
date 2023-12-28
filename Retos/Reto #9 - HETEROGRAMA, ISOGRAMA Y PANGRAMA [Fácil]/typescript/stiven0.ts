/*
 * Crea 3 funciones, cada una encargada de detectar si una cadena de
 * texto es un heterograma, un isograma o un pangrama.
 * - Debes buscar la definición de cada uno de estos términos.
 */

const removeDiacritics = ( text: string ): string => {
    return text.normalize( 'NFD' ).replace( /[\u0300-\u036f]/g ,"" );
}

const isHeterograma = ( text: string ): boolean => {

    let textIsHetrograma = true;
    removeDiacritics( text ).split('').reduce( ( acc: string, crv: string ) => {
        acc = acc.toLowerCase();
        crv = crv.toLowerCase();
        if ( acc.includes( crv ) ) textIsHetrograma = false;
        return acc + crv;
    }, '');
    return textIsHetrograma;

}

const isAnIsograma = ( text: string ): boolean => {

    let textIsAnIsogram = false;
    removeDiacritics( text ).split('').reduce( ( acc: string, crv: string ) => {
        acc = acc.toLowerCase();
        crv = crv.toLowerCase();
        if ( acc.includes( crv ) ) textIsAnIsogram = true;
        return acc + crv;
    }, '');
    return textIsAnIsogram;

}


const isPangrama = ( text: string ): boolean => {

    text = removeDiacritics( text ).trim().toLowerCase();
    if ( text.length < 26 ) return false;
    const alphabet = [ ...Array(26).keys() ].map( (i) => String.fromCharCode(i + 97) );
    for ( const letter of text.split('') ) {
        if ( alphabet.includes( letter ) ) alphabet.splice( alphabet.indexOf( letter ), 1 );
        if ( alphabet.length === 0 ) break;
    }   
    return alphabet.length === 0 ? true : false;

}

const challenge = ( text: string ) => {

    const heterograma = isHeterograma( text ) ? 'es un heterograma' : 'no es un heterograma';
    const isograma = isAnIsograma( text ) ? 'es un isograma' : 'no es un isograma';
    const pangrama = isPangrama( text ) ? 'es un pangrama' : 'no es un pangrama';

    return `El texto ""${ text }"" ${ heterograma }, ${ isograma } y ${ pangrama }`;

}

// heterograma
console.log( challenge( 'centrifugado' ) );

// isograma
console.log( challenge( 'acondicionar' ) );

// pangrama
console.log( challenge( 'Benjamín pidió una bebida de kiwi y fresa. Noé, sin vergüenza, la más exquisita champaña del menú.' ) );