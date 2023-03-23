fn main() {
    for number in 1..=100{
        let mut text : String = number.to_string();
        if number % 3 == 0 && number % 5 == 0 {
            text =  "fizzbuzz".to_string();
        }
        if number % 3 == 0 {
            text =  "fizz".to_string();
        } 
        if number % 5 == 0 {
            text =  "buzz".to_string();
        }
        println!("{text}")
    }
}