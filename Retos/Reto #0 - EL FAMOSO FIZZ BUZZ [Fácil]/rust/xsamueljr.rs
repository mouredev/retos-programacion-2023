fn main() {
    for number in 1..=100 {
        let divisible_by_three = number % 3 == 0;
        let divisible_by_five = number % 5 == 0;

        if divisible_by_three && divisible_by_five {
            println!("fizzbuzz");
        } else if divisible_by_three {
            println!("fizz");
        } else if divisible_by_five {
            println!("buzz");
        } else {
            println!("{}", number);
        }
    }
}
