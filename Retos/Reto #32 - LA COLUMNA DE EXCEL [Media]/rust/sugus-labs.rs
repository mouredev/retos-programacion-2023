fn calculate_excel_column(mut column_name: String, alphabet_vec: Vec<char>) -> u32 {

    //println!("{:?}", alphabet_vec);
    column_name = column_name.to_uppercase().chars().rev().collect::<String>();
    let column_name_vec: Vec<char> = column_name.chars().collect();
    let column_name_search_vec = column_name_vec.clone();
    let mut column_value: u32 = 0;
    let mut column_pos: u32 = 0;
    let vec_size: u32 = 26;
    
    for (iter, c) in column_name_vec.into_iter().enumerate() {
        let idx: u32 = (alphabet_vec.iter().position(|&r| r == c).unwrap() + 1) as u32;
        //println!("{} {}", c, idx);
        if iter!= 0 {
            column_value = vec_size.pow(iter as u32) * idx;
        } else {
            column_value = idx;
        }
        column_pos = column_pos + column_value;
    }

    return column_pos

}
fn main() {

    let alphabet_vec: Vec<char> = vec![
        'A', 'B', 'C', 'D', 'E', 'F', 'G', 
        'H', 'I', 'J', 'K', 'L', 'M', 'N', 
        'O', 'P', 'Q', 'R', 'S', 'T', 'U', 
        'V', 'W', 'X', 'Y', 'Z'];
    let column_name: String = String::from("AAA");
    let column_pos: u32 = calculate_excel_column(
        column_name, alphabet_vec);
    println!("{}", column_pos);
    
}