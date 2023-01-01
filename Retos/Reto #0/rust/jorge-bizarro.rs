fn main() {
  for value_number in 1..101 {
    let mut value_string: String = "".to_owned();

    if value_number % 3 == 0 {
      let string_to_concat: &str = "Fizz";
      value_string.push_str(string_to_concat);
    }

    if value_number % 5 == 0 {
      let string_to_concat: &str = "Buzz";
      value_string.push_str(string_to_concat);
    }

    if value_string.len() == 0 {
      println!("{}", value_number);
    } else {
      println!("{}", value_string);
    }
  }
}
