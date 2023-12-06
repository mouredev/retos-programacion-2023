use std::io;

fn selection_hat() {
    
    // Selection hat function
    let mut last_user_input: String = String::new();
    let mut user_input_clean: char = ' ';
    let mut user_input = String::from("");
    let mut political_vision: String = String::from("");
    let zero_val: u32 = 64;
    let mut sum_val: u32 = 0;
    let mut choice_list: Vec<char> = vec![];
    let question_list: Vec<(&str, &str)> = vec![
        ("What is your prefered colour?", "A - RED\nB - BLUE\nC - WHITE\nD - YELLOW\n"),
        ("What is your prefered shape?","A - CIRCLE\nB - RECTANGLE\nC - SQUARE\nD - TRIANGLE\n")
    ];  

    for question in question_list {
        
        while true { 

            println!("{}", question.0);     
            println!("{}", question.1);   
            let mut user_input = String::new();
            let stdin = io::stdin();
            let _ = stdin.read_line(&mut user_input); 
            //println!("User Input: {}", user_input);
            let mut user_input_clean: char = user_input.trim().to_uppercase().chars().next().unwrap();
            if user_input_clean == 'A'
                || user_input_clean == 'B'
                || user_input_clean == 'C'
                || user_input_clean == 'D' {
                
                choice_list.push(user_input_clean);
                break;
            }
            //let last_user_input: String = user_input.clone();
        }                         
    }
    println!("input {:?} ", choice_list); 

    for c in choice_list {
        let val: u32 = c.into(); 
        //println!("{} - {}", c, val);
        sum_val = sum_val + (val - zero_val)
    }
    // let mut a: char = 'a';
    // let mut b: u32 = a.into(); 
    //println!("{}", sum_val)

    if sum_val < 5 {
        political_vision.push_str(&String::from("LIBERAL"));
    } else {
        political_vision.push_str(&String::from("CONSERVATIVE"));
    }    
    println!("You are {political_vision}")    
}

fn main() {

    selection_hat();

}