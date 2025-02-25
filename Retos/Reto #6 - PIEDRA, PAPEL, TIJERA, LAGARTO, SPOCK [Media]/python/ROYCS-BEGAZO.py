def spsls(games):
    pl1 = 0
    pl2 = 0

    d_rules =   {"🗿": ["✂️", "🦎"],
                "📄": ["🗿", "🖖"],
                "✂️": ["📄", "🦎"],
                "🦎": ["🖖", "📄"],
                "🖖": ["🗿", "✂️"]}

    for game in games:
        pl1_game = game[0]
        pl2_game = game[1]
        if pl1_game == pl2_game:
            pass
        if pl2_game in d_rules[pl1_game]:
            pl1 += 1
        else:
            pl2 += 1
    if pl1 == pl2:
        return 'Tie'
    elif pl1 > pl2:
        return f'ganador player1 {pl1}pts'
    else:
        return f'ganador player2 {pl2}pts'
print(spsls([("🗿","✂️"), ("✂️","🗿"), ("📄","✂️")]))