trait Squarable {
    fn sqrt(&self) -> u32;
}

impl Squarable for u32 {
    fn sqrt(self: &Self) -> u32 {
        f32::sqrt(*self as f32) as u32
    }
}

fn is_prime(n: u32) -> bool {
    let mut i = 2u32;
    while i <= n.sqrt() {
        if n % i == 0 {
            return false;
        }
        i += 1;
    }

    true
}

fn is_perfect_square(n: u32) -> bool {
    let nsq = n.sqrt();
    nsq*nsq == n
}

fn is_fib(n: u32) -> bool {
    let ps  = 5*n*n;

    return is_perfect_square(ps + 4) || is_perfect_square(ps - 4);
}

fn is_even(n: u32) -> bool {
    (n & 1) == 0
}

fn is_or_not(is: bool) -> &'static str {
    match is {
        true  => "es",
        false => "no es"
    }
}

fn run(input: &str) {
    let num = input.parse::<u32>().ok();
    if let Some(n) = num {
        println!("{} {} primo, {} fibonnaci, {} par"
            , n, is_or_not(is_prime(n))
            , is_or_not(is_fib(n)), is_or_not(is_even(n))
        );
    } else {
        println!("ERROR: '{}' is not a u32 valid number", input);
    }
}

fn usage(program: &str) {
    println!("USAGE:\n    {} <n32>", program);
    print!(r#"
    Checks whether the number <n32> is prime, fibonnaci and/or even.

PARAMS:
    - <n32> : must be a valid unsigned 32-bits integer number

"#)
}

fn main() {
    use std::env;

    let argn = env::args().count();

    match argn {
        2 => run(&env::args().last().unwrap()),
        _ => usage(&env::args().nth(0).unwrap())
    }
}
