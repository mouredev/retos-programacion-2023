pub fn main() {

    println!("-------------------------------------");
    println!("FizzBuzz using imperative programming");
    println!("-------------------------------------");
    fizzbuzz_for();

    println!("------------------------------------");
    println!("FizzBuzz using funtional programming");
    println!("------------------------------------");
    fizzbuzz_vec();
}

// Classic for loop with an if statement inside
fn fizzbuzz_for() {
    for index in 1..=100 {
        if index%3 == 0 && index%5 == 0 {
            println!("fizzbuzz");
        } else if index%3 == 0 {
            println!("fizz");
        } else if index%5 == 0 {
            println!("buzz");
        } else {
            println!("{}", index);
        }
    }
}

// Functional example
// 1 Create a iterator from a range with 1..100 numbers
// 2 Use filter_map function. This function applies convertion to each element and allows to transform the result type
// 3 Iterate over String structure to print values
fn fizzbuzz_vec() {
    
    // An integer range converted to an iterator.
    let iter_num = (1..=100).into_iter(); 

    // Use filter_map function over iterator with same logic that imperative version
    let iter_string = iter_num.filter_map(|x| {
        if x%3 == 0 && x%5 == 0 {
            Some(String::from("fizzbuzz"))
        } else if x%3 == 0 {
            Some(String::from("fizz"))
        } else if x%5 == 0 {
            Some(String::from("buzz"))
        } else {
            Some(x.to_string())
        }
    });

    // Iterate to print values
    iter_string.for_each(|s| {
        println!("{}",s);
    });
}
