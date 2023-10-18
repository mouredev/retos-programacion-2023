from bs4 import BeautifulSoup
import requests
import re
import string

player_list = ["P1", "P1", "P2", "P2", "P1", "P2", "P1", "P2", "P1", "P2", "P2", "P2"]
game_step_list = ["Love", "15", "30", "40"]
            
def generate_game_steps(player_list: list, game_step_list: list = game_step_list):
    
    """ text to Tennis game function """
    
    player_1_pos = 0
    player_2_pos = 0
    first_deuce = False
    
    print(f"{game_step_list[player_1_pos]} - {game_step_list[player_2_pos]}")
    
    for player in player_list:
        if player == "P1":
            if first_deuce:
                player_1_pos = player_1_pos + 1
                player_1_str = "Advantage P1"
                player_2_str = ""
            else:
                player_1_pos = player_1_pos + 1
                player_1_str = game_step_list[player_1_pos]
                player_2_str = game_step_list[player_2_pos]
        elif player == "P2":
            if first_deuce:
                player_2_pos = player_2_pos + 1
                player_1_str = ""
                player_2_str = "Advantage P2"
            else:            
                player_2_pos = player_2_pos + 1
                player_1_str = game_step_list[player_1_pos]
                player_2_str = game_step_list[player_2_pos]
        if player_1_pos < 4 and player_2_pos < 4:
            if player_1_str != "" and player_2_str != "":
                game_str = f"{player_1_str} - {player_2_str}"
            else:
                game_str = f"{player_1_str}{player_2_str}"
            if player_1_pos == 3 and player_2_pos == 3:
                game_str = "Deuce"
                first_deuce = True
                player_1_pos = player_1_pos - 1
                player_2_pos = player_2_pos - 1
        else:
            if player_1_pos == 4: 
                game_str = "P1 wins!"
            elif player_2_pos == 4:
                game_str = "P2 wins!"          
        print(game_str)
            
if __name__ == "__main__":
    generate_game_steps(player_list, game_step_list)