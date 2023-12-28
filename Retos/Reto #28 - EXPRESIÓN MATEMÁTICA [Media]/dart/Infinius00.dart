/*
 * Crea una función que reciba una expresión matemática (String)
 * y compruebe si es correcta. Retornará true o false.
 * - Para que una expresión matemática sea correcta debe poseer
 *   un número, una operación y otro número separados por espacios.
 *   Tantos números y operaciones como queramos.
 * - Números positivos, negativos, enteros o decimales.
 * - Operaciones soportadas: + - * / % 
 *
 * Ejemplos:
 * "5 + 6 / 7 - 4" -> true
 * "5 a 6" -> false
 */

import 'dart:io';

void main() {
  // función que evalúa si el valor es uno de los operadores posibles
  bool isOperator(String valor) {
    if ((valor == "+") ||
        (valor == "-") ||
        (valor == "*") ||
        (valor == "/") ||
        (valor == "%")) {
      return true;
    } else {
      return false;
    }
  }

  /* función que evalúa si la expresión es correcta recorriendo el arreglo
  considera si es el valor es un número 
  o bien si es un operador y está precedido por un número
  */

  bool expresionCorrecta(List<String> expresion) {
    for (int i = 0; i < expresion.length; i++) {
      if ((expresion[i] is num) ||
          (isOperator(expresion[i]) & (expresion[i--] is num))) {
        continue;
      } else {
        return false;
      }
    }
    return true;
  }

  // se lee la entrada por teclado de una expresión
  print("Ingrese la expresion matemática a evaluar");
  var expresionConEspacios = stdin.readLineSync();

  // se eliminan los espacios de la expresión
  String expresionSinEspacios = expresionConEspacios!.replaceAll(" ", "");

  // se divide la expresión por caracteres dentro de un arreglo y se la evalúa
  if (expresionCorrecta(expresionSinEspacios.split(""))) {
    print("La expresión matemática ingesada es correcta");
  } else {
    print("La expresión matemática ingesada es incorrecta");
  }
}
