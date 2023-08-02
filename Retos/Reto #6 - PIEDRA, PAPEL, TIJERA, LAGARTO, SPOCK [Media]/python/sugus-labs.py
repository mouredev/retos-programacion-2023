import itertools

def scissor_game(game_list: list):
    
    """ Scissor game function
    
    Codification:
    ------------
    ST: "🗿" (piedra) 
    PA: "📄" (papel)
    SC: "✂️" (tijera)
    LI: "🦎" (lagarto)
    SP: "🖖" (spock)
    
    """
    
    #comp_list = ["ST", "PA", "SC", "LI", "SP"]
    #permutation_list = list(itertools.permutations(comp_list, 2))
    #print(permutation_list)
    
    final_point_list = list()
    player_1_points = 0
    player_2_points = 0
        
    for hand in game_list:
        hand_list = list(hand)
        point_list = [0, 0]
        
        if hand_list[0] == hand_list[1]:
            point_list = [1, 1]
        
        else:
        
            if "ST" in hand_list:
                if "PA" in hand_list:
                    st_idx = hand_list.index("ST")
                    point_list[st_idx] = 0
                    point_list[int(not(bool(st_idx)))] = 1
                elif "SC" in hand_list:
                    st_idx = hand_list.index("ST")
                    point_list[st_idx] = 1
                    point_list[int(not(bool(st_idx)))] = 0   
                elif "LI" in hand_list:
                    st_idx = hand_list.index("ST")
                    point_list[st_idx] = 1
                    point_list[int(not(bool(st_idx)))] = 0
                elif "SP" in hand_list:
                    st_idx = hand_list.index("ST")
                    point_list[st_idx] = 0
                    point_list[int(not(bool(st_idx)))] = 1                     
                            
            if "PA" in hand_list:
                if "SC" in hand_list:
                    st_idx = hand_list.index("PA")
                    point_list[st_idx] = 0
                    point_list[int(not(bool(st_idx)))] = 1
                elif "LI" in hand_list:
                    st_idx = hand_list.index("PA")
                    point_list[st_idx] = 0
                    point_list[int(not(bool(st_idx)))] = 1
                elif "SP" in hand_list:
                    st_idx = hand_list.index("PA")
                    point_list[st_idx] = 1
                    point_list[int(not(bool(st_idx)))] = 0    
                    
            if "SC" in hand_list:
                if "LI" in hand_list:
                    st_idx = hand_list.index("SC")
                    point_list[st_idx] = 1
                    point_list[int(not(bool(st_idx)))] = 0
                elif "SP" in hand_list:
                    st_idx = hand_list.index("SC")
                    point_list[st_idx] = 0
                    point_list[int(not(bool(st_idx)))] = 1   
                    
            if "LI" in hand_list:
                if "SP" in hand_list:
                    st_idx = hand_list.index("LI")
                    point_list[st_idx] = 1
                    point_list[int(not(bool(st_idx)))] = 0               
                
        final_point_list.append(point_list)                      
        #done_int = sum(point_list)
        #done_int = sum(point_list)
    for player_1, player_2 in final_point_list:
        player_1_points = player_1_points + player_1
        player_2_points = player_2_points + player_2
            
    if player_1_points > player_2_points:
        print("Player 1 wins!")
    elif player_2_points > player_1_points:
        print("Player 2 wins!")
    else:
        print("Tie!")
                
if __name__ == "__main__":
    
    game_list = [
        ('ST', 'SC'), ('SC', 'ST'), ('PA', 'SC')
    ]
    
    scissor_game(game_list)