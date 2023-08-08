/*
 * Crea una función que reciba dos parámetros para crear una cuenta atrás.
 * - El primero, representa el número en el que comienza la cuenta.
 * - El segundo, los segundos que tienen que transcurrir entre cada cuenta.
 * - Sólo se aceptan números enteros positivos.
 * - El programa finaliza al llegar a cero.
 * - Debes imprimir cada número de la cuenta atrás.
 */

 // Importar la función flush para asegurar que se muestra el número sin esperar
 // a que se llene el buffer de salida
 use std::io::Write;

 // Función que recibe dos parámetros para crear una cuenta atrás
 fn countdown(start: u32, seconds: u32) {
    // Validar que los parámetros sean números enteros positivos
    if start > 0 && seconds > 0 {
        // Iniciar la cuenta atrás y limpiar la pantalla
        print!("{}[2J", 27 as char);

        // Recorrer el rango de números en orden descendente
        for i in (1..=start).rev() {
            // Imprimir el número y asegurar que se muestra. 
            // El bloqueo del thread impide que se muestre el número en caso contrario
            print!("{}..", i);
            std::io::stdout().flush().unwrap();
            // Esperar los segundos indicados
            std::thread::sleep(std::time::Duration::from_secs(seconds as u64));
        }
        // Imprimir el mensaje final
        println!("💥")
    } else {
        // Imprimir el mensaje de error
        println!("Los parámetros deben ser números enteros positivos");
    }
 }

fn main() {
    // Iniciar la cuenta atrás
    countdown(10, 1);
}
