""" 
Not an accurate use of the characteristics of each house.
I apologize beforehand for any inconvenience.
This is just an implementation of the excercise.
Also, I'd love to hear or read any suggestions in order to improve the code.  
"""

from collections import Counter
from time import sleep
from random import choice

houses = {
    "Hufflepuff": 0,
    "Slytherin": 0,
    "Gryffindor": 0,
    "Ravenclaw": 0
}

"""
Function that evaluates any type of input the user 
could give in order to avoid any error. Then, based on 
the response, adds a point to the corresponding house.
"""
def verification():
    global houses
    
    try:
        election = int(input(""))
    except ValueError:
        print("You must provide a *number* between 1 and 4")
        return verification()
    else:
        if election < 1 or election > 4:
            print("You must provide a number between 1 and 4")
            return verification()

    if election == 1:
        houses["Hufflepuff"] += 1

    elif election == 2:
        houses["Slytherin"] += 1

    elif election == 3:
        houses["Gryffindor"] += 1

    else:
        houses["Ravenclaw"] += 1

    print("================================================================================================")

def question_one():
    print("""\n*First question*
You consider yourself:
    1. Optimistic
    2. Cunning
    3. extrovert
    4. Imaginative
    (Please choose by number.)""")   
    
    verification()


def question_two():
    print("""\n*Second question*
You consider yourself:
    1. Friendly
    2. Ambitious
    3. Courageous
    4. Creative
    (Please choose by number.)""")
    
    verification()


def question_three():
    print("""\n*Third question*
You consider yourself:
    1. Supportive
    2. Prideful
    3. Do-ers
    4. Intuitive
    (Please choose by number.)""")
    
    verification()


def question_four():
    print("""\n*Fourth question*
You consider yourself:
    1. Loyal
    2. Resourceful
    3. Hands-on
    4. Intelligent
    (Please choose by number.)""")
    
    verification()


def question_five():
    print("""\n*Fifth question*
You consider yourself:
    1. Generous
    2. Confident
    3. Conscientious
    4. Witty
    (Please choose by number.)""")
    
    verification()
    
def question_opt():
    print("""\n*Tie-breaker question*
You consider yourself:
    1. Humble
    2. Greedy
    3. Instrospective
    4. Reliable
    (Please choose by number.)""")
    
    verification()


print("================================================================================================")
print("\nYou will be selected for one of the houses depending on your choices. Be honest... if you wish.\n")
print("================================================================================================")

count = 0
while count < 6:
    count += 1
    if count == 1:
        question_one()

    elif count == 2:
        question_two()

    elif count == 3:
        question_three()
        
    elif count == 4:
        question_four()

    elif count == 5:
        question_five()
        
        
# the times the function is called
draw_times = 0

def draw_check():
    global draw_times
    draw_times += 1
    
    # making the houses dir a Counter so I can use the most_common function
    checker = Counter(houses)

    # will look for the two highest points
    draw = checker.most_common(2)

    # the first time it will compare the values and if they are the same, a next question is going
    # to be asked for the tie-breaker
    if draw_times <=1:
        if draw[0][1] == draw[1][1]:
            print(f"You're between {draw[0][0]} and {draw[1][0]}. I'll make one last question to make the last decision.")
            question_opt()
            
            return draw_check()
    
    # checks a second time to see wether there's a draw or not
    elif draw_times > 1:
        draw = checker.most_common(3)
        
        # in case there's no draw after the checkup
        if draw[0][1] != draw[1][1]: 
            print("\nBroke the deadlock. Making a decision now...\n")
            for i in range(0,3):
                print("...\n")
                sleep(1)
 
            return max(draw, key = lambda points: draw[0])[0]
        
        #! done in case the response makes a draw again 
        print("""\nWell, it've been hard. I'm going to pick a -semi- random house for you, since you are a special
        wizard, and can't fit in only one house. I'm amazed.\n""")

        for i in range(0,3):
                print("...\n")
                sleep(1)
                
        final_house = choice(draw)
        return final_house[0]
    
    # returns None in case there's no draw
    return

result = draw_check()

if not(result):
    """
    Obtain the house with the highest points based on the houses' values.
    ! It will only print if there's no draw or tie-breaker.
    """
    house = max(houses, key = lambda points: houses[points])
    print(f"\nYou've been selected for the {house} house. Congratulations.\n")

else:
    # prints in case of a previous draw
    print(f"\nYou've been -hardly- selected for the {result} house. Congratulations... (not really).\n")