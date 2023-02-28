/*
 * Crea un generador de números pseudoaleatorios entre 0 y 100.
 * - No puedes usar ninguna función "random" (o semejante) del lenguaje de programación seleccionado.
 * 
 * Para este ejercicio, usaremos:
 * - Usa una llamada al tiempo del sistema para generar una semilla.
 * - Utiliza una sucesión de multiplicaciones y sumas para generar un número pseudoaleatorio.
 */

// Importación de librerías.
use std::time::UNIX_EPOCH;
use std::time::SystemTime;

fn main() {

    // Obtener el tiempo actual.
    let rightnow : SystemTime = SystemTime::now();

    // Se genera una semilla a partir del tiempo del sistema.
    let millis = rightnow.duration_since(UNIX_EPOCH).unwrap().as_millis();

    // Realizar el modulo con 65535 y se convierte a u64.
    let seed = (millis % 65535) as u16;

    // Se muestra la semilla por linea de comandos.
    println!("Semilla: {}", seed);

    // Se genera un número pseudoaleatorio.
    let random_number = pseudoaleatorio(seed);

    // Se muestra el número pseudoaleatorio por linea de comandos.
    println!("Número pseudoaleatorio: {}", random_number);
}

// Función que genera un número pseudoaleatorio entre 0 y 100 usando el fractal de Mandelbrot.
fn pseudoaleatorio(seed: u16) -> u8 {

    // Se inicializa el número pseudoaleatorio con la semilla.
    let mut random_number : u32 = seed as u32;

    // Se genera el número pseudoaleatorio aplicando la sucesión de multiplicaciones y sumas.
    // Se repite 100 veces y se mantiene el valor acotado en 65535.
    for _ in 0..100 {
        random_number = (random_number * random_number + seed as u32) % 65535;
    }

    // Se devuelve el número pseudoaleatorio.
    return (random_number % 101) as u8;
}

// Test de la función pseudoaleatorio.
#[test]
fn test_pseudoaleatorio() {

    // Se ejecuta la función 10000 veces, con la semilla 100, validando que el resultado es un número entre 0 y 100.
 
    for _ in 0..10000 {
        let random_number = pseudoaleatorio(100);
        vector[random_number as usize] += 1;
        assert!(random_number <= 100);
    }
}