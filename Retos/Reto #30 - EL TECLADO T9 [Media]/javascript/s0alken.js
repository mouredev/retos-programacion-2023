const decodeMessage = (pressed) => {

    keys = [
        ' 0',
        '.?!1',
        'ABC2',
        'DEF3',
        'GHI4',
        'JKL5',
        'MNO6',
        'PQRS7',
        'TUV8',
        'WXYZ9',
    ]

    return pressed.split('-').reduce((message, sequence) => {
        const number = Number(sequence[0]);
        const char = sequence.length - 1;
        message += keys[number][char];
        return message;
    }, '')
}

console.log(decodeMessage('6-666-88-777-33-3-33-888'))


