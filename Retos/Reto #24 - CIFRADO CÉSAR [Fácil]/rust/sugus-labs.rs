fn caesar_cypher_decypher(
    mut text: String, _type: &String, movement: &String, 
    num_positions: i16, alphabet_vec: &Vec<char>) -> String{
     
    text = text.to_lowercase(); 
    let mut new_alphabet_vec: Vec<char> = vec![];
    let mut magic_num: i16 = 0;
    let mut source_idx: i16;
    let mut dest_idx: i16;

    if movement == &String::from("R") {
        if _type == &String::from("cypher") {
            magic_num = num_positions as i16;
        } else {
            magic_num = -1 * (num_positions as i16);
        }
    } else if movement == &String::from("L") {
        if _type == &String::from("cypher") {
            magic_num = -1 * (num_positions as i16);
        } else {
            magic_num = num_positions as i16;
        }
    }
    
    //println!("{}", text);
    //println!("{:?}", alphabet_vec);

    for word in text.chars() {
        if word != ' ' {
            //println!("{}", word); 
            source_idx = (alphabet_vec.iter().position(|&x| x == word).unwrap() as i16);
            dest_idx = (source_idx + magic_num) % 27;
            new_alphabet_vec.push(alphabet_vec[(dest_idx as usize)]);
        } else {
            new_alphabet_vec.push(' ');
        }
    }

    let edited_text = new_alphabet_vec.into_iter().collect();
    return edited_text;

}

fn main() {

    let alphabet: String = String::from("abcdefghijklmnopqrstuvwxyz");
    let alphabet_vec: Vec<char> = alphabet.chars().collect();
    //println!("{:?}", alphabet_vec);
    let text: String = String::from("HELLO WORLD");
    let movement: String = String::from("R");
    let num_positions: i16 = 2;
    let mut _type: String = String::from("cypher");
    let cyphered_text = caesar_cypher_decypher(
        text, &_type, &movement, num_positions, &alphabet_vec);
    println!("{}", cyphered_text);
    _type = String::from("decypher");
    let decyphered_text = caesar_cypher_decypher(
        cyphered_text, &_type, &movement, num_positions, &alphabet_vec);
    println!("{}", decyphered_text);

}