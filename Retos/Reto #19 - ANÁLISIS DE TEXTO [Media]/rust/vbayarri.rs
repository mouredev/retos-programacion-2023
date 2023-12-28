/*
 * Crea un programa que analice texto y obtenga:
 * - Número total de palabras.
 * - Longitud media de las palabras.
 * - Número de oraciones del texto (cada vez que aparecen un punto).
 * - Encuentre la palabra más larga.
 *
 * Todo esto utilizando un único bucle.
 */

use std::io;

// Función principal
fn main() {
 
    // Solicitamos el texto
    println!("Introduce un texto:");
    let mut texto : String = String::new();
    io::stdin().read_line(&mut texto).expect("Error al leer el texto");

    // Eliminamos los saltos de línea y signos de puntuación
    texto = eliminar_signos(texto);

    // Separamos el texto en palabras
    let palabras: Vec<&str> = texto.split(" ").collect();

    // Declaramos las variables
    let mut num_palabras = 0;
    let mut longitud_total = 0;
    let mut num_oraciones = 0;
    let mut palabra_mas_larga = "";

    // Recorremos las palabras
    for palabra in palabras {
        // Incrementamos el número de palabras
        num_palabras += 1;

        // Incrementamos la longitud total
        longitud_total += palabra.len();

        // Comprobamos si es la palabra más larga
        if palabra.len() > palabra_mas_larga.len() {
            palabra_mas_larga = palabra;
        }

        // Comprobamos si es una oración
        if palabra.contains(".") {
            num_oraciones += 1;
        }
    }

    // Mostramos los resultados
    println!("Estadísticas del texto:");
    println!("Número de palabras: {}", num_palabras);
    println!("Longitud media de las palabras: {}", longitud_total / num_palabras);
    println!("Número de oraciones: {}", num_oraciones);
    println!("Palabra más larga: {}", palabra_mas_larga);
}

// Funcion para eliminar salto de linea y signos de puntuacion
fn eliminar_signos(texto: String) -> String {
    let mut texto = texto;
    texto = texto.replace("\n", "");
    texto = texto.replace(",", "");
    texto = texto.replace(";", "");
    texto = texto.replace(":", "");
    texto = texto.replace("!", "");
    texto = texto.replace("¡", "");
    texto = texto.replace("?", "");
    texto = texto.replace("¿", "");
    return texto;
}