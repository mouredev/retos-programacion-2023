use std::thread;
use std::time::Duration;

fn cuenta_atras(inicio: u32, intervalo: u64) {
    // Verificar que los parámetros sean enteros positivos
    if inicio == 0 || intervalo == 0 {
        println!("Error: Los parámetros deben ser enteros positivos.");
        return;
    }

    // Ciclo de cuenta regresiva utilizando un for y Range
    for i in (0..inicio).rev() {
        println!("{}", i); // Imprimir el número actual
        thread::sleep(Duration::from_secs(intervalo)); // Esperar el intervalo de tiempo especificado en segundos
    }

    println!("¡Cuenta regresiva finalizada!");
}

fn main() {
    cuenta_atras(10, 1);
}
