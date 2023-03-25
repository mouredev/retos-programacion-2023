/*
 * Dada una URL con parámetros, crea una función que obtenga sus valores.
 * No se pueden usar operaciones del lenguaje que realicen esta tarea directamente.
 *
 * Ejemplo: En la url https://retosdeprogramacion.com?year=2023&challenge=0
 * los parámetros serían ["2023", "0"]
 */

// Definir una función que reciba una url y devuelva un array con los valores de los parámetros
fn get_parametros(url: &str) -> Vec<&str> {

    // Definir un array para almacenar los parámetros
    let mut params = Vec::new();

    // Validar que la url tenga parámetros
    if !url.contains('?') {
        return params;
    }

    // Obtener los parámetros
    let mut url = url.split('?');
    url.next();
    let url = url.next().unwrap();
    for param in url.split('&') {
        params.push(param);
    }
    params
}

// Validar que la función funciona correctamente
#[test]
fn test_get_parametros() {

    // Definir un array con 10 urls de ejemplo de 0 a 9 parámetros cada una
    // La url empieza por example.com y los parámetros son nombres de pokemon
    let urls = [
        "https://example.com",
        "https://example.com?bulbasaur",
        "https://example.com?bulbasaur&ivysaur",
        "https://example.com?bulbasaur&ivysaur&venusaur",
        "https://example.com?bulbasaur&ivysaur&venusaur&charmander",
        "https://example.com?bulbasaur&ivysaur&venusaur&charmander&charmeleon",
        "https://example.com?bulbasaur&ivysaur&venusaur&charmander&charmeleon&charizard",
        "https://example.com?bulbasaur&ivysaur&venusaur&charmander&charmeleon&charizard&squirtle",
        "https://example.com?bulbasaur&ivysaur&venusaur&charmander&charmeleon&charizard&squirtle&wartortle",
        "https://example.com?bulbasaur&ivysaur&venusaur&charmander&charmeleon&charizard&squirtle&wartortle&blastoise",
    ];

    // Recorrer el array de urls
    for (i, url) in urls.iter().enumerate() {
        // Mostar la url por consola
        let params = get_parametros(url);
        println!("{}: {}", i, url);

        // Mostrar los obtenidos por consola
        for param in &params {
            println!("  {}", param);
        }

        // Validar que el número de parámetros sea correcto
        assert_eq!(params.len(), i);
    }
}