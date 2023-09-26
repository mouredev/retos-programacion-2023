#[repr(u8)]
#[derive(Clone, Copy)]
enum Flag {
    CapitalLetters = 1,
    Numbers = 1 << 1,
    Symbols = 1 << 2,
}

impl Flag {
    fn check(self, flags: u8) -> bool {
        self as u8 & flags == self as u8
    }
}

pub fn gen_password(length: usize, flags: u8) -> String {
    use rand::seq::SliceRandom;

    assert!(length >= 8);
    assert!(length <= 16);
    let mut result = String::with_capacity(length);
    let mut sources = vec!["abcdefghijklmnopqrstuvwxyz"];
    if Flag::CapitalLetters.check(flags) {
        sources.push("ABCDEFGHIJKLMNOPQRSTUVWXYZ");
    }
    if Flag::Numbers.check(flags) {
        sources.push("0123456789");
    }
    if Flag::Symbols.check(flags) {
        sources.push("!\"#$%&'()=*+,-./[]{}\\|~`");
    }
    while result.len() != length {
        let source = sources.choose(&mut rand::thread_rng());
        let Some(source) = source else {
            continue;
        };
        let Some(chr) = source.as_bytes().choose(&mut rand::thread_rng()) else {
            continue;
        };
        result.push(*chr as char);
    }
    result
}

pub fn main() -> Result<(), Box<dyn std::error::Error>> {
    let mut flags = 0;
    let length: usize = input("Please introduce the desired pass len [8..=16]: ")?.parse()?;

    if yes_no("Do you want Capital letters in your password? [y/N]: ")? {
        flags |= Flag::CapitalLetters as u8
    }
    if yes_no("Do you want Numbers in your password? [y/N]: ")? {
        flags |= Flag::Numbers as u8
    }
    if yes_no("Do you want Symbols in your password? [y/N]: ")? {
        flags |= Flag::Symbols as u8
    }

    println!("{}", gen_password(length, flags));

    Ok(())
}

// Helper functions
fn input(prompt: &str) -> Result<String, Box<dyn std::error::Error>> {
    use std::io::Write;
    print!("{}", prompt);
    std::io::stdout().flush()?;
    let mut input = String::new();
    std::io::stdin().read_line(&mut input)?;
    Ok(input.trim().to_string())
}

fn yes_no(prompt: &str) -> Result<bool, Box<dyn std::error::Error>> {
    let response = input(prompt)?;
    Ok(response.eq_ignore_ascii_case("y")
        || response.eq_ignore_ascii_case("yes")
        || response.eq_ignore_ascii_case("s")
        || response.eq_ignore_ascii_case("si"))
}
