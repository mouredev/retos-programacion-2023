const partidoTenis = (...points) => {
        let stateOne = "Love";
        let stateTwo = "Love";
        
        
        let playerOne = 0;
        let playerTwo = 0;
        
        
        for (let i = 0; i < points.length; i++) {
            if (points[i] !== "P2" && points[i] != "P1") {
                console.log("La entrada registrada de puntaje no es valida");
                continue;
            }
            

            const pointsOne = playerOne;
            const pointsTwo = playerTwo;
            
            
            
            if (points[i] === "P1") {
                playerOne += pointsOne == 30 ? 10 : 15;
                stateOne = playerOne > 40 ? "Ventaja P1" : playerOne.toString();
            } else if (points[i] === "P2") {
                playerTwo += pointsTwo == 30 ? 10 : 15;
                stateTwo = playerTwo > 40 ? "Ventaja P2" : playerTwo.toString();
            }  
            
            
            
            if (playerOne === playerTwo && playerTwo >= 40 && playerOne >= 40) {
                console.log("Deuce");
                continue;
            }
            
            if(points[i] === "P1" && pointsOne > 40) {
                if (playerOne - playerTwo >= 30) {
                    console.log("Ha ganado el P1");
                    return;
                }
                
                
                console.log(stateOne);
                continue;
                
            } else if (points[i] === "P2" && pointsTwo > 40) {
                if (playerTwo - playerOne >= 30) {
                    console.log("Ha ganado el P2");
                    return;
                }
                
                
                console.log(stateTwo);
                continue;
            }
            
            
            
            
            
            if (stateOne === "Ventaja P1" || stateTwo === "Ventaja P2") {
                console.log(stateOne === "Ventaja P1" ? "Ventaja P1" : "Ventaja P2");
                continue;
            }
            console.log(stateOne + " - " + stateTwo);
        }
    }



partidoTenis("P1", "P1", "P2", "P2", "P1", "P2", "P1", "P1");