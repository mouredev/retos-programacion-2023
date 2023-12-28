use std::io;

fn main() {
    println!("{}", to_hacker_lan(get_input()));
}

fn get_input() -> String {
    println!("Enter text: ");
    let mut input = String::new();
    io::stdin().read_line(&mut input).expect("Error reading input");
    input
}

fn to_hacker_lan(mut input: String) -> String {
    input = input.to_uppercase();
    let mut output = String::new();

    for letter in input.chars() {
        match letter {
            'A' => output.push_str("4"),
            'B' => output.push_str("I3"),
            'C' => output.push_str("["),
            'D' => output.push_str(")"),
            'E' => output.push_str("3"),
            'F' => output.push_str("|="),
            'G' => output.push_str("&"),
            'H' => output.push_str("#"),
            'I' => output.push_str("1"),
            'J' => output.push_str(",_|"),
            'K' => output.push_str(">|"),
            'L' => output.push_str("1"),
            'M' => output.push_str("/\\/\\"),
            'N' => output.push_str("^/"),
            'O' => output.push_str("0"),
            'P' => output.push_str("|*"),
            'Q' => output.push_str("(_,)"),
            'R' => output.push_str("I2"),
            'S' => output.push_str("5"),
            'T' => output.push_str("7"),
            'U' => output.push_str("(_)"),
            'V' => output.push_str("\\//"),
            'W' => output.push_str("\\/\\/"),
            'X' => output.push_str("><"),
            'Y' => output.push_str("j"),
            'Z' => output.push_str("2"),
            ' ' => output.push(' '),
            '0' => output.push_str("o"),
            '1' => output.push_str("L"),
            '2' => output.push_str("R"),
            '3' => output.push_str("E"),
            '4' => output.push_str("A"),
            '5' => output.push_str("S"),
            '6' => output.push_str("b"),
            '7' => output.push_str("T"),
            '8' => output.push_str("B"),
            '9' => output.push_str("g"),
            other => output.push_str(&other.to_string()),
        }
    }

    output
}

#[cfg(test)]
mod tests {
    use crate::to_hacker_lan;

    #[test]
    fn test_numbers() {
        assert_eq!(to_hacker_lan(String::from("4251173256")), String::from("ARSLLTERSb"));
    }

    #[test]
    fn test_text() {
        assert_eq!(to_hacker_lan(String::from("Hola mundo!")), String::from("#014 /\\/\\(_)^/)0!"));
    }
}