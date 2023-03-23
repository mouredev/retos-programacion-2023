use rand::prelude::*;

struct Options {
    range: i16,
    upper: bool,
    numbers: bool,
    symbols: bool,
}

impl Options {
    fn new(range: i16, upper: bool, numbers: bool, symbols: bool) -> Self {
        Self {
            range,
            upper,
            numbers,
            symbols,
        }
    }
}

fn pass_gen(config: Options) -> String {
    let mut result = String::new();
    let mut chars = vec![];
    const SPECIAL_CHARS: [char; 14] = [
        '!', '#', '$', '%', '&', '*', ']', '[', '(', ')', '{', '}', '+', '-',
    ];
    if config.symbols {
        chars.append(&mut SPECIAL_CHARS.to_vec());
    }
    if config.upper {
        for i in 'A' as u8..'Z' as u8 + 1 {
            chars.push(i as char);
        }
    }

    if config.numbers {
        for i in '0' as u8..'9' as u8 + 1 {
            chars.push(i as char);
            chars.push(i as char);
        }
    }
    for i in 'a' as u8..'z' as u8 + 1 {
        chars.push(i as char);
    }

    for _ in 0..config.range {
        let x = random::<usize>();
        result += &chars[x % chars.len()].to_string();
    }
    result
}

fn main() {
    let options_1 = Options::new(8, true, true, true);
    let options_2 = Options::new(16, true, false, true);

    println!("{}", pass_gen(options_1));
    println!("{}", pass_gen(options_2));
}
