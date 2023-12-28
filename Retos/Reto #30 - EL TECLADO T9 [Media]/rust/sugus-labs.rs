use std::collections::HashMap;

fn t9_to_text(text: String, alphabet_hash: &HashMap<char,  Vec<char>>) {
        
    let mut new_str_vec: Vec<char> = vec![];
    let text_parts = text.split("-");
    let text_vec = text_parts.collect::<Vec<&str>>();
    let mut pos: usize;
    let mut new_char: char;
    let mut ch: char;

    for t in text_vec {
        pos = t.len() - 1;
        ch = String::from(t).chars().next().unwrap();
        new_char = alphabet_hash.get(&ch);
        dbg!(t, pos, new_char);
    }
    //    
    //    new_char = alphabet_dict.get(t[0])[pos]
    //    new_str_list.append(new_char)
    //new_str = "".join(new_str_list)
    
   //return new_str
}

fn main() {

    let text: String = String::from("6-666-88-777-33-3-33-888");
    let alphabet_hash: HashMap<char,  Vec<char>> = [
        ('2', vec!['a', 'b', 'c']), 
        ('3', vec!['d', 'e', 'f']), 
        ('4', vec!['g', 'h', 'i']), 
        ('5', vec!['j', 'k', 'l']), 
        ('6', vec!['m', 'n', 'o']), 
        ('7', vec!['p', 'q', 'r', 's']), 
        ('8', vec!['t', 'u', 'v']), 
        ('9', vec!['w', 'x', 'y', 'z'])]
        .iter()
        .cloned()
        .collect();
    t9_to_text(text, &alphabet_hash);
    //println!("{:?}", alphabet_hash);

}