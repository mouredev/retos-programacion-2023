function generatePassword({ size, upperCaseLetters, numbers, symbols }) {
    let password = '';    
    if(size == null || size < 8 || size > 16) throw new RangeError('Size must between 8-16 characters');

    let getRandomNumber = (max) => Math.floor(Math.random() * (max));

    let availableCharCodes = Array.from(Array(25), (_, i) => i+97);
    if(upperCaseLetters)
        availableCharCodes = availableCharCodes.concat(Array.from(Array(25), (_, i) => i+65));   
    if(numbers)
        availableCharCodes = availableCharCodes.concat(Array.from(Array(10), (_, i) => i+48));
    if(symbols)
        availableCharCodes = availableCharCodes.concat(Array.from(Array(10), (_, i) => i+33));
    
    let availableCharCodeLength = availableCharCodes.length;

    for (let index = 0; index < size; index++) {
        password += String.fromCharCode(availableCharCodes[getRandomNumber(availableCharCodeLength)]);            
    }

    return password;
}

let options = {
    size: 9,
    numbers: true,
    symbols: true,
    upperCaseLetters: true
}

try { 
    let password = generatePassword(options); 
    console.log(password);
}
catch(error){    
    console.log(`ERROR: ${error.message}`);
}