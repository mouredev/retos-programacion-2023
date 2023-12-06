/*

* Crea un pequeño juego que consista en adivinar palabras en un número máximo de intentos:
 * - El juego comienza proponiendo una palabra aleatoria incompleta
 *   - Por ejemplo "m_ur_d_v", y el número de intentos que le quedan
 * - El usuario puede introducir únicamente una letra o una palabra (de la misma longitud que
 *   la palabra a adivinar)
 *   - Si escribe una letra y acierta, se muestra esa letra en la palabra. Si falla, se resta
 *     uno al número de intentos
 *   - Si escribe una resolución y acierta, finaliza el juego, en caso contrario, se resta uno
 *     al número de intentos
 *   - Si el contador de intentos llega a 0, el jugador pierde
 * - La palabra debe ocultar de forma aleatoria letras, y nunca puede comenzar ocultando más del 60%
 * - Puedes utilizar las palabras que quieras y el número de intentos que consideres 
*/


function game(words) {
  var word = words[Math.floor(Math.random() * words.length)];
  var hidden_letters = Math.floor(word.length * 0.6);
  var hidden_position = [];
  while (hidden_position.length < hidden_letters) {
    var random_index = Math.floor(Math.random() * word.length);
    if (hidden_position.indexOf(random_index) === -1) {
      hidden_position.push(random_index);
    }
  }
  var hidden_word = "";
  for (var i = 0; i < word.length; i++) {
    if (hidden_position.indexOf(i) !== -1) {
      hidden_word += "_";
    } else {
      hidden_word += word[i];
    }
  }
  var attempts = 5;
  while (attempts > 0) {
    console.log("Adivina la palabra: " + hidden_word);
    console.log("Tienes " + attempts + " intentos.");
    var text = prompt("Introduce una letra o la solución completa: ");
    if (text.length === 1) {
      var new_hidden_word = "";
      var success = false;
      for (var index = 0; index < word.length; index++) {
        if (text === word[index] && hidden_word[index] === "_") {
          new_hidden_word += text;
          success = true;
        } else {
          new_hidden_word += hidden_word[index];
        }
      }
      hidden_word = new_hidden_word;
      if (success) {
        if (word === hidden_word) {
          return `¡Has acertado! La palabra oculta era ${word}.`;
        } else {
          console.log("¡Has acertado la letra!");
        }
      } else {
        console.log("Letra no encontrada o ya visible.");
        attempts--;
      }
    } else if (text.length === word.length) {
      if (text === word) {
        return `Ganaste! la palabra era: ${word}.`;
      } else {
        console.log("Palabra incorrecta.");
        attempts--;
      }
    } else {
      console.log("Texto inválido.");
    }
  }
  if (attempts === 0) {
    return `Has perdido. La palabra oculta era ${word}.`;
  }
}

console.log(game(["lemito66", "murcielago", "casa", "perro", "gato"]));
