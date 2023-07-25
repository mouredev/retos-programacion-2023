pregunta_1 = """
Si pudieras tener algún poder, ¿Cuál elegirias?
a) Poder de invisibilidad.
b) Poder de cambiar la apariencia.
c) Fuerza sobrehumana.
d) Poder de cambiar el pasado.
"""

pregunta_2 = """
¿Qué camino te tienta más?
a) El camino serpenteante y cubierto de hojas a través del bosque.
b) La calle adoquinada bordeada de edificios antiguos.
c) El camino ancho, soleado y cubierto de hierba.
d) El callejón estrecho, oscuro e iluminado con linternas.
"""

pregunta_3 = """
¿Cuál es lo que más esperas aprender en Hogwarts?
a) Secretos sobre el castillo.
b) Transformaciones y todas las áreas de la magia.
c) Criaturas mágicas.
d) Maleficios.
"""

pregunta_4 = """
¿Qué tipo de instrumento agrada más a tu oido?
a) El tambor
b) El piano
c) La trompeta
d) El violín
"""

pregunta_5 = """
¿Cuál de los siguientes odiarías más que la gente te llame?
a) Cobarde
b) Ignorante
c) Egoísta
d) Ordinario
"""

scores = [0, 0, 0, 0]
houses = ["Gryffindor", "Ravenclaw", "Hufflepuff", "Slytherin"]

for pregunta in (pregunta_1, pregunta_2, pregunta_3, pregunta_4, pregunta_5):
    res = ''
    while res not in ("a", "b", "c", "d", "d"):
        res = input(pregunta)
    if res == "a":
        scores[0] += 1
    elif res == "b":
        scores[1] += 1
    elif res == "c":
        scores[2] += 1
    else:
        scores[3] += 1

print("Te toca en: ", houses[scores.index(max(scores))])
