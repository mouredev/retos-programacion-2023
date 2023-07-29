BEATINGS = {
    "✂️": ["📄", "🦎"],
    "📄": ["🗿", "🖖"],
    "🗿": ["✂️", "🦎"],
    "🦎": ["📄", "🖖"],
    "🖖": ["✂️", "🗿"]
}

def game(plays: list[tuple]) -> str:
    p1_points = 0
    p2_points = 0
    
    for play in plays:
        p1_play = play[0]
        p2_play = play[1]
        
        if p2_play in BEATINGS[p1_play]:
            p1_points += 1
        elif p1_play in BEATINGS[p2_play]:
            p2_points += 1
            
    if p1_points > p2_points:
        return "Player 1"
    elif p2_points > p1_points:
        return "Player 2"
    
    return "Empate"
            
    
if __name__ == "__main__":
    first_play = game(plays=[("🗿", "✂️"), ("✂️", "🗿"), ("📄", "✂️")])
    assert first_play == "Player 2"
    print(first_play)
    
    second_play = game(plays=[("🦎", "✂️"), ("🦎", "📄"), ("📄", "🖖"), ("✂️", "✂️")])
    assert second_play == "Player 1"
    print(second_play)
    
    third_play = game(plays=[("✂️", "🦎"), ("🗿", "🦎"), ("🗿", "🗿"), ("🗿", "🖖"), ("📄", "🦎")])
    assert third_play == "Empate"
    print(third_play)