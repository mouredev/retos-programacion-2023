let string = 'i need a v';
let arr = string.split('');


for ( let letter of arr ) {
    
    letter === 'a' ? console.log(letter.replace('a', '4'))                :
    letter === 'b' ? console.log(letter.replace('b', 'I3'))               :
    letter === 'c' ? console.log(letter.replace('c', '['))                :
    letter === 'd' ? console.log(letter.replace('d', 'I)'))               :
    letter === 'e' ? console.log(letter.replace('e', '3'))                :
    letter === 'f' ? console.log(letter.replace('f', '|='))               :
    letter === 'g' ? console.log(letter.replace('g', '&'))                :
    letter === 'h' ? console.log(letter.replace('h', '#'))                :
    letter === 'i' ? console.log(letter.replace('i', '1'))                :
    letter === 'j' ? console.log(letter.replace('j', ',_|'))              :
    letter === 'k' ? console.log(letter.replace('k', '>|'))               :
    letter === 'l' ? console.log(letter.replace('l', '1'))                :
    letter === 'm' ? console.log(letter.replace('m', '{V}'))              :
    letter === 'n' ? console.log(letter.replace('n', '^/'))               :
    letter === 'ñ' ? console.log(letter.replace('ñ', 'letter not found')) :
    letter === 'o' ? console.log(letter.replace('o', '0'))                :
    letter === 'p' ? console.log(letter.replace('p', '|*'))               :
    letter === 'q' ? console.log(letter.replace('q', '(_,)'))             :
    letter === 'r' ? console.log(letter.replace('r', 'I2'))               :
    letter === 's' ? console.log(letter.replace('s', '5'))                :
    letter === 't' ? console.log(letter.replace('t', '7'))                :
    letter === 'u' ? console.log(letter.replace('u', '(_)'))              :
    letter === 'v' ? console.log(letter.replace('v', 'V'))               :
    letter === 'w' ? console.log(letter.replace('w', 'VV'))             :
    letter === 'x' ? console.log(letter.replace('x', '><'))               :
    letter === 'y' ? console.log(letter.replace('y', 'j'))                :
    letter === ' ' ? console.log(letter.replace(' ', '  '))               :
    letter === 'z' ? console.log(letter.replace('z', 'I3')) : 'Sorry letter not founded' ;
        
}



