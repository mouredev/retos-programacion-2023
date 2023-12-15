const TicTacToe = (stepGame) => {
   if (!(stepGame instanceof Array)) {
      console.error("Ohh no!! Something went wrong");
      return;
   }

   const counterPointsToPlayers = {
      P1: 0,
      P2: 0
   };

   const rules = {
      "lacoste": ["spock", "paper"],
      "rook": ["lacoste", "scissors"],
      "scissors": ["paper", "lacoste"],
      "spock": ["scissors", "rook"],
      "paper": ["rook", "spock"]
   };

   stepGame.forEach((array) => {
      if (array[0] === array[1]) {
         return;
      }

      if (rules[array[0]] && rules[array[0]].includes(array[1])) {
         counterPointsToPlayers.P1++;
      } else {
         counterPointsToPlayers.P2++;
      }
   });

   if (counterPointsToPlayers.P1 === counterPointsToPlayers.P2) {
      console.log("Empate");
   } else if (counterPointsToPlayers.P1 > counterPointsToPlayers.P2) {
      console.log("Gano Player 1");
   } else {
      console.log("Gano Player 2");
   }
};

TicTacToe([["lacoste", "paper"], ["paper", "rook"], ["lacoste", "lacoste"], ["paper", "scissors"], ["scissors", "rook"], ["paper", "scissors"]]);