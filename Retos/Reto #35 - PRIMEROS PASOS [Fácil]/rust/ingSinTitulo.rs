fn main() {
    // Punto 1: Hola, mundo!
    println!("Hola, mundo!");

    // Punto 2: Crea una variable de texto o string
    let mi_texto = "¡Hola desde Rust!";

    // Punto 3: Crea una variable de número entero
    let mi_entero = 42;

    // Punto 4: Crea una variable de número con decimales
    let mi_decimal = 3.14;

    // Punto 5: Crea una variable de tipo booleano
    let mi_booleano = true;

    // Punto 6: Crea una constante
    const MI_CONSTANTE: i32 = 10;

    // Punto 7: Usa un if, else if y else
    if mi_entero > 50 {
        println!("El número es mayor que 50");
    } else if mi_entero < 50 {
        println!("El número es menor que 50");
    } else {
        println!("El número es igual a 50");
    }

    // Punto 8: Crea un Array (vector en Rust)
    let mi_array = vec![1, 2, 3, 4, 5];

    // Punto 9: Crea una lista (vector en Rust)
    let mi_lista = vec!["Manzana", "Banana", "Naranja"];

    // Punto 10: Crea una tupla
    let mi_tupla = (1, "dos", 3.14);

    // Punto 11: Crea un set (no aplicable en Rust)

    // Punto 12: Crea un diccionario (hashmap en Rust)
    use std::collections::HashMap;
    let mut mi_diccionario = HashMap::new();
    mi_diccionario.insert("clave1", "valor1");
    mi_diccionario.insert("clave2", "valor2");

    // Punto 13: Usa un ciclo for
    for elemento in &mi_array {
        println!("{}", elemento);
    }

    // Punto 14: Usa un ciclo foreach (no aplicable en Rust)

    // Punto 15: Usa un ciclo while
    let mut contador = 0;
    while contador < 3 {
        println!("Contador: {}", contador);
        contador += 1;
    }

    // Punto 16: Crea una función sin parámetros que no retorne nada
    fn funcion_sin_parametros() {
        println!("Función sin parámetros");
    }
    funcion_sin_parametros();

    // Punto 17: Crea una función con parámetros que no retorne nada
    fn funcion_con_parametros(param1: i32, param2: &str) {
        println!("Parámetro 1: {}", param1);
        println!("Parámetro 2: {}", param2);
    }
    funcion_con_parametros(1, "dos");

    // Punto 18: Crea una función con parámetros que retorne valor
    fn funcion_con_retorno(a: i32, b: i32) -> i32 {
        a + b
    }
    let resultado = funcion_con_retorno(3, 4);
    println!("Resultado: {}", resultado);

    // Punto 19: Crea una estructura (struct en Rust)
    struct Persona {
        nombre: String,
        edad: u32,
    }
    let persona = Persona {
        nombre: String::from("Juan"),
        edad: 30,
    };

    // Punto 20: Muestra control de excepciones (Result en Rust)
    let division_resultado = dividir(10, 2);
    match division_resultado {
        Ok(resultado) => println!("Resultado de la división: {}", resultado),
        Err(error) => println!("Error: {}", error),
    }
}

// Punto 20: Muestra control de excepciones (Result en Rust)
fn dividir(dividendo: i32, divisor: i32) -> Result<i32, String> {
    if divisor == 0 {
        Err(String::from("División por cero"))
    } else {
        Ok(dividendo / divisor)
    }
}
