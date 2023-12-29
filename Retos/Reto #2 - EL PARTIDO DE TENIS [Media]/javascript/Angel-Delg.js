const validatePlayers = players => {
   return players.some(player =>  player !== "P1" && player !== "P2")
}

const tennisGame = (simulate )=> {
   const points = {
      0: 'love',
      1: 15,
      2: 30,
      3: 40,
      4: 50,
      6: 60,
   }

   const countersPointsToPlayers = {
      P1: 0,
      P2: 0
   }
   
   if(!(simulate instanceof Array)){
      console.error("Ohh no!! Something went wrong");
      return
   }

   if(validatePlayers(simulate)){
      console.error("Ohh no!! only p1 and p2, other doesn't works");
      return
   }

   simulate.forEach(( player ) => {
      if(player === "P1" || player === "P2"){
         countersPointsToPlayers[player]++
      }

      countersPointsToPlayers.P1 === countersPointsToPlayers.P2 
      ? console.log("Deuce") :
      (countersPointsToPlayers.P1 - countersPointsToPlayers.P2) >= 2
      ? console.log("Ventaja Player 1") :
      (countersPointsToPlayers.P2 - countersPointsToPlayers.P1) >= 2
      ? console.log("Ventaja Player 2")
      : console.log(`${points[countersPointsToPlayers.P1]} - ${points[countersPointsToPlayers.P2]}`);
   })

   if(countersPointsToPlayers.P1 > countersPointsToPlayers.P2){
      console.log("Winner Player 1")
   }
   else{
      console.log("Winner Player 2")
   }
}

tennisGame(["P1", "P1", "P2", "P2", "P1", "P2", "P1", "P1"])