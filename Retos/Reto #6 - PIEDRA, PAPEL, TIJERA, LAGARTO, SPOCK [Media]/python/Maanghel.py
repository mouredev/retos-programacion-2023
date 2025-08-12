"""
Crea un programa que calcule quien gana más partidas al piedra,
    papel, tijera, lagarto, spock.
- El resultado puede ser: "Player 1", "Player 2", "Tie" (empate)
- La función recibe un listado que contiene pares, representando cada jugada.
- El par puede contener combinaciones de "🗿" (piedra), "📄" (papel),
    "✂️" (tijera), "🦎" (lagarto) o "🖖" (spock).
- Ejemplo. Entrada: [("🗿","✂️"), ("✂️","🗿"), ("📄","✂️")]. Resultado: "Player 2".
- Debes buscar información sobre cómo se juega con estas 5 posibilidades.
"""

from typing import List, Tuple, Literal

Move = Literal["🗿", "📄", "✂️", "🦎", "🖖"]
Result = Literal["Player 1", "Player 2", "Tie", "Invalid Input"]

def validate_game(game: List[Tuple[Move, Move]]) -> bool:
    """
    Validates that all rounds contain only valid moves.

    Parameters:
        game (List[Tuple[Move, Move]]): 
            A list of tuples, each containing the moves for Player 1 and Player 2.

    Returns:
        bool: True if all moves are valid, False otherwise.
    """
    valid_moves = {"🗿", "📄", "✂️", "🦎", "🖖"}
    return all(p1 in valid_moves and p2 in valid_moves for p1, p2 in game)


def winner(p1: Move, p2: Move) -> int:
    """
    Determines the winner of a single round.

    Parameters:
        p1 (Move): Move chosen by Player 1.
        p2 (Move): Move chosen by Player 2.

    Returns:
        int:
            0 -> Tie
            1 -> Player 1 wins
            2 -> Player 2 wins
    """
    win_rules = {
            "🗿": ["✂️", "🦎"],
            "📄": ["🗿", "🖖"],
            "✂️": ["📄", "🦎"],
            "🦎": ["🖖", "📄"],
            "🖖": ["🗿", "✂️"]
            }
    if p1 == p2:
        return 0
    elif p2 in win_rules[p1]:
        return 1
    else:
        return 2


def rock_paper_scissors_lizard_spock(game: List[Tuple[Move, Move]]) -> Result:
    """
    Determines the overall winner of a Rock, Paper, Scissors, Lizard, Spock game.

    Parameters:
        game (List[Tuple[Move, Move]]):
            List of tuples with moves for Player 1 and Player 2.

    Returns:
        Result: "Player 1", "Player 2", "Tie", or "Invalid Input".
    """
    if not validate_game(game):
        return "Invalid Input"

    if not game:
        return "Invalid Input"

    p1_score = p2_score = 0

    for p1, p2 in game:
        result = winner(p1, p2)
        if result == 1:
            p1_score += 1
        elif result == 2:
            p2_score += 1

    if p1_score > p2_score:
        return "Player 1"
    elif p2_score > p1_score:
        return "Player 2"
    else:
        return "Tie"


if __name__ == "__main__":
    plays: List[Tuple[Move, Move]] = [("🗿","✂️"), ("✂️","🗿"), ("📄","✂️")]
    result = rock_paper_scissors_lizard_spock(plays)
    print(f"Resultado del juego: {result}")
