fn is_prime(num: i32) -> bool {
    if num == 2 {
        return true;
    }
    if num < 2 || is_even(num) {
        return false;
    }
    for n in (3..num).step_by(2) {
        if num % n == 0 {
            return false;
        }
    }
    return true;
}

fn is_fibonacci(number: i32) -> bool {
    let x = 5 * number.pow(2);
    let psr = f64::sqrt((x + 4) as f64);
    let nsr = f64::sqrt((x - 4) as f64);
    if psr == psr.floor() {
        return true;
    } else if nsr == nsr.floor() {
        return true;
    }
    return false;
}

fn is_even(num: i32) -> bool {
    let res: bool;
    if num % 2 == 0 {
        res = true;
    } else {
        res = false;
    };
    return res;
}

fn pfe(num: i32) {
    let prime: &str;
    let fibo: &str;
    let even: &str;
    if is_prime(num) {
        prime = "es primo";
    } else {
        prime = "no es primo";
    }

    if is_fibonacci(num) {
        fibo = "fibonacci";
    } else {
        fibo = "no es fibonacci";
    }

    if is_even(num) {
        even = "es par";
    } else {
        even = "es impar";
    }

    println!("{} {}, {} y {}", num, prime, fibo, even);
}

fn main() {
    pfe(2);
    pfe(7);
}
