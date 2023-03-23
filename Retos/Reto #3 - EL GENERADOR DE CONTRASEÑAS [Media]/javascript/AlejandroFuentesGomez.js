/*
 * Escribe un programa que sea capaz de generar contraseñas de forma aleatoria.
 * Podrás configurar generar contraseñas con los siguientes parámetros:
 * - Longitud: Entre 8 y 16.
 * - Con o sin letras mayúsculas.
 * - Con o sin números.
 * - Con o sin símbolos.
 * (Pudiendo combinar todos estos parámetros entre ellos)
 */
const passwordConditions= {
    length:10,
    capitalLetters: true,
    numbers: true,
    simbols:true,
}
console.log(generatePassword(passwordConditions));
function generatePassword(passwordConditions){
    if(passwordConditions["length"]<8 || passwordConditions["length"]>16 ) return Error('La longitud de la contraseña tiene que estar entre 8 y 16 caracteres');
    let initialDataset = 'abcdefghijklmnopqrstuvwxyz';
    let optionalDataset = {
        capitalLetters: 'ABCDEFGHIJKLMNOPQRSTUVWXYZ',
        numbers: '0123456789',
        simbols: '~`!@#$%^&*()_-+={[}]|\:;"<,>.?/',
    }
    Object.keys(passwordConditions).forEach(element => {
        if(element!== "length"){
            initialDataset = passwordConditions[element] ? (initialDataset + optionalDataset[element]) : initialDataset;
        }
    });
    initialDataset = initialDataset.split('').sort((a,b)=> 0.5 - Math.random()).join('');
    result = initialDataset.substring(0,passwordConditions["length"]);
    return result;
}