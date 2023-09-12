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
const readline = require('readline');

const rl = readline.createInterface({
    input: process.stdin,
    output: process.stdout
});

// Función para obtener una palabra aleatoria
function obtenerPalabraAleatoria() {
    const palabras = ['python', 'programacion', 'desarrollo', 'computadora', 'teclado'];
    const randomIndex = Math.floor(Math.random() * palabras.length);
    return palabras[randomIndex];
}

// Función para mostrar el tablero del ahorcado
function mostrarTablero(intentos) {
    const figura = [
        `
          +---+
          |   |
              |
              |
              |
              |
        =======`,
        `
          +---+
          |   |
          O   |
              |
              |
              |
        =======`,
        `
          +---+
          |   |
          O   |
          |   |
              |
              |
        =======`,
        `
          +---+
          |   |
          O   |
         /|   |
              |
              |
        =======`,
        `
          +---+
          |   |
          O   |
         /|\\  |
              |
              |
        =======`,
        `
          +---+
          |   |
          O   |
         /|\\  |
         /    |
              |
        =======`,
        `
          +---+
          |   |
          O   |
         /|\\  |
         / \\  |
              |
        =======`
    ];
    console.log(figura[intentos]);
}

// Función para jugar al ahorcado
function jugarAhorcado() {
    const palabra = obtenerPalabraAleatoria();
    const letrasAdivinadas = [];
    let intentos = 0;

    function jugar() {
        mostrarTablero(intentos);
      console.log(palabra);
        let estado = '';
        for (const letra of palabra) {
            if (letrasAdivinadas.includes(letra)) {
                estado += letra + ' ';
            
            } else {
                estado += '_ ';
             
            }
        }
        console.log(estado);

        if (estado.replace(/ /g, "") === palabra) {
          console.log("aca",/ /g);
            console.log('¡Felicidades! ¡Has adivinado la palabra correctamente!');
            rl.close();
            return;
        }

        if (intentos === 6) {
            console.log('¡Oh no! Te has quedado sin intentos. La palabra era:', palabra);
            rl.close();
            return;
        }

        rl.question('Ingresa una letra: ', (letra) => {
            letra = letra.toLowerCase();

            if (letra.length !== 1 || !/^[a-z]$/.test(letra)) {
                console.log('Por favor, ingresa una sola letra válida.');
                jugar();
                return;
            }

            if (letrasAdivinadas.includes(letra)) {
                console.log('Ya has ingresado esa letra antes. ¡Intenta con otra!');
                jugar();
                return;
            }

            letrasAdivinadas.push(letra);

            if (!palabra.includes(letra)) {
                intentos++;
                console.log('La letra', letra, 'no está en la palabra. ¡Te quedan', 6 - intentos, 'intentos!');
            }

            jugar();
        });
    }

    jugar();
}

// Iniciar el juego
jugarAhorcado();
