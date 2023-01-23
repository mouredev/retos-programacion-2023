fn tennis_match(points: Vec<String>) {
    let mut p1 = 0;
    let mut p2 = 0;
    let mut advantage = "";

    for point in points {
        if point == "P1" {
            if p1 == 30 && p1 < 46 {
                p1 = 40
            } else {
                p1 += 15;
            }
        } else if point == "P2" {
            if p2 == 30 && p2 < 46 {
                p2 = 40
            } else {
                p2 += 15;
            }
        } else {
            println!("Invalid point");
        }

        if p1 >= 40 && p2 >= 40 {
            if p1 == p2 {
                println!("Deuce");
            } else if p1 > p2 {
                if advantage == "P1" {
                    println!("P1 Wins");
                    break;
                }
                println!("P1 Advantage");
                advantage = "P1";
            } else {
                if advantage == "P2" {
                    println!("P2 Wins");
                    break;
                }
                println!("P2 Advantage");
                advantage = "P2";
            }
        } else if p1 > 40 {
            println!("P1 Wins");
            break;
        } else if p2 > 40 {
            println!("P2 Wins");
            break;
        } else {
            if p1 == 0 {
                println!("P1: Love - P2: {}", p1);
            } else if p2 == 0 {
                println!("P1: {} - P2: Love", p1);
            } else {
                println!("P1: {} - P2: {}", p1, p2);
            }
        }
    }
}

fn main() {
    let points = vec![
        String::from("P1"),
        String::from("P1"),
        String::from("P2"),
        String::from("P2"),
        String::from("P1"),
        String::from("P2"),
        String::from("P1"),
        String::from("P1"),
    ];

    tennis_match(points);
}
