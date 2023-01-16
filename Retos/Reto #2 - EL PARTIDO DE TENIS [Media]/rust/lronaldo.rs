struct Points {
    p1: u32,
    p2: u32
}

fn score_points2str(points: u32) -> &'static str {
    match points {
        0 => "Love",
        1 => "15",
        2 => "30",
        3 => "40",
        _ => "Ha ganado el"
    }
}

fn show_score_points(sc: &Points) {
    let p1_str = score_points2str(sc.p1);
    let p2_str = score_points2str(sc.p2);
    
    match (sc.p1, sc.p2) {
        (v, _) if v > 3 => println!("{} P1", p1_str),
        (_, v) if v > 3 => println!("{} P2", p1_str),
        _ => println!("{} - {}", p1_str, p2_str),
    }
}

fn show_score_deuce_or_more(sc: &Points) {
    if sc.p1 == sc.p2 {
        println!("Deuce");
    } else {
        let difference: u32;
        let player: &str;

        if sc.p1 > sc.p2 { 
            player = "P1";
            difference = sc.p1 - sc.p2; 
        } else { 
            player = "P2";
            difference = sc.p2 - sc.p1; 
        }

        let info_str = match difference {
            1 => "Ventaja",
            _ => "Ha ganado el"
        };
        println!("{} {}", info_str, player);
    }  
}

fn show_score(sc: &Points) {
    let total = sc.p1 + sc.p2;
    
    if total >= 6 { show_score_deuce_or_more(&sc); }
    else          { show_score_points(&sc); }
}

fn process_byte(prev_byte: u8, byte: u8, score: &mut Points) {
    match (prev_byte as char, byte as char) {
        ('P', '1') => { score.p1 += 1; show_score(score); },
        ('P', '2') => { score.p2 += 1; show_score(score); },
        _ => (),
    };
}

fn main() {
    use std::io::Read;

    let mut prev_byte = 0u8;
    let mut score = Points{ p1: 0, p2: 0 };

    let stdin = std::io::stdin();
    for next in stdin.bytes() {
        match next {
            Ok(byte) => { 
                process_byte(prev_byte, byte, &mut score);
                prev_byte = byte;
            },
            _ => (),
        };
    }
}
