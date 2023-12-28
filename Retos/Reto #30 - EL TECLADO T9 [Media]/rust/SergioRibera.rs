/*
 * Los primeros dispositivos móviles tenían un teclado llamado T9
 * con el que se podía escribir texto utilizando únicamente su
 * teclado numérico (del 0 al 9).
 *
 * Crea una función que transforme las pulsaciones del T9 a su
 * representación con letras.
 * - Debes buscar cuál era su correspondencia original.
 * - Cada bloque de pulsaciones va separado por un guión.
 * - Si un bloque tiene más de un número, debe ser siempre el mismo.
 * - Ejemplo:
 *     Entrada: 6-666-88-777-33-3-33-888
 *     Salida: MOUREDEV
 */

//
// Solution by @SergioRibera
//
// Without external dependency
//

//
// Algorithm of compliance with the statement
//
fn from_numbers(keys: &[&str], input: &str) -> String {
    // input: 6-666-88-777-33-3-33-888
    //
    // The main idea is to separate the text into letters using the character -
    // assuming that we will always receive the text in this format.
    //
    // input after split:
    //  ["6","666","88","777","33","3","33","888"]
    // i: 0    1     2    3    4    5   6    7
    //
    //
    // i: 3 => "777": len = 3
    //          ^
    //          first character
    //
    //  keys[7] = "PQRS"
    //
    // then the idea is to grab the first element of each separate element
    // that corresponds to the first character, this is a number and that number
    // corresponds to the index of our keys vector
    //
    //  keys[7] = "PQRS"
    //
    //  "PQRS": len = 4
    //  "777":  len = 3
    //
    //  "PQRS"
    //   ^^^
    //     => R
    //
    //  "777" = R
    // Once we have the index parameter we have to fetch the index element based on
    // the size of the split-element we had, this will tell us how many times the button
    // was pressed to display that character.
    input
        .split('-') // Split the input
        // We choose the first character of each separation, only in case it exists, i.e. Some(_),
        // we pass it to the next stage after mapping it into a tuple that will store
        // (len of the separation, first character).
        .filter_map(|c| c.chars().next().map(|x| (c.len(), x)))
        // In this step we convert the character to a number and only in case of success we map
        // it to the same tuple as before, but now it looks like this
        // (len of the separation, character as usize)
        // this is to be able to follow the idea I mentioned above, also we filter only the success cases.
        .filter_map(|(l, c)| char_to_usize(c).map(|c| (l, c)))
        // Here we convert all input separations into letters or characters.
        .map(|(l, key)| {
            let letter = l - 1;
            // we capture the element i from the list of keys (based on the first character)
            // and only select the nth that corresponds to the number of times the number has been pressed.
            keys[key].chars().nth(letter).unwrap().to_string()
        })
        // At the end we put everything together in a single string using the collect
        .collect()
}

//
// Extra algorithm for inverse operation
//
fn to_numbers(keys: &[&str], input: &str) -> String {
    // input: SERGIO RIBERA
    //
    // character: I
    //
    // Here the idea is reversed, having the text we will iterate between all the characters it contains,
    //
    // keys:
    //  4: "GHI"
    //  ^     ^
    // pos   character
    //
    // then we iterate between all the keys to see in which one is present that character to obtain the position of the text.
    //
    //  4: "GHI"
    //      ^^^
    //       3 times
    //
    // knowing the position of the key and of the letter the rest is simple
    input
        // We obtain all the characters
        .chars()
        // we filter and map only the existing characters
        .filter_map(|c| {
            keys.iter()
                // We search in the keys for one that contains the character
                // we are in and we get its position
                .position(|g| g.contains(c))
                // we convert the position number into text and repeat it the number of times
                // before we find the character we need
                //plus 1 because the machine counts from 0
                .map(|p| p.to_string().repeat(keys[p].find(c).unwrap() + 1))
        })
        .collect::<Vec<_>>()
        // we collect and unite all with the character -
        .join("-")
}

//
// Helper function
//
fn char_to_usize(c: char) -> Option<usize> {
    c.to_digit(10).map(|digit| digit as usize)
}

//
// **********************************************
// *                                            *
// *        No Relevante, puede ignorar         *
// *                                            *
// **********************************************
//

//
// In application usage example
//
fn main() {
    let keys = vec![
        //       0
                " ",
        // 1      2     3
        ",.?!", "ABC", "DEF",
        // 4      5     6
        "GHI", "JKL", "MNO",
        // 7      8     9
        "PQRS", "TUV", "WXYZ",
    ];

    println!("This program can detect if you're put a text sentence or encoded number sentence\n");
    let input = user_input::get_input("Write your sentence: ");
    let output = if input.contains('-') {
        from_numbers(&keys, &input)
    } else {
        to_numbers(&keys, &input)
    };
    println!("\nOutput: {output}");
}

//
// Module helper for capture user input
//
mod user_input {
    use std::io::{self, Write};
    pub fn get_input(prompt: &str) -> String {
        print!("{}", prompt);
        io::stdout().flush().expect("Failed to print prompt");
        let mut input = String::new();
        io::stdin()
            .read_line(&mut input)
            .expect("Failed to read input");
        input.trim().to_string()
    }
}
