/*
 * Llamar a una API es una de las tareas más comunes en programación.
 *
 * Implementa una llamada HTTP a una API (la que tú quieras) y muestra su
 * resultado a través de la terminal. Por ejemplo: Pokémon, Marvel...
 *
 * Aquí tienes un listado de posibles APIs: 
 * https://github.com/public-apis/public-apis
 */

// Documentación de apoyo:
// https://github.com/seanmonstar/reqwest

// Requiere la dependencia reqwest con la opción de blocking para poder realizar llamadas en modo sincrono y 
// la opción de json para poder parsear la respuesta facilmente.

// [dependencies]
// reqwest = { version = "0.11", features = ["blocking", "json"] }

use std::collections::HashMap;

fn main() -> Result<(), Box<dyn std::error::Error>> {

    // Llamar a una API para obtener la IP del usuario
    let resp = reqwest::blocking::get("https://httpbin.org/ip")?
            .json::<HashMap<String, String>>()?;
    println!("Tu IP es {:#?}", resp);
    
    Ok(())
} 