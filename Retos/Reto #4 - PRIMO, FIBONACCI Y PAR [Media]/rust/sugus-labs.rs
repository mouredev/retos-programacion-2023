fn test_math_chars(num: usize) {
    
    // Generate password function

    fn is_even(num: usize) -> bool {
        return num % 2 == 0
    }
    
    fn is_prime(num: usize) -> bool {
        let mut is_prime: bool = true;
        for n in 2..num {
            if num % n == 0 {
                is_prime = false;
                break
            }
        }
        return is_prime
    }

    fn is_fibonacci(num: usize) -> bool {
        let mut last_num: usize = 0;
        let mut curr_num: usize = 1;
        let mut fibo_num: usize = 0;
        let mut fibo_list: Vec<usize> = vec![0, 1];
        while curr_num < num {
            fibo_num = curr_num + last_num;
            fibo_list.push(fibo_num);
            last_num = curr_num;
            curr_num = fibo_num ;    
        }       
        //println!("{:?}", fibo_list);
        return fibo_list.iter().any(|&i| i == num)
    }


    let even: bool = is_even(num);
    let prime: bool = is_prime(num);
    let fibo: bool = is_fibonacci(num);

    println!("The number {num}\n- even: {even}\n- prime: {prime}\n- fibo: {fibo}")

}

fn main() {

    test_math_chars(13);

}