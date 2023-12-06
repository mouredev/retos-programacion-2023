def main():
    print('\n\t\tPara salir escribe: salir\n\n')
    scoreList = []
    scoreP1 = 0
    scoreP2 = -1
    exitGame = ''
    puntuations = {
    '0': 'Love',
    '1': 15,
    '2': 30,
    '3': 40,
    '4': '40',
    '5': 'Ha ganado '
    }

    while(scoreP1 != 5 and scoreP2 != 5):        
        exitGame = str(input('Punto de: ')).upper()

        if(exitGame == 'P1'):                        
            scoreList.append(pointP1())
            scoreP1 = scoreList.count('P1')

            if(scoreP1 == 5):
                print('Ha ganado el P1')
                print(scoreList)
                break
            elif(scoreP1 == 4):
                if(scoreP1 == scoreP2):
                    print('Deuce')
                    scoreP2 -= 1
                print('Ventaja de P1')
            else:
                if(scoreP1 == scoreP2):
                    print('Deuce')
            print(updateScore(puntuations, scoreP1, scoreP2))

        elif(exitGame == 'P2'):
            scoreList.append(pointP2())
            scoreP2 = scoreList.count('P2')
            
            if(scoreP2 == 5):
                print('Ha ganado el P2')
                print(scoreList)
                break
            elif(scoreP2 == 4):
                if(scoreP2 == scoreP1):
                    print('Deuce')
                    scoreP1 -= 1
                print('Ventaja de P2')
            else:
                if(scoreP1 == scoreP2):
                    print('Deuce')                
            print(updateScore(puntuations, scoreP1, scoreP2))

        elif(exitGame == 'SALIR'):
            break
        else:
            print('Ingresa un jugador válido, o salir para salir')        

def pointP1():
    point = 'P1'
    return point

def pointP2():
    point = 'P2'
    return point

def updateScore(puntuations,scoreP1, scoreP2):
    currentP1 = puntuations.get(str(scoreP1))
    currentP2 = puntuations.get(str(scoreP2))

    if(currentP1 == None):
        currentP1 = 'Love'
    elif(currentP2 == None):
        currentP2 = 'Love'
    
    score = f'Puntaje Actual: {currentP1} | {currentP2}'
    return score

if __name__ == '__main__':
    main()