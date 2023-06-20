SCORE = ["Love",15,30,40]
ADVANTAGE = ["Null","P1","P2"]

def verify(sequence):
    format = True
    for player in sequence:
        if player.strip() != "p1" and player.strip() != "p2":
            format = False
            break
    
    p1_count = sequence.count("p1")
    p2_count = sequence.count("p2")
    
    if (p1_count < 4 or p1_count-p2_count < 2) and (p2_count < 4 or p2_count-p1_count < 2):
        print("The inserted sequence must have a winner.")
        format = False
    return format

def update_score(player, p1_score, p2_score, adv):
    if player == "p1":
        index = SCORE.index(p1_score)
        p1_score = SCORE[index + 1]
    else:
        index = SCORE.index(p2_score)
        p2_score = SCORE[index + 1]
    return p1_score, p2_score

def update_advantage(player, adv):
    if adv == "Null":
        return f"Advantage {player.upper()}"
    return "Deuce"

def print_score(p1_score, p2_score, adv):
    if adv == "Deuce":
        print(adv)
    elif "Advantage" in adv:
        print(adv)
    else:
        print(p1_score, " - ", p2_score)

def play(sequence):
    adv = ADVANTAGE[0]
    p1_score = SCORE[0]
    p2_score = SCORE[0]

    for player in sequence:
        if p1_score == 40 and p2_score == 40:
            adv = update_advantage(player, adv)
            print_score(p1_score, p2_score, adv)
        else:
            p1_score, p2_score = update_score(player, p1_score, p2_score, adv)
            print_score(p1_score, p2_score, adv)

        if p1_score == 40 and p1_score - p2_score >= 2:
            print("The winner is P1")
            break
        elif p2_score == 40 and p2_score - p1_score >= 2:
            print("The winner is P2")
            break

print("Enter the game sequence. Example: P1, P1, P2, P2, P1, P2, P1, P1")
sequence = input().lower().split(",")
if verify(sequence) is True:
    play(sequence)