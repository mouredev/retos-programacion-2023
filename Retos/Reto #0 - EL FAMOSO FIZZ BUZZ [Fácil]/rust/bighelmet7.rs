fn main() {
    let num = 100;
    fizzbuzz(num);
}

fn fizzbuzz(num: i32) {
    if num == 0 {
        return;
    }

    fizzbuzz(num - 1);

    match (num % 3 == 0, num % 5 == 0) {
        (true, true) => println!("fizzbuzz"),
        (true, false) => println!("fizz"),
        (false, true) => println!("buzz"),
        _ => println!("{num}"),
    }
}
