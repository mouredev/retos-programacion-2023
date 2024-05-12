/*
 * Crea un generador de números pseudoaleatorios entre 0 y 100.
 * - No puedes usar ninguna función "random" (o semejante) del lenguaje de programación seleccionado.
 *
 * Es más complicado de lo que parece...
 */

const randomNumber = () => {
    const now = new Date();

    const m = now.getMinutes();
    const ms = now.getMilliseconds();
    const random = (m * ms).toString();

    let newNumber: string[] = [];
    let result: string = "";

    for (let i = 0; i < random.length; i++) newNumber.unshift(random[i]);

    for (let i = 0; i < newNumber.length; i++) {        
        if (i === 2) {
            if (newNumber[0] === "0" && newNumber[1] === "0" && newNumber[2] === "1") {
                result = "100";
                break;
            }; 
            
            break;     
        };
        result += newNumber[i];
    };

    return parseInt(result);
};

console.log(randomNumber());