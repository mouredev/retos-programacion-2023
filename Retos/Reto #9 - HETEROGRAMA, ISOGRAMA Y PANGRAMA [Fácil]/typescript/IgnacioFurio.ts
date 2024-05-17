/*
 * Crea 3 funciones, cada una encargada de detectar si una cadena de
 * texto es un heterograma, un isograma o un pangrama.
 * - Debes buscar la definición de cada uno de estos términos.
 */
const frase = "Yuxtaponer";
// const frase = "Escritura";
// const frase = "Benjamín pidió una bebida de kiwi y fresa. Noé, sin vergüenza, la más exquisita champaña del menú";

const heterograma = (frase: string) => {
    let letrasUsadas: string = ""
    let result :string = `¡¡${frase}!! Es un heterograma.`;

    for (let i = 0; i < frase.length; i++) {
        if (frase[i] !== " ") {
            for (let j = 0; j < letrasUsadas.length; j++) {
                if (frase[i] === letrasUsadas[j]) {
                    result = `¡¡${frase}!! No es un heterograma.`;
                    break;
                };
                
            };
            letrasUsadas += frase[i];
        };
    };

    return result;
};

const isograma = (frase: string) => {
    let letrasUsadas: Record<string, number> = {};
    let repeticiones: number = 0;
    let result :string = `¡¡${frase}!! No es un isograma.`;

    for (let i = 0; i < frase.length; i++) {
        if (frase[i] !== " ") {
            let letra = frase[i].toLowerCase()
            letrasUsadas[letra] = (letrasUsadas[letra] || 0) + 1;            
        };
    };

    for (const letra in letrasUsadas) {
        if (repeticiones === 0) {
            repeticiones = letrasUsadas[letra];
        } else if (repeticiones !== letrasUsadas[letra]) {
            result = `¡¡${frase}!! Es un isograma de ${repeticiones}º orden.`;
            break;
        };        
    };
    return result;
};

const pangrama = (frase: string) => {
    const abecedario: string = "abcdefghijklmnñopqrstuvwxyz";
    
    let letrasUsadas: Record<string, number> = {};
    let repeticiones: number = 1;
    let perfecto: boolean = true;
    let result: string = `¡¡Es un pangrama!!`;
    
    for (let i = 0; i < abecedario.length; i++) {

        if (frase.includes(abecedario[i]) !== true) {
            console.log(frase.includes(abecedario[i]));
            return  result = `¡¡No es un pangrama.!!`
        };
    };
    
    return result;
};

console.log(heterograma(frase));
console.log(isograma(frase));
console.log(pangrama(frase));
