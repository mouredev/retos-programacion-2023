/*
  Crea un pequeño juego que consista en adivinar palabras en un número máximo de intentos:
  - El juego comienza proponiendo una palabra aleatoria incompleta
    - Por ejemplo "m_ur_d_v", y el número de intentos que le quedan
  - El usuario puede introducir únicamente una letra o una palabra (de la misma longitud que
    la palabra a adivinar)
    - Si escribe una letra y acierta, se muestra esa letra en la palabra. Si falla, se resta
    uno al número de intentos
    - Si escribe una resolución y acierta, finaliza el juego, en caso contrario, se resta uno
    al número de intentos
    - Si el contador de intentos llega a 0, el jugador pierde
  - La palabra debe ocultar de forma aleatoria letras, y nunca puede comenzar ocultando más del 60%
  - Puedes utilizar las palabras que quieras y el número de intentos que consideres
*/

const palabras = ["murcielago", "televisor", "camaleon", "platano", "guitarra"];

const maxIntentos = 5;

let palabraAzar = palabras[Math.floor(Math.random() * palabras.length)];
let palabraOcultar = ocultarPalabra(palabraAzar);

let intentosRestantes = maxIntentos;

function ocultarPalabra(palabra) {
  const ocultarI = Math.floor(Math.random() * palabra.length * 0.4);
  const ocultarF = Math.floor(Math.random() * (palabra.length - ocultarI));

  let palabraOculta = "";

  for (let i = 0; i < palabra.length; i++) {
    if (i >= ocultarI && i < ocultarF) {
      palabraOculta = palabraOculta + "_";
    } else {
      palabraOculta = palabraOculta + palabra[i];
    }
  }

  return palabraOculta;
}

function mostrarJuego() {
  console.log(
    "Palabra a adivinar: " +
      palabraOcultar +
      " - " +
      "Intentos restantes: " +
      intentosRestantes
  );
}

function comprobarVictoria() {
  return palabraAzar === palabraOcultar;
}

function actualizarPalabra(letra) {
  let nuevaPalabraOculta = "";

  for (let i = 0; i < palabraAzar.length; i++) {
    if (palabraAzar[i] === letra) {
      nuevaPalabraOculta = nuevaPalabraOculta + letra;
    } else {
      nuevaPalabraOculta = nuevaPalabraOculta + palabraOcultar[i];
    }
  }

  palabraOcultar = nuevaPalabraOculta;
}


async function jugar() {
  const readline = require("readline").createInterface({
    input: process.stdin,
    output: process.stdout,
  });

  while (intentosRestantes > 0 && !comprobarVictoria()) {
    mostrarJuego();
    const respuesta = await pregunta("Introduce una letra o una palabra: ");
    if (respuesta.length === 1) {
      if (palabraAzar.includes(respuesta)) {
        actualizarPalabra(respuesta);
      } else {
        intentosRestantes = intentosRestantes - 1;
      }
    } else {
      if (respuesta === palabraAzar) {
        palabraOcultar = palabraAzar;
      } else {
        intentosRestantes = intentosRestantes - 1;
      }
    }
  }

  if (comprobarVictoria()) {
    console.log(`¡Felicidades, has ganado! La palabra era ${palabraAzar}.`);
  } else {
    console.log(`¡Lo siento, has perdido! La palabra era ${palabraAzar}.`);
  }

  readline.close();
}

function pregunta(pregunta) {
  return new Promise((resolve) => {
    const readline = require("readline").createInterface({
      input: process.stdin,
      output: process.stdout,
      terminal:false
    });
    readline.question(pregunta, (respuesta) => {
      resolve(respuesta.toLowerCase());
      readline.close();
    });
  });
}

jugar();
