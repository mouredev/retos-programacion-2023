use chrono;
use rand::seq::SliceRandom;

use std::io::{stdin,stdout,Write};

fn guess_the_word(word_vec: &Vec<String>) {

    fn input(text: String, hidden_word_vec: &Vec<char>) -> String {

        let mut guess_word: String = String::new();
        print!("{}", text);
        print!("{:?}\n", hidden_word_vec);
        print!(">>> ");
        let _ = stdout().flush();
        stdin().read_line(&mut guess_word).expect("Did not enter a correct string");
        if let Some('\n') = guess_word.chars().next_back() {
            guess_word.pop();
        }
        if let Some('\r') = guess_word.chars().next_back() {
            guess_word.pop();
        }
        println!("Your response is: {}", guess_word);

        return guess_word
    }


    let mut num_guesses: i32 = 3;
    let dt_now: chrono::DateTime<chrono::Local> = chrono::offset::Local::now();
    let ts_now: i64 = dt_now.timestamp();
    let mut selected_word_vec: Vec<char> = vec![];
    let selector_num: usize = usize::try_from(ts_now % 3).unwrap();    
    for c in word_vec[selector_num].chars() {
        selected_word_vec.push(c.to_ascii_lowercase());
    }
    let mut hidden_word_vec: Vec<char> = selected_word_vec.clone();
    let num_chars: i16 = selected_word_vec.len() as i16;
    let num_hidden_chars: f32 = (0.6 * f32::try_from(num_chars).unwrap()).floor();
    let mut pos_vec: Vec<i16> = vec![];
    for n in 0..num_chars {
        pos_vec.push(n);
    }
    let mut selected_pos: i16;
    for _ in 0..((num_hidden_chars) as i32) {

        selected_pos = *pos_vec.choose(&mut rand::thread_rng()).unwrap();   
        println!("{} ", selected_pos);
        pos_vec.remove(pos_vec.iter().position(|x| *x == selected_pos).expect("not found"));
        hidden_word_vec[usize::try_from(selected_pos).unwrap()] = '_'
    }
    //let mut guess_word: String = String::from(" ");
    println!("{} - {:?} - {:?} - {} - {}", selector_num, selected_word_vec, hidden_word_vec, num_chars, num_hidden_chars);
    let mut is_winner: bool = false;

    while num_guesses > 0 {
        if hidden_word_vec.contains(&'_') {
            let guess_word: String = input(String::from(
                "Try to guess one character or the complete word!\nYou have "),
                &hidden_word_vec).to_ascii_lowercase(); 
            if guess_word.len() == 1 {
                let guess_char: char = guess_word.chars().next().unwrap();
                if selected_word_vec.contains(&guess_char) {
                    let mut idx_vec: Vec<usize> = vec![];
                    for (num, elem) in selected_word_vec.iter().enumerate() {
                        if elem == &guess_char {
                            idx_vec.push(num)   
                        }
                    }
                    for idx in &idx_vec {
                        hidden_word_vec[*idx] = guess_char
                    }                     
                } else {
                    num_guesses = num_guesses - 1;
                }
                println!("You guess! Now you have this: {:?}", hidden_word_vec) 
            } else {
                println!("You think that the word to guess is: {guess_word}");   
                let mut guess_word_vec: Vec<char> = vec![];
                for c in guess_word.chars() {
                    guess_word_vec.push(c.to_ascii_lowercase());
                }
                if guess_word_vec == selected_word_vec {
                    is_winner = true;
                    break;
                } else {
                    println!("The word is not: {guess_word}");
                    num_guesses = num_guesses - 1;  
                }    
            }
        } else {
            if hidden_word_vec == selected_word_vec {
                is_winner = true;
                break;
            } else {
                break;
            }
        }
        if num_guesses == 0 {
            println!("You LOST!. The word was: {:?}", selected_word_vec);
        }
    }
    if is_winner == true {
        println!("You WIN!. The word was: {:?}", selected_word_vec);
    }
}

fn main() {

    let word_vec: Vec<String> = vec![
        String::from("sugus"), 
        String::from("mouredev"), 
        String::from("flinstones")];
    guess_the_word(&word_vec);
}