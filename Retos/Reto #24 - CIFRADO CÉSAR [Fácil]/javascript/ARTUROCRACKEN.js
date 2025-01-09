/*
 * Crea un programa que realize el cifrado César de un texto y lo imprima.
 * También debe ser capaz de descifrarlo cuando así se lo indiquemos.
 *
 * Te recomiendo que busques información para conocer en profundidad cómo
 * realizar el cifrado. Esto también forma parte del reto.
 */

const abecedario = "abcdefghijklmnopqrstuvwxyz";

const cesar = (text, num, decode) => {
  if (typeof text !== "string" || typeof num !== "number") {
    console.error("Invalid input:\n    Input must be: (string, number)");
    return;
  } else if (num < 0) {
    console.error("Number must be positive.");
    return;
  }
  num = Math.floor(num);

  let newAbecedario = "";
  let output = "";

  if (!decode) {
    // codificar abecedario
    for (let i = 0; i < abecedario.length; i++) {
      if (i + num < 26) {
        newAbecedario += abecedario[i + num];
      }
    }
    for (let j = 0; j < num; j++) {
      newAbecedario += abecedario[j];
    }

    // sustituyendo las letras del antiguo abecedario por el codificado
    let letterValues = {
      a: newAbecedario[0],
      b: newAbecedario[1],
      c: newAbecedario[2],
      d: newAbecedario[3],
      e: newAbecedario[4],
      f: newAbecedario[5],
      g: newAbecedario[6],
      h: newAbecedario[7],
      i: newAbecedario[8],
      j: newAbecedario[9],
      k: newAbecedario[10],
      l: newAbecedario[11],
      m: newAbecedario[12],
      n: newAbecedario[13],
      o: newAbecedario[14],
      p: newAbecedario[15],
      q: newAbecedario[16],
      r: newAbecedario[17],
      s: newAbecedario[18],
      t: newAbecedario[19],
      u: newAbecedario[20],
      v: newAbecedario[21],
      w: newAbecedario[22],
      x: newAbecedario[23],
      y: newAbecedario[24],
      z: newAbecedario[25],
    };

    // imprimir nuevo texto
    for (let l = 0; l < text.length; l++) {
      if (text[l].toLowerCase() in letterValues) {
        output += letterValues[text[l].toLowerCase()];
      } else {
        output += text[l];
      }
    }
  } else if (decode == true && typeof decode == "boolean") {
    // codificar abecedario

    for (let j = num; j > 0; j--) {
      newAbecedario += abecedario[abecedario.length - j];
    }

    for (let i = 0; i < abecedario.length; i++) {
      if (
        i - num < abecedario.length - num &&
        abecedario[i - num] !== undefined
      ) {
        newAbecedario += abecedario[i - num];
      }
    }

    // sustituyendo las letras del antiguo abecedario por el codificado
    let letterValues = {
      a: newAbecedario[0],
      b: newAbecedario[1],
      c: newAbecedario[2],
      d: newAbecedario[3],
      e: newAbecedario[4],
      f: newAbecedario[5],
      g: newAbecedario[6],
      h: newAbecedario[7],
      i: newAbecedario[8],
      j: newAbecedario[9],
      k: newAbecedario[10],
      l: newAbecedario[11],
      m: newAbecedario[12],
      n: newAbecedario[13],
      o: newAbecedario[14],
      p: newAbecedario[15],
      q: newAbecedario[16],
      r: newAbecedario[17],
      s: newAbecedario[18],
      t: newAbecedario[19],
      u: newAbecedario[20],
      v: newAbecedario[21],
      w: newAbecedario[22],
      x: newAbecedario[23],
      y: newAbecedario[24],
      z: newAbecedario[25],
    };

    // imprimir nuevo texto
    for (let l = 0; l < text.length; l++) {
      if (text[l].toLowerCase() in letterValues) {
        output += letterValues[text[l].toLowerCase()];
      } else {
        output += text[l];
      }
    }
  } else {
    console.log("Third parameter must be boolean");
    return;
  }

  console.log(output);
};

let decodedString = "pepe juan pedro hijo zzz";
let codedString = "shsh mxdq shgur klmr ccc";

cesar(decodedString, 3); // decode == false // Expected output: shsh mxdq shgur klmr ccc
cesar(codedString, 3, true); // decode == true // Expected output: pepe juan pedro hijo zzz
