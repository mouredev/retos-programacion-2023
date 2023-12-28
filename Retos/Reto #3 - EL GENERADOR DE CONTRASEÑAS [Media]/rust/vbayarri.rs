/*
 * Escribe un programa que sea capaz de generar contraseñas de forma aleatoria.
 * Podrás configurar generar contraseñas con los siguientes parámetros:
 * - Longitud: Entre 8 y 16.
 * - Con o sin letras mayúsculas.
 * - Con o sin números.
 * - Con o sin símbolos.
 * (Pudiendo combinar todos estos parámetros entre ellos)
 * 
 * El programa debe funcionar con UTF-8 en lugar de caracteres ASCII.
 */

// Importamos la librería para generar números aleatorios
use rand::Rng;
use std::io;

// Estructura para guardar las opciones
struct Opciones {
    longitud: u32,
    mayusculas: bool,
    numeros: bool,
    simbolos: bool,
}

// Función para pedir las opciones al usuario y retornar una estrcutura con los datos
fn program_options() -> Opciones {
    
    // Pedimos la longitud de la contraseña
    println!("Introduce la longitud de la contraseña (entre 8 y 16):");
    let mut longitud = String::new();
    io::stdin().read_line(&mut longitud).expect("Error al leer la longitud");
    let longitud: u32 = longitud.trim().parse().expect("Error al convertir la longitud a entero");

    // Pedimos si queremos mayúsculas
    println!("¿Quieres mayúsculas? (s/n)");
    let mut mayusculas = String::new();
    io::stdin().read_line(&mut mayusculas).expect("Error al leer la respuesta");
    let mayusculas: bool = mayusculas.trim() == "s";

    // Pedimos si queremos números
    println!("¿Quieres números? (s/n)");
    let mut numeros = String::new();
    io::stdin().read_line(&mut numeros).expect("Error al leer la respuesta");
    let numeros: bool = numeros.trim() == "s";

    // Pedimos si queremos símbolos
    println!("¿Quieres símbolos? (s/n)");
    let mut simbolos = String::new();
    io::stdin().read_line(&mut simbolos).expect("Error al leer la respuesta");
    let simbolos: bool = simbolos.trim() == "s";

    // Retornamos la estructura con las opciones
    return Opciones {
        longitud: longitud,
        mayusculas: mayusculas,
        numeros: numeros,
        simbolos: simbolos,
    };
}

fn main() {

    // Pedimos las opciones al usuario
    let opciones = program_options();

    // Comprobamos que la longitud está entre 8 y 16
    if opciones.longitud < 8 || opciones.longitud > 16 {
        println!("La longitud debe estar entre 8 y 16");
        return;
    }

    // Comprobamos que se ha seleccionado al menos una opción
    if !opciones.mayusculas && !opciones.numeros && !opciones.simbolos {
        println!("Debes seleccionar al menos una opción");
        return;
    }

    // Generamos la contraseña
    let mut contrasena = String::new();
    
    // En función de las variable opciones, generamos un vector con los caracteres que se pueden usar
    let mut caracteres: Vec<char> = Vec::new();

    // Incluimos los caracteres ASCII de a-z
    for i in 97..123 {
        caracteres.push(char::from(i));
    }

    // Incluimos los caracteres ASCII de A-Z si se ha seleccionado la opción
    if opciones.mayusculas {
        for i in 65..91 {
            caracteres.push(char::from(i));
        }
    }
    
    // Incluimos los caracteres ASCII de 0-9 si se ha seleccionado la opción
    if opciones.numeros {
        for i in 48..58 {
            caracteres.push(char::from(i));
        }
    }

    // Incluimos los caracteres ASCII de 33-47, 58-64, 91-96 y 123-126 si se ha seleccionado la opción
    if opciones.simbolos {
        for i in 33..48 {
            caracteres.push(char::from(i));
        }
        for i in 58..65 {
            caracteres.push(char::from(i));
        }
        for i in 91..97 {
            caracteres.push(char::from(i));
        }
        for i in 123..127 {
            caracteres.push(char::from(i));
        }
    }

    // Generamos la contraseña con el vector de caracteres
    let mut rng = rand::thread_rng();
    for _ in 0..opciones.longitud {
        let caracter = rng.gen_range(0..caracteres.len());
        contrasena.push(caracteres[caracter]);
    }

    println!("Contraseña generada: {}", contrasena);
}