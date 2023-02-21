/*
 * Crea un generador de números pseudoaleatorios entre 0 y 100.
 * - No puedes usar ninguna función "random" (o semejante) del lenguaje de programación seleccionado.
 *
 * Es más complicado de lo que parece...
 */

const getNumber = () => {
  const date = new Date();
  return date.getTime() % 100;
};

const getNumber2 = () => {
  const date = new Date();
  return date.getMilliseconds() % 100;
};

// Visita mi repo en GitHub para ver y correr los tests de este código --> https://github.com/marcode24/weekly-challenges
