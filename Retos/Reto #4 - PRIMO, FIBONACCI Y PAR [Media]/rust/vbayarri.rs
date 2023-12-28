/*
 * Escribe un programa que, dado un número, compruebe y muestre si es primo, fibonacci y par.
 * Ejemplos:
 * - Con el número 2, nos dirá: "2 es primo, fibonacci y es par"
 * - Con el número 7, nos dirá: "7 es primo, no es fibonacci y es impar"
 */

// Se importa la librería de entrada y salidaq
use std::io::stdin;

// Función que compra si un número es primo
fn es_primo(n: u32) -> bool {

    // Si el número es 1, no es primo
    if n == 1 {
        return false;
    } 

    // Se comprueba si el número es divisible por algún número entre 2 y el número
    for i in 2..n {
        if n % i == 0 {
            return false;
        }
    }

    // Si no es divisible por ningún número, es primo
    true
}

// Función que comprueba si un número es fibonacci
// La forma estándar (aparte de generar hasta N) es para comprobar si (5N^2+4) o (5N^2−4) es un cuadrado perfecto.
// Fuente: https://www.i-ciencias.com/pregunta/1714/comprobando-si-un-numero-es-un-fibonacci-o-no#comment-16243
fn es_fibonacci(n: u32) -> bool {
   
    // Se eleva el número al cuadrado
    let n = n.pow(2);

    // Se multiplica por 5
    let n = n * 5;

    // Obtenemos el número que se tiene que sumar o restar para comprobar si es fibonacci
    let checker1 = (n + 4) as f32;
    let checher2 = (n - 4) as f32;

    // Se comprueba si el número es raíz cuadrada de checker1 o checker2
    if checker1.sqrt().floor().powf(2.0) == checker1 || checher2.sqrt().floor().powf(2.0) == checher2 {
        return true;
    } else {
        return false;
    }   
}

// Función que comprueba si un número es par
fn es_par(n: u32) -> bool {

    // Si el resto de dividir el número entre 2 es 0, es par
    n % 2 == 0
}

// Función que describe un número
fn describe_numero(n: u32) {

    // Se comprueba si el número es primo
    let primo = es_primo(n);
    let sprimo = if primo { "es primo" } else { "no es primo" };

    // Se comprueba si el número es fibonacci
    let fibonacci = es_fibonacci(n);
    let sfibonacci = if fibonacci { "es fibonacci" } else { "no es fibonacci" };

    // Se comprueba si el número es par
    let par = es_par(n);
    let spar = if par { "es par" } else { "es impar" };

    // Se muestra el resultado
    println!("El número {} {}, {} y {}", n, sprimo, sfibonacci, spar);
}

// Función principal
fn main() {

    // Se declara la variable que va a contener el número
    let mut numero = String::new();

    // Se pide el número
    println!("Introduce un número: ");

    // Se guarda el número
    stdin().read_line(&mut numero).expect("Error al leer el número");

    // Se convierte el número a u32
    let numero: u32 = numero.trim().parse().expect("Error al convertir el número");

    // Se describe el número
    describe_numero(numero);
}