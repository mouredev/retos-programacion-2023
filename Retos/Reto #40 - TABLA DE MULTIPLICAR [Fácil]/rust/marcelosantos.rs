use std::io;

/*
 * Crea un programa que sea capaz de solicitarte un número y se
 * encargue de imprimir su tabla de multiplicar entre el 1 y el 10.
 * - Debe visualizarse qué operación se realiza y su resultado.
 *   Ej: 1 x 1 = 1
 *       1 x 2 = 2
 *       1 x 3 = 3
 *       ...
 */

fn main() {
    let mut numero = String::new();

    println!("Digite um número: ");

    io::stdin()
        .read_line(&mut numero)
        .expect("Erro ao ler o número");
    let numero = numero.trim().parse::<i32>().unwrap();

    for i in 1..=10 {
        println!("{} x {} = {}", numero, i, numero * i);
    }
}
