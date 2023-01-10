//Prueba: https://play.rust-lang.org/?version=stable&mode=debug&edition=2021&gist=089dd81aad4711a6321f49dc66aad90c

use std::collections::HashMap;

fn main() {
    let text ="¡Hola mundo!";
    let mut translate = "".to_string();
    let dic = HashMap::from([
        ("a", "4"),
        ("b", "I3"),
        ("c", "["),
        ("d", ")"),
        ("e", "3"),
        ("f", "|="),
        ("g", "&"),
        ("h", "#"),
        ("i", "1"),
        ("j", ",_|"),
        ("k", ">|"),
        ("l", "1"),
        ("m", "/\\/\\"),
        ("n", "^/"),
        ("o", "0"),
        ("p", "|*"),
        ("q", "(_,)"),
        ("r", "I2"),
        ("s", "5"),
        ("t", "7"),
        ("u", "(_)"),
        ("v", "\\/"),
        ("w", "\\/\\/"),
        ("x", "><"),
        ("y", "j"),
        ("z", "2"),
        ("1", "L"),
        ("2", "R"),
        ("3", "E"),
        ("4", "A"),
        ("5", "S"),
        ("6", "b"),
        ("7", "T"),
        ("8", "B"),
        ("9", "g"),
        ("0", "o"),
    ]);
    
    for i in text.chars() {
        if i.is_alphanumeric() {
            let letter: &str = dic[&i.to_string().to_lowercase().as_str()];
            translate.push_str(&letter);
        }
        else {
            translate.push(i);
        }
    }
    println!("{text}");
    println!("{translate}");
}