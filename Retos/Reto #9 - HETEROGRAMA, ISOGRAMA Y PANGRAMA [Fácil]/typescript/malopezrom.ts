
/*
 * Crea 3 funciones, cada una encargada de detectar si una cadena de
 * texto es un heterograma, un isograma o un pangrama.
 * - Debes buscar la definición de cada uno de estos términos.
 */


/**
 * Declaracion de los miembros de la extension de la clase String
 */
declare interface String {
    cleanText(): string;
    isIsogram(): boolean;
    isPangram(): boolean;
    isHetereogram(): boolean;

}



/**
 * Funcion que detecta si una palabra es un heterograma con una expresion regular
 * Un Heterograma es una palabra que no tiene letras repetidas
 */
String.prototype.isHetereogram = function(): boolean {
    return /^(?!.*(.).*\1)[a-zA-Z]+$/.test(this.toLowerCase().cleanText().replace(/[^a-z]/g, ''));
}
/**
 * Funcion que detecta si una palabra es un pangrama
 * Un Pangrama es una frase que contiene todas las letras del alfabeto
 */
String.prototype.isPangram = function(): boolean {
    const textLower = this.toLowerCase().cleanText().trim().replace(/[^a-z]/g, '')
    const regExp = /[a-z]/g;
    const alphabet = 'abcdefghijklmnopqrstuvwxyz';
    const numberOfLetters = regExp.test(alphabet) ? alphabet.length : 0;
    const letters = new Set(textLower.match(regExp));
    return letters.size === numberOfLetters;
}
/**
 * Funcion que detecta si una palabra es un isograma.
 * Un isograma es una palabra en la que cada letra se repite exactamente el mismo numero de veces
 * Una palabra en la que cada letra se repite una sola vez es a su vez un heterograma.
 * Un palabra en la que cada letra se repite dos veces es un isograma de grado 2 y asi sucesivamente.
 */
String.prototype.isIsogram = function(): boolean {
    const countLetters: {[key: string]: number} = {};
    const textLower = this.toLowerCase().cleanText().trim().replace(/[^a-z]/g, '')
    for (const element of textLower) {
        countLetters[element] = (countLetters[element] || 0) + 1;
    }
    const values = Object.values(countLetters);
    const uniqueValues = new Set(values);
    return uniqueValues.size === 1;
}
/**
 * Funcion de extension de un string que limpia los acentos de una cadena de texto y
 * los sustituye por su equivalente sin acento
 */

String.prototype.cleanText = function(): string {
    const regExp = /[áéíóúÁÉÍÓÚ]/g;
    const accents: {[key: string]: string} = {
        'á': 'a',
        'é': 'e',
        'í': 'i',
        'ó': 'o',
        'ú': 'u',
        'Á': 'A',
        'É': 'E',
        'Í': 'I',
        'Ó': 'O',
        'Ú': 'U'
    };
    const newText = this.replace(regExp, match => accents[match]);
    return newText;
};



    function checkWord(word: string): void {
        let message = `La frase "${word}" es: `;
        const conditions = [];

        if (word.isIsogram()) {
            conditions.push('isograma');
        }

        if (word.isPangram()) {
            conditions.push('pangrama');
        }

        if (word.isHetereogram()) {
            conditions.push('heterograma');
        }

        if (conditions.length === 0) {
            message += 'ni un isograma, ni un pangrama, ni un heterograma.';
        } else {
            message += conditions.join(', ') + '.';
        }

        console.log(message);
    }

    /**
     * Funcion que detecta si una palabra es un heterograma con una expresion regular
     * Un Heterograma es una palabra que no tiene letras repetidas
     */



    checkWord('Ecuador, cada quince de noviembre');
    checkWord('esdrújula');
    checkWord('aliento');
    checkWord('mama');
    checkWord("El veloz murciélago hindú comía feliz cardillo y kiwi. La cigüeña tocaba el saxofón detrás del palenque de paja");
    checkWord("Jovencillo emponzoñado de whisky, ¡qué figurota exhibe!");





