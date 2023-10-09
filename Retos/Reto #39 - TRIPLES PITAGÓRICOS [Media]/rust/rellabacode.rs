use std::io;

fn read_integer() -> u128 {
    println!("---------------------------");
    println!("Calc Of Pythagorean triples");
    println!("---------------------------\n");
    println!("Insert a number as UPPER LIMIT");
    let mut value: u128 = 0;
    let mut valid: bool = false;
    let mut input = String::new();
    while !valid {
        io::stdin()
            .read_line(&mut input)
            .expect("Failed to read integer");

        value = match input.trim().parse::<u128>() {
            Ok(v) => v,
            Err(_) => 0,
        };
        valid = value != 0;
        if !valid {
            println!("ERROR: incorrect number, Try Again");
            input.clear();
        }
    }
    return value;
}

struct Triple {
    a: u128,
    b: u128,
    c: u128,
}

fn main() {
    let mut LIMIT: u128 = read_integer() + 1;
    let mut triples = Vec::new();

    for a in 1..LIMIT {
        for b in a + 1..LIMIT {
            for c in b + 1..LIMIT {
                if a * a + b * b == c * c {
                    triples.push(Triple { a: a, b: b, c: c });
                }
            }
        }
    }

    println!("Found:");
    for (pos, triple) in triples.iter().enumerate() {
        print!("({}, {}, {}) ", triple.a, triple.b, triple.c);
    }
}
