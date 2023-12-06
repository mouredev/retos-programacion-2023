fn draw_triforce(num: usize) {

    let num_rows: usize = num;
    let step = 2;
    let big_row = (step * num) - 1;
    let mut num_vec: Vec<usize> = vec![];
    let mut num_stars: usize = 1;
    for n in 1..(big_row + step) {
        //println!("{}", num_stars);
        if num_stars <= big_row {
            num_vec.push(num_stars);
            num_stars = num_stars + step;
        } else {
            break;
        }
    }
    let mut padding_num: usize = 0;
    let mut curr_num: usize = 0;
    let mut padding_str: String = String::new();
    let mut stars_str: String = String::new();
    //println!("{:?}", num_vec);

    for iter in 0..num_rows {
        padding_num = ((num_vec[num - 1] - num_vec[iter]) / 2) as usize;
        curr_num = num_vec[iter];
        padding_str = " ".repeat(padding_num + num);
        stars_str = "*".repeat(curr_num);
        println!("{padding_str}{stars_str}{padding_str}")
    }
    for iter in 0..num_rows {
        padding_num = ((num_vec[num - 1] - num_vec[iter]) / 2) as usize;
        curr_num = num_vec[iter];
        padding_str = " ".repeat(padding_num);
        stars_str = "*".repeat(curr_num);
        println!("{padding_str}{stars_str}{padding_str} {padding_str}{stars_str}{padding_str}")
    }
}

fn main() {

    let num: usize = 4;
    draw_triforce(num);

}