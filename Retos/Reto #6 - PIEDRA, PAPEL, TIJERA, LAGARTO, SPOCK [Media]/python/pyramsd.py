def game(players):
  p1 = 0
  p2 = 0
  tie = 0
  dic_moves_win= {
  "piedra": ["tijeras", "lagarto"],
  "papel": ["piedra", "spock"],
  "tijeras" : ["papel","lagarto"],
  "lagarto": ["papel","spock"],
  "spock": ["tijeras","piedra"]  
  }  
  
  for i in players:      
    if i[0] == i[1]:
      tie +=1 
    elif i[0] in dic_moves_win[i[1]]:
      p2 +=1 
    else:
      p1 +=1
      
  if p1  > p2:
    r = "Player 1"
  elif p1 == p2:
    r = "Tie"
  else:
    r = "Player 2"
  
  return r

print(game([("piedra","spock"), ("lagarto","piedra"), ("lagarto","tijeras")]))
print(game([("lagarto","papel"), ("tijeras","papel"), ("papel","spock")]))
print(game([ ("tijeras","lagarto"), ("papel","tijeras")]))
