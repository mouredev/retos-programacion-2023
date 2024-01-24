/*
 * Crea un programa que simule el comportamiento del sombrero seleccionador del
 * universo mágico de Harry Potter.
 * - De ser posible realizará 5 preguntas (como mínimo) a través de la terminal.
 * - Cada pregunta tendrá 4 respuestas posibles (también a selecciona una a través de terminal).
 * - En función de las respuestas a las 5 preguntas deberás diseñar un algoritmo que
 *   coloque al alumno en una de las 4 casas de Hogwarts (Gryffindor, Slytherin , Hufflepuff y Ravenclaw)
 * - Ten en cuenta los rasgos de cada casa para hacer las preguntas y crear el algoritmo seleccionador.
 *   Por ejemplo, en Slytherin se premia la ambición y la astucia.
 */

/**
 * Caracteristicas a tener en cuenta para determinar la casa:
 * Gryffindor: valora la valentía, la audacia y la determinación.
 * Slytherin: valora la astucia, la ambición y la determinación.
 * Ravenclaw: valora la inteligencia, la sabiduría y la creatividad.
 * Hufflepuff: valora la lealtad, la amabilidad y el trabajo en equipo.
 *
 */
/**
 * Preguntas a ser planteadas:
1. **¿Qué cualidad valoras más en ti mismo/a?**
   - a) Valentía
   - b) Astucia
   - c) Intelecto
   - d) Lealtad

2. **En una situación difícil, ¿cuál sería tu enfoque principal?**
   - a) Afrontarla con valentía y determinación.
   - b) Analizar la situación y buscar la mejor estrategia.
   - c) Utilizar el conocimiento y la creatividad para encontrar soluciones.
   - d) Trabajar en equipo y mostrar lealtad a los demás.

3. **¿Qué tipo de logro te haría sentir más orgulloso/a?**
   - a) Alcanzar algo valiente y audaz.
   - b) Alcanzar un objetivo ambicioso y estratégico.
   - c) Obtener reconocimiento por tus habilidades intelectuales.
   - d) Ser reconocido/a por tu lealtad y servicio a los demás.

4. **¿Qué entorno te resulta más atractivo?**
   - a) Un lugar emocionante lleno de desafíos.
   - b) Un entorno competitivo donde puedes demostrar tus habilidades.
   - c) Un lugar tranquilo y estimulante para el aprendizaje.
   - d) Un ambiente cálido y amigable donde la gente se apoya mutuamente.

5. **¿Cuál es tu enfoque principal al aprender magia?**
   - a) Desarrollar habilidades mágicas poderosas y enfrentar desafíos.
   - b) Aprender hechizos y técnicas mágicas avanzadas.
   - c) Explorar la teoría mágica y expandir tu conocimiento.
   - d) Colaborar con otros y utilizar la magia para el bien común.
 */
const readline = require("readline");
const rl = readline.createInterface({
  input: process.stdin,
  output: process.stdout,
});

function cuestionario() {
  rl.question(
    "¿Qué cualidad valoras más en ti mismo/a?(Selecciona la letra que corresponda)\n- a) Valentía\n- b) Astucia\n- c) Intelecto\n- d) Lealtad:\n",
    (res1) => {
      rl.question(
        "En una situación difícil, ¿cuál sería tu enfoque principal?\n - a) Afrontarla con valentía y determinación.\n - b) Analizar la situación y buscar la mejor estrategia.\n - c) Utilizar el conocimiento y la creatividad para encontrar soluciones.\n - d) Trabajar en equipo y mostrar lealtad a los demás:\n",
        (res2) => {
          rl.question(
            "¿Qué tipo de logro te haría sentir más orgulloso/a?\n- a) Alcanzar algo valiente y audaz.\n- b) Alcanzar un objetivo ambicioso y estratégico.\n- c) Obtener reconocimiento por tus habilidades intelectuales.\n- d) Ser reconocido/a por tu lealtad y servicio a los demás:\n",
            (res3) => {
              rl.question(
                "¿Qué entorno te resulta más atractivo?\n- a) Un lugar emocionante lleno de desafíos.\n- b) Un entorno competitivo donde puedes demostrar tus habilidades.\n- c) Un lugar tranquilo y estimulante para el aprendizaje.\n- d) Un ambiente cálido y amigable donde la gente se apoya mutuamente:\n",
                (res4) => {
                  rl.question(
                    "¿Cuál es tu enfoque principal al aprender magia?\n- a) Desarrollar habilidades mágicas poderosas y enfrentar desafíos.\n- b) Aprender hechizos y técnicas mágicas avanzadas.\n- c) Explorar la teoría mágica y expandir tu conocimiento.\n- d) Colaborar con otros y utilizar la magia para el bien común:\n",
                    (res5) => {
                      seleccionador(res1, res2, res3, res4, res5);
                      rl.close();
                    }
                  );
                }
              );
            }
          );
        }
      );
    }
  );
}

function seleccionador(res1, res2, res3, res4, res5) {
  if (res1 == "a" && res2 == "a" && res3 == "a" && res4 == "a" && res5 == "a") {
    console.log("Perteneces a Grifindor");
  } else if (
    res1 == "b" &&
    res2 == "b" &&
    res3 == "b" &&
    res4 == "b" &&
    res5 == "b"
  ) {
    console.log("Perteneces a Slytherin");
  } else if (
    res1 == "c" &&
    res2 == "c" &&
    res3 == "c" &&
    res4 == "c" &&
    res5 == "c"
  ) {
    console.log("Perteneces a Ravenclaw");
  } else if (
    res1 == "d" &&
    res2 == "d" &&
    res3 == "d" &&
    res4 == "d" &&
    res5 == "d"
  ) {
    console.log("Perteneces a Hufflepuff");
  }
}

cuestionario();
