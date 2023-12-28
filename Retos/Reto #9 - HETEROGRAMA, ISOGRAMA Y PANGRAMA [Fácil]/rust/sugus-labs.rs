

fn test_string(text: &str, alphabet: Vec<char>) -> (bool, bool, bool) {
    
    println!("{}", text);
    let text: &str = &String::from(text).to_lowercase();

    fn count_words(text: &str, alphabet: &Vec<char>)  -> (Vec<(char, u32)>, bool) {
        let mut count_vec: Vec<(char, u32)> = vec![];
        //let mut char_exists = false;
        //let mut tup: (char, u32) = (' ', 0);
        let mut glob_pos: usize = 0;
        let mut glob_num: u32 = 0;
        let mut is_heterogram = true;
        //count_vec[0] = ('f', 7);
        //println!("{:?}", count_vec);

        for c in text.chars() { // iterate over input text
            if alphabet.contains(&c) { // test if text is in the alphabet
                let mut char_exists = false;
                for (pos, (ch, num)) in count_vec.iter().enumerate() {
                    //println!("char:{} - pos: {}, {}, {}", c, pos, ch, num);
                    if c == *ch {
                        char_exists = true;
                        glob_pos = pos;
                        glob_num = *num;
                        break;
                    }
                }
                if char_exists == false{
                    let tup: (char, u32)= (c, 1);
                    count_vec.push(tup);
                } else {
                    let tup: (char, u32)= (c, glob_num + 1);
                    count_vec[glob_pos] = tup;
                    is_heterogram = false;
                }
            }
        }
        //println!("{:?}", count_vec);
        return (count_vec, is_heterogram)
    }

    fn heterogram(text: &str, alphabet: &Vec<char>) -> bool {  
        let counts: (Vec<(char, u32)>, bool) = count_words(text, alphabet);
        return counts.1
    }

    fn isogram(text: &str, alphabet: &Vec<char>) -> bool {
        let counts: (Vec<(char, u32)>, bool) = count_words(text, alphabet);
        let mut master_val = 0;
        let mut is_isogram = true;
        for (pos, (_, val)) in counts.0.iter().enumerate() {
            if pos == 0 {
                master_val = *val;
            } else {
                if *val != master_val {
                    is_isogram = false;
                    break
                }
            }
        }
        return is_isogram
    }

    fn pangram(text: &str, alphabet: &Vec<char>) -> bool {
        let mut is_pangram = true;
        let mut alphabet_clean = alphabet.clone();
        let counts: (Vec<(char, u32)>, bool) = count_words(text, alphabet);
        //let mut char_vec: Vec<char> = vec![];
        if counts.0.len() != alphabet.len() {
            is_pangram = false;        
        } else {
            for (ch, _) in counts.0.iter() {
                //char_vec.push(*ch);
                if alphabet_clean.contains(&ch) {
                    let index = alphabet_clean.iter().position(|&r| r == *ch).unwrap();
                    alphabet_clean.remove(index);
                } else {
                    is_pangram = false;
                    break;
                }           
            }
        }
        if alphabet_clean.is_empty() {
            is_pangram = true; 
        } else {
            is_pangram = false;
        }
        //println!("{:?}", char_vec);
        //alphabet_list = list(string.ascii_lowercase)
        //if text_list == alphabet_list:
        //    is_pangram = True
        return is_pangram
    }



    let is_hete: bool = heterogram(text, &alphabet);
    let is_isogram: bool = isogram(text, &alphabet);
    let is_pangram: bool = pangram(text, &alphabet);
    //println!("{}", is_hete);
    return (is_hete, is_isogram, is_pangram)

}

fn main() {
   
    const INPUT: &str = "supercalifragilisticoespialidoso";  
    let alphabet: Vec<char> = vec![
        'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 
        'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 
        'u', 'v', 'w', 'x', 'y', 'z'];
    //hete, iso, pan = 
    let result: (bool, bool, bool) = test_string(INPUT, alphabet);
    //println!("{:?}", result);
    println!("The string {}\n- heterogram: {}\n- isogram: {}\n- pangram: {}",
        INPUT, result.0, result.1, result.2) 

}