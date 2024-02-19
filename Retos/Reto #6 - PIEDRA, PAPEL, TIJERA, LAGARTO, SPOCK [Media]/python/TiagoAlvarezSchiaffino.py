def rock_paper_scissors_lizard_spock(games):
    """
    Determine the winner based on the rules of rock, paper, scissors, lizard, Spock.
    
    Args:
        games (list): List of pairs representing each play.
        
    Returns:
        str: The winner ("Player 1", "Player 2", or "Tie").
    """
    rules = {"🗿": ["✂️", "🦎"],
             "📄": ["🗿", "🖖"],
             "✂️": ["📄", "🦎"],
             "🦎": ["🖖", "📄"],
             "🖖": ["🗿", "✂️"]}

    player_one = 0
    player_two = 0

    for match in games:
        player_one_match = match[0]
        player_two_match = match[1]
        if player_one_match != player_two_match:
            if player_two_match in rules[player_one_match]:
                player_one += 1
            else:
                player_two += 1

    return "Tie" if player_one == player_two else "Player 1" if player_one > player_two else "Player 2"

# Test cases
print(rock_paper_scissors_lizard_spock([("🗿", "🗿")]))
print(rock_paper_scissors_lizard_spock([("🗿", "✂️")]))
print(rock_paper_scissors_lizard_spock([("✂️", "🗿")]))
print(rock_paper_scissors_lizard_spock([("🗿", "🗿"), ("🗿", "🗿"), ("🗿", "🗿"), ("🗿", "🗿")]))
print(rock_paper_scissors_lizard_spock([("🖖", "🗿"), ("✂️", "📄"), ("🗿", "🗿"), ("🦎", "🖖")]))
