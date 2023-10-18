# Reto #7: El sombrero seleccionador
# * Crea un programa que simule el comportamiento del sombrero selccionador del
# * universo mágico de Harry Potter.
# * - De ser posible realizará 5 preguntas (como mínimo) a través de la terminal.
# * - Cada pregunta tendrá 4 respuestas posibles (también a selecciona una a través de terminal).
# * - En función de las respuestas a las 5 preguntas deberás diseñar un algoritmo que
# coloque al alumno en una de las 4 casas (Gryffindor, Slytherin , Hufflepuff y Ravenclaw)
# Ten en cuenta los rasgos de cada casa para hacer las preguntas y crear el algoritmo seleccionador.
# *   Por ejemplo, en Slytherin se premia la ambición y la astucia.

GRYFFINDOR=0
SLYTHERIN=0
HUFFLEPUFF=0
RAVENCLAW=0
casas=['GRYFFINDOR','HUFFLEPUFF','RAVENCLAW','SLYTHERIN']

d1={
    "A) ¿Cómo te consideras?": [' 1. Defensor de los demas.',' 2. Trabajador.',' 3. Sabio.',' 4. Lider.'],
    "B) Elige una mascota": [' 1. León.',' 2. Tejón.',' 3. Águila.',' 4. Serpiente.'],
    "C) ¿Qué cualidad valoras más en una persona?": [' 1. Coraje.',' 2. Lealtad.',' 3. Inteligencia.',' 4. Ambición.'],
    "D) ¿Qué color prefieres?": [' 1. Amarillo.',' 2. Escarlata.',' 3. Azul.',' 4. Plateado.'],
    "E) En una situación social": [' 1. Soy sociable y me gusta hacer amigos.',
                                   ' 2. No te gustan los prejuicios.',
                                   ' 3. Me gusta estar aprendiendo algo.',
                                   ' 4. Le doy importancia a las apariencias.']
}

def respuesta(): 
    option=0
    while not (option>0 and option<5):
        option=int(input("Ingrese la option (1-4): "))
    return option

print("Bienvenido al sombrero seleccionador")
print("Responda las siguientes preguntas:")
for i in d1:
    print(i)
    pregunta=d1[i]
    for x in pregunta:
        print(x)
    RESP=respuesta()

    if RESP==1:
        GRYFFINDOR+=1
    elif RESP==2:
        HUFFLEPUFF+=1
    elif RESP==3:
        RAVENCLAW+=1
    else:
        SLYTHERIN+=1
puntaje=[GRYFFINDOR,HUFFLEPUFF,RAVENCLAW,SLYTHERIN]

for i in puntaje:
    if i>2:
        orden=puntaje.index(i)
        break
    if i==2:
        orden=puntaje.index(i)
        break
casa=casas[orden]

print('Tú casa es: '+ casa)
