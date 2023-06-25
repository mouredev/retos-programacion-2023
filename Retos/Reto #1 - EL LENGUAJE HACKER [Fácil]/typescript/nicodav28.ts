/*
 * Escribe un programa que reciba un texto y transforme lenguaje natural a
 * "lenguaje hacker" (conocido realmente como "leet" o "1337"). Este lenguaje
 *  se caracteriza por sustituir caracteres alfanuméricos.
 * - Utiliza esta tabla (https://www.gamehouse.com/blog/leet-speak-cheat-sheet/) 
 *   con el alfabeto y los números en "leet".
 *   (Usa la primera opción de cada transformación. Por ejemplo "4" para la "a")
 */
class Leet{
    private dictionary: Record<string, string> = {
        a: '4',
        b: 'I3',
        c: '[',
        d: ')',
        e: '3',
        f: '|=',
        g: '&',
        h: '#',
        i: '1',
        j: ',_|',
        k: '>|',
        l: '1',
        m: '/\\/\\',
        n: '^/',
        o: '0',
        p: '|*',
        q: '(_,)',
        r: 'I2',
        s: '5',
        t: '7',
        u: '(_)',
        v: '\\/',
        w: '\\/\\/',
        x: '><',
        y: 'j',
        z: '2'
    }

    public encode(text: string): string { 
        text = text.toLowerCase();
        const destructuring = text.split('');
        
        const result = destructuring.map((letter) => {
            return this.dictionary[letter] || letter;
        })
        
        return result.join('');
    }

}

const hackerLanguage = new Leet;
const translate = hackerLanguage.encode("Hola mi nombre es Nicolas");
console.log(translate);
