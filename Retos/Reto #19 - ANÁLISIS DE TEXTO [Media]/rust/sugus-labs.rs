fn mean(numbers: &[i32]) -> f32 {
    numbers.iter().sum::<i32>() as f32 / numbers.len() as f32
}

fn analyze_text(text: String) -> (i32, f32, i32, String) {

    let text_vec: Vec<String> = text.split(" ").map(str::to_string).collect();//.unwrap();
    //println!("{:?}", text_vec);
    let mut word_length_vec: Vec<i32> = vec![];
    let mut word_length: i32 = 0;
    let mut num_words = 0;
    let mut num_sentences = 0;
    let mut num_words_longest_word = 0;
    let mut longest_word = String::new();
    let mean_length_words: f32;

    for word in text_vec {
        //println!("{}", word);
        if word != String::from("\n") 
            && word != String::from("") {
            num_words = num_words + 1;   
            word_length = (word
                .replace(".", "")
                .replace(",", "")
                .replace(":", "").len() as i32);
            word_length_vec.push(word_length);
            if word_length > num_words_longest_word {
                longest_word = word
                    .replace(".", "")
                    .replace(",", "")
                    .replace(":", "");
                num_words_longest_word = word_length;
            }
        }    

        if word.contains(&".") {
            num_sentences = num_sentences + 1;
        }
    }
    mean_length_words = mean(&word_length_vec);

    return (num_words, mean_length_words, num_sentences, longest_word);
}

fn main() {

    let text: String = String::from("
        Lorem ipsum dolor sit amet, consectetur adipiscing elit, 
        sed do eiusmod tempor incididunt ut labore et dolore magna 
        aliqua. Ut enim ad minim veniam, quis nostrud exercitation 
        ullamco laboris nisi ut aliquip ex ea commodo consequat. 
        Duis aute irure dolor in reprehenderit in voluptate velit 
        esse cillum dolore eu fugiat nulla pariatur. Excepteur sint 
        occaecat cupidatat non proident, sunt in culpa qui officia 
        deserunt mollit anim id est laborum.");
    let analytics = analyze_text(text);
    //println!("{:?}\n", analytics.2);
    println!("Analytics for the text.
             - Number of words: {}
             - Mean lenght of words: {}
             - Number of sentences: {}
             - Longest word: {}", 
        analytics.0, analytics.1, 
        analytics.2, analytics.3);
}