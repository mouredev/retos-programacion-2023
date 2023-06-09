/*
 * Crea 3 funciones, cada una encargada de detectar si una cadena de
 * texto es un heterograma, un isograma o un pangrama.
 */

// Importación de librerías
use std::collections::HashMap;

// Definición de constantes
const ALFABETO : &str = "abcdefghijklmnñopqrstuvwxyz";

// Definición de funciones

// Función que detecta si una cadena de texto es un heterograma
// Un heterograma (del griego heteros, 'diferente' y gramma, 'letra') es una palabra o frase en la que
// cada letra aparece una sola vez.
fn es_heterograma(texto: &str) -> bool {

    // Se inicializa un hashmap para almacenar las letras y su número de apariciones
    let mut letras = HashMap::new();

    // Se recorre la cadena de texto y se almacenan las letras en el hashmap con su número de apariciones
    for letra in texto.chars() {
        if letra.is_alphabetic() {
            let count = letras.entry(letra.to_ascii_lowercase()).or_insert(0);
            *count += 1;
        }
    }

    // Se valida que el número de apariciones de todas las letras sea 1
    for (_letra, apariciones) in letras.iter() {
        if *apariciones != 1 {
            return false;
        }
    }

    // Si cumple la validación es un heterograma
    return true;
}

// Función que detecta si una cadena de texto es un isograma
// Un isograma (del griego isos, 'igual' y gramma, 'letra') es una palabra o frase en la que 
// cada letra aparece el mismo número de veces.
fn es_isograma(texto: &str) -> bool {

    // Se inicializa un hashmap para almacenar las letras y su número de apariciones
    let mut letras = HashMap::new();

    // Se recorre la cadena de texto y se almacenan las letras en el hashmap con su número de apariciones
    for letra in texto.chars() {
        if letra.is_alphabetic() {
            let count = letras.entry(letra.to_ascii_lowercase()).or_insert(0);
            *count += 1;
        }
    }
    
    // Se valida que el número de apariciones de todas las letras tengan el miso número de apariciones
    let mut count = 0;
    for (_letra, apariciones) in letras.iter() {
        if count == 0 {
            count = *apariciones;
        } else {
            if count != *apariciones {
                return false;
            }
        }
    }

    // Si cumple la validación es un isograma
    return true;
}

// Función que detecta si una cadena de texto es un pangrama
fn es_pangrama(texto: &str) -> bool {

    // Se alamacenan las letras de la cadena en un vector sin repetir
    let mut letras = Vec::new();
    for letra in texto.chars() {
        if letra.is_alphabetic() {
            if letras.contains(&letra.to_ascii_lowercase()) {
                continue;
            } else {
                letras.push(letra.to_ascii_lowercase());
            }
        }
    }

    // Se validan las letras del alfabeto contra el vector de letras
    for letra in ALFABETO.chars() {
        if !letras.contains(&letra) {
            return false;
        }
    }

    // Si cumple la validación es un panagrama
    return true;
}

// Casos de test
#[test]
fn test_heterograma_ok() {

    let heterograma = "Hiperblanduzcos";

    assert_eq!(es_heterograma(heterograma), true);
}

#[test]
fn test_heterograma_ko() {

    let heterograma = "Hiperblanduzcas";

    assert_eq!(es_heterograma(heterograma), false);
}

#[test]
fn test_isograma_ok() {

    let isograma = "HiperblanduzcosHiperblanduzcos";

    assert_eq!(es_isograma(isograma), true);
}

#[test]
fn test_isograma_ko() {

    let isograma = "HiperblanduzcosHiperblanduzcas";

    assert_eq!(es_isograma(isograma), false);
}

#[test]
fn test_panagrama_ok() {

    let pangrama = "El cadáver de Wamba, rey godo de España, fue exhumado y trasladado en una caja de zinc que pesó un kilo.";

    assert_eq!(es_pangrama(pangrama), true);
}

#[test]
fn test_panagrama_ko() {

    let pangrama = "Los pangramas perfectos son los pangramas que son también heterogramas, es decir en los que no se repite ninguna de las letras.";

    assert_eq!(es_pangrama(pangrama), false);
}
