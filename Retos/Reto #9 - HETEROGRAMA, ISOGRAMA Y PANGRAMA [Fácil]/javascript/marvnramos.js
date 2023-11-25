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


const isPangram = function(string){
    // logic here
};

let string = "abcdefg 1xyz";
// console.log(isHeterogram(string));
console.log(isIsogram(string));
