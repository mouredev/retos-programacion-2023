fn check_primo(n: u32) -> String {
    if n == 1 {
        return "no es primo".to_string();
    }

    for i in 2..n {
        if n % i == 0 {
            return "no es primo".to_string();
        }
    }

    "es primo".to_string()
}

fn check_par(n: u32) -> String {
    if n % 2 == 0 {
        "es par".to_string()
    } else {
        "es impar".to_string()
    }
}

fn check_pefect_square(n: f64) -> bool {
    let square = n.sqrt().floor();
    return square * square == n;
}

fn check_fibonnacci(n: u32) -> String {
    let n = n as f64;
    let checker: f64 = 5.0 * n * n;

    if check_pefect_square(checker + 4.0) || check_pefect_square(checker - 4.0) {
        return "fibonnacci".to_string();
    } else {
        return "no es fibonnacci".to_string();
    }
}

fn main() {
    let numbers = vec![3, 4, 5, 8, 7, 10];

    for i in numbers {
        let primo = check_primo(i);
        let par = check_par(i);
        let fibonnacci = check_fibonnacci(i);
        println!("{}, {}, {} y {}", i, primo, fibonnacci, par);
    }
}
