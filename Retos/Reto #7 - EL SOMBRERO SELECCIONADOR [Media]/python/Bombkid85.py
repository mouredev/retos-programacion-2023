import random

def sorting_hat ():
    gryffindor = 0
    hufflepuff = 0
    ravenclaw = 0
    slytherin = 0

    winner =[]
    
    questions = ["\n¿Que cualidad te describe mejor?:\n1.Valor\n2.Lealtad\n3.Erudición\n4.Ambición\nRespuesta:", 
                "\n¿Que cualidad te discribe mejor?:\n1.Paciencia\n2.Fuerza\n3.Inteligencia\n4.Astucia\nRespuesta:", 
                "\n¿Que valoras mas?:\n1.Audacia\n2.Justicia\n3.Creatividad\n4.Determinación\nRespuesta:", 
                "\n¿Que animal te gusta mas?:\n1.Serpiente\n2.Tejón\n3.Cuervo\n4.León\nRespuesta:", 
                "\nQue lugar te gusta mas?\n1.Torre Ravenclaw\n2.Mazmorras\n3.Torre Gryffindor\n4.Cocina\nRespuesta:"]

    answers = [["1","2","3","4"], ["2","1","3","4"], ["1","2","3","4"], ["4","2","3","1"], ["3","4","1","2"]]

    for index, question in enumerate(questions):
        answer = input(question)
        while answer != "1" and answer != "2" and answer != "3" and answer != "4":
            print("\nRespuesta incorrecta\nVuelve a responder")
            answer = input(question)
        if answer == answers[index][0]:
            gryffindor +=1
        elif answer == answers[index][1]:
            hufflepuff +=1
        elif answer == answers[index][2]:
            ravenclaw +=1
        elif answer == answers[index][3]:
            slytherin +=1
    
    if gryffindor >= hufflepuff and gryffindor >= ravenclaw and gryffindor >= slytherin:
        winner.append("Eres de Gryffindor")
    if hufflepuff >= gryffindor and hufflepuff >= ravenclaw and hufflepuff >= slytherin:
        winner.append("Eres de Hufflepuff")
    if ravenclaw >= gryffindor and ravenclaw >= hufflepuff and ravenclaw >= slytherin:
        winner.append("Eres de Slytherin")
    if slytherin >= gryffindor and slytherin >= hufflepuff and slytherin >= ravenclaw:
        winner.append("Eres de Slytherin")

    print(random.choice(winner))
    
sorting_hat()
            



