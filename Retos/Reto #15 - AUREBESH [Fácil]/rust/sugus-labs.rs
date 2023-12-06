use std::collections::HashMap;
use std::env;

fn text_to_aurebesh(mut text: String, alphabet_hash: &HashMap<String, String>) -> String {

    //println!("'{:?}'", alphabet_hash);
    text = text.to_ascii_lowercase();
    let mut new_str_vec: Vec<String> = vec![];
    let mut fake_num: i32 = -1;
    let mut new_str: String = String::new();

    for (num, char) in text.chars().enumerate(){
        //println!("num: {} - fake_num: {} - char: {}", num, fake_num, char);

        if (num as i32) != fake_num {
            //println!("num: {} - fake_num: {} - char: {}", num, fake_num, char);
            if num == text.len() - 1 {
                //println!("Entering last one");
                new_str = (*alphabet_hash.get(&String::from(char)).unwrap().clone()).to_string(); 
                fake_num = num as i32;                
            } else {
                if (char == 'c' &&  text.chars().nth(num + 1).unwrap() == 'h')
                    || (char == 'e' &&  text.chars().nth(num + 1).unwrap() == 'o')
                    || (char == 'k' &&  text.chars().nth(num + 1).unwrap() == 'h')
                    || (char == 'n' &&  text.chars().nth(num + 1).unwrap() == 'g')
                    || (char == 'o' &&  text.chars().nth(num + 1).unwrap() == 'o')
                    || (char == 's' &&  text.chars().nth(num + 1).unwrap() == 'h')
                    || (char == 't' &&  text.chars().nth(num + 1).unwrap() == 'h') {

                    new_str = (*alphabet_hash.get(&(String::from(char) + &String::from(text.chars().nth(num + 1).unwrap()))).unwrap().clone()).to_string(); 
                    fake_num = (num as i32) + 1;
                } else { 
                    new_str = (*alphabet_hash.get(&String::from(char)).unwrap().clone()).to_string(); 
                    fake_num = num as i32;
                }
            }
            new_str_vec.push(new_str);
            //println!("{:?}", new_str_vec);
        }
    }
    
    let joined_str: String = new_str_vec.join(" ");
    return joined_str

}

fn main() {

    env::set_var("RUST_BACKTRACE", "full");
    let text: String = String::from("LEOT");
    let alphabet_hash: HashMap<String, String> = [
        (String::from("a"),  String::from("aurek")),
        (String::from("b"),  String::from("besh")),
        (String::from("c"),  String::from("cresh")),
        (String::from("ch"),  String::from("cherek")),
        (String::from("d"),  String::from("dorn")),
        (String::from("e"),  String::from("esk")),
        (String::from("æ"),  String::from("enth")),
        (String::from("eo"),  String::from("onith")), 
        (String::from("f"),  String::from("forn")),
        (String::from("g"),  String::from("grek")),
        (String::from("h"),  String::from("herf")),
        (String::from("i"),  String::from("isk")),
        (String::from("j"),  String::from("jenth")),
        (String::from("k"),  String::from("krill")),
        (String::from("kh"),  String::from("krenth")),
        (String::from("l"),  String::from("leth")),   
        (String::from("m"),  String::from("mern")),
        (String::from("n"),  String::from("nern")),
        (String::from("ng"),  String::from("nen")),
        (String::from("o"),  String::from("osk")),
        (String::from("oo"),  String::from("orenth")),
        (String::from("p"),  String::from("peth")),
        (String::from("q"),  String::from("qek")),
        (String::from("r"),  String::from("resh")),      
        (String::from("s"),  String::from("senth")),
        (String::from("sh"),  String::from("shen")),
        (String::from("t"),  String::from("trill")),
        (String::from("th"),  String::from("thesh")),
        (String::from("u"),  String::from("usk")),
        (String::from("v"),  String::from("vev")),
        (String::from("w"),  String::from("wesk")),
        (String::from("x"),  String::from("xesh")),          
        (String::from("y"),  String::from("yirt")),
        (String::from("z"),  String::from("zerek"))]
        .iter()
        .cloned()
        .collect();
        //'s': 'senth', 'sh': 'shen', 't': 'trill', 'th': 'thesh', 'u': 'usk', 'v': 'vev', 'w': 'wesk', 'x': 'xesh', 'y': 'yirt', 'z': 'zerek']
    let s = text_to_aurebesh(text, &alphabet_hash);
    println!("'{}'", s);
}