use std::env;
use std::process::exit;

enum Parity {
    Odd,
    Even,
}

fn is_prime(num: i32) -> bool {

    if num < 2 {
        return false;
    }

    for i in 2..(num/2) + 1  {
        if num % i == 0{
            return false;
        } 
    }
    return true;
}

fn is_odd_or_even(num: i32) -> Parity {

    if (num % 2 == 1) | (num % 2 == -1) { Parity::Odd } else { Parity::Even } 

}

fn is_fibonacci(num: i32) -> bool {

    let (mut a, mut b) = (1, 1);
    let mut n;
    let mut go = true;
    let mut fibonacci = false;

    while go {
        n = a + b;
        a = b;
        b = n;        
        if b == num  {
            go = false;
            fibonacci = true;
        }
        if b > num {
            go = false;
        } 
    }

    return fibonacci;
}

fn main() {

    let num: i32;

    let args: Vec<String> = env::args().collect();

    if args.len() != 2 { 
        println!("\nUsage: {} num \n\nChecks if the number is prime, fibonacci, odd or even. \n 
    - num: Integer number", args[0]);
        exit(0);
    }

    num = match &args[1].parse::<i32>() {
        Ok(n) => {
            (*n).try_into().unwrap()
        },
        Err(_) => {
            eprintln!("The number has to be a integer number");
            return
        },
    };

    if is_prime(num) {
        print!("{} is prime, ", num);
    } else {
        print!("{} is not prime, ", num);
    }

    if is_fibonacci(num) { 
        print!("it is fibonacci "); 
    } else {
        print!("it is not fibonacci ");
    }

    match is_odd_or_even(num) {
        Parity::Odd => {
            print!("and it is odd."); 
        },
        Parity::Even => {
            print!("and it is even."); 
        },
    }  
}