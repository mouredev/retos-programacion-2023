from time import sleep


GRYFF = 'gryffindor'
SLYTH = 'slytherin'
HUFFL = 'hufflepuff'
RAVEN = 'ravenclaw'


class Sombrero:
    gryffindor = 0
    slytherin = 0
    hufflepuff = 0
    ravenclaw = 0

    preguntas = [
        {
            'enunciado': '¿Cuáles de los siguientes adjetivos odiarías más que te digan los otros?',
            'respuestas': {'a': 'Ordinario', 'b': 'Ignorante', 'c': 'Cobarde', 'd': 'Egoista'},
            'casa': {'a': SLYTH, 'b': RAVEN, 'c': GRYFF, 'd': HUFFL}
        },
        {
            'enunciado': '¿Qué es lo que más ansías aprender en Hogwarts?',
            'respuestas': {
                'a': 'Aparición y Desaparición (poder materializarse y desmaterializarse a voluntad)',
                'b': 'Transfiguración (convertir un objeto en otro)',
                'c': 'Secretos sobre el castillo',
                'd': 'Todo acerca de criaturas mágicas y como ser amigo/cuidar de ellos'
            },
            'casa': {'a': SLYTH, 'b': RAVEN, 'c': GRYFF, 'd': HUFFL}
        },
        {
            'enunciado': 'Dada la elección, preferirías inventar una poción que te garantizara:',
            'respuestas': {'a': 'Amor', 'b': 'Gloria', 'c': 'Sabiduría', 'd': 'Poder'},
            'casa': {'a': HUFFL, 'b': GRYFF, 'c': RAVEN, 'd': SLYTH}
        },
        {
            'enunciado': '¿Qué tipo de instrumento le agrada más a tu oído?',
            'respuestas': {'a': 'El violín', 'b': 'La trompeta', 'c': 'El piano', 'd': 'El tambor'},
            'casa': {'a': SLYTH, 'b': HUFFL, 'c': RAVEN, 'd': GRYFF}
        },
        {
            'enunciado': '¿Cuál de las siguientes criaturas le gustaría estudiar?',
            'respuestas': {'a': 'Centauros', 'b': 'Sirenas', 'c': 'Troll', 'd': 'Hombres Lobo'},
            'casa': {'a': RAVEN, 'b': SLYTH, 'c': GRYFF, 'd': HUFFL}
        },
    ]

    def sumar_gryff(self):
        self.gryffindor += 1

    def sumar_huffl(self):
        self.hufflepuff += 1

    def sumar_slyth(self):
        self.slytherin += 1

    def sumar_raven(self):
        self.ravenclaw += 1

    def obtener_opcion(self):
        while True:
            opcion = input('Elige tu respuesta(a-b-c-d): ').lower()
            if opcion not in 'abcd' or len(opcion) > 1 or len(opcion) == 0:
                continue
            else:
                return opcion

    def seleccion(self):
        sumar_puntos = {GRYFF: self.sumar_gryff, SLYTH: self.sumar_slyth,
                        RAVEN: self.sumar_raven, HUFFL: self.sumar_huffl}

        print('Bienvenido a Hogwarts, el sombrero seleccionador te hara una serie de preguntas para asignarte a una casa')
        print('Unicamente tendras que responder a cada pregunta con una letra (a, b, c, d) correspondiente a la respuesta que desees')
        print('\n\n\n-Empezamos con las preguntas\n')

        for pregunta in self.preguntas:

            print(f"\n\n{pregunta['enunciado']}")
            for respuesta in pregunta['respuestas'].keys():
                print(f"{respuesta}. {pregunta['respuestas'][respuesta]}")

            opcion = self.obtener_opcion()
            sumar_puntos.get(pregunta['casa'][opcion])()

    def casa_seleccionada(self):
        casas = {GRYFF: self.gryffindor, SLYTH: self.slytherin,
                 HUFFL: self.hufflepuff, RAVEN: self.ravenclaw}
        casas_ordenadas = sorted(casas.items(), key=lambda x: x[1])
        sleep(1.5)
        print('\n\n\nEstoy tomando una decision...')
        sleep(1.7)
        print('\n...')
        sleep(1.9)
        print('\nMmm...')
        sleep(2.1)
        print(f'\nTe asignare a {casas_ordenadas[-1][0].capitalize()}!!!')


def run():
    sombrero = Sombrero()
    sombrero.seleccion()
    sombrero.casa_seleccionada()


if __name__ == '__main__':
    run()
