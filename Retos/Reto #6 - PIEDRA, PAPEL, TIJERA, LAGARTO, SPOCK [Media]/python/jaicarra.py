
import random
winner = {
#(UserSlection,Machinaselection) -----> key : Value
    ("Rock","Rock"):"Even",
    ("Rock","Paper"):"User",
    ("Rock","Scissors"):"User",
    ("Rock","Lizard"):"User",
    ("Rock","Spock"):"Machine",

    ("Paper","Rock"):"Machine",
    ("Paper","Paper"):"Even",
    ("Paper","Scissors"):"Machine",
    ("Paper","Lizard"):"Machine",
    ("Paper","Spock"):"User",

    ("Scissors","Paper"):"User",
    ("Scissors","Rock"):"Machine",
    ("Scissors","Scissors"):"Even",
    ("Scissors","Lizard"):"User",
    ("Scissors","Spock"):"Machine",

    ("Lizard","Paper"):"User",
    ("Lizard","Rock"):"Machine",
    ("Lizard","Scissors"):"Machine",
    ("Lizard","Lizard"):"Even",
    ("Lizard","Spock"):"User",

    ("Spock","Rock"):"Even",
    ("Spock","Paper"):"Machine",
    ("Spock","Scissors"):"User",
    ("Spock","Lizard"):"Machine",
    ("Spock","Spock"):"Even"
     }


######## PRIMERA OPERACION ########### 
def chosee_option ():
    while True:
        options = ("Rock", "Paper", "Scissors", "Lizard", "Spock")
        user_option = input("Please make an input   => Rock, Paper, Scissors, Lizard, Spock ")
        user_selection = user_option.capitalize()
        print(user_selection)
        if user_selection  not in options:
            print("Invalid input. Please choose from Rock, Paper, Scissors, Lizard, or Spock.")
            
        else:
            break

    maquina_selection = random.choice(options)
    print("User input    --> :",user_selection) 
    print("Maquina input --> :",maquina_selection)
    
    return user_selection,maquina_selection
    
def check_rules(user_selection,maquina_selection,round,user_wins,maquina_wins):
     if (user_selection, maquina_selection) in winner:
        result = winner[(user_selection, maquina_selection)]
        #retrieves the value associated with the key 
        # (user_selection, maquina_selection) from the winner dictionary. 
        # The value represents the winner of the round ("User", "Machine", or "Even").
        print("The round is for ", result)
        if result == "User":
            user_wins += 1
        elif result == "Machine":
            maquina_wins += 1
        else:
            print("It's a tie!")
        round += 1
        return user_wins,maquina_wins

def game_start():
    round = 1
    user_wins=0
    maquina_wins=0
    while user_wins !=2 and maquina_wins!=2:
        print("*" *10)
        print("Welcome to the ROUND",round)
        print("*"*10)
        print("Computer wins",maquina_wins)
        print("Computer wins",user_wins)
        user_selection,maquina_selection = chosee_option ()
        user_wins,maquina_wins = check_rules(user_selection,maquina_selection,round,user_wins,maquina_wins)

    if user_wins == 2:
        print("Congratulations! You won the game!")
    else:
        print("Sorry, the computer won the game!")

game_start()

