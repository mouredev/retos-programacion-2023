use std::{thread, time};

fn countdown_from(num: i16, secs: i16) {

    if num < 1 || secs < 1 {
        eprintln!("We need only positive integers greater than zero!");
        std::process::exit(1)
    }

    let secs = time::Duration::from_millis((secs as u64) * 1000);

    for iter in 0..num + 1{
        let n = num - iter;
        println!("{}", n);
        if n > 0 {
            thread::sleep(secs);
        } else {
            break;
        }
    }
}

fn main() {

    let num: i16 = 5;
    let secs: i16 = 1;
    countdown_from(num, secs)

}