use std::error::Error;

// Defining the InvalidGame enum with possible errors
#[derive(Debug)]
pub enum InvalidGameError {
    InvalidPlayer(String),
    InvalidScore(i8, i8),
    UnfinishedGame,
    AlreadyEndedGame,
}

// Implementing the Display trait for InvalidGame
impl std::fmt::Display for InvalidGameError {
    fn fmt(&self, f: &mut std::fmt::Formatter<'_>) -> std::fmt::Result {
        match self {
            InvalidGameError::InvalidPlayer(input) => {
                write!(f, "Invalid player name {input} only P1 and P2 are allowed")
            }
            InvalidGameError::InvalidScore(a, b) => {
                write!(f, "Invalid Score P1: {a}, P2: {b} this will never happens")
            }
            InvalidGameError::UnfinishedGame => write!(
                f,
                "Game is not finished yet but there are not more points left"
            ),
            InvalidGameError::AlreadyEndedGame => {
                write!(f, "Game is already finished but there are more points left")
            }
        }
    }
}

// Implementing the Error trait for InvalidGame
impl std::error::Error for InvalidGameError {}

// Defining the Player enum
#[derive(PartialEq, Eq, Debug, Clone, Copy)]
pub enum Player {
    P1,
    P2,
}

// Defining the Game enum
enum Game {
    Score(i8, i8),
    Deuce,
    Advantage(Player),
    Game(Player),
}

// Implementing methods for Game enum
impl Game {
    // Method to create a new game
    fn new() -> Self {
        Self::Score(0, 0)
    }

    // Method to update the game state after a point is scored by a player
    fn point(self, player: Player) -> Result<Self, InvalidGameError> {
        use Player as P;
        match self {
            Self::Score(a, b) if a < 3 && b < 3 => match player {
                P::P1 => Ok(Self::Score(a + 1, b)),
                P::P2 => Ok(Self::Score(a, b + 1)),
            },
            Self::Score(2, 3) if player == P::P1 => Ok(Self::Deuce),
            Self::Score(3, 2) if player == P::P2 => Ok(Self::Deuce),
            Self::Score(a, b) if player == P::P1 && (a + 1) - b == 2 => Ok(Self::Game(P::P1)),
            Self::Score(a, b) if player == P::P2 && (b + 1) - a == 2 => Ok(Self::Game(P::P1)),
            Self::Deuce => Ok(Self::Advantage(player)),
            Self::Advantage(p) if p == player => Ok(Self::Game(p)),
            Self::Advantage(_) => Ok(Self::Deuce),
            Self::Score(a, b) => Err(InvalidGameError::InvalidScore(a, b)),
            Self::Game(_) => Err(InvalidGameError::AlreadyEndedGame),
        }
    }
}

fn format_points(a: i8) -> String {
    match a {
        0 => "Love".to_string(),
        1..=3 => format!("{}", (a * 15).min(40)),
        _ => panic!("This should never happening"),
    }
}

// Function to display the game state after each point
// The generic Output is used to facilitate testing by faking the output to a string,
// but the function is intended to be used with the standard input (stdin)
pub fn show_game<Output: std::io::Write>(
    points: &[Player],
    out: &mut Output,
) -> Result<(), Box<dyn Error>> {
    let mut game = Game::new();
    for player_point in points {
        match game {
            Game::Game(_) => Err(InvalidGameError::AlreadyEndedGame)?,
            _ => {}
        }
        game = game.point(*player_point)?;
        match game {
            Game::Score(a, b) => writeln!(out, "{} - {}", format_points(a), format_points(b)),
            Game::Deuce => writeln!(out, "Deuce"),
            Game::Advantage(p) => writeln!(out, "Ventaja {p:?}"),
            Game::Game(p) => writeln!(out, "Ha ganado el {p:?}"),
        }?;
    }
    match game {
        Game::Game(_) => Ok(()),
        _ => Err(InvalidGameError::UnfinishedGame)?,
    }
}

// Main function
pub fn main() -> Result<(), Box<dyn Error>> {
    use std::io::{self, BufRead};
    let stdin = io::stdin();
    let mut handle = stdin.lock();
    let mut buffer = String::new();
    handle.read_line(&mut buffer)?;
    let points: Result<Vec<Player>, InvalidGameError> = buffer
        .trim()
        .to_uppercase()
        .split(|c| c == ',' || c == ' ')
        .filter(|s| !s.is_empty())
        .map(|s| match s {
            "P1" => Ok(Player::P1),
            "P2" => Ok(Player::P2),
            _ => Err(InvalidGameError::InvalidPlayer(s.to_string())),
        })
        .collect();
    show_game(&points?, &mut io::stdout())
}

#[cfg(test)]
mod test {
    #[test]
    fn exercise_example() {
        use super::Player::*;
        let mut result = vec![];
        let mut cursor = std::io::Cursor::new(&mut result);
        let points = [P1, P1, P2, P2, P1, P2, P1, P1];
        match super::show_game(&points, &mut cursor) {
            Ok(_) => assert!(true),
            Err(err) => assert!(
                false,
                "The example should finish correctly with P1 Winning {err}"
            ),
        }
        assert_eq!(
            std::string::String::from_utf8(result),
            Ok(format!("15 - Love\n30 - Love\n30 - 15\n30 - 30\n40 - 30\nDeuce\nVentaja P1\nHa ganado el P1\n"))
        )
    }

    #[test]
    fn test_unfinished_game() {
        use super::Player::*;
        let mut result = vec![];
        let mut cursor = std::io::Cursor::new(&mut result);
        let points = [P1, P1];
        match super::show_game(&points, &mut cursor) {
            Ok(_) => assert!(false, "This test should fail with UnfinishedGame error"),
            Err(err) => assert_eq!(
                err.to_string(),
                "Game is not finished yet but there are not more points left"
            ),
        }
    }

    #[test]
    fn test_already_ended_game() {
        use super::Player::*;
        let mut result = vec![];
        let mut cursor = std::io::Cursor::new(&mut result);
        let points = [P1, P1, P2, P2, P1, P2, P1, P1, P1];
        match super::show_game(&points, &mut cursor) {
            Ok(_) => assert!(false, "This test should fail with AlreadyEndedGame error"),
            Err(err) => assert_eq!(
                err.to_string(),
                "Game is already finished but there are more points left"
            ),
        }
    }
}
