pub trait FizzBuzz {
    fn fizz(&self) -> String;
}

impl FizzBuzz for i32 {
    fn fizz(&self) -> String {
        match (self % 3, self % 5) {
            (0, 0) => "FizzBuzz".to_string(),
            (0, _) => "Fizz".to_string(),
            (_, 0) => "Buzz".to_string(),
            _ => format!("{}", self),
        }
    }
}

fn main() {
    // Idiomatic solution
    for x in 1..=100 {
        println!("{}", x.fizz())
    }
    // Simple solution
    /*   for x in 1..=100 {
        if x % 3 == 0 && x % 5 == 0 {
            println!("FizzBuzz")
        } else if x % 3 == 0 {
            println!("Fizz")
        } else if x % 5 == 0 {
            println!("Buzz")
        } else {
            println!("{}", x)
        }
    } */
}
