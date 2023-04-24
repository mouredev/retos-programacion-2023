#[derive(Debug, Default)]
struct Player {
    index: i32,
}
#[derive(Debug, Default)]
struct Game {
    p1: Player,
    p2: Player,
    puntuacion: Vec<i32>,
    finished: bool,
}

impl Game {
    fn new() -> Self {
        Self::default()
    }
    fn ronda(&mut self, player: &str) {
        match player {
            "P1" => self.p1.index += 1,
            "P2" => self.p2.index += 1,
            _ => println!("Error no valid player"),
        }

        if self.p1.index >= 3 && self.p2.index >= 3 {
            let p1_state = self.p1.index;
            let p2_state = self.p2.index;
            let diff = p1_state - p2_state;
            if diff == 0 {
                println!("Deuce");
            } else if diff == 1 {
                println!("Ventaja P1");
            } else if diff == -1 {
                println!("Ventaja P2");
            } else if diff >= 2 {
                println!("Ha ganado P1");
                self.finished = true;
            } else {
                println!("Ha ganado P2");
                self.finished = true;
            }
        } else {
            let mut p1_state = self.puntuacion[self.p1.index as usize].to_string();
            let mut p2_state = self.puntuacion[self.p2.index as usize].to_string();

            if &p1_state == "0" {
                p1_state = "Love".to_string();
            }
            if &p2_state == "0" {
                p2_state = "Love".to_string();
            }

            println!("{} - {}", p1_state, p2_state);
        }
    }
}

fn main() {
    let sequencia = vec!["P1", "P1", "P2", "P2", "P1", "P2", "P1", "P1"];
    let mut game = Game::new();
    game.puntuacion = vec![0, 15, 30, 40];
    for s in sequencia {
        if game.finished {
            break;
        }
        game.ronda(s);
    }
}
