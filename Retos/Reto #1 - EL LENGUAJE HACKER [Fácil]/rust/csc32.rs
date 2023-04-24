use std::collections::HashMap;
use std::io::{ stdin};
fn text_to_leetcode(_text: &str) -> String {
    let leet_code: HashMap<char, &str>  = HashMap::from([
        ('a', "4"),
        ('b',"I3"),
        ('c',"["),
        ('d',")"),
        ('e',"3"),
        ('f', "|="),
        ('g',"&"),
        ('h',"#"),
        ('i',"1"),
        ('j',",_/"),
        ('k',">|"),
        ('l',"1"),
        ('m',"/\\/\\"),
        ('n',"^/"),
        ('o',"0"),
        ('p',"|*"),
        ('q',"(_,)"),
        ('r',"I2"),
        ('s',"5"),
        ('t',"7"),
        ('u',"(_)"),
        ('v',"\\/"),
        ('w',"\\/\\/"),
        ('x',"><"),
        ('y',"j"),
        ('z',"2"),
        ('1',"L"),
        ('2',"R"),
        ('3',"E"),
        ('4',"A"),
        ('5',"S"),
        ('6',"b"),
        ('7',"T"),
        ('8',"B"),
        ('9',"g"),
        ('0',"o") 


    ]);
  let mut text_output = String::new();

  for i in _text.to_lowercase().chars(){
        if let Some(value) = leet_code.get(&i){
            text_output.push_str(value);
        }else {
            text_output.push(i);
        }
  }
  return text_output;

}
fn main()  {
    println!("Please write a text");
   let mut text_input = String::new();

   stdin().read_line(&mut text_input ).unwrap();
    text_input = text_input.to_string();
   let result = text_to_leetcode(text_input.to_string().as_str());

   println!("Your word {text_input} is: {result}");

}
