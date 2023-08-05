use rand::seq::SliceRandom;

fn generate_password(length: usize, 
    upper_letters: bool,
    numbers: bool,
    symbols: bool) {
    
    // Generate password function

    let mut alphabet_list = vec!['a', 'b', 'c', 'd', 'e', 
        'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 
        'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 
        'z'];

    if upper_letters == true {

        let mut alphabet_upper_list = vec!['A', 'B', 'C', 
            'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 
            'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 
            'V', 'W', 'X', 'Y', 'Z'];

        alphabet_list.append(&mut alphabet_upper_list);
    } 
    if numbers == true {

        let mut alphabet_number_list = vec!['0', '1', '2', 
            '3', '4', '5', '6', '7', '8', '9'];

        alphabet_list.append(&mut alphabet_number_list);
    }   
    if symbols == true {

        let mut alphabet_symbol_list = vec!['!', '"', '#', 
            '$', '%', '&', '\'', '(', ')', '*', '+', ',', 
            '-', '.', '/', ':', ';', '<', '=', '>', '?', 
            '@', '[', '\\', ']', '^', '_', '`', '{', '|', 
            '}', '~'];

        alphabet_list.append(&mut alphabet_symbol_list);
    }        
    //alphabet_list = alphabet_list.append(new_alphabet_list);
    //println!("{alphabet_list:?}");
    let mut password: String = String::from("");

    for _ in 0..length {
        let choice = alphabet_list.choose(&mut rand::thread_rng()).unwrap();
        password.push(*choice)
        //println!("{choice:?}");
    //    password = password + char
    }
    println!("{password}")

}

fn main() {

    generate_password(16, true, true, true);

}