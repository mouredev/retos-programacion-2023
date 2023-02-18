# Nota aclaratoria --> Preguntas tomadas del repositorio.

class SortingHat():
    def __init__(self):
        self.houses = {
            "Gryffindor": 0,
            "Hufflepuff": 0,
            "Ravenclaw":  0,
            "Slythering": 0
        }

        self.questions = [
            "¿Cuál de las siguientes opciones odiaría más que la gente lo llamara?",
            "¿Qué poción preferirías inventar?",
            "¿Qué tipo de instrumento agrada más a tu oído?",
            "¿Cuál preferirías ser?",
            "Entras en un jardín encantado, ¿Qué sería lo más curioso de examinar primero?"
        ]
        
        self.alternatives = [
            ["Ordinario", "Ignorante", "Cobarde", "Egoista"],
            ["Gloria", "Sabiduria", "Amor", "Poder"],
            ["Violin", "Tambores", "Piano", "Trompeta"],
            ["De confianza", "Querido", "Imitado", "Alabado"],
            ["El arbol de hojas de plata con manzanas doradas", "Las setas rojas gordas que parecen estar hablando entre si", "El estanque burbujeante en cuyas profundidades se arremolina algo luminoso", "La estatua del viejo mago con un raro centelleo en los ojos"]
        ]

        self.answers = {
            "Gryffindor": ["Cobarde", "Gloria", "Trompeta", "Querido", "Las setas rojas gordas que parecen estar hablando entre si"],
            "Hufflepuff": ["Egoista", "Amor", "Piano", "De confianza", "El estanque burbujeante en cuyas profundidades se arremolina algo luminoso"],
            "Ravenclaw":  ["Ignorante", "Sabiduria", "Violin", "Imitado", "El arbol de hojas de plata con manzanas doradas"],
            "Slythering": ["Ordinario", "Poder", "Tambores", "Alabado", "La estatua del viejo mago con un raro centelleo en los ojos"]
        }


    def get_questions(self):
        return self.questions


    def get_alternatives(self):
        return self.alternatives


    def get_house(self):
        selected_house = "Gryffindor"

        for house in self.houses:
            if self.houses[house] > self.houses[selected_house]:
                selected_house = house

        return selected_house


    def add_point(self, answer):
        for house in self.houses:
            if answer in self.answers[house]:
                self.houses[house] += 1
                break


def select_house():
    hat = SortingHat()
    questions = hat.get_questions()
    alternatives = hat.get_alternatives()

    option = 0
    answer = ""

    for i, question in enumerate(questions):
        print(f"{question}:", end="\n"*2)

        for j, alternative in enumerate(alternatives[i]):
            print(f"{j+1}. {alternative}")

        print()

        option = int(input("Seleccione una opción: "))
        answer = alternatives[i][option-1]
        hat.add_point(answer)
        print()
    
    print(hat.get_house())


select_house()
