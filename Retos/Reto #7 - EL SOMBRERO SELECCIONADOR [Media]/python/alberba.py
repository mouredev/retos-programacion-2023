import random

def get_answer():
    resp = int(input("Responda con 1, 2, 3 o 4: "))
    if resp in range(1,5):
        return resp
    return get_answer()
    
questions_and_answer = [["¿Cómo te definirías?", [
                            ("1. Valiente", "gryffindor"),
                            ("2. Leal", "hufflepuff"),
                            ("3. Sabio", "ravenclaw"),
                            ("4. Ambicioso", "slytherin")]], 
                            ["¿Cuál es tu clase favorita?", [
                            ("1. Vuelo", "gryffindor"),
                            ("2. Pociones", "ravenclaw"),
                            ("3. Defensa contra las artes oscuras", "slytherin"),
                            ("4. Animales fantásticos", "hufflepuff")]],
                            ["¿Dónde pasarías más tiempo?", [
                            ("1. Invernadero", "hufflepuff"),
                            ("2. Biblioteca", "ravenclaw"),
                            ("3. En la sala común", "slytherin"),
                            ("4. Explorando", "gryffindor")]],
                            ["¿Cuál es tu color favorito?", [
                            ("1. Rojo", "gryffindor"),
                            ("2. Azul", "ravenclaw"),
                            ("3. Verde", "slytherin"),
                            ("4. Amarillo", "hufflepuff")]],
                            ["¿Cuál es tu mascota?", [
                            ("1. Sapo", "ravenclaw"),
                            ("2. Lechuza", "gryffindor"),
                            ("3. Gato", "hufflepuff"),
                            ("4. Serpiente", "slytherin")]]]

houses = {
    "gryffindor": 0,
    "hufflepuff": 0,
    "ravenclaw": 0,
    "slytherin": 0
}
if __name__ == "__main__":
    for question_and_answers in questions_and_answer:
        print(question_and_answers[0])
        for answer in question_and_answers[1]:
            print(answer[0])
        house = question_and_answers[1][get_answer() - 1][1]
        houses[house] += 1

        print()

    selected_house = []
    max_points = 0

    for house, points in houses.items():
        if points > max_points:
            selected_house.clear()
            selected_house.append(house)
            max_points = points
        elif points == max_points:
            selected_house.append(house)

    if len(selected_house) == 1:
        print(f'Ha sido facil...¡{selected_house[0].capitalize()}!')
    else:
        print(f'Ha sido dificil...¡{random.choice(selected_house).capitalize()}!')