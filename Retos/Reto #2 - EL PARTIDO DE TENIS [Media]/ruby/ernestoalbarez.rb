def get_score(score)
    scores_mapping = { 0 => "Love", 15 => "15", 30 => "30", 40 => "40" }
    scores_mapping[score] || score.to_s
end
  
def get_game_result(score_p1, score_p2)
    if score_p1 >= 40 && score_p2 >= 40
      if score_p1 == score_p2
        return "Deuce"
      elsif score_p1 - score_p2 == 1
        return "Ventaja P1"
      elsif score_p2 - score_p1 == 1
        return "Ventaja P2"
      end
    end
  
    nil
end
  
def tennis_game(sequence)
    score_p1 = 0
    score_p2 = 0
  
    sequence.each do |point|
      if point == "P1"
        score_p1 += 15
      elsif point == "P2"
        score_p2 += 15
      end
  
      game_result = get_game_result(score_p1, score_p2)
      if game_result
        puts "#{get_score(score_p1)} - #{get_score(score_p2)}"
        puts game_result
        if game_result.start_with?("Ventaja")
          next
        else
          return "Ha ganado el P1" if score_p1 > score_p2
          return "Ha ganado el P2" if score_p2 > score_p1
        end
      end
  
      puts "#{get_score(score_p1)} - #{get_score(score_p2)}"
    end
  
    "Ha ganado el P1" if score_p1 > score_p2
    "Ha ganado el P2" if score_p2 > score_p1
end
