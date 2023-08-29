def rps_winner(player1_move, player2_move):
    rules = {
        ("🗿", "✂️"): "Player 1",
        ("✂️", "📄"): "Player 1",
        ("📄", "🗿"): "Player 1",
        ("✂️", "🗿"): "Player 2",
        ("📄", "✂️"): "Player 2",
        ("🗿", "📄"): "Player 2",
    }
    
    if player1_move == player2_move:
        return "Tie"
    elif (player1_move, player2_move) in rules:
        return rules[(player1_move, player2_move)]
    else:
        return "Player 2"

def play_rps_game(game_moves):
    results = []
    
    for moves in game_moves:
        result = rps_winner(moves[0], moves[1])
        results.append(result)
    
    return results

# Ejemplo de entrada
game_moves = [("🗿", "✂️"), ("✂️", "🗿"), ("📄", "✂️")]
results = play_rps_game(game_moves)

for idx, result in enumerate(results):
    print(f"Juego {idx + 1}: {result}")
