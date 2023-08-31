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
 *
 * CREADO POR LAURA ORTEGA - 30/08/2023
 */

const readline = require("readline");
const rl = readline.createInterface({
  input: process.stdin,
  output: process.stdout,
});

const palabras = [
  "Perro",
  "Doctor",
  "Anaranjado",
  "Morado",
  "Tiffany",
  "Arthuro",
  "Sancocho",
  "Amarillo",
  "Blanco",
  "Paranguaricutirimicuaro",
  "Rojizo",
  "HolaMundo",
];

String.prototype.replaceAt = function (index, replacement) {
  //Para reemplazar caracteres por *
  if (index >= this.length) {
    return this.valueOf();
  }

  return this.substring(0, index) + replacement + this.substring(index + 1);
};

const ocultarLetras = (palabra) => {
  const maxLetrasAOcultarPermitidas = Math.floor(palabra.length * 0.6);
  let aux = palabra;
  ocultas = 0;

  palabra.split("").forEach((letra, index) => {
    if (
      ocultas < maxLetrasAOcultarPermitidas &&
      Math.random() > 0.5 &&
      letra !== "_"
    ) {

      if(contarPresenciaDeLetra(palabra, letra) <= (maxLetrasAOcultarPermitidas - ocultas)){ 
        for (let i = 0; i < aux.length; i++) {
          if (aux[i] === letra) {
            aux = aux.replaceAt(i, "_");
            ocultas++;
  
            if (ocultas < maxLetrasAOcultarPermitidas) {
              break;
            }
          }
        }
      }
    }
  });

  return aux;
};

const destaparLetra = (palabra, palabraOculta, letra) =>{
  for (let i = 0; i < palabra.length; i++) {
    if (palabra[i] === letra) {
      palabraOculta = palabraOculta.replaceAt(i, letra);
    }
  }
  return palabraOculta;
}

const contarPresenciaDeLetra = (palabra, letra) => {
  let contador = 0;
  for (let i = 0; i < palabra.length; i++) {
    if (palabra[i] === letra) {
      contador++;
    }
  }

  return contador;
}

const imprimirMensaje = (palabraOculta, intentos) => {
  console.log(`Palabra a adivinar: ${palabraOculta}`);
  console.log(`Intentos restantes : ${intentos}`);
};

const leerString = (palabra) => {
  return new Promise((resolve, reject) => {
    rl.question("Ingresa una letra o palabra: ", (input) => {
      if (input.trim() === "") {
        console.log("¡Debes ingresar algo!");
        leerString(palabra).then(resolve).catch(reject);
        return;
      }

      if (input.length !== 1 && input.length !== palabra.length) {
        console.log("La entrada debe tener 1 caracter o tener la misma longitud que la palabra a adivinar.");
        leerString(palabra).then(resolve).catch(reject);
        return;
      }

      resolve(input);
    });
  });
};




const main = async () => {
  let palabra = palabras[Math.floor(Math.random() * palabras.length)];
  palabra = palabra.toLowerCase();
  let palabraOculta = ocultarLetras(palabra);
  let intentos = 3;

  console.log("---- ADIVINA LA PALABRA ----");
  imprimirMensaje(palabraOculta, intentos);

  let input;

  do{
    do{
    input =  await leerString(palabraOculta);
    console.log(input);
    } while(input.length != 1 && input.length != palabraOculta.length);

    if (input === palabra) {
      palabraOculta = input;
      break;
    }else if(palabra.includes(input)){
      palabraOculta = destaparLetra(palabra, palabraOculta, input);
    }else{
      intentos--;
      console.log(`¡Has fallado! La ${input.length===1 ? "letra" : "palabra"} no es correcta.`);
    }

    if(palabraOculta === palabra)break;
    if (intentos === 0) break;
    imprimirMensaje(palabraOculta, intentos);
    
  }while(intentos > 0);

  rl.close();

  palabraOculta === palabra ? console.log("¡Has ganado!") : console.log("¡Has perdido!");
};

main();
