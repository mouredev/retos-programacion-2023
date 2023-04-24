rules = {
    '🗿' : '✂️🦎',
    '📄' : '🗿🖖',
    '✂️' : '📄🦎',
    '🦎' : '📄🖖',
    '🖖' : '🗿✂️'
}


def game_results(pairs):
    p1 = p2 = 0
    
    for pair in pairs:
        if pair[1] in rules[pair[0]]:
            p1 += 1
            continue
        elif pair[1] == pair[0]:
            continue
        p2 += 1
    
    return 'Player 1' if p1 > p2 else 'Player 2' if p2 > p1 else 'Tie'
