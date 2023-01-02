/*
 * Escribe un programa que muestre por consola (con un print) los
 * números de 1 a 100 (ambos incluidos y con un salto de línea entre
 * cada impresión), sustituyendo los siguientes:
 * - Múltiplos de 3 por la palabra "fizz".
 * - Múltiplos de 5 por la palabra "buzz".
 * - Múltiplos de 3 y de 5 a la vez por la palabra "fizzbuzz".
 */

fn main() {
  for value_number in 1..101 {
    let mut value_string: String = "".to_owned();

    if value_number % 3 == 0 {
      let string_to_concat: &str = "Fizz";
      value_string.push_str(string_to_concat);
    }

    if value_number % 5 == 0 {
      let string_to_concat: &str = "Buzz";
      value_string.push_str(string_to_concat);
    }

    if value_string.len() == 0 {
      println!("{}", value_number);
    } else {
      println!("{}", value_string);
    }
  }
}
