const letras = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J',
    'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U',
    'V', 'W', 'X', 'Y', 'Z',' ','.',','
];

const conversion = ['4', 'I3', '[', ')', '3', '|=', '&', '#', '1', ',_|',
    '>|', '1', '/\\/\\', '^/', '0', '|*', '(_,)', 'I2', '5', '7', '(_)',
    '\\/', '\\/\\/', '><', 'j', '2',' ','.',','
];

function traductorLeet(text: string): string {

    const texto = text.toUpperCase().split('')
    let textoTraducido : string = '';
    texto.map((character) => {
        let indice = letras.indexOf(character)
        textoTraducido+= conversion[indice]
    })
    return textoTraducido;
}

traductorLeet('Esto es un ejemplo de pruebas')
