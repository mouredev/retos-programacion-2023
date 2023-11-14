// const nigmaToNormal = (letter) =>{
//     switch (letter) {
//         case '4':
//             return 'A';
        
//         case 'I3':
//             return 'B';
        
//         case '[':
//             return 'C';
        
//         case ')':
//             return 'D';
        
//         case '3':
//             return 'E';
        
//         case '|=':
//             return 'F';
            
//         case '&':
//             return 'G';
        
//         case '#':
//             return 'H';
        
//         case '1':
//             return 'I';

//         case ',_|':
//             return 'J';

//         case '>|':
//             return 'K';

//         case '1':
//             return 'L';

//         case `'/\/\'`:
//             return 'M';

//         case '^/':
//             return 'N';

//         case '0':
//             return 'O';

//         case '|*':
//             return 'P';

//         case '(_,)':
//             return 'Q';

//         case 'I2':
//             return 'R';

//         case '5':
//             return 'S';

//         case '7':
//             return 'T';

//         case '(_)':
//             return 'U';

//         case '\/':
//             return 'V';

//         case '\/\/':
//             return 'W';

//         case '><':
//             return 'X';

//         case 'j':
//             return 'Y';

//         case '2':
//             return 'Z';


//         //Numbers

//         case 'L':
//             return '1';

//         case 'R':
//             return '2';

//         case 'E':
//             return '3';

//         case 'A':
//             return '4';

//         case 'S':
//             return '5';

//         case 'b':
//             return '6';

//         case 'T':
//             return '7';

//         case 'B':
//             return '8';

//         case 'g':
//             return '9';

//         case 'o':
//             return '0';
//         default:
//             return (letter);
//     }
// }

// const textToConvert = (word) => {
//     for (letter of word) {
//         console.log(normalToNigma(letter))
//     }
// }

// textToConvert('SLIM COW')

const normalToNigma = (letter) =>{
    switch (letter) {
        case 'A':
            return '4';
        
        case 'B':
            return 'I3';
        
        case 'C':
            return '[';
        
        case 'D':
            return ')';
        
        case 'E':
            return '3';
        
        case 'F':
            return '|=';
            
        case 'G':
            return '&';
        
        case 'H':
            return '#';
        
        case 'I':
            return '1';

        case '1':
            return 'I';

        case 'J':
            return ',_|';

        case 'K':
            return '>|';

        case 'L':
            return '1';

        case 'M':
            return `/\\/\\`;

        case 'N':
            return '^/';

        case 'O':
            return '0';

        case 'P':
            return '|*';

        case 'Q':
            return '(_,)';

        case 'R':
            return 'I2';

        case 'S':
            return '5';

        case 'T':
            return '7';

        case 'U':
            return '(_)';

        case 'V':
            return '\\/';

        case 'W':
            return `\\/\\/`;

        case 'X':
            return '><';

        case 'Y':
            return 'j';

        case 'Z':
            return '2';


        //Numbers

        case '1':
            return 'L';

        case '2':
            return 'R';

        case '3':
            return 'E';

        case '4':
            return 'A';

        case '5':
            return 'S';

        case '6':
            return 'b';

        case '7':
            return 'T';

        case '8':
            return 'B';

        case '9':
            return 'g';

        case '0':
            return 'o';
        default:
            return (letter);
    }
}

let normalText = 'slim cow'

let arr = normalText.toUpperCase().split('')

let convertedText = arr.map(item => normalToNigma(item))

let finalString = convertedText.join('')

console.log(finalString)
