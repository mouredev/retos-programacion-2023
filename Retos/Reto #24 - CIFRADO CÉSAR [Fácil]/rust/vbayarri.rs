/*
 * Crea un programa que realize el cifrado César de un texto y lo imprima.
 * También debe ser capaz de descifrarlo cuando así se lo indiquemos.
 *
 * Te recomiendo que busques información para conocer en profundidad cómo
 * realizar el cifrado. Esto también forma parte del reto.
 */

/*
 * Información sobre el cifrado César: https://es.wikipedia.org/wiki/Cifrado_C%C3%A9sar
 * Función de módulo para no utilizar dos arrays visto en ejercicio de fegorama.c con referencia 
 * a https://stackoverflow.com/questions/14997165/fastest-way-to-get-a-positive-modulo-in-c-c/14997413#14997413
 */

// Constantes
const ALPHABET: &str = "abcdefghijklmnopqrstuvwxyz";

fn main() {
    
    // Se comprueban los argumentos de entrada.
    let args: Vec<String> = std::env::args().collect();

    // Validar el número de argumentos.
    if args.len() != 4 {
        println!("Uso: vbayarri -e|-d number texto");
        println!("  -e: cifrar");
        println!("  -d: descifrar");
        println!("  number: número de posiciones a desplazar");
        println!("  texto: texto a cifrar o descifrar");
        return;
    }

    // Validar la opción.
    if args[1] != "-e" && args[1] != "-d" {
        println!("Opción no válida.");
        return;
    }
    let option = &args[1];

    // Validar el número de posiciones.
    let number: i32 = match args[2].parse() {
        Ok(n) => n,
        Err(_) => {
            println!("Número de posiciones no válido.");
            return;
        }
    };

    // Validar el texto y convertirlo a minúsculas.
    let text = &args[3];
    let text = text.to_lowercase();

    // Mostrar la información por consola.
    println!("Opción: {}", option);
    println!("Número de posiciones: {}", number);
    println!("Texto entrada: {}", text);

    // Cifrar o descifrar el texto.
    let result = match option.as_str() {
        "-e" => encrypt(text, number),
        "-d" => decrypt(text, number),
        _ => {
            println!("Opción no válida.");
            return;
        }
    };

    // Mostrar el resultado.
    println!("Texto salida: {}", result);
}

// Función para cifrar un texto.
fn encrypt(text: String, number: i32) -> String {
    cesar(text, number)
}

// Función para descifrar un texto.
fn decrypt(text: String, number: i32) -> String {
    cesar(text, -number)
}

// Función base para cifrar y descifrar una cadena de texto.
fn cesar(text: String, number: i32) -> String {
    let mut result = String::new();
    for c in text.chars() {
        let index = ALPHABET.find(c);
        match index {
            Some(i) => {
                let new_index = modulo(i as i32 + number, ALPHABET.len() as u32);
                result.push(ALPHABET.chars().nth(new_index as usize).unwrap());
            },
            None => result.push(c)
        }
    }
    result
}

// Función de módulo para calcular el desplazamiento.
fn modulo(value: i32, m: u32) -> i32 {
    let mut modu = value % (m as i32);
    if modu < 0 {
        modu += m as i32;
    }
    modu
}