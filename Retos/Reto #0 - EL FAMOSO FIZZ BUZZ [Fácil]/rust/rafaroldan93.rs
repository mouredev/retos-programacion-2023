//Prueba: https://play.rust-lang.org/?version=stable&mode=debug&edition=2021&gist=24317fa2ee26285c01a8e077c750bb47

fn main() {
    let mut n = 1;
    while n <= 100 {
        if n % 3 == 0 && n % 5 == 0 {
            println!("fizzbuzz");
        } else if n % 3 == 0 {
            println!("fizz");
        } else if n % 5 == 0 {
            println!("buzz");
        } else {
            println!("{n}");
        }
        n += 1;
    }
}