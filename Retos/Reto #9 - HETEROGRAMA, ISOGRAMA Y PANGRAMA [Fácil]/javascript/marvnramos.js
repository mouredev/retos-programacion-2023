/**
 * A function that tests if a string is a heterogram
 * @param {*} string - a string to be tested
 * @returns - true if the string is a heterogram, false otherwise
 */
const isHeterogram = function(string){
    for(let i = 0; i < string.length; i++){
        let character = string[i];

        if(string.indexOf(character) !== string.lastIndexOf(character)){
            return false; // the character is repeated
        };
    };

    return true;
};

/**
 * Validates if a string is an isogram
 * @param {*} string - a string to be tested
 * @returns - true if the string is an isogram, false otherwise
 */
const isIsogram = function(string){
    const containsNumbers = /[0-9]/;
    
    if(containsNumbers.test(string)){
        return false; // the string contains numbers so it is not an isogram
    }

    for(let i = 0; i < string.length; i++){
        let character = string[i];

        if(string.indexOf(character) !== string.lastIndexOf(character)){
            return false; // the character is repeated
        };
    };

    return true;
};

/**
 * Validates if a string is a pangram
 * @param {*} string - a string to be tested
 * @returns - true if the string is a pangram, false otherwise
 */
const isPangram = function(string){
    const containsNumbers = /[0-9]/;
    const containsSpecialCharacters = /[!@#$%^&*()_+\-=\[\]{};':"\\|,.<>\/?]/;
    
    if(containsNumbers.test(string) || containsSpecialCharacters.test(string)){
        return false; // the string contains numbers or special characteres so it is not an pangram
    }
    
    const regex = /[a-z]/g;
    let lowerCaseString = string.toLowerCase();
    let letters = new Set(lowerCaseString.match(regex));

    return letters.size === 26; // the string contains all the letters of the alphabet
};


let string_heterogram = "Hi, het3rog4m";
console.log(isHeterogram(string_heterogram));


let string_isogram = "H3y, 1s0gr4ms 4r3 c00l!";
let string_isogram2 = "Hey isogram";
console.log(isIsogram(string_isogram));
console.log(isIsogram(string_isogram2));

let string_pangram = "The quick brown fox jumps over a lazy dog";
console.log(isPangram(string_pangram));

