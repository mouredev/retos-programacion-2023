// * Crea un pequeño juego que consista en adivinar palabras en un número máximo de intentos:
// * - El juego comienza proponiendo una palabra aleatoria incompleta
// *   - Por ejemplo "m_ur_d_v", y el número de intentos que le quedan
// * - El usuario puede introducir únicamente una letra o una palabra (de la misma longitud que
// *   la palabra a adivinar)
// *   - Si escribe una letra y acierta, se muestra esa letra en la palabra. Si falla, se resta
// *     uno al número de intentos
// *   - Si escribe una resolución y acierta, finaliza el juego, en caso contrario, se resta uno
// *     al número de intentos
// *   - Si el contador de intentos llega a 0, el jugador pierde
// * - La palabra debe ocultar de forma aleatoria letras, y nunca puede comenzar ocultando más del 60%
// * - Puedes utilizar las palabras que quieras y el número de intentos que consideres
const rl = require('readline').createInterface({ input: process.stdin, output: process.stdout});
const catFigure: { [key: number]: string } = {
  0: `
   /\\___\/\\  (
  ( ^ .^ ) _)
 \\"/\\/"\\ (
  (  | | )
 (__d b__) GAME OVER`,
  1: `
   /\\___\/\\  (
  ( ^ .^ ) _)
   \\"/\\/"\\ (
  ( | | )
 (__d b__)`,
  2: `
   /\\___\/\\  
  ( ^ .^ ) 
   \\"/\\/"\\ 
  ( | | )
 (__d b__)`,
  3: `
   /\\___\/\\  
  (^ .^ ) 
   \\"/\\/"\\ 
  ( | | )`,
  4: `
   /\\___\/\\  
  ( ^ .^ ) 
   \\"/\\/"\\ `,
  5: `
   /\\___\/\\  
  ( ^ .^ ) `,
};
const words: { [key: string]: string[] } = {
  EN: [ 'Apple', 'Banana', 'Monitor', 'Lemon', 'Elephant', 'Flower', 'Grape', 'House', 'Fish', 'Jacket', 'Rice', 'Lion', 'Camera', 'Notebook', 'Orange', 'Tomato', 'Queen', 'Rabbit', 'Shirt', 'Tree', 'Umbrella', 'Violin', 'Water', 'Xylophone', 'Yellow', 'Book', 'Shoe', 'Chair','Desk', 'Egg', 'Goat', 'Globe', 'Lion', 'Duck', 'mouse', 'Juice', 'Kite', 'Lamp', 'Moon', 'Nail', 'Ocean', 'berserk'],
  ES: [ 'Amarillo', 'Bicicleta', 'Casa', 'Diente', 'Elefante', 'Flor', 'Gato', 'Helado', 'Isla', 'Jirafa', 'Kilometro', 'Lapiz', 'Manzana', 'Naranja', 'Oso','Pajaro','Queso', 'Rana', 'Silla', 'Tigre', 'Uva', 'Vaso', 'Mascara','Yate', 'Zanahoria', 'Arbol', 'Goma', 'Cama', 'Ducha', 'Escalera', 'Fiesta', 'Gafas', 'Huevo', 'Invierno', 'Jardín', 'Llave', 'Maleta', 'Nube', 'Ojo', 'Piso'],
};

const getRandomWord = (lang: string): [string, number] => {
  const DEFAULTPERCENTAGE = 60;
  const word = words[lang][Math.floor(Math.random() * words[lang].length)].toLowerCase();
  const revealWord = Math.ceil((DEFAULTPERCENTAGE /100 ) * word.length);
  return [word, revealWord];
};

function hideWord(lang:string): string[] {
  const [word, hiddenCount] =  getRandomWord(lang);
  const hiddenIndexes = new Set<number>();

  while (hiddenIndexes.size < hiddenCount) {
    hiddenIndexes.add(Math.floor(Math.random() * word.length));
  };

  let hiddenWord = '';

  for (let i = 0; i < word.length; i++) {
    if (hiddenIndexes.has(i)) {
      hiddenWord += '_';
    } else {
      hiddenWord += word[i];
    }
  };
  return [word, hiddenWord];
};

const letsPlay = ():void => {
 const DEFAULTLIVES = 5;

 rl.question('Choose Lag: EN or ES:', (answer:string) => {
  if (answer === "ES" || answer === "EN") {
    const [originalWord, currentWord] = hideWord(answer);
    _letsPlay(DEFAULTLIVES, originalWord, currentWord); 
  } else {
    return letsPlay();
  }
 });
};

const printMsg = (guess:string, lives:number, currentWord:string, additional=false):void => {
  console.log('');
  console.log(`your letter, ${guess}` + `${additional ? ' is not in the word' : ' is in the word'}`);
  console.log(`you have ${lives} lives left`);
  console.log("current word: " + currentWord + '\n');
};

const _letsPlay = (lives:number, originalWord:string, currentWord:string):void => {
  if (lives === 0)  {
    console.log("you have no more lives");
    console.log(catFigure[lives] + 'the word was', originalWord);
    rl.close();
    return
  }
  if (originalWord === currentWord) {
    console.log('YOU WIN!!, The word was', originalWord);
    rl.close()
    return;
  }
  rl.question('Guess a letter: ', (guess:string) => {
    if (originalWord.includes(guess)) {
      let newWord = '';
      for (let index = 0; index < originalWord.length; index++) {
        if (originalWord[index] === guess) {
          newWord += guess;
        } else {
           newWord += currentWord[index];
        }
      }
      printMsg(guess, lives, currentWord)
      _letsPlay(lives, originalWord, newWord);
    } else {
      printMsg(guess, lives, currentWord, true);
      console.log(catFigure[lives]);
      _letsPlay(lives-1, originalWord, currentWord);
    }
  });
};

letsPlay();
