wins_to = {
    '🗿' : ['✂️', '🦎'],
    '📄' : ['🖖', '🗿'],
    '✂️' : ['🦎', '📄'],
    '🦎' : ['🖖', '📄'],
    '🖖' : ['✂️', '🗿']
} 
def run_game(game):
    p1 = 0
    p2 = 0
    
    for i in game:
        option = (i[0], i[1])
        
        if option[0] == option[1]:
            print('Tie')
        elif option[1] in wins_to[option[0]]:
            p1 += 1
        elif option[0] in wins_to[option[1]]:
            p2 += 1
            
    if p1>p2:
        print('Player 1')
    elif p2>p1:
        print('Player 2')
    else:
        print('Tie')
            
    
   
    
if __name__ == '__main__':
    game =  [("🗿","✂️"), ("✂️","🗿"), ("📄","✂️")]
    run_game(game)