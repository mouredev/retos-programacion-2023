/*
 * Escribe un programa que reciba un texto y transforme lenguaje natural a
 * "lenguaje hacker" (conocido realmente como "leet" o "1337"). Este lenguaje
 *  se caracteriza por sustituir caracteres alfanuméricos.
 * - Utiliza esta tabla (https://www.gamehouse.com/blog/leet-speak-cheat-sheet/) 
 *   con el alfabeto y los números en "leet".
 *   (Usa la primera opción de cada transformación. Por ejemplo "4" para la "a")
 */
use std::io;
use std::io::BufRead;
use std::io::Write;

fn main () {

    // Leemos el texto de entrada por la entrada estandar.

    // Bonus 1: En lugar de almacenarlo en un String en memoria y tratarlo, 
    // para soportar textos de gran tamaño, se usa un iterador en la entrada.
    // Referencia: https://www.becomebetterprogrammer.com/rust-read-user-input-stdin/

    let mut lines = io::stdin().lock().lines();
    let mut handle = io::stdout().lock();

    // Mientras hay contenido para procesar, tratamos linea a linea.
    while let Some(line) = lines.next() {

        // Convertimos result to String y verificamos final de entrada.
        let last_input : String = line.unwrap();
        if last_input.len() == 0 {
            break;
        }
        // Se realiza la codificacion
        let last_output : String = to_hacker(last_input);

        // Escritura en el standar output
        writeln!(handle, "{}", last_output).unwrap();
    }
}

fn to_hacker(input: String) -> String {

    // Asegurar el match transformando a mayúsculas. 
    let input_uppercase = input.to_uppercase();
    
    // Aplicamos una funcion map para transformar todos los caracteres a una cadena segun la tabla indicada
    let iter_input_uppercase = input_uppercase.chars().map(|c| {
        match c {
            'A' => "4",
            'B' => "I3",
            'C' => "[",
            'D' => ")",
            'E' => "3",
            'F' => "|=",
            'G' => "&",
            'H' => "#",
            'I' => "1",
            'J' => ",_|",
            'K' => ">|",
            'L' => "1",
            'M' => "/\\/\\",
            'N' => "^/",
            'O' => "0",
            'P' => "|*",
            'Q' => "(_,)",
            'R' => "I2",
            'S' => "5",
            'T' => "7",
            'U' => "(_)",
            'V' => "\\//",
            'W' => "\\/\\/",
            'X' => "><",
            'Y' => "j",
            'Z' => "2",
            ' ' => " ",
            '0' => "o",
            '1' => "L",
            '2' => "R",
            '3' => "E",
            '4' => "A",
            '5' => "S",
            '6' => "b",
            '7' => "T",
            '8' => "B",
            '9' => "g",
            _ => "",
        }
    });

    // Convertimos el map de chars a una única cadena con reduce
    let result = iter_input_uppercase
        .map(|s| s.to_string())
        .reduce(|cur: String, nxt: String| cur + &nxt)
        .unwrap();

    return result;
}