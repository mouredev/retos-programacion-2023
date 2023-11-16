def main():
    print('PIEDRA, PAPEL, TIJERA, LAGARTO, SPOCK')
    rockWin = ['lagarto', 'tijera']
    paperWin = ['piedra', 'spock']
    scissorsWin = ['papel', 'lagarto']
    lizzardWin = ['spock', 'papel']
    spockWin = ['piedra','tijera']
    playLog = []
    for x in range(1,4):
        print(f'RONDA {x}')
        fPlayerInput = str(input('Player 1 plays: ')).lower
        sPlayerInput = str(input('Player 2 plays: ')).lower
        result = 0
        fPlayerScore = 0
        sPlayerScore = 0

        if(fPlayerInput == sPlayerInput):
            result = 'Tie'
        # Piedra if
        elif(fPlayerInput == 'piedra'):
            if(sPlayerInput in rockWin):
                result = 1
            else:
                result = 2
        # Papel if
        elif(fPlayerInput == 'papel'):
            if(sPlayerInput in paperWin):
                result = 1
            else:
                result = 2
        # Tijera if
        elif(fPlayerInput == 'tijera'):
            if(sPlayerInput in scissorsWin):
                result = 1
            else:
                result = 2
        # Lagarto if
        elif(fPlayerInput == 'lagarto'):
            if(sPlayerInput in lizzardWin):
                result = 1
            else:
                result = 2
        # Spock if
        elif(fPlayerInput == 'spock'):
            if(sPlayerInput in spockWin):
                result = 1
            else:
                result = 2
        # First Player Score
        if(result == 1):
            fPlayerScore += 1
        # Second Player Score
        if(result == 2):
            sPlayerScore += 1
        playLog.append(result)
    if(fPlayerScore == sPlayerScore):
        winner = 'Tie'
    elif(fPlayerScore > sPlayerScore):
        winner = 'Player 1'
    else:
        winner = 'Player 2'
    print(f'Resultado: {winner}')

if __name__ == '__main__':
    main()