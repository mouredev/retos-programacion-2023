import itertools
from functools import reduce

def selection_hat():
    
    """ Selection hat function """
    choice_list = []
    question_dict = {
        "What is your prefered colour?\n":
            """
            A - RED\n
            B - BLUE\n
            C - WHITE\n
            D - YELLOW\n
            """,
        "What is your prefered shape?\n":
            """
            A - CIRCLE\n
            B - RECTANGLE\n
            C - SQUARE\n
            D - TRIANGLE\n
            """                                     
    }           
         
    for question, response in question_dict.items():
        choice = None
        while choice not in ["A", "B", "C", "D"]:
            choice = input(question + response).upper()
        choice_list.append(choice)
        
    total = reduce(
        lambda a, b: 
            (ord(a) - (ord("A") - 1)) + (ord(b)  - (ord("A") - 1)), 
        choice_list)
    #print(total)
    
    if total < 5:
        political_vision = "LIBERAL"
    else:
        political_vision = "CONSERVATIVE"
        
    print(f"You are {political_vision}")
                                              
if __name__ == "__main__":

    selection_hat()