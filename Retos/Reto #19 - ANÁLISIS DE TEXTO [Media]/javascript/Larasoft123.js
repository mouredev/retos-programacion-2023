function analizeText(text) {
  const dataWord = {
    wordsCount: 0,
    lettersCount: 0,
    sentences_count: 0,
    longestWord: [],
  };

  const words = text.replaceAll("\n", " ").split(" ");

  for (const word of words) {
    if (word === "") continue;
    dataWord.wordsCount++;
    dataWord.lettersCount += word.length;

    // SI HAY UN PUNTO ENTONCES ES OTRA ORACION, EN ESTE CASO NO IMPORTA QUE TERMINE EN ... YA QUE SOLO CONTARÁ 1 PUNTO
    if (word.includes(".")) dataWord.sentences_count++;

    if (dataWord.longestWord.length == 0) {
      dataWord.longestWord.push(word);
    }
    // ACTUALIZAMOS LA PALABRA MAS LARGA SI LA NUEVA ES MAS LARGA QUE LA ANTERIOR
    if (word.length > dataWord.longestWord[0].length) {
      dataWord.longestWord.pop();
      dataWord.longestWord.push(word);
    }
  }

  console.log(`el numero de palabras es ${dataWord.wordsCount}`);
  console.log(
    `La longitud media de las palabras en la oracion es ${Math.floor(
      dataWord.lettersCount / dataWord.wordsCount
    )}`
  );
  console.log(`numero de oraciones en el texto ${dataWord.sentences_count}`);
  console.log(`La palabra mas larga en el texto es ${dataWord.longestWord}`);
}

analizeText(`Nos encontramos en un
periodo de guerra civil. Las
naves espaciales rebeldes,
atacando desde una base
oculta, han logrado su 
primera victoria contra
el malvado Imperio
Galáctico.

Durante la batalla, los 
espías rebeldes han
conseguido apoderarse de 
los planos secretos del
arma total y definitiva del
Imperio, la ESTRELLA
DE LA MUERTE,
una estación espacial
acorazada, llevando en sí
potencia suficiente para
destruir a un planeta
entero.

Perseguida por los 
siniestros agentes del 
Imperio, la Princesa Leia 
vuela hacia su patria, a
bordo de su nave espacial,
llevando consigo los
planos robados, que
pueden salvar a su pueblo
y devolver la libertad a la
galaxia....`);
