import random
# Gryffindor, Ravenclaw, Slytherin, Hafflepuff

class Hat:
    def __init__(self, questions, answers) -> None:
        self.questions = questions
        self.answers = answers

questions = [Hat("Como te defininirías en una palabra?", [
            ("1. Valiente", "Gryffindor"),
            ("2. Ambicioso", "Slytherin"),
            ("3. Leal", "Hafflepuff"),
            ("4. Curioso", "Ravenclaw")]),
            Hat("Cual emocion te caracteriza mas?", [
            ("1. Empatia", "Gryffindor"),
            ("2. Envidia", "Slytherin"),
            ("3. Amigable", "Hafflepuff"),
            ("4. Inquietud", "Ravenclaw")]),
            Hat("Con cual personaje te relacionas mejor?",[
            ("1. Hermione Granger", "Gryffindor"),
            ("2. Cedric Diggory","Hafflepuff"),
            ("3. Luna Lovegood", "Ravenclaw"),
            ("4. Draco Malfoy","Slytherin")]),
            Hat("Cual es tu lenguaje de programacion favorito?",[ 
            ("1. Python", "Slytherin"),
            ("2. JavaScript", "Ravenclaw"),
            ("3. C/C++", "Gryffindor"),
            ("4. Rust", "Hafflepuff")])
]

def get_answer() -> int:
    answer = input("Seleccione una opción del 1 al 4: ")
    if answer == "1" or answer == "2" or answer == "3" or answer == "4":
        return int(answer)
    return get_answer()

def define_house(houses:dict) -> str:
    max_points = 1 # This controls appending a house that din't get any vote
    defined_house = []
    for house, points in houses.items():
        if points > max_points:
            defined_house.append(house)
            max_points = points
        elif points == max_points:
            defined_house.append(house)
            max_points = points

    if len(defined_house) == 1:
        return defined_house[0]
    else:
        return random.choice(defined_house)

if __name__ == '__main__':
    houses = {"Gryffindor": 0, "Slytherin": 0, "Hafflepuff": 0, "Ravenclaw": 0}

    for index in range(len(questions)):
        print(questions[index].questions)
        for i in questions[index].answers:
            print(i[0])
        
        house_points = questions[index].answers[get_answer() - 1][1]
        houses[house_points] += 1

        print()

    result = define_house(houses)
    # print(houses)
    print(f"La casa seleccionada es: {result}")
