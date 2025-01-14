/*
 * Crea una función que simule las condiciones climáticas (temperatura y probabilidad de lluvia)
 * de un lugar ficticio al pasar un número concreto de días según estas reglas:
 * - La temperatura inicial y el % de probabilidad de lluvia lo define el usuario.
 * - Cada día que pasa:
 *   - 10% de posibilidades de que la temperatura aumente o disminuya 2 grados.
 *   - Si la temperatura supera los 25 grados, la probabilidad de lluvia al día
 *     siguiente aumenta en un 20%.
 *   - Si la temperatura baja de 5 grados, la probabilidad de lluvia al día
 *     siguiente disminuye en un 20%.
 *   - Si llueve (100%), la temperatura del día siguiente disminuye en 1 grado.
 * - La función recibe el número de días de la predicción y muestra la temperatura
 *   y si llueve durante todos esos días.
 * - También mostrará la temperatura máxima y mínima de ese periodo y cuántos días va a llover.
 */

function weather({ days = 1, temperatura = 25, probLluvia = 10 }) {
  // Validando inputs
  if (
    typeof days !== "number" ||
    typeof temperatura !== "number" ||
    typeof probLluvia !== "number"
  ) {
    console.error(
      "Error: Invalid input.\n    Input must be: ({ int, int, int })"
    );
  } else if (days < 1) {
    console.error("Error: Invalid input.\n    days must be Positive.");
  } else if (probLluvia < 0 || probLluvia > 100) {
    console.error(
      "Error: Invalid input.\n    probLluvia must be positive and less or equal than 100."
    );
  }

  // Declarando variables
  let estado = "Soleado";
  let diasLluviosos = 0;
  let minTemp = temperatura;
  let maxTemp = temperatura;

  console.log("---------- Clima ----------\n");
  for (let i = 0; i < days; i++) {
    let randomNum = Math.round(Math.random() * 9);

    // Logica de la temperatura
    if (randomNum == 8) {
      temperatura += 2;
    } else if (randomNum == 7) {
      temperatura -= 2;
    }

    // Seteando la temperatura maxima y minima del periodo
    if (temperatura > maxTemp) {
      maxTemp = temperatura;
    }
    if (temperatura < minTemp) {
      minTemp = temperatura;
    }

    // Logica de la probabilidad de lluvia
    if (temperatura > 25) {
      probLluvia += 20;
      if (probLluvia > 100) {
        probLluvia = 100;
      }
    } else if (temperatura < 5) {
      probLluvia -= 20;
      if (probLluvia < 0) {
        probLluvia = 0;
      }
    }

    // Logica del estado del clima
    let num = Math.round(probLluvia / 10);
    estado = "Soleado";

    // Si la probabilidad de lluvia es de 100%
    if (num == 10) {
      estado = "Lluvioso";
      diasLluviosos += 1;
    }

    // Imprimiendo los datos en pantalla
    console.log(`Dia ${i + 1}:\n
        Temperatura: ${temperatura}°
        Probabilidad de lluvia: ${probLluvia}%
        Estado: ${estado}
        `);
    console.log("---------------------------");

    if (estado == "Lluvioso") {
      temperatura -= 1;
    }
  }

  console.log("---------------------------");

  console.log(`\nTotal:
    Dias lluviosos: ${diasLluviosos}
    Temperatura minima: ${minTemp}°
    Temperatura maxima: ${maxTemp}°
    `);

  console.log("---------------------------");
}

weather({ days: 24, temperatura: 24, probLluvia: 80 });
