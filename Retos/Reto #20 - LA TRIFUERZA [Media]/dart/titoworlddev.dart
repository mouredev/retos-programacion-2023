/*
 *	¡El nuevo "The Legend of Zelda: Tears of the Kingdom" ya está disponible! 
 *
 * Crea un programa que dibuje una Trifuerza de "Zelda"
 * formada por asteriscos.
 * - Debes indicarle el número de filas de los triángulos con un entero positivo (n).
 * - Cada triángulo calculará su fila mayor utilizando la fórmula 2n-1.
 *
 * Ejemplo: Trifuerza 2
 * 
 *    *
 *   ***
 *  *   *
 * *** ***
 *
 */

void main() {
  print(trifuerza(10));
}

String trifuerza(int triNum) {
  String result = '';
  int spaces = 0;

  for (int i = 0; i <= triNum; i++) {
    result = '*** ' * (triNum - i) + result;
    result = ' ' * (spaces) + result;
    result = '\n$result';
    result = ' *  ' * (triNum - i) + result;
    result = ' ' * (spaces) + result;
    result = '\n$result';
    spaces += 2;
  }

  return result;
}

/*
                       *  
                      *** 
                     *   *  
                    *** *** 
                   *   *   *  
                  *** *** *** 
                 *   *   *   *  
                *** *** *** *** 
               *   *   *   *   *  
              *** *** *** *** *** 
             *   *   *   *   *   *  
            *** *** *** *** *** *** 
           *   *   *   *   *   *   *  
          *** *** *** *** *** *** *** 
         *   *   *   *   *   *   *   *  
        *** *** *** *** *** *** *** *** 
       *   *   *   *   *   *   *   *   *  
      *** *** *** *** *** *** *** *** *** 
     *   *   *   *   *   *   *   *   *   *  
    *** *** *** *** *** *** *** *** *** *** 
   *   *   *   *   *   *   *   *   *   *   * 
  *** *** *** *** *** *** *** *** *** *** ***
 */