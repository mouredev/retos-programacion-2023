/*
 * Crea un generador de números pseudoaleatorios entre 0 y 100.
 * - No puedes usar ninguna función "random" (o semejante) del lenguaje de programación seleccionado.
 *
 * Es más complicado de lo que parece...
 */

import 'dart:math';

/**
 * Clase que genera números pseudoaleatorios utilizando el algoritmo de congruencia lineal
 * Contiene un metodo estático que devuelve un número pseudoaleatorio entre un rango de valores
 *
 */
class CustomRandom {

    const CustomRandom();
    /**
     * Genera un retraso de tiempo para que el algoritmo de congruencia lineal funcione correctamente
     */
    void delay(int miliSeconds)  {
      var start = DateTime.now().microsecondsSinceEpoch;

      while (new DateTime.now().microsecondsSinceEpoch < start + miliSeconds) {
        // Consumir tiempo de CPU
      }
    }


    /**
    * Genera una semilla para el algoritmo de congruencia lineal
    */
    int getSeed()  {
      const int multiplier = 1103515245;
      const int increment = 12345;
      num bits = pow(2, 32);
      delay(1000);
      int nanoSeconds = DateTime.now().microsecondsSinceEpoch;

      return ((multiplier.toInt() * nanoSeconds) + increment.toInt()).toInt() % bits.toInt();

    }
    /**
     * Devuelve un número pseudoaleatorio entre un rango de valores
     * @param min
     * @param max
     */
    static int random(int min,int max) {
      CustomRandom rand = CustomRandom();
      int seed = rand.getSeed();
      return min + (seed % max);
    }
}

int main() {
  for (int i = 0; i < 10; i++){
    print(CustomRandom.random(0, 100));
  }
  return 0;
}