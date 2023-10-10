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

 // Se utiliza la librería regex para validar la expresión matemática
 use regex::Regex;

 // Se define la expresión regular para validar la expresión matemática
const EXPRESION_REGULAR: &str = r"^(\s*\-?\d+(\.\d+)?\s*[\+\-\*\/\%]\s*)+\-?\d+(\.\d+)?\s*$";

// Función que recibe una expresión matemática y retorna true si es correcta
fn check_math_exp(expresion: &str) -> bool {
    // Se crea la expresión regular
    let re = Regex::new(EXPRESION_REGULAR).unwrap();
    // Se retorna el resultado de la validación
    re.is_match(expresion)
}

// Validación de la función con un ejemplo complejo
fn main() {
    let result : bool = check_math_exp("3 + 5 - 1 / 4 % 8");
    println!("Result: {}", result);
}

#[test]
// Test de la función con los casos de ejemplo de MoureDev
fn test() {
    assert_eq!(check_math_exp("3 + 5"), true);
    assert_eq!(check_math_exp("3 a 5"), false);
    assert_eq!(check_math_exp("-3 + 5"), true);
    assert_eq!(check_math_exp("- 3 + 5"), false);
    assert_eq!(check_math_exp("-3 a 5"), false);
    assert_eq!(check_math_exp("-3+5"), true);
    assert_eq!(check_math_exp("3 a 5"), false);
    assert_eq!(check_math_exp("3 + 5 - 1 / 4 % 8"), true);
}

