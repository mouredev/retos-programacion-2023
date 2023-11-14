fn read_abacus_str(abacus_vec: Vec<String>) -> usize {
    
    let mut abacus_num_str = String::new();
    let mut chunks: Vec<&str> = vec![];
    let mut num;
    let abacus_number: usize;

    for line in abacus_vec {
        chunks = line.split("---").collect();
        num = chunks[0].len(); 
        //println!("{:?}", num);
        abacus_num_str.push_str(&num.to_string());
    }
    let abacus_number: usize = abacus_num_str.parse().unwrap();
    
    return abacus_number;
        
}

fn main() {

    let abacus_vec: Vec<String> = vec![
        String::from("O---OOOOOOOO"),
        String::from("OOO---OOOOOO"),
        String::from("---OOOOOOOOO"),
        String::from("OO---OOOOOOO"),
        String::from("OOOOOOO---OO"),
        String::from("OOOOOOOOO---"),
        String::from("---OOOOOOOOO")];
    let abacus_number = read_abacus_str(abacus_vec);
    println!("{}",abacus_number);

}