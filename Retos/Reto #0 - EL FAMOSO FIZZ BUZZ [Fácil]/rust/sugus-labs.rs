fn fizz_buzz(
    start_num: usize, 
    stop_num: usize,
    fizz_str: &str,
    buzz_str: &str) {
    
    // Fizz Buzz function
    for num in start_num..stop_num + 1 {
        if num % 3 == 0 && num % 5 == 0 {
            print!("{} {}", num, fizz_str);
            println!("{}", buzz_str);
        } else if num % 3 == 0 {
            println!("{} {}",num, fizz_str);
        }
        else if num % 5 == 0 {
            println!("{} {}",num, buzz_str);
        }
     }        
}
            
fn main() {

    let fizz_str = String::from("fizz");
    let buzz_str = String::from("buzz");

    fizz_buzz(1, 100, &fizz_str, &buzz_str)
}
    