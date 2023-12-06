 const alfabeto = [ 
  'a',
  'b',
  'c',
  'd',
  'e',
  'f',
  'g',
  'h',
  'i',
  'j',
  'k',
  'l',
  'm',
  'n',
  'o',
  'p',
  'q',
  'r',
  's',
  't',
  'u',
  'v',
  'w',
  'x',
  'y',
  'z'
];

const concatenar = (prev, next) => prev + next;

function obtenerCaracterEquivalente(caracter)  {
  let indexAlfabeto = 0;
  let caracterEquivalente = '';
  const index = alfabeto.indexOf(caracter);

  if (index === -1) {
    return caracter;
  }
  
  if (this.operador === 'codificar') {
    indexAlfabeto = index + this.desplazamiento;
    caracterEquivalente = indexAlfabeto > 25 ? alfabeto[indexAlfabeto - 24] : alfabeto[indexAlfabeto];
  }
  
  if (this.operador === 'decodificar') {
    indexAlfabeto = index - this.desplazamiento;
    caracterEquivalente = indexAlfabeto < 0 ? alfabeto[24 + indexAlfabeto] : alfabeto[indexAlfabeto];
  }
  
  return caracter === caracter.toUpperCase() ? caracterEquivalente.toUpperCase() : caracterEquivalente;
};

const obtenerTextoEquivalente = (texto, configuracion) => {
  return [...texto]
    .map(obtenerCaracterEquivalente, configuracion)
    .reduce(concatenar, '');
};

const codificar = (texto, desplazamiento) => obtenerTextoEquivalente(texto, { desplazamiento, operador: 'codificar' });

const decodificar = (texto, desplazamiento) => obtenerTextoEquivalente(texto,{ desplazamiento, operador: 'decodificar' });
