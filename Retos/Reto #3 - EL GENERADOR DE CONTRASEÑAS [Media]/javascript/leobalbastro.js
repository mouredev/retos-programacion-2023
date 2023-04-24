/*
 * Escribe un programa que sea capaz de generar contraseñas de forma aleatoria.
 * Podrás configurar generar contraseñas con los siguientes parámetros:
 * - Longitud: Entre 8 y 16.
 * - Con o sin letras mayúsculas.
 * - Con o sin números.
 * - Con o sin símbolos.
 * (Pudiendo combinar todos estos parámetros entre ellos)
 */

function randomPassword(long, mayus, num, sim) {
  let abc = "a b c d e f g h i j k l m n o p q r s t u v w x y z".split(" ");
  let numList = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9];
  let sym = [
    "|",
    "#",
    "@",
    "~",
    "€",
    "¬",
    "/",
    "(",
    ")",
    "!",
    "·",
    "$",
    "%",
    "&",
  ];

  let generatedPass = "";

  for (let index = 0; index < long; index++) {
    try {
      if (long > 7 && long < 17) {
        let randomizerString = Math.floor(Math.random() * 26);
        let randomizerStringMayus = Math.floor(Math.random() * 26);
        let randomizerNum = Math.floor(Math.random() * 10);
        let randomizerSym = Math.floor(Math.random() * 14);
        generatedPass += abc[randomizerString];
        if (mayus && generatedPass.length < long) {
          generatedPass += abc[randomizerStringMayus].toUpperCase();
          index += 1;
        }
        if (num && generatedPass.length < long) {
          generatedPass += numList[randomizerNum];
          index += 1;
        }
        if (sim && generatedPass.length < long) {
          generatedPass += sym[randomizerSym];
          index += 1;
        }
      } else {
        throw new Error(
          "La longitud ingresada no es correcta, debes ingresar una longitud entre 8 y 16 digitos"
        );
      }
    } catch (error) {
      console.log(error.message);
      break;
    }
    
    if (generatedPass.length===long) console.log(`tu password Generada es: ${generatedPass}`);
  }
}

randomPassword(15, true, true, true);
