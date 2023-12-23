import time

def ask_questions(houses: dict) -> dict:
    """
    Ask a series of questions to determine the house placement.

    Args:
        houses (dict): Dictionary to keep track of points for each house.

    Returns:
        dict: Updated dictionary with points for each house.
    """
    questions = {
        "What quality do you value most in a friend?": "a. Bravery b. Cunning c. Wisdom d. Loyalty",
        "\nWhat subject do you find most interesting?": "a. Defense Against the Dark Arts b. Potions c. Astronomy d. Herbology",
        "\nWhat type of task is most satisfying for you?": "a. Overcoming your own limits b. Defeating your opponents c. Discovering new knowledge d. Helping others",
        "\nWhich place would you like to explore at Hogwarts?": "a. Room of Requirement b. Dungeons c. Library d. Greenhouses",
        "\nWhat motivates you to keep going?": "a. The search for adventure b. The search for power c. The search for knowledge d. The search for truth",
    }

    for question in questions:
        while True:
            print(question)
            print(questions[question])
            answer = input("Answer: ").lower()
            if answer in ["a", "b", "c", "d"]:
                if answer == "a":
                    houses["Gryffindor"] += 1
                elif answer == "b":
                    houses["Slytherin"] += 1
                elif answer == "c":
                    houses["Ravenclaw"] += 1
                elif answer == "d":
                    houses["Hufflepuff"] += 1
                break
            else:
                print("\nInvalid answer")
    return houses

def hats_choice(houses: dict) -> str:
    """
    Determine the house based on the points.

    Args:
        houses (dict): Dictionary with points for each house.

    Returns:
        str: The selected house.
    """
    max_points = max(houses.values())
    for house, points in houses.items():
        if points == max_points:
            return house

def main():
    houses = {
        "Gryffindor": 0,
        "Slytherin": 0,
        "Hufflepuff": 0,
        "Ravenclaw": 0
    }

    selected_house = hats_choice(ask_questions(houses))
    print("It has been a very difficult decision...")
    time.sleep(2)
    print("But...")
    time.sleep(2)
    print("But...")
    time.sleep(2)
    print(f"\nYour house is: {selected_house}!\n")

if __name__ == "__main__":
    main()
