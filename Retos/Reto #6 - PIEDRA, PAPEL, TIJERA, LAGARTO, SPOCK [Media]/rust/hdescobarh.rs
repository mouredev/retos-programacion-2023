// Rock, paper, scissors, lizard, spock game!
use std::{collections::HashMap, io};

fn main() {
    let mut game = Game::new();
    let rounds_list = parser();
    game.check_all_rounds(rounds_list);
    formatter(game.get_winner());
}

#[derive(PartialEq, Eq, Debug)]
enum Winner {
    Player1,
    Player2,
    Draw,
}

struct Game<'a> {
    rules: HashMap<&'a str, [&'a str; 2]>,
    player1_score: usize,
    player2_score: usize,
}

impl Game<'static> {
    pub fn new() -> Self {
        Self {
            rules: HashMap::from([
                ("🦎", ["🖖", "📄"]),
                ("🖖", ["✂️", "🗿"]),
                ("✂️", ["🦎", "📄"]),
                ("📄", ["🖖", "🗿"]),
                ("🗿", ["🦎", "✂️"]),
            ]),
            player1_score: 0,
            player2_score: 0,
        }
    }

    fn check_single_round(&mut self, player1_play: &str, player2_play: &str) {
        if self
            .rules
            .get(player1_play)
            .unwrap()
            .contains(&player2_play)
        {
            self.player1_score += 1;
        } else if self
            .rules
            .get(player2_play)
            .unwrap()
            .contains(&player1_play)
        {
            self.player2_score += 1;
        }
    }

    pub fn check_all_rounds(&mut self, rounds_list: Vec<Vec<String>>) {
        for pair in rounds_list.iter() {
            let player1_play = pair.get(0).unwrap();
            let player2_play = pair.get(1).unwrap();
            self.check_single_round(player1_play, player2_play);
        }
    }

    pub fn get_winner(&self) -> Winner {
        if self.player1_score > self.player2_score {
            Winner::Player1
        } else if self.player2_score > self.player1_score {
            Winner::Player2
        } else {
            Winner::Draw
        }
    }
}

fn formatter(winner: Winner) {
    let player = match winner {
        Winner::Player1 => "Player 1",
        Winner::Player2 => "Player 2",
        Winner::Draw => "Tie",
    };
    println!("Winner: {}", player);
}

fn parser() -> Vec<Vec<String>> {
    println!("Please insert a non-empty list of rounds.\nExample\n[(\"🗿\",\"✂️\"), (\"✂️\",\"🗿\"), (\"📄\",\"✂️\")]\n");

    let mut input = String::new();
    io::stdin()
        .read_line(&mut input)
        .expect("Error while reading line");

    let input_list = input
        .trim()
        .split(&['[', ']', ',', '(', ')', '"'])
        .filter(|s| ["🦎", "🖖", "✂️", "📄", "🗿"].contains(s))
        .collect::<Vec<&str>>();

    let mut result: Vec<Vec<String>> = Vec::new();

    if input_list.len() != 0 && input_list.len() % 2 == 0 {
        for index in (0..input_list.len()).step_by(2) {
            result.push(vec![
                input_list[index].to_string(),
                input_list[index + 1].to_string(),
            ])
        }
    } else {
        panic!("No valid input. Input must be a non-empty list with the following format: \n[(\"🗿\",\"✂️\"), (\"✂️\",\"🗿\"), (\"📄\",\"✂️\")]");
    }

    result
}

#[cfg(test)]
mod tests {
    use crate::{Game, Winner};

    #[test]
    fn check_a_single_match() {
        let mut game = Game::new();
        let test_rounds_list = [["🖖", "🗿"]]
            .iter()
            .map(|pair| vec![pair[0].to_string(), pair[1].to_string()])
            .collect::<Vec<Vec<String>>>();
        game.check_all_rounds(test_rounds_list);
        assert_eq!(Winner::Player1, game.get_winner());
    }

    #[test]
    fn check_player2_wins() {
        //  Ejemplo. Entrada: [("🗿","✂️"), ("✂️","🗿"), ("📄","✂️")]. Resultado: "Player 2".
        let mut game = Game::new();
        let test_rounds_list = [["🗿", "✂️"], ["✂️", "🗿"], ["📄", "✂️"]]
            .iter()
            .map(|pair| vec![pair[0].to_string(), pair[1].to_string()])
            .collect::<Vec<Vec<String>>>();
        game.check_all_rounds(test_rounds_list);
        assert_eq!(Winner::Player2, game.get_winner());
    }

    #[test]
    fn check_draw() {
        let mut game = Game::new();
        let test_rounds_list = [["🦎", "🖖"], ["🗿", "📄"]]
            .iter()
            .map(|pair| vec![pair[0].to_string(), pair[1].to_string()])
            .collect::<Vec<Vec<String>>>();
        game.check_all_rounds(test_rounds_list);
        assert_eq!(Winner::Draw, game.get_winner());
    }

    #[test]
    fn check_player1_wins() {
        let mut game = Game::new();
        let test_rounds_list = [
            ["🦎", "🖖"],
            ["🗿", "✂️"],
            ["🗿", "📄"],
            ["🖖", "✂️"],
            ["🖖", "📄"],
        ]
        .iter()
        .map(|pair| vec![pair[0].to_string(), pair[1].to_string()])
        .collect::<Vec<Vec<String>>>();
        game.check_all_rounds(test_rounds_list);
        assert_eq!(Winner::Player1, game.get_winner());
    }
}
