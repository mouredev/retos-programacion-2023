const leet = {
    a: '4',
    b: 'l3',
    c: '[',
    d: ')',
    e: '3',
    f: '|=',
    g: '&',
    h: '#',
    i: '1',
    j: ',_|',
    k: '>|',
    l: '1',
    m: '/\\/\\"',
    n: '^/',
    o: '0',
    p: '|*',
    q: '(_,)',
    r: 'I2',
    s: '5',
    t: '7',
    u: '(_)',
    v: '\\/',
    w: '\\/\\/',
    x: '><',
    y: 'j',
    z: '2'
}

const readline = 
    require('readline').createInterface({ 
        input: process.stdin, 
        output: process.stdout 
    });

readline.question('Escribe tu texto: ', (texto) => {
    console.log(convertirALeet(texto));
    readline.close();
});

function convertirALeet(texto) {
    let resultado = '';

    for (const caracter of texto.toLowerCase()) {
        resultado += leet[caracter] ?? caracter;
    }

    return resultado;
}