let string = 'i am 21 year old';
let arr = string.split('');


for ( let numberAndLetter of arr ) {

    numberAndLetter === '0' ? console.log(numberAndLetter.replace('0', 'o'))                :
    numberAndLetter === '1' ? console.log(numberAndLetter.replace('1', 'L'))                :
    numberAndLetter === '2' ? console.log(numberAndLetter.replace('2', 'R'))                :
    numberAndLetter === '3' ? console.log(numberAndLetter.replace('3', 'E'))                :
    numberAndLetter === '4' ? console.log(numberAndLetter.replace('4', 'A'))                :
    numberAndLetter === '5' ? console.log(numberAndLetter.replace('5', 'S'))                :
    numberAndLetter === '6' ? console.log(numberAndLetter.replace('6', 'b'))                :
    numberAndLetter === '7' ? console.log(numberAndLetter.replace('7', 'T'))                :
    numberAndLetter === '8' ? console.log(numberAndLetter.replace('8', 'B'))                :
    numberAndLetter === '9' ? console.log(numberAndLetter.replace('9', 'g'))                :
    
    numberAndLetter === 'a' ? console.log(numberAndLetter.replace('a', '4'))                :
    numberAndLetter === 'b' ? console.log(numberAndLetter.replace('b', 'I3'))               :
    numberAndLetter === 'c' ? console.log(numberAndLetter.replace('c', '['))                :
    numberAndLetter === 'd' ? console.log(numberAndLetter.replace('d', 'I)'))               :
    numberAndLetter === 'e' ? console.log(numberAndLetter.replace('e', '3'))                :
    numberAndLetter === 'f' ? console.log(numberAndLetter.replace('f', '|='))               :
    numberAndLetter === 'g' ? console.log(numberAndLetter.replace('g', '&'))                :
    numberAndLetter === 'h' ? console.log(numberAndLetter.replace('h', '#'))                :
    numberAndLetter === 'i' ? console.log(numberAndLetter.replace('i', '1'))                :
    numberAndLetter === 'j' ? console.log(numberAndLetter.replace('j', ',_|'))              :
    numberAndLetter === 'k' ? console.log(numberAndLetter.replace('k', '>|'))               : 
    numberAndLetter === 'l' ? console.log(numberAndLetter.replace('l', '1'))                :
    numberAndLetter === 'm' ? console.log(numberAndLetter.replace('m', '{V}'))              :
    numberAndLetter === 'n' ? console.log(numberAndLetter.replace('n', '^/'))               :
    numberAndLetter === 'ñ' ? console.log(numberAndLetter.replace('ñ', 'letter not found')) :
    numberAndLetter === 'o' ? console.log(numberAndLetter.replace('o', '0'))                :
    numberAndLetter === 'p' ? console.log(numberAndLetter.replace('p', '|*'))               :
    numberAndLetter === 'q' ? console.log(numberAndLetter.replace('q', '(_,)'))             :
    numberAndLetter === 'r' ? console.log(numberAndLetter.replace('r', 'I2'))               :
    numberAndLetter === 's' ? console.log(numberAndLetter.replace('s', '5'))                :
    numberAndLetter === 't' ? console.log(numberAndLetter.replace('t', '7'))                :
    numberAndLetter === 'u' ? console.log(numberAndLetter.replace('u', '(_)'))              :
    numberAndLetter === 'v' ? console.log(numberAndLetter.replace('v', 'V'))                :
    numberAndLetter === 'w' ? console.log(numberAndLetter.replace('w', 'VV'))               :
    numberAndLetter === 'x' ? console.log(numberAndLetter.replace('x', '><'))               :
    numberAndLetter === 'y' ? console.log(numberAndLetter.replace('y', 'j'))                :
    numberAndLetter === ' ' ? console.log(numberAndLetter.replace(' ', '  '))               :
    numberAndLetter === 'z' ? console.log(numberAndLetter.replace('z', 'I3')) : 'Sorry letter not founded' ;      
    
}



