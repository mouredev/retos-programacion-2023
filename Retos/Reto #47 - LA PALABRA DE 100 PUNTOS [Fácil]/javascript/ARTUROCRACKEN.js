/*
 * La última semana de 2021 comenzamos la actividad de retos de programación,
 * con la intención de resolver un ejercicio cada semana para mejorar
 * nuestra lógica... ¡Hemos llegado al EJERCICIO 100! Gracias 🙌
 *
 * Crea un programa que calcule los puntos de una palabra.
 * - Cada letra tiene un valor asignado. Por ejemplo, en el abecedario
 *   español de 27 letras, la A vale 1 y la Z 27.
 * - El programa muestra el valor de los puntos de cada palabra introducida.
 * - El programa finaliza si logras introducir una palabra de 100 puntos.
 * - Puedes usar la terminal para interactuar con el usuario y solicitarle
 *   cada palabra.
 */

// Para empezar, creamos una cadena que contiene los 27 caracteres del abecedario en mayúsculas.
const letras = "ABCDEFGHIJKLMNÑOPQRSTUVWXYZ";

// creamos la función main (La principal para ejecutar el programa)
function palabra_de_100_Pts() {
  // a continuación, creamos una serie de ventanas emergentes para decirle al usuario
  // de que trata el juego. (OPCIONAL)
  alert("¡Bienvenido al juego de los 100 puntos!");
  alert(
    "Este juego consiste en que debes formar una palabra que sume exactamente 100 puntos."
  );
  alert("Donde A vale 1 punto, y Z vale 27.");
  alert("El juego termina cuando la palabra valga 100pts. ¡SUERTE!");

  // utilizamos un bucle while, para pedirle la palabra al usuario hasta que su valor sea igual
  // a 100 puntos.
  // luego, utilizamos el template string para decir cuantos puntos suma la palabra introducida
  // por el usuario.
  while (true) {
    let palabra = prompt("Introduce una palabra de 100pts: ");
    let puntos = puntuar_letras(palabra);

    if (puntos == 100) {
      alert("¡Excelente! Esa palabra vale 100pts. ¡GANASTE!");
      break;
    } else {
      alert(`Intentalo de nuevo, esa palabra suma ${puntos}pts, no 100pts.`);
    }
  }
}

// creamos una función para puntuar cada caracter. (La función retorna la cantidad de puntos de
// la palabra)
function puntuar_letras(palabra) {
  let pts = 0;
  // convertimos los caracteres a mayúsculas para que coincidan con los de la cadena 'Letras'.
  palabra = palabra.toUpperCase();
  for (let i = 0; i < letras.length; i++) {
    pts += letras.indexOf(palabra[i]) + 1;
  }
  return pts;
}

// ejecutamos la funcion main.
palabra_de_100_Pts();
