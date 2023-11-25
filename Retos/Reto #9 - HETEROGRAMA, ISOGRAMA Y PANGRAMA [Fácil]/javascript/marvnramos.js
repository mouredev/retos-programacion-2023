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

const isIsogram = function(string){
    // logic here
};


const isPangram = function(string){
    // logic here
};

let string = "abcdefga";

console.log(isHeterogram(string));
