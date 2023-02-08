use std::{io, mem};

fn main() {
    let testing_number = spanish_imput_parser();
    let formatted_message = spanish_formatter(testing_number, check_all(&testing_number));
    println!("{}", formatted_message);
}

fn check_if_fibonnacci(testing_number: &usize) -> Option<usize> {
    // be aware that Fn is not invertible at Fn = 1. F^-1[1] = {1,2}
    let mut second_last_fibo: usize = 0;
    let mut last_fibo: usize = 1;
    let mut second_last_index: usize = 0;
    while *testing_number >= last_fibo {
        mem::swap(&mut second_last_fibo, &mut last_fibo);
        last_fibo = second_last_fibo + last_fibo;
        second_last_index += 1;
    }
    if second_last_fibo == *testing_number {
        return Some(second_last_index);
    } else {
        return None;
    }
}

fn check_if_prime(testing_odd_number: &usize) -> bool {
    assert!(*testing_odd_number > 2);
    let max_possible_divisors = (*testing_odd_number as f64).sqrt() as usize;
    let mut divisors: Vec<usize> = (3..max_possible_divisors).step_by(2).collect();
    while divisors.len() > 0 {
        let checking = divisors[0];
        if testing_odd_number % checking == 0 {
            return false;
        } else {
            divisors = divisors.into_iter().filter(|x| x % checking != 0).collect();
        }
    }
    return true;
}

fn check_all(testing_number: &usize) -> [bool; 3] {
    let is_odd = {
        if testing_number % 2 != 0 {
            true
        } else {
            false
        }
    };

    let is_prime = {
        if *testing_number == 1 {
            false
        } else if *testing_number == 2 {
            true
        } else if !is_odd {
            false
        } else {
            check_if_prime(testing_number)
        }
    };

    let is_fibonacci = match check_if_fibonnacci(testing_number) {
        Some(_) => true,
        None => false,
    };

    return [is_prime, is_fibonacci, is_odd];
}

fn spanish_formatter(testing_number: usize, result: [bool; 3]) -> String {
    let prime = {
        if result[0] {
            "es primo"
        } else {
            "no es primo"
        }
    };

    let fibonacci = {
        if result[1] {
            "es fibonacci"
        } else {
            "no es fibonacci"
        }
    };

    let parity = {
        if result[2] {
            "impar"
        } else {
            "par"
        }
    };

    format!("{testing_number} {prime}, {fibonacci} y es {parity}")
}

fn spanish_imput_parser() -> usize {
    println!(
        "\nPor favor ingresa un numero entero POSITIVO menor a {}:\n",
        usize::MAX
    );
    let mut input = String::new();
    io::stdin()
        .read_line(&mut input)
        .expect("Error al leer la linea.");

    input
        .trim()
        .parse()
        .expect("POR FAVOR INGRESAR UN NUMERO ENTERO POSITIVO.\n")
}

#[test]
fn test_if_fibonacci() {
    assert_eq!(None, check_if_fibonnacci(&832045));
    assert_eq!(None, check_if_fibonnacci(&24157819));
    assert_eq!(3, check_if_fibonnacci(&2).unwrap());
    assert_eq!(4, check_if_fibonnacci(&3).unwrap());
    assert_eq!(29, check_if_fibonnacci(&514229).unwrap()); // prime
    assert_eq!(40, check_if_fibonnacci(&102334155).unwrap()); // no prime
    assert_eq!(46, check_if_fibonnacci(&1836311903).unwrap()); // no prime
    assert_eq!(47, check_if_fibonnacci(&2971215073).unwrap()); //prime
}

#[test]
fn test_if_prime() {
    assert_eq!(true, check_if_prime(&3)); // fibo
    assert_eq!(false, check_if_prime(&832045)); // no fibo
    assert_eq!(false, check_if_prime(&24157819)); // no fibo
    assert_eq!(true, check_if_prime(&514229)); // fibo
    assert_eq!(false, check_if_prime(&102334155)); // fibo
    assert_eq!(true, check_if_prime(&2971215073)); // fibo
    assert_eq!(true, check_if_prime(&3657500101)); // fibo
}

#[test]
fn test_check_all() {
    // [is_prime, is_fibonacci, is_odd];
    assert_eq!([true, true, true], check_all(&514229)); // prime, fibonacci, odd: &514229
    assert_eq!([false, false, true], check_all(&832045)); // no prime, no fibonacci, odd &832045
    assert_eq!([false, true, false], check_all(&14930352)); // no prime, is fibonacci, even &14930352
}

#[test]
fn test_formatter() {
    // Con el número 2, nos dirá: "2 es primo, fibonacci y es par"
    assert_eq!(
        "2 es primo, es fibonacci y es par",
        spanish_formatter(2, check_all(&2))
    );
    // Con el número 7, nos dirá: "7 es primo, no es fibonacci y es impar"
    assert_eq!(
        "7 es primo, no es fibonacci y es impar",
        spanish_formatter(7, check_all(&7))
    );

    assert_eq!(
        "1 no es primo, es fibonacci y es impar",
        spanish_formatter(1, check_all(&1))
    );

    assert_eq!(
        "14930352 no es primo, es fibonacci y es par",
        spanish_formatter(14930352, check_all(&14930352))
    )
}
  
