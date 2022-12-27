
fn main() {
    for num in 1..=100{
        if num%3==0 && num %5==0{
         println!("{} - fizzbuzz",num);
        }else if num%3 == 0{
         println!("{} - fizz",num);
        }else if num%5==0{
         println!("{} - buzz",num);
        }else{
         println!("{}",num);
        }
    }
}
