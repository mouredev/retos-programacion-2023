use std::collections::HashMap;

fn main() {
    let leet_codes = HashMap::from([
        ("A", "4"),
        ("B", "I3"),
        ("C", "["),
        ("D", ")"),
        ("E", "3"),
        ("F", "|="),
        ("G", "&"),
        ("H", "#"),
        ("I", "1"),
        ("J", ",_|"),
        ("K", ">|"),
        ("L", "1"),
        ("M", "/\\/\\"),
        ("N", "^/"),
        ("O", "0"),
        ("P", "|*"),
        ("Q", "(_,)"),
        ("R", "I2"),
        ("S", "5"),
        ("T", "7"),
        ("U", "(_)"),
        ("V", "\\/"),
        ("W", "\\/\\/"),
        ("X", "><"),
        ("Y", "j"),
        ("Z", "2"),
    ]);

    let mut input = String::new();

    std::io::stdin().read_line(&mut input).unwrap();

    let mut output = String::new();

    for character in input.chars() {
        if let Some(leet_code) = leet_codes.get(&character.to_string().to_uppercase().as_str()) {
            output.push_str(leet_code);
        } else {
            output.push(character);
        }
    }

    println!("{}", output);
}
