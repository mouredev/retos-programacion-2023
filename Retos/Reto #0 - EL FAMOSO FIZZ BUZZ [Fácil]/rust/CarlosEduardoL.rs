use std::io::{stdout, BufWriter, Write};

pub fn fizz_buzz() -> Result<(), Box<dyn std::error::Error>> {
    // Crea un buffer para stdout, para evitar el flush en cada llamada a la macro println!
    let mut out = BufWriter::new(stdout().lock());

    for n in 1..=100 {
        // Usa una expresión match para verificar si el número es divisible por 3 o 5
        match (n % 3, n % 5) {
            (0, 0) => writeln!(out, "fizzbuzz")?, // Si es divisible por ambos, escribe "fizzbuzz"
            (0, _) => writeln!(out, "fizz")?,     // Si solo es divisible por 3, escribe "fizz"
            (_, 0) => writeln!(out, "buzz")?,     // Si solo es divisible por 5, escribe "buzz"
            _ => writeln!(out, "{}", n)?, // Si no es divisible por ninguno, escribe el número en sí
        }
    }
    // Hace flush al buffer de salida a stdout al final
    out.flush()?;
    Ok(())
}

pub fn main() -> Result<(), Box<dyn std::error::Error>> {
    fizz_buzz()
}