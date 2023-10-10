const ALPHABET_ARRAY: [(char, &str); 36] = [
    ('A', "∆"),
    ('B', "8"),
    ('C', "&lt;"),
    ('D', "|)"),
    ('E', "3"),
    ('F', "7"),
    ('G', "9"),
    ('H', "#"),
    ('I', "1"),
    ('J', "√"),
    ('K', "|&lt;"),
    ('L', "|_"),
    ('M', "44"),
    ('N', "|\\|"),
    ('O', "0"),
    ('P', "|o"),
    ('Q', "O_"),
    ('R', "|2"),
    ('S', "5"),
    ('T', "7"),
    ('U', "|_|"),
    ('V', "\\/"),
    ('W', "\\/\\/"),
    ('X', "×"),
    ('Y', "`/"),
    ('Z', "5"),
    ('0', "O"),
    ('1', "I"),
    ('2', "Z"),
    ('3', "E"),
    ('4', "h"),
    ('5', "S"),
    ('6', "b"),
    ('7', "T"),
    ('8', "B"),
    ('9', "g")
];

fn text_to_leet(text: String, alphabet_array: &[(char, &str); 36]) -> String {
    
    // text to Leet function
    
    //println!("{text}");

    const WHITE_SPACE: char = ' '; 
    let mut new_text: String = String::from("");
    
    
    for c in text.chars() {

        for (orig, dest) in alphabet_array.iter() {
            if c == *orig {
                new_text.push_str(dest);
            } else if c == WHITE_SPACE {
                new_text.push_str(&WHITE_SPACE.to_string());
                break
            }
        }
    }

    new_text

    //println!("{new_text}");
}

fn main() {

    //println!("{ALPHABET_ARRAY:?}");
    let s: String = String::from("LET ME KNOW");
    let t: String = text_to_leet(s, &ALPHABET_ARRAY);
    println!("{t}");

}
    