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
            ["¿Cuál de las siguientes opciones odiaría más que la gente lo llamara?", ("Ordinario", "Ignorante", "Cobarde", "Egoista")],
            ["¿Qué poción preferirías inventar?", ("Gloria", "Sabiduria", "Amor", "Poder")],
            ["¿Qué tipo de instrumento agrada más a tu oído?", ("Violin", "Tambores", "Piano", "Trompeta")],
            ["¿Cuál preferirías ser?", ("De confianza", "Querido", "Imitado", "Alabado")],
            ["Entras en un jardín encantado, ¿Qué sería lo más curioso de examinar primero?", ("El arbol de hojas de plata con manzanas doradas", "Las setas rojas gordas que parecen estar hablando entre si", "El estanque burbujeante en cuyas profundidades se arremolina algo luminoso", "La estatua del viejo mago con un raro centelleo en los ojos")]
        ]

        self.answers = {
            "Gryffindor": ["Cobarde", "Gloria", "Trompeta", "Querido", "Las setas rojas gordas que parecen estar hablando entre si"],
            "Hufflepuff": ["Egoista", "Amor", "Piano", "De confianza", "El estanque burbujeante en cuyas profundidades se arremolina algo luminoso"],
            "Ravenclaw":  ["Ignorante", "Sabiduria", "Violin", "Imitado", "El arbol de hojas de plata con manzanas doradas"],
            "Slythering": ["Ordinario", "Poder", "Tambores", "Alabado", "La estatua del viejo mago con un raro centelleo en los ojos"]
        }


    def get_question(self, index):
        return self.questions[index][0]


    def get_alternative(self, index):
        return self.questions[index][1]


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
    answer = ""
    option = 0

    for i, question in enumerate(hat.questions):
        print(f"{hat.get_question(i)}:\n")

        for j, alternative in enumerate(hat.get_alternative(i)):
            print(f"{j+1}. {alternative}")

        print()

        option = int(input("Seleccione una opción: "))
        print()
        
        answer = hat.get_alternative(i)[option-1]
        hat.add_point(answer)
    
    print(f"Tu casa es... ¡{hat.get_house()}!")


select_house()
