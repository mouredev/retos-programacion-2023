scores <- list("love", "15", "30", "40", "win")
points_won <- list("P1", "P1", "P1", "P2", "P2", "P2", "P1", "P2", "P2", "P1", "P1", "P1")
p1_points <- 1
p2_points <- 1
deuce_score <- 1

for (point in points_won) {
  if (point == "P1") {
    p1_points <- p1_points + 1
  }else if (point == "P2") {
    p2_points <- p2_points + 1
  }
  
  p1_score <- scores[p1_points]
  p2_score <- scores[p2_points]
  
  
  if ((p1_score == "40" & p2_score == "40")) {
    print(paste("deuce # ", deuce_score))
    p1_points <- 4
    p2_points <- 4
    deuce_score <- deuce_score + 1
  }else if ((p1_points == 5 & p2_points == 4) | (p2_points == 5 & p1_points == 4)) {
    if (p1_points > p2_points) {
      print(paste("ventaja", point))
      p1_points <- 4
      p2_points <- 3

    } else if (p2_points > p1_points) {
      print(paste("ventaja", point))
      p1_points <- 3
      p2_points <- 4

    }
  }else if (p1_points > 4 | p2_points > 4) {
    print(paste("GAME", point))
    break
  }else
    print(paste(p1_score, p2_score))
}
