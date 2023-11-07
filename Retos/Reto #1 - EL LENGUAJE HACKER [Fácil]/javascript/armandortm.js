
const LOWER_CASE_LETTERS =
    ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm',
    'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z'];    
     
const UPPER_CASE_LETTERS =
    ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M',
    'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']; 

const LEET_SPEAK_ALPHABET =
    ['4', 'I3', '[', ')', '3', '|=', '&', '#', '1', ',_|', '>|', '1', 'IVI',
    '^/', '0', '|*', '(_,)', 'I2', '5', '7', '(_)', '\/', '\/\/', '><', 'j', '2'] 
    
const LEET_NUMBERS = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9];
const NUMBERS_TO_LEET = ['()', 'L', 'R', 'E', 'A', 'S', 'b', 'T', 'B', 'g'];


function convert_to_leet_alphabet(){

    // get the string
    let stringFromUser = prompt("Please enter an entry");
    let string_hacked = [];

    // convert to an array
    let arrayFromString = stringFromUser.split("");

    // using a foreach to compare each character with each array element
    arrayFromString.forEach(element => {

        let indexOfLetters;
        let indexOfNumbers;
        
        // to check if it's a lower case letter
        if (LOWER_CASE_LETTERS.includes(element)) { 

            indexOfLetters = LOWER_CASE_LETTERS.indexOf(element);
            string_hacked.push(LEET_SPEAK_ALPHABET[indexOfLetters]);
        }

        // to check if it's a upper case letter
        else if (UPPER_CASE_LETTERS.includes(element)) {

            indexOfLetters = UPPER_CASE_LETTERS.indexOf(element);
            string_hacked.push(LEET_SPEAK_ALPHABET[indexOfLetters]);            
        }

        // To check if it's a number
        else if (LEET_NUMBERS.includes(Number(element))) { 
            
            indexOfNumbers = LEET_NUMBERS.indexOf(Number(element));
            string_hacked.push(NUMBERS_TO_LEET[indexOfNumbers]);
        }
            
        // to identify if there is a space
        else if (element == "") {
            
            string_hacked.push(" ");
        }
    });

    console.log(string_hacked);
}

// calling the function
convert_to_leet_alphabet();