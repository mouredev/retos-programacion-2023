use std::collections::HashMap;

pub trait Leet {
    fn transform_to_leet(&self) -> String;
}

impl Leet for char {
    fn transform_to_leet(&self) -> String {
        let alphabet: HashMap<char, &str> = HashMap::from([
            ('A', "4"),
            ('B', "I3"),
            ('C', "["),
            ('D', ")"),
            ('E', "3"),
            ('F', "|="),
            ('G', "&"),
            ('H', "#"),
            ('I', "1"),
            ('J', ",_|"),
            ('K', ">|"),
            ('L', "1"),
            ('M', r"/\/\"),
            ('N', "^/"),
            ('O', "0"),
            ('P', "|*"),
            ('Q', "(_,)"),
            ('R', "I2"),
            ('S', "5"),
            ('T', "7"),
            ('U', "(_)"),
            ('V', r"\/"),
            ('W', r"\/\/"),
            ('X', "><"),
            ('Y', "j"),
            ('Z', "2"),
            ('1', "L"),
            ('2', "R"),
            ('3', "E"),
            ('4', "A"),
            ('5', "S"),
            ('6', "b"),
            ('7', "T"),
            ('8', "B"),
            ('9', "g"),
            ('0', "O"),
        ]);

        alphabet
            .get(&self.to_ascii_uppercase())
            .unwrap()
            .to_string()
    }
}

fn main() {
    let sample = "leet";
    println!(
        "{}",
        sample
            .chars()
            .map(|l| l.transform_to_leet())
            .collect::<String>()
    );
}
