/*
 * Crea una función que reciba un número decimal y lo trasforme a Octal
 * y Hexadecimal.
 * - No está permitido usar funciones propias del lenguaje de programación que
 * realicen esas operaciones directamente.
 */

// Función principal. Muestra el resultado de las funciones con los primeros
// 30 números decimales.
fn main() {
    for i in 0..30 {
        println!("Decimal: {}", i);
        println!("Octal: {}", to_octal(i));
        println!("Hexadecimal: {}", to_hex(i));
        println!("");
    }
}

// Función que convierte un número decimal a octal
fn to_octal(num: i32) -> String {
    let mut octal = String::new();
    let mut num = num;
    // Validar el caso de 0
    if num == 0 {
        return "0".to_string();
    }
    // Mientras el número sea mayor que 0, se añade el resto de la división
    while num > 0 {
        octal.push_str(&format!("{}", num % 8));
        num /= 8;
    }
    octal.chars().rev().collect()
}

// Función que convierte un número decimal a hexadecimal
fn to_hex(num: i32) -> String {
    let mut hex = String::new();
    let mut num = num;
     // Validar el caso de 0
     if num == 0 {
        return "0".to_string();
    }
    // Mientras el número sea mayor que 0, se añade el resto de la división
    while num > 0 {
        // Calcular el valor hexadecimal
        if num % 16 > 9 {
            match num % 16 {
                10 => hex.push_str("A"),
                11 => hex.push_str("B"),
                12 => hex.push_str("C"),
                13 => hex.push_str("D"),
                14 => hex.push_str("E"),
                15 => hex.push_str("F"),
                _ => (),
            }
        } else {
            hex.push_str(&format!("{}", num % 16));
        }
        num /= 16;
    }
    hex.chars().rev().collect()
}