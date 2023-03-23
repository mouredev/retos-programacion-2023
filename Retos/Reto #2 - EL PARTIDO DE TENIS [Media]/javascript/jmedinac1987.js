function tenis(arrayPoints) {
    let points = { 0: "Love", 1: 15, 2: 30, 3: 40 };
    let response = [];
    let pointsPlayer1 = 0;
    let pointsPlayer2 = 0;
  
    for (let i = 0, j = arrayPoints.length; i < j; i++) {
      if (arrayPoints[i] === "P1") {
        pointsPlayer1 += 1;
        
        if (pointsPlayer1 == 3 && pointsPlayer2 == 3) {
          response.push("Deuce");
          continue;
        }
  
        if (points[pointsPlayer1] != undefined) {
          response.push(points[pointsPlayer1] + " - " + points[pointsPlayer2]);
          continue;
        }
      } else {
        pointsPlayer2 += 1;
        if (pointsPlayer1 == 3 && pointsPlayer2 == 3) {
          response.push("Deuce");
          continue;
        }
        if (points[pointsPlayer2] != undefined) {
          response.push(points[pointsPlayer1] + " - " + points[pointsPlayer2]);
          continue;
        }
      }
  
      if (i == 6) {
        response.push(`Ventaja ${arrayPoints[i]}`);
        continue;
      }
  
      if (i == 7) {
        response.push(`Ha ganado el ${arrayPoints[i]}`);
        continue;
      }
    }
  
    return response;
  }
  
  console.table(tenis(["P1", "P1", "P2", "P2", "P1", "P2", "P1", "P1"]));
  console.table(tenis(["P1", "P2", "P2", "P2", "P1", "P2", "P2", "P2"]));