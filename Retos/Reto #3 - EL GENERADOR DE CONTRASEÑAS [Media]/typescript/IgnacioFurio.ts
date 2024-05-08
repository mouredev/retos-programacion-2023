/*
 * Escribe un programa que sea capaz de generar contraseñas de forma aleatoria.
 * Podrás configurar generar contraseñas con los siguientes parámetros:
 * - Longitud: Entre 8 y 16.
 * - Con o sin letras mayúsculas.
 * - Con o sin números.
 * - Con o sin símbolos.
 * (Pudiendo combinar todos estos parámetros entre ellos)
 */

const passwordSettings: any = {
    passwordLength: Math.floor((Math.random()* (16 - 8 + 1) + 8)),
    characters: true, 
    uppercase: true, 
    number: true, 
    simbol: true, 
};

const passwordGenerator = (passwordSettings: any) => {
    const alphabetLower: string = "abcdefghijklmnopqrstuvwxyz";
    const alphabetUpper: string = "ABCDEFGHIJKLMNOPQRSTUVWXYZ";
    const numbers: string = "0123456789";
    const simbols: string = "&/\\^=?!@#$%*+.,:;|()[]{}<>-_";
    const settings: any = passwordSettings
    
    let filter: string = ""
    let password: string = "";
    let variables: number = 0;

    
    if (settings.characters === true) filter += alphabetLower;
    if (settings.uppercase === true) filter += alphabetUpper;
    if (settings.number === true) filter += numbers;
    if (settings.simbol === true) filter += simbols;

    console.log(filter);
    
    for (let i = 0; i < settings.passwordLength ; i++) {
        let random = Math.floor(Math.random()* (filter.length - 1));
        console.log(random);
        
        password += filter[random];
    };
    
    return password;
};

passwordGenerator(passwordSettings);