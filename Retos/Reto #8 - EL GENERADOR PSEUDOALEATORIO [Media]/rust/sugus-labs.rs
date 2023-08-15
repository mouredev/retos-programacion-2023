use chrono;

fn generate_pseudorandom_number() -> u32 {
    
    // Generate pseudo random number function
    let dt_now: chrono::DateTime<chrono::Local> = chrono::offset::Local::now();
    let ts_now: i64 = dt_now.timestamp();
    let ts_now_str: String = ts_now.to_string(); 
    //println!("{}", ts_now_str);
    let first_num: &u32 = &ts_now_str[..2].parse::<u32>().unwrap();
    let second_num: &u32 = &ts_now_str[2..4].parse::<u32>().unwrap();
    let third_num: &u32 = &ts_now_str[4..6].parse::<u32>().unwrap();
    let fourth_num: &u32 = &ts_now_str[6..8].parse::<u32>().unwrap();
    let fiveth_num: &u32 = &ts_now_str[8..].parse::<u32>().unwrap();
    //println!("{first_num} {second_num} {third_num} {fourth_num} {fiveth_num}");
    //for num in (0..ts_now).step_by(100000000) {
    //    println!("{}", num)
    //}
    let date_num: u32 = (first_num + second_num + third_num 
        + fourth_num + fiveth_num) % 101;
    //println!("{date_num}");

    let mut vers_num: u32 = 0;
    let vers: String = os_info::get().version().to_string();
    for c in vers.chars() {
        if c.is_digit(10) == true {
            //println!("{c}")
            vers_num = vers_num + c.to_digit(10).unwrap();
        }
    }
    if vers_num >= 101 {
        vers_num = vers_num % 101;
    }

    return (date_num + vers_num) % 101;


}

fn main() {
   
    let num = generate_pseudorandom_number();
    println!("{num}") 

}