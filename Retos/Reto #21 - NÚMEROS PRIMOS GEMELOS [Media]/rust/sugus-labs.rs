fn twin_primes(num_max: usize) -> Vec<(usize, usize)> {

    let mut is_prime: bool = true;
    let mut prime_vec: Vec<usize> = vec![];
    let mut twin_prime_vec: Vec<(usize, usize)> = vec![];
    
    for num in 2..num_max {
        is_prime = true;
        for pos in 2..num {
            if num % pos == 0 {
                is_prime = false;
                break;
            }
        }
        if is_prime {
            prime_vec.push(num)
        }
    }
    //println!("{:?}", prime_vec);

    for iter in 0..prime_vec.len() {
        if iter < prime_vec.len() - 1 {
            if prime_vec[iter + 1] - prime_vec[iter] == 2 {
                twin_prime_vec.push((prime_vec[iter], prime_vec[iter + 1]));  
            }  
        }
    }

    return twin_prime_vec;
}

fn main() {

    let num_max: usize = 14;
    let twin_prime_vec = twin_primes(num_max);
    println!("{:?}", twin_prime_vec);

}