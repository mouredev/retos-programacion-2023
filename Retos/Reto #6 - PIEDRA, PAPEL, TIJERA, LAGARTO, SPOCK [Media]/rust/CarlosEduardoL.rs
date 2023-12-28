use regex::Regex;
use std::env;

// Define an enum to represent the two players
#[derive(PartialEq, Eq, Debug)]
enum Player {
    Player1,
    Player2,
}

// Define an enum to represent the valid movements
#[derive(PartialEq, Eq)]
enum Movement {
    Rock,
    Paper,
    Scissors,
    Lizard,
    Spock,
}

impl Movement {
    // Define a function to convert a string into a Movement
    // This function catch user invalid movements
    fn from_str(s: &str) -> Option<Movement> {
        match s {
            "🗿" => Some(Movement::Rock),
            "✂️" => Some(Movement::Scissors),
            "📄" => Some(Movement::Paper),
            "🦎" => Some(Movement::Lizard),
            "🖖" => Some(Movement::Spock),
            _ => None,
        }
    }
}

// Define a struct to represent the game
struct Game {
    score: (u32, u32),
}

impl Game {
    // Define a function to play a single match and update the score
    fn play_match(&mut self, pair: (Movement, Movement)) {
        // Match the pair of moves and update the score accordingly
        match (pair.0, pair.1) {
            (Movement::Rock, Movement::Lizard)
            | (Movement::Rock, Movement::Scissors)
            | (Movement::Scissors, Movement::Lizard)
            | (Movement::Scissors, Movement::Paper)
            | (Movement::Paper, Movement::Spock)
            | (Movement::Paper, Movement::Rock)
            | (Movement::Lizard, Movement::Spock)
            | (Movement::Lizard, Movement::Paper)
            | (Movement::Spock, Movement::Scissors)
            | (Movement::Spock, Movement::Rock) => self.score.0 += 1,
            (a, b) if a == b => {}
            _ => self.score.1 += 1,
        }
    }

    // Define a function to determine the winner based on the final scores
    fn get_winner(&self) -> Option<Player> {
        if self.score.0 > self.score.1 {
            Some(Player::Player1)
        } else if self.score.0 < self.score.1 {
            Some(Player::Player2)
        } else {
            None
        }
    }
}

pub fn main() -> Result<(), Box<dyn std::error::Error>> {
    // Read input from first console argument
    let args: Vec<String> = env::args().collect();
    let input = if args.len() > 1 {
        args[1].to_string()
    } else {
        println!(r#"Please provide an input in the following format: '[("🗿","✂️"), ("✂️","🗿"), ("📄","✂️")]'."#);
        return Ok(());
    };
    
    let input = parse_input(&input)?;
    let mut game = Game { score: (0, 0) };

    for pair in input {
        game.play_match(pair);
    }

    let winner = game.get_winner();
    
    match winner {
        Some(Player::Player1) => println!("Player 1"),
        Some(Player::Player2) => println!("Player 2"),
        None => println!("Tie"),
    }

    Ok(())
}

// Define a function to parse the input string into a vector of matches
fn parse_input<'a>(input: &str) -> Result<Vec<(Movement, Movement)>, Box<dyn std::error::Error>> {
    // Define a regular expression to match pairs of moves in the input string
    let re = Regex::new(r#"\(\s*"([^"]*)"\s*,\s*"([^"]*)"\s*\)"#)?;
    
    // Initialize an empty vector to store the matches
    let mut result = Vec::new();
    
    // Iterate over each capture in the input string and add it to the result vector
    for cap in re.captures_iter(input) {
        let move1 = cap[1].to_string();
        let move2 = cap[2].to_string();
        
        // Use pattern matching to handle the case where an invalid move is detected
        match (Movement::from_str(&move1), Movement::from_str(&move2)) {
            (Some(a), Some(b)) => result.push((a, b)),
            _ => return Err("Invalid move detected".into()),
        }
    }
    
    Ok(result)
}

#[cfg(test)]
mod test {
    use super::Movement::*;

    #[test]
    fn winner_p1() {
        let mut game = super::Game { score: (0, 0) };
        let matches = [(Spock, Rock), (Spock, Lizard), (Rock, Lizard)];
        for pair in matches {game.play_match(pair)}
        assert_eq!(game.get_winner(), Some(super::Player::Player1));
    }

    #[test]
    fn winner_p2() {
        let mut game = super::Game { score: (0, 0) };
        let matches = [(Spock, Rock), (Spock, Lizard), (Rock, Spock)];
        for pair in matches {game.play_match(pair)}
        assert_eq!(game.get_winner(), Some(super::Player::Player2));
    }

    #[test]
    fn tie() {
        let mut game = super::Game { score: (0, 0) };
        let matches = [(Spock, Rock), (Spock, Lizard), (Rock, Rock)];
        for pair in matches {game.play_match(pair)}
        assert_eq!(game.get_winner(), None);
    }
}