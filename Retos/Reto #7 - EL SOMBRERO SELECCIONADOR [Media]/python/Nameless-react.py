import time

class create_question:
    def __init__ (self, question, answer):
        self.question = question
        self.answer = answer




def selection_house():
    print("Bienvenido(a) yo soy el sombrero seleccionador, a continuación voy a hacer unas preguntas para saber a que casa perteneces")
    hat_questions = [create_question("¿Cómo te definirías?", [
                            ("1. Valiente", "gryffindor"),
                            ("2. Leal", "hufflepuff"),
                            ("3. Sabio", "ravenclaw"),
                            ("4. Ambicioso", "slytherin")]),
                 create_question("¿Cuál es tu clase favorita?", [
                            ("1. Vuelo", "gryffindor"),
                            ("2. Pociones", "ravenclaw"),
                            ("3. Defensa contra las artes oscuras", "slytherin"),
                            ("4. Animales fantásticos", "hufflepuff")]),
                 create_question("¿Dónde pasarías más tiempo?", [
                            ("1. Invernadero", "hufflepuff"),
                            ("2. Biblioteca", "ravenclaw"),
                            ("3. En la sala común", "slytherin"),
                            ("4. Explorando", "gryffindor")]),
                 create_question("¿Cuál es tu color favorito?", [
                            ("1. Rojo", "gryffindor"),
                            ("2. Azul", "ravenclaw"),
                            ("3. Verde", "slytherin"),
                            ("4. Amarillo", "hufflepuff")]),
                 create_question("¿Cuál es tu mascota?", [
                            ("1. Sapo", "ravenclaw"),
                            ("2. Lechuza", "gryffindor"),
                            ("3. Gato", "hufflepuff"),
                            ("4. Serpiente", "slytherin")])]
    houses = {
        "gryffindor": 0,
        "hufflepuff": 0,
        "ravenclaw": 0,
        "slytherin": 0
    }


    for question in hat_questions:
        text = question.question + "".join(map(lambda x: "\n" + x[0], question.answer)) + "\n"
        answer = ""
        while answer not in [1, 2 ,3, 4]:
            answer = int(input(text))
        
        for index, house in enumerate(question.answer):
            if index + 1 == answer:
                houses[house[1]] += 1
    
                
    print("Hmmmmm....")
    time.sleep(1)
    print("Creo...")
    time.sleep(1)
    print("Que podrias encajar en....")
    time.sleep(1)
    print(f"\n{'#' * 20} {max(houses).capitalize()} {'#' * 20}")


selection_house()