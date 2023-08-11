use evalexpr::*;
use std::any::type_name;
use std::panic;

fn type_of<T>(_: T) -> &'static str {
    type_name::<T>()
}

fn test_math_expr(mut text: String, symbol_vec: Vec<char>) -> bool {

    let mut is_math_expr: bool = false;
    let mut text_symbol_vec: Vec<char> = vec![];

    let _eval: Result<Value, EvalexprError> = eval(&text);
    //println!(" - {:?}", _eval);

    let response: Value = match _eval {
        Ok(res) => res,
        Err(err) => return false
    };

    for c in text.replace(" ", "").chars() {
        //println!("{}", c);
        if !symbol_vec.contains(&c) 
            && !c.is_digit(10) {
            //println!(" - {}", c);
            is_math_expr = false;
            return is_math_expr
        }
    }    

    return true
}

fn main() {

    let mut symbol_vec: Vec<char> = vec![' ', '.'];
    let mut operation_vec: Vec<char> = vec![
        '+', '-', '*', '/', '%'];
    symbol_vec.append(&mut operation_vec);
    let text: String = String::from("1 + 1 / -6.5");
    let is_math_expr: bool = test_math_expr(text, symbol_vec);
    println!("{}", is_math_expr)

}