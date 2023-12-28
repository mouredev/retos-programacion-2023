use std::env;
use std::process::exit;
use rand::Rng;

fn main(){

    const MIN_LENGTH: usize = 8;
    const MAX_LENGTH: usize = 16;

    let lower_case_letters: &'static str = "abcdefghijklmnopqrstuvwxyz";
    let upper_case_letters: &'static str = "ABCDEFGHIJKLMNOPQRSTUVWXYZ";
    let numbers: &'static str = "1234567890";
    let symbols: &'static str = "!$&()=~,.-;:_";

    let mut characters = String::with_capacity(80);

    let args: Vec<String> = env::args().collect();

    if args.len() == 1 {
            println!("\nUsage: {} num [OPTIONS] \n\n\
            Get a multicharacter password (Default: lower case letters) \n\n\
            - num: number of characters of the password. \n\n\
            - OPTIONS: \n    U: Upper case letters \n    n: Numbers \n    s: Symbol
            ", args[0]);
            exit(0);    
    } 

    let len = match &args[1].parse::<usize>() {
        Ok(n) => {
            (*n).try_into().unwrap()
        },
        Err(_) => {
            eprintln!("The first argument has to be a number between {} and {}", MIN_LENGTH, MAX_LENGTH);
            return;
        },
    };

    let length_password = if len >= MIN_LENGTH && len <= MAX_LENGTH { len } else { 0 };

    if length_password == 0 {
        println!("The first argument has to be a number between {} and {}", MIN_LENGTH, MAX_LENGTH);
    } else {

        characters.push_str(lower_case_letters);
    
        if args.len() == 3 {
            if args[2].contains("U"){ characters.push_str(upper_case_letters); }
            if args[2].contains("n"){ characters.push_str(numbers); }
            if args[2].contains("s"){ characters.push_str(symbols); }
        }

        let mut rng = rand::thread_rng();
        let letters: Vec<char> = characters.chars().collect();

        print!("Password --> ");

        for _i in 0..length_password {
            print!("{}", letters[ rng.gen::<usize>() % characters.len() ]);
        }
    }
}