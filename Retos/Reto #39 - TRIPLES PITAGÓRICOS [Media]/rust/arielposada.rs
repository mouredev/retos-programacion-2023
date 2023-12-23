fn find_pythagorean_triples(max: i32) -> Vec<(i32, i32, i32)> {
    let mut r = Vec::new();
    for i in 1..=max {
        for j in i..=max {
            for k in j..=max {
                if i*i + j*j == k*k {
                    r.push((i, j, k));
                }
            }
        }
    }
    r
}

fn main() {
    let max = 10;
    let r = find_pythagorean_triples(max);
    println!("{:?}", r);
}
