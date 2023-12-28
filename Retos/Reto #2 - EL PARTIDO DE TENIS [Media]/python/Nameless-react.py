def partidoTenis (*points):
        stateOne = "Love"
        stateTwo = "Love"
        
        
        playerOne = 0
        playerTwo = 0
        
        
        for point in points:
            if (point != "P2" and point != "P1"):
                print("La entrada registrada de puntaje no es valida")
                continue
            

            pointsOne = playerOne
            pointsTwo = playerTwo
            
            
            
            if (point == "P1"):
                playerOne +=  10 if pointsOne == 30 else 15
                stateOne = "Ventaja P1" if playerOne > 40 else str(playerOne)
            elif (point == "P2"):
                playerTwo +=  10 if pointsTwo == 30 else 15
                stateTwo =  "Ventaja P2" if playerTwo > 40 else str(playerTwo)
            
            
            
            
            if (playerOne == playerTwo and playerTwo >= 40 and playerOne >= 40):
                print("Deuce")
                continue
            
            
            if(point == "P1" and pointsOne > 40):
                if (playerOne - playerTwo >= 30):
                    print("Ha ganado el P1")
                    return
                
                
                
                print(stateOne)
                continue
                
            elif (point == "P2" and pointsTwo > 40):
                if (playerTwo - playerOne >= 30):
                    print("Ha ganado el P2")
                    return
                
                
                
                print(stateTwo)
                continue
            
            
            
            
            
            if (stateOne == "Ventaja P1" or stateTwo == "Ventaja P2"):
                print("Ventaja P1" if stateOne == "Ventaja P1" else "Ventaja P2")
                continue
            
            print(stateOne + " - " + stateTwo)



partidoTenis("P1", "P1", "P2", "P2", "P1", "P2", "P1", "P1")