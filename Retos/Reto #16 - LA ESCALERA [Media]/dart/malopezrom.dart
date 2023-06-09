/*
 * Crea una función que dibuje una escalera según su número de escalones.
 * - Si el número es positivo, será ascendente de izquiera a derecha.
 * - Si el número es negativo, será descendente de izquiera a derecha.
 * - Si el número es cero, se dibujarán dos guiones bajos (__).
 *
 * Ejemplo: 4
 *         _
 *       _|
 *     _|
 *   _|
 * _|
 *
 */

/**
 * Función principal
 */
void main(){
  
  printSteps(-15);
  printSteps(2);
  printSteps(10);
  printSteps(0);
}


/**
 * Función que imprime una escalera de un determinado número de escalones
 * @param steps número de escalones de la escalera
 */
void printSteps(int steps) {
  if (steps == 0) {
    print("__");
  } else {
    if (steps > 0) {
      print(" " * (steps * 2) + "_");
    } else {
      print("_");
    }
    stepsRecursive(steps, 1);
  }
}
/**
 * Función recursiva que imprime los escalones de la escalera
 * @param steps número de escalones de la escalera
 * Si el número de escalones es positivo, la escalera es ascendente y si es negativo, es descendente
 */
void stepsRecursive(int steps, int currentStep) {
  //Caso base
  if (currentStep > steps.abs()) {
    return;
  }
  if (steps > 0) {
    print(" " * ((steps - currentStep) * 2) + "_|");
  } else {
    print(" " * ((currentStep) * 2 - 1) + "|_");
  }
  // LLamada recursiva
  stepsRecursive(steps, currentStep + 1);
}
