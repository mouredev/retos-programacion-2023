preguntas = [
    '¿Qué cualidad te describe mejor?', 
    '¿Qué asignatura se te daría mejor?', 
    '¿Cuál de estos hechizos prefieres?', 
    '¿Le temes al Señor Oscuro?', 
    '¿Con cuál de estos animales te sientes más identificado?']
    
opciones = [
    ['Lealtad', 'Ingenio', 'Ambición', 'Valentía'],  
    ['Astronomía', 'Encantamientos', 'Herbología', 'Defensa contra las Artes Oscuras'], 
    ['Expelliarmus', 'Avada Kedavra', 'Ascendio', 'Geminio'], 
    ['Sí, hay que obedecerle', 'Sí, mucho miedo', 'No, hay que tener cuidado con él', 'No, hay que enfrentarse a él'], 
    ['Oso', 'Cuervo', 'León', 'Águila']]
    
puntos = [
    [2, 3, 1, 0], 
    [3, 0, 2, 1], 
    [0, 1, 2, 3], 
    [1, 2, 3, 0], 
    [2, 1, 0, 3]]
    
puntos_casas = [
    [0, 'Gryffindor'],
    [0, 'Slytherin'],
    [0, 'Hufflepuff'],
    [0, 'Ravenclaw']]
    
for i in range(0, 5):
    
    opcion = 0
    
    print(preguntas[i], "(Elije una opcion de 1 a 4)")
    for j in range(0, 4):
        print((j + 1), "->", opciones[i][j])
    
    opcion = int(input())
    
    while (opcion < 1 or opcion > 4):
        print("OPCION NO VALIDA, elije un numero entre 1 y 4")
        opcion = int(input())
        
    puntos_casas[puntos[i][opcion - 1]][0] += 1

casa_elegida = ""
mas_puntos = -1

for i in puntos_casas:
    if (i[0] > mas_puntos):
        casa_elegida = i[1]
        mas_puntos = i[0]
        
print("La casa a la que vas es...", casa_elegida, "!!!")
