fn main() {
    for i in 1..100 {
        if i % 5 == 0 && i % 3 == 0 {
            println!("{} fizzbuzz", i);
        }
        else if i % 3 == 0 {
            println!("{} fizz", i);
        }
        else if i % 5 == 0 {
            println!("{} buzz", i);
        }
    }
}