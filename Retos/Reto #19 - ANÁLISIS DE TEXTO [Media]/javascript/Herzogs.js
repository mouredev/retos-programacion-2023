let palabraMasLarga = '';
let nPal = 0;
let nOrac = 0;
let nCar = 0;

const text = `Nos encontramos en un periodo de guerra civil.
              Las naves espaciales rebeldes, atacando desde una base oculta, han logrado su primera victoria contra el malvado Imperio Galáctico.
              Durante la batalla, los espías rebeldes han conseguido apoderarse de los planos secretos del arma total y definitiva del Imperio,
              la ESTRELLA DE LA MUERTE, una estación espacial acorazada, llevando en sí potencia suficiente para destruir a un planeta entero.
              Perseguida por los siniestros agentes del Imperio, la Princesa Leia vuela hacia su patria, abordo de su nave espacial,
              llevando consigo los planos robados, que pueden salvar a su pueblo y devolver la libertad a la galaxia....`;

const array = text.toLowerCase().split(' ');
nPal = array.length;
array.forEach(word =>{
  if(word.indexOf('.') !== -1)
    nOrac++;
  const newWord = word.replaceAll('[^\w]','');
  nCar += newWord.length;
  //console.log(nCar);
  if(palabraMasLarga === '' || palabraMasLarga.length < newWord.length)
    palabraMasLarga = newWord;
});

console.log(`La cadena analizada contiene:
             Palabras: ${nPal}
             Oraciones ${nOrac}
             Longitud media: ${nCar/nPal}
             Palabra mas larga: ${palabraMasLarga}`);
