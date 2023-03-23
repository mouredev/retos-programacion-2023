use std::collections::HashMap;

fn str_to_leet(input: &str) -> String {
    let alphabet = HashMap::from([
        ("0", "o"),
        ("1", "L"),
        ("2", "R"),
        ("3", "E"),
        ("4", "A"),
        ("5", "S"),
        ("6", "b"),
        ("7", "T"),
        ("8", "B"),
        ("9", "g"),
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
        ("m", r"/\/\"),
        ("n", "^/"),
        ("o", "0"),
        ("p", "|*"),
        ("q", "(_,)"),
        ("r", "I2"),
        ("s", "5"),
        ("t", "7"),
        ("u", "(_)"),
        ("v", r"\/"),
        ("w", r"\/\/"),
        ("x", "><"),
        ("y", "j"),
        ("z", "2"),
    ]);

    let mut output = String::new();

    for i in input.to_lowercase().chars() {
        if let Some(value) = alphabet.get(i.to_string().as_str()) {
            output.push_str(value)
        } else {
            output.push(i)
        }
    }

    return output
}

fn main() {
    let cases = HashMap::from([
        ("demo", r")3/\/\0"),
        ("hacker", r"#4[>|3I2"),
        ("H4x0r", r"#A><oI2"),
        ("Hello World!", r"#3110 \/\/0I21)!"),
        ("My password is: 17o^DuQn$qNj", r"/\/\j |*455\/\/0I2) 15: LT0^)(_)(_,)^/$(_,)^/,_|"),
    ]);

    for case in cases {
        let got = str_to_leet(case.0);

        if got.eq(case.1) {
            println!("Case passed:")
        } else {
            println!("Case failed:")
        }

        println!("\tinput:\t\"{}\"\n\twant:\t\"{}\"\n\tgot:\t\"{}\"\n", case.0, case.1, got)
    }
}
