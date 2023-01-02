fn main() {
    for i in 1..=100 {
        if i % 3 == 0 {
            if i % 5 == 0 {
                println!("fizzbuzz");
            } else {
                println!("fizz");
            }
            continue;
        }

        if i % 5 == 0 {
            println!("buzz");
            continue;
        }

        println!("{}", i);
    }
}
