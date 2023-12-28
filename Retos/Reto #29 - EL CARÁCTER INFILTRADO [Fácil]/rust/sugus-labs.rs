fn diff_chars(first_text: String, sec_text: String) -> Vec<(char, char)> {
    
    let mut error_vec: Vec<(char, char)> = vec![];
    let first_text_vec: Vec<char> = first_text.chars().collect();
    let sec_text_vec: Vec<char> = sec_text.chars().collect();

    let iter = first_text_vec.iter().zip(sec_text_vec.iter());

    for (c1, c2) in iter {
        //println!("{} {}", c1, c2);
        if c1 != c2 {
            error_vec.push((*c1, *c2))
        }          
    }

    return error_vec;
}

fn main() {

    let first_text: String = String::from("Me llamo.Brais Moure");
    let sec_text: String = String::from("Me llamo brais moure");
    let result_vec: Vec<(char, char)> = diff_chars(first_text, sec_text);
    println!("{:?}", result_vec);

}