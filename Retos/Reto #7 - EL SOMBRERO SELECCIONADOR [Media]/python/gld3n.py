""" 
Not an accurate use of the characteristics of each house.
I apologize beforehand for any inconvenience.
This is just an implementation of the excercise.
Also, I'd love to hear or read any suggestions in order to improve the code.  
"""

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

    while True:
        try:
            election = int(input(""))
        except ValueError:
            print("You must provide a *number* between 1 and 4")
            continue
        else:
            if election < 1 or election > 4:
                print("You must provide a number between 1 and 4")
                continue 

            break

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

# Obtain the house with the highest points based on the houses' values.
house = max(houses, key = lambda points: houses[points])
print(f"\nYou've been -sadly- selected for the {house} house. Congratulations... (not really).\n")