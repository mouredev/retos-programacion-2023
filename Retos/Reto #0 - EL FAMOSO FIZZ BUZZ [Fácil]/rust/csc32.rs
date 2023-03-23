fn main() {
    for i in 1..101 {
        fizzbuzz(i)
    }
}
fn fizzbuzz(i: i32) {
    if i % 3 == 0 && i % 5 == 0 {
        return println!("fizzbuzz");
    }
    if i % 3 == 0 {
        return println!("fizz");
    }
    if i % 5 == 0 {
        return println!("buzz");
    }
    return println!("{i}");
}
