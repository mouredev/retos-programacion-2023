def define_winner(matches):
    win_against = {
        'πΏ': 'βοΈπ¦',
        'π': 'πΏπ',
        'βοΈ': 'ππ¦',
        'π¦': 'ππ',
        'π': 'βοΈπΏ'
        }

    p1_score = 0
    p2_score = 0

    for match in matches:
        if(match[1] in win_against[match[0]]):
            p1_score += 1
        elif(match[0] in win_against[match[1]]):
            p2_score += 1
    
    if p1_score == p2_score:
        return 'Tie'
    elif p1_score > p2_score:
        return 'Player 1'
    elif p2_score > p1_score:
        return 'Player 2'


encounter = [("πΏ","βοΈ"), ("βοΈ","πΏ"), ("π","βοΈ"), ("π¦","π")]

print(define_winner(encounter))