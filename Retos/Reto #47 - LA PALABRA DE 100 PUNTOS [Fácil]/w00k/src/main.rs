use std::collections::HashMap;
use std::io;

fn create_map() -> HashMap<&'static str, u32> {
    HashMap::from([
        ("a", 1),
        ("b", 2),
        ("c", 3),
        ("d", 4),
        ("e", 5),
        ("f", 6),
        ("g", 7),
        ("h", 8),
        ("i", 9),
        ("j", 10),
        ("k", 11),
        ("l", 12),
        ("m", 13),
        ("n", 14),
        ("ñ", 15),
        ("o", 16),
        ("p", 17),
        ("q", 18),
        ("r", 19),
        ("s", 20),
        ("t", 21),
        ("u", 22),
        ("v", 23),
        ("w", 24),
        ("x", 25),
        ("y", 26),
        ("z", 27),
        ("á", 1),
        ("é", 5),
        ("í", 9),
        ("ó", 16),
        ("ú", 22),
    ])
}

fn remove_last_character(word :String) -> String {
    return (&word[0..word.len() - 1]).parse().unwrap_or("".parse().unwrap());
}

fn get_values(letters: HashMap<&str, u32>, words: String) -> u32 {
    let mut index = 0;
    let mut result = 0;
    while index <= words.len() - 1 {
        let char_aux = words.chars().nth(index).unwrap_or(" ".parse().unwrap());
        result += letters.get(&*char_aux.to_string()).unwrap_or(&0);
        index += 1;
    }
    return result;
}

fn main() {

    // instance  map and variables
    let letters = create_map();
    let mut result = 0;
    let max_value = 100;

    // instructions
    println!("Would you like to play a game?");
    println!("Evaluaremos una palabra, calculando su peso en valores, si es mayor a {} finalizará el programa, en caso contrario no ", max_value);

    while result < max_value {
        println!("Ingresa la palabra que evaluaremos");
        // get the inputs
        let mut words = String::new();
        io::stdin().read_line(&mut words).unwrap();

        words = remove_last_character(words);
        let words_in_lower_case = words.to_lowercase().clone();
        result = get_values(letters.clone(), words_in_lower_case);

        println!("La palabra ingresada es '{}', posee el peso {}.", words, result);
    }

    println!("Felidades has completado el reto");
}
