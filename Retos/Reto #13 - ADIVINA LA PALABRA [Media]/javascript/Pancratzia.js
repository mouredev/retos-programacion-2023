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
  });

  return aux;
};

const imprimirMensaje = (palabraOculta, intentos) => {
  console.log(`Palabra a adivinar: ${palabraOculta}`);
  console.log(`Intentos restantes : ${intentos}`);
};

const leerString = () => {
  return "leyendo...";
}

const main = () => {
  let palabra = palabras[Math.floor(Math.random() * palabras.length)];
  palabra = palabra.toLowerCase();
  let palabraOculta = ocultarLetras(palabra);
  let intentos = 3;

  console.log("---- ADIVINA LA PALABRA ----");
  imprimirMensaje(palabraOculta, intentos);

  for (let i = 0; i < intentos; i++) {
    leerString();
  }

  
};

main();
