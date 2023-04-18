preguntas = ["¿Cuál de estos colores es tu favorito?","¿Que elemento te gusta más?","¿Cuál es tu mayor virtud?", "¿Cuál de estos animales te gusta más?","¿Que fantasma te llama más la atención?"]
respuestas=[["1- Rojo","2- Azul","3- Amarillo","4- Verde"],["1- Fuego","2- Aire","3- Tierra","4- Agua"],["1- Valentia","2- Sabiduría","3- Lealtad","4- Astucia"],["1- León","2- Aguila","3- Tejón","4- Serpiente"],["1- Porpington","2- Dama gris","3- El faile gordo","4- El barón sanguinario"]]   
contador=[]
for i in range (5):
    print(preguntas[i])
    for j in range (4):
        print(respuestas[i][j])
    contador.append(int(input()))
    print()
elecciones=[contador.count(1),contador.count(2),contador.count(3),contador.count(4)]
eleccion=elecciones.index(max(elecciones))
casas=["Gryffindor","Ravenclaw","Hufflepuff","Slytherin"]
print("####################################################")
p="Felicidades has sido elegido para la casa: "
p+=casas[eleccion]
print(p)
print("####################################################")
