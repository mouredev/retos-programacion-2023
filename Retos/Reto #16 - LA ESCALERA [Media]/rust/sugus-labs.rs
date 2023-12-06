fn create_stair_to(floor: i32) {

    let space_str: String = String::from(" ");

    if floor == 0 {
        println!("__");
    }
    else if floor > 0 {
        let mut correct_num = 0;
        let mut f: String = space_str.repeat((floor as usize) * 2);
        println!("{}_", f); 
        for num in 0..floor {
            correct_num = floor - (num + 1);
            f = space_str.repeat((correct_num as usize) * 2);
            println!("{}_|", f)
        }
    }
    else {
        let mut f: String = String::new();
        println!("_");
        for num in 0..-floor {
            f = space_str.repeat(((num as usize) * 2) + 1);
            println!("{}|_", f)
        }
    }
}

fn main() {

    let floor: i32 = -4;
    create_stair_to(floor);
}