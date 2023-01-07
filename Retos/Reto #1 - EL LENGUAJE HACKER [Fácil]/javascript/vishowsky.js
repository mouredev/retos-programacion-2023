const diccionario = {
    a: '4', b: 'I3', c: '[', d: ')', e: '3',
    f: '|=', g: '&', h: '#', i: '1', j: ',_|',
    k: '>|', l: '1', m: '/\\/\\', n: '^/', o: '0',
    p: '|*', q: '(_,)', r: 'I2', s: '5', t: '7',
    u: '(_)', v: '\\/', w: '\\/\\/', x: '><', y: 'j',
    z: '2', ' ': ' '
  };

  function convertirHacker(texto) {
    texto = texto.toLowerCase();
    let resultado = '';
    for (let i = 0; i < texto.length; i++) {
        if (diccionario[texto[i]]) {
            resultado += diccionario[texto[i]];
        }else {
            resultado += texto[i];
          }
        }
        return resultado;

            
}

const palabra = 'vishowsky';
const textoHacker = convertirHacker(palabra);
console.log(textoHacker)