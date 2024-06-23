const alphabetHacker = new Map([
    ['1', 'L'], ['2', 'R'], ['3', 'E'], ['4', 'A'], ['5', 'S'], ['6', 'b'], ['7', 'T'], ['8', 'B'], ['9', 'g'], ['0', 'o'],
    ['a', '4'], ['b', 'I3'], ['c', '['], ['d', ')'], ['e', '3'], ['f', '|='], ['g', '&'], ['h', '#'], ['i', '1'],
    ['j', ',_|'], ['k', '>|'], ['l', '1'], ['m', '/\\/\\'], ['n', '^/'], ['o', '0'], ['p', '|*'], ['q', '(_,)'],
    ['r', 'I2'], ['s', '5'], ['t', '7'], ['u', '(_)'], ['v', '\/'], ['w', '\/\/'], ['x', '><'], ['y', 'j'], ['z', '2'],
]);

const convertHacker = (phrase) => {
    alphabetHacker.forEach((hacker, abecedario) => {
        phrase = phrase.replaceAll(abecedario, hacker);
    })

    console.log(phrase);
}

let phrase = 'La noche es oscura por lo que el dia es soleado. Pero cuidado que en la noche te atacan 3 moustros.'; //Example

convertHacker(phrase);
