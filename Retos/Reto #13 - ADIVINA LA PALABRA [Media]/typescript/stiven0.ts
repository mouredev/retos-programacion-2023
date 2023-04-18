/*
 * Crea un pequeño juego que consista en adivinar palabras en un número máximo de intentos:
 * - El juego comienza proponiendo una palabra aleatoria incompleta
 *   - Por ejemplo "m_ur_d_v", y el número de intentos que le quedan
 * - El usuario puede introducir únicamente una letra o una palabra (de la misma longitud que
 *   la palabra a adivinar)
 *   - Si escribe una letra y acierta, se muestra esa letra en la palabra. Si falla, se resta
 *     uno al número de intentos
 *   - Si escribe una resolución y acierta, finaliza el juego, en caso contrario, se resta uno
 *     al número de intentos
 *   - Si el contador de intentos llega a 0, el jugador pierde
 * - La palabra debe ocultar de forma aleatoria letras, y nunca puede comenzar ocultando más del 60%
 * - Puedes utilizar las palabras que quieras y el número de intentos que consideres
 */

import * as readline from 'node:readline/promises';
import { stdin as input, stdout as output } from 'node:process';
    
const runGame = async () => {
    
    const rl = readline.createInterface({ input, output });
    const phrases = [ 'ambulancia', 'helado', 'jirafa' ];
    let phrase = phrases[ Math.floor( Math.random() * ( phrases.length - 0 ) - 0 ) ];
    let hidePhrase = hideCharactersPhrase( phrase );
    let restOfAttempts = hidePhrase.split('').filter( val => val === '_' ).length * 2;

    console.log('======= Inicia el juego (Adivina la palabra) =======');

    while ( restOfAttempts > 0 ) {
        let answer = await askWord( hidePhrase, restOfAttempts, rl );
        let { currentPhraseState, isFoundWord } = checkLetterInSentence( answer, phrase, hidePhrase );
        hidePhrase = currentPhraseState;
        if ( currentPhraseState === phrase ) {
            console.log(`======= Felicidades has encontrado la palabra correcta !!!: "${ currentPhraseState }" =======`);
            break;
        }
        isFoundWord ? console.log(`La letra "${ answer }" ha sido encontrada en: ${ currentPhraseState }`) 
                    : console.log(`La ${ answer.length > 1 ? 'frase' : 'palabra' } "${ answer }" no es correcta`);
        restOfAttempts--;
    }

    if ( restOfAttempts === 0 ) console.log(`======= Lo siento has fallado, la palabra correcta es "${ phrase }" =======`);
    rl.close();

}

const askWord = async ( phrase: string, restOfAttempts: number, rl: readline.Interface ): Promise<string> => {

    console.log(`======= Palabra: ${ phrase }, numero de intentos faltantes ${ restOfAttempts } =======`);
    return (await rl.question('Introduce una letra o palabra? ')).toLowerCase();

}

const hideCharactersPhrase = ( phrase: string ): string => {
 
    let newPhrase = '';
    for ( let i = 0; i < phrase.length; i++ ) {
        newPhrase += i > 1 && i % 2 === 0 ? '_' : phrase[i];
    }
    return newPhrase;    

}   

const checkLetterInSentence = ( letter: string, phrase: string, hidePhrase: string ): { currentPhraseState: string, isFoundWord?: boolean } => {

    let isFoundWord = false;
    let currentPhraseState: any = hidePhrase;
    if ( letter === phrase ) return { currentPhraseState: letter };
    for ( let i = 0; i < phrase.length; i++ ) {
        if ( hidePhrase[i] === '_' ) {
            if ( phrase[i] === letter ) {
                currentPhraseState = currentPhraseState.split('');
                currentPhraseState[i] = letter;
                currentPhraseState = currentPhraseState.join('');
                isFoundWord = true;
            }
        }
    }
    return { currentPhraseState, isFoundWord };

}

runGame();