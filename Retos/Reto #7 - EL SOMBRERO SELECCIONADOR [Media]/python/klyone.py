#!/usr/bin/env python3

import random

class HatQuestion:
    def __init__(self, question, answers, categories):

        if len(answers) != len(categories):
            raise Exception

        self.question = question
        self.answers = answers
        self.categories = categories

    def get_question(self):
        return self.question

    def get_answers(self):
        return self.answers

    def get_categories(self):
        return self.categories

    def answer(self, selection):
        result = None

        if isinstance(selection, int):
            if selection >= 0 and selection < len(self.answers):
                selection = self.answers[selection]
            else:
                return None

        for i in range(0, len(self.answers)):
            if self.answers[i] == selection:
                result = self.categories[i]
                break
        return result

    def __str__(self):
        s = "El Sombrero seleccionador pregunta: " + self.question + "\n"
        for i in range(0,len(self.answers)):
            s = s + "\t" + str(i+1) + ") " + self.answers[i] + "\n"
        return s

class HatQuestionRepository:
    def __init__(self):
        self.questions = []
        self.selected_questions = []

    def add_question(self, question):
        self.questions.append(question)

    def get_random_question(self):
        if len(self.questions) == 0:
            return None

        question = random.choice(self.questions)
        self.questions.remove(question)
        self.selected_questions.append(question)

        return question

    def clear_selected_questions(self):
        for i in range(0, len(self.selected_questions)):
            self.questions.append(self.selected_questions[i])
        self.selected_questions = []

    def get_amount_questions(self):
        return len(self.questions)

def initialize_question_repository():
    questions_repo = HatQuestionRepository()
    question = HatQuestion("¿Cual de las siguientes opciones odiaria mas que la gente lo llamara?", ["Ordinario", "Ignorante", "Cobarde", "Egoista"], ["Slytherin", "Ravenclaw", "Gryffindor", "Hufflepuff"])
    questions_repo.add_question(question)
    question = HatQuestion("¿Que pocion preferirias inventar?", ["Gloria", "Sabiduria", "Amor", "Poder"], ["Gryffindor", "Ravenclaw", "Hufflepuff", "Slytherin"])
    questions_repo.add_question(question)
    question = HatQuestion("¿Que tipo de instrumento agrada mas a tu oido?", ["Violin", "Tambores", "Piano", "Trompeta"], ["Ravenclaw", "Slytherin", "Hufflepuff", "Gryffindor"])
    questions_repo.add_question(question)
    question = HatQuestion("¿Cual preferirias ser?", ["De confianza", "Querido", "Imitado", "Alabado"], ["Hufflepuff", "Gryffindor", "Ravenclaw", "Slytherin"])
    questions_repo.add_question(question)
    question = HatQuestion("¿Entras en un jardin encantado, ¿Que seria lo mas curioso de examinar primero?", ["El arbol de hojas de plata con manzanas doradas", "Las setas rojas gordas que parecen estar hablando entre si", "El estanque burbujeante en cuyas profundidades se arremolina algo luminoso", "La estatua del viejo mago con un raro centelleo en los ojos"], ["Ravenclaw", "Gryffindor", "Hufflepuff", "Slytherin"])
    questions_repo.add_question(question)

    return questions_repo

if __name__ == "__main__":
    results = {
        "Gryffindor" : 0,
        "Slytherin" : 0,
        "Hufflepuff" : 0,
        "Ravenclaw" : 0,
    }

    questions_repo = initialize_question_repository()
    number_questions = questions_repo.get_amount_questions()

    for i in range(0, number_questions):
        current_question = questions_repo.get_random_question()
        if current_question == None:
            break
        print(current_question)
        selection = int(input("Tu respuesta: "))
        while selection <= 0 or selection >= len(current_question.get_answers())+1:
                selection = int(input("Tu respuesta: "))
        team = current_question.answer(selection - 1)
        results[team] = results[team] + 1

    print(results)
    print("¡Enhorabuena! Perteneces a la casa "+ max(results, key=results.get) + " de Hogwarts")
