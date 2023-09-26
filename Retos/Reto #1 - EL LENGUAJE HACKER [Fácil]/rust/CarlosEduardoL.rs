// Mapping of alphabet chars 0 indexed [char - 'A'] to their l33t representation
const ALPHA_MAPPING: [&'static str; 26] = [
    "4", "I3", "[", ")", "3", "|=", "&", "#", "1", ",_|", ">|", "1", r"/\/\", "^/", "0", "|*",
    "(_,)", "I2", "5", "7", "(_)", r"\/", r"\/\/", "><", "j", "2",
];

// Mapping of number chars 0 indexed [char - '0'] to their l33t representation
const NUM_MAPPING: [&'static str; 10] = ["o", "L", "R", "E", "A", "S", "b", "T", "B", "g"];

pub fn str_to_l33t(message: &str) -> String {
    let mut answer: String = String::with_capacity(message.len());
    for chr in message.chars() {
        match chr {
            'A'..='Z' => answer.push_str(ALPHA_MAPPING[(chr as u8 - b'A') as usize]),
            'a'..='z' => answer.push_str(ALPHA_MAPPING[(chr as u8 - b'a') as usize]),
            '0'..='9' => answer.push_str(NUM_MAPPING[(chr as u8 - b'0') as usize]),
            _ => answer += &format!("{}", chr),
        }
    }
    answer
}

pub fn main() -> Result<(), Box<dyn std::error::Error>> {
    let input = std::io::stdin();
    let mut buffer = String::new();
    loop {
        input.read_line(&mut buffer)?;
        if buffer == "exit;\n" {
            return Ok(());
        }
        println!("-> {}", str_to_l33t(&buffer.trim()));
        buffer.clear();
    }
}

#[cfg(test)]
mod test {
    #[test]
    fn hello_world_to_l33t() {
        assert_eq!(super::str_to_l33t("Hello World!"), r"#3110 \/\/0I21)!")
    }

    #[test]
    fn wikipedia_to_l33t() {
        assert_eq!(
            super::str_to_l33t("Wikipedia was created by Jimmy Wales and Larry Sanger on January 15, 2001, it is hosted by the Wikimedia Foundation"),
            r"\/\/1>|1|*3)14 \/\/45 [I23473) I3j ,_|1/\/\/\/\j \/\/4135 4^/) 14I2I2j 54^/&3I2 0^/ ,_|4^/(_)4I2j LS, RooL, 17 15 #0573) I3j 7#3 \/\/1>|1/\/\3)14 |=0(_)^/)4710^/"
        )
    }
}
