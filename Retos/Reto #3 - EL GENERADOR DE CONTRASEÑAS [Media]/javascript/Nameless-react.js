const readlinePromises = require('node:readline/promises');


const passwordGenerator = async (rl) => {
    let characters = "abcdefghijklmnopqrstuvwxyz";
    let length = 0;
    
    do {
        length = await rl.question("Digite la longitud que desea que tenga la constraseña entre 8 y 16 caracteres: ");
        length = parseInt(length);
    } while (length < 8 || length > 16);
    
    let password = " ".repeat(length);
    
    
    const upperCaseletters = "ABCDEFGHIJKLMNOPQRSTUVWXYZ";
    const numbers = "0123456789";
    const symbols = "!$%&()=/?¿¡:,;_-|@#+*{}[]^\\ñ";
    
    
    
    const containsLetters = await rl.question("¿Desea que su contraseña contenga letras mayúsculas?"
            + "\n s) si"
            + "\n n) no \n")
    characters += containsLetters.toLowerCase().trim().charAt(0) === 's' ? upperCaseletters : "";
    
    
    const containsNumbers = await rl.question("¿Desea que su contraseña contenga números?"
            + "\n s) si"
            + "\n n) no \n")
    characters += containsNumbers.toLowerCase().trim().charAt(0) === 's' ? numbers : "";
    
    
    const containsSymbols = await rl.question("¿Desea que su contraseña contenga símbolos?"
            + "\n s) si"
            + "\n n) no \n");
    characters += containsSymbols.toLowerCase().trim().charAt(0) === 's' ? symbols : "";
    
    
    
    if (characters.length === 0) {
        console.log("No se puede generar una contraseña sin caracteres");
        return "";
    }
        
    console.log(Array.from(password).map(letter => characters[Math.floor(Math.random() * characters.length)]).join(""));
    rl.close();
}


const rl = readlinePromises.createInterface({
    input: process.stdin,
    output: process.stdout
});


passwordGenerator(rl);

