casas = {
    "a":"Gryffindor",
    "b":"Huffplepuff",
    "c":"Slytherin",
    "d":"Ravenclaw"
}

preguntas_y_alternativas = [
    {
        "pregunta":"1. ¿Cuál de las siguientes opciones odiaría más que la gente lo llamara?",
        "alternativas":[
            "a) Cobarte",
            "b) Egoísta",
            "c) Ordinario",
            "d) Ignorante"
        ]
    },
    {
        "pregunta":"2. Después de su muerte ¿qué es lo que más le gustaría que hiciera la gente cuando escuche su nombre?",
        "alternativas":[
            "a) Pide mas historias sobre tus aventuras",
            "b) Te extraña, pero sonríe",
            "c) Piensa con admiración tus logros",
            "d) No me importa lo que la gente piense de mí después de mi muerte, es lo que piensan de mi mientras estoy vivo lo que cuenta"
        ]
    },
    {
        "pregunta":"3. Dada la opción, preferirías inventar una poción que garantizara:",
        "alternativas":[
            "a) Gloria",
            "b) Amor",
            "c) Poder",
            "d) Sabiduría"
        ]
    },
    {
        "pregunta":"4. ¿Cómo le gustaría ser conocido en la historia?",
        "alternativas":[
            "a) El gran",
            "b) El bueno",
            "c) El audaz",
            "d) El sabio"
        ]
    },
    {
        "pregunta":"5. Tú y dos amigos deben cruzar un puente custodiado por un troll de río que insiste en luchar contra uno de ustedes antes de que los deje pasar a todos. Tú:",
        "alternativas":[
            "a) ¿Sugiere que los tres deben luchar? (sin decírselo al troll)",
            "b) Te ofreces como voluntario",
            "c) ¿Intentas confundir al troll para que te deje pasar a los tres sin luchar?",
            "d) Sugerir sorteo para decidir quién de ustedes peleará"
        ]
    }
]

pnts = {"a":0, "b":0, "c":0, "d":0}

print("\t\t\tBinvenido a Hogwarts!\
    \n\t\t\t-------------------\
    \nEl sombrero seleccionardor se encargará de seleccionar tu casa de Hogwarts\
    \n--------------------------------------------------------------------------")

r_valida = False

while not r_valida:
    try:
        for pregunta in preguntas_y_alternativas:
            print(f'\n{pregunta["pregunta"]}')
            for alternativa in pregunta["alternativas"]:
                print(alternativa)
            r = input("Rpta (a, b, c, d): ").lower()
            if r not in pnts:
                raise ValueError(f"Alternativa no válida: {r}")
            pnts[r] += 1
        r_valida = True
    except ValueError as e:
        print(f"Error: {e}\nIntente de nuevo")

max_pnts = max(pnts, key=pnts.get)
casa_final = casas[max_pnts]
print(f"Eres {casa_final}!")
