use chrono::{self, NaiveDate};
use chrono::Datelike;

fn friday_13th_exists(year: &str, month: &str) -> (NaiveDate, bool){
    
    let year: i32 = year.parse::<i32>().unwrap();
    let month: u32 = month.parse::<u32>().unwrap();
    let day: u32 = 13;
    let dt: NaiveDate = NaiveDate::from_ymd_opt(year, month, day).unwrap();
    let week_day: String = dt.weekday().to_string();
    let mut is_friday: bool = false;
    //println!("{}", week_day);
    if week_day == String::from("Fri") {
        is_friday = true;
    }
    //println!("{x:?}");
    return (dt, is_friday)
}

fn main() {

    let year: String = String::from("2023");
    let month: String = String::from("11");
    let result: (NaiveDate, bool) = friday_13th_exists(&year, &month);
    println!("{} is friday?: {}", result.0, result.1);
}