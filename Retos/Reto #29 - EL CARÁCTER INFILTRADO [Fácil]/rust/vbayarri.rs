/*
 * Crea una función que reciba dos cadenas de texto casi iguales,
 * a excepción de uno o varios caracteres. 
 * La función debe encontrarlos y retornarlos en formato lista/array.
 * - Ambas cadenas de texto deben ser iguales en longitud.
 * - Las cadenas de texto son iguales elemento a elemento.
 * - No se pueden utilizar operaciones propias del lenguaje
 *   que lo resuelvan directamente.
 * 
 * Ejemplos:
 * - Me llamo mouredev / Me llemo mouredov -> ["e", "o"]
 * - Me llamo.Brais Moure / Me llamo brais moure -> [" ", "b", "m"]
 */

// Funcion que recibe dos cadenas de texto casi iguales y retorna un Vector con los caracteres diferentes
fn find_differences(first_text: &str, second_text: &str) -> Vec<char> {

    // Creamos un vector para almacenar los caracteres diferentes
    let mut differences: Vec<char> = Vec::new();
    
    // Convertimos las cadenas de texto en vectores de caracteres
    let first_text: Vec<char> = first_text.chars().collect();
    let second_text: Vec<char> = second_text.chars().collect();
    
    // Recorremos los vectores de caracteres
    for i in 0..first_text.len() {
        // Si los caracteres son diferentes, lo añadimos al vector de diferencias
        if first_text[i] != second_text[i] {
            differences.push(second_text[i]);
        }
    }
    
    // Retornamos el vector de diferencias
    differences.into_iter().collect()
}

// Funcion para validar las cadenas de texto introducidas por el usuario
fn validate_strings(first_text: &str, second_text: &str) -> bool {
    // Comprobamos que las cadenas de texto tengan la misma longitud
    if first_text.len() != second_text.len() {
        println!("Las cadenas de texto deben tener la misma longitud");
        return false;
    }
    
    // Comprobamos que las cadenas de texto sean iguales
    if first_text == second_text {
        println!("Las cadenas de texto deben ser diferentes");
        return false;
    }
    
    // Retornamos true si las cadenas de texto son válidas
    true
}

// Funcion para validar las dos cadenas de texto introducidas por el usuario y retornar el vector de diferencias
fn caracter_infiltrado(first_text: &str, second_text: &str) -> Vec<char> {
    // Validamos las cadenas de texto
    if validate_strings(first_text, second_text) {
        // Retornamos el vector de diferencias
        find_differences(first_text, second_text)
    } else {
        // Retornamos un vector vacío
        Vec::new()
    }
}

#[test]
fn test1() {
    assert_eq!(caracter_infiltrado("Me llamo mouredev", "Me llemo mouredov"), ['e', 'o']);
}

#[test]
fn test2() {
    assert_eq!(caracter_infiltrado("Me llamo.Brais Moure", "Me llamo brais moure"), [' ', 'b', 'm']);
}

#[test]
fn test3() {
    assert_eq!(caracter_infiltrado("Me llamo mouredev", "Me llamo mouredev"), Vec::<char>::new());
}

#[test]
fn test4() {
    assert_eq!(caracter_infiltrado("Me llamo mouredev", "Me llamo mouredevv"), Vec::<char>::new());
}