player1=1
player2=1
summary={}
rounds = 0
run = true

function scoreboard(v1,v2)
  summary[(rounds*2)+1]=v1
  summary[(rounds*2)+2]=v2
  rounds=rounds+1  
end
function printscoreboard()
  for i=1,rounds do
    print(summary[(i*2)-1].." - "..summary[i*2])
  end
end
function puntajes(p)
  local scale = {"Love","15","30","40"}
  if p=="P1" then
    player1=player1+1
  else
    player2=player2+1
  end
  if player1>4 or player2>4 then
    if player1-player2 >=2 then
      scoreboard("Gano Player 1","")
      printscoreboard()
      run=false
    elseif player2-player1 >=2 then
      scoreboard("Gano Player 2","")
      printscoreboard()
      run=false
    elseif player1-player2 >=1 then
      scoreboard("Ventaja Player 1","")
    elseif player2-player1 >=1 then
      scoreboard("Ventaja Player 2","")
    elseif player2-player1 ==0 then
      scoreboard("Deuce","")
    end
  else
    scoreboard(scale[player1],scale[player2])
  end
end

while run do
  local point = io.read()
  if point=="P1" or point=="P2" then
    puntajes(point)
  else
    print("Ingrese P1 o P2")
  end
end

