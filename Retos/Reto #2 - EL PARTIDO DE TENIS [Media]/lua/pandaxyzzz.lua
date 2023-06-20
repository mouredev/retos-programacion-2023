player1_points=0
player2_points=0
player1_games=0
player2_games=0
player1_sets=0
player2_sets=0
player1_name="Naim Darrechi"
player2_name="Rivers"
game_in_progress=true

function print_scoreboard()
  print("------------------------------")
  print("   SET     GAME     POINTS")
  print("   "..player1_sets.."        "..player1_games.."-"..player2_games.."        "..get_points_display(player1_points))
  print("   "..player2_sets.."        "..player2_games.."-"..player1_games.."        "..get_points_display(player2_points))
  print("------------------------------")
end

function get_points_display(points)
  if points == 0 then
    return "Love"
  elseif points == 1 then
    return "15"
  elseif points == 2 then
    return "30"
  elseif points == 3 then
    return "40"
  elseif points == 4 then
    return "Adv"
  elseif points > 4 then
    return "Win"
  end
end

function add_point_to_player(player)
  if player == "P1" then
    player1_points=player1_points+1
  elseif player == "P2" then
    player2_points=player2_points+1
  end
  update_game_score()
end

function update_game_score()
  if player1_points >= 4 and player1_points-player2_points >= 2 then
    player1_games=player1_games+1
    player1_points=0
    player2_points=0
    check_set_score()
  elseif player2_points >= 4 and player2_points-player1_points >= 2 then
    player2_games=player2_games+1
    player1_points=0
    player2_points=0
    check_set_score()
  elseif player1_points == 4 and player2_points == 4 then
    player1_points=3
    player2_points=3
  end
end

function check_set_score()
  if player1_games >= 6 and player1_games-player2_games >= 2 then
    player1_sets=player1_sets+1
    player1_games=0
    player2_games=0
    check_match_score()
  elseif player2_games >= 6 and player2_games-player1_games >= 2 then
    player2_sets=player2_sets+1
    player1_games=0
    player2_games=0
    check_match_score()
  end
end

function check_match_score()
  if player1_sets >= 2 then
    print(player1_name.." wins the match!")
    game_in_progress=false
  elseif player2_sets >= 2 then
    print(player2_name.." wins the match!")
    game_in_progress=false
  end
end

function play_game()
  while game_in_progress do
    print_scoreboard()
    local point = io.read()
    if point == "P1" or point == "P2" then
      add_point_to_player(point)
    else
      print("Invalid input. Please enter P1 or P2.")
    end
  end
end

play_game()
