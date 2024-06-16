#!/usr/bin/env python3

'''
/*
 * Crea un programa que simule el comportamiento del sombrero seleccionador del
 * universo mágico de Harry Potter.
 * - De ser posible realizará 5 preguntas (como mínimo) a través de la terminal.
 * - Cada pregunta tendrá 4 respuestas posibles (también a selecciona una a través de terminal).
 * - En función de las respuestas a las 5 preguntas deberás diseñar un algoritmo que
 *   coloque al alumno en una de las 4 casas de Hogwarts (Gryffindor, Slytherin , Hufflepuff y Ravenclaw)
 * - Ten en cuenta los rasgos de cada casa para hacer las preguntas y crear el algoritmo seleccionador.
 *   Por ejemplo, en Slytherin se premia la ambición y la astucia.
 */
'''

import random


preguntas = [
    {
        "pregunta": "¿Cuál de estas cualidades te identifica más?",
        "opciones": {"Gryffindor":"Valiente", "Slytherin":"Ambicioso/a", "Hufflepuff":"Inteligente", "Ravenclaw":"Leal"}
    },
    {
        "pregunta": "¿Qué prefieres hacer en tu tiempo libre?",
        "opciones": {"Gryffindor":"Explorar lugares emocionantes y desconocidos", "Slytherin":"Trabajar en proyectos para alcanzar tus metas personales", "Hufflepuff":"Leer y aprender sobre diferentes temas interesantes", "Ravenclaw":"Pasado tiempo con amigos y seres queridos"}
    },
    {
        "pregunta": "¿Qué tipo de desafío te emociona más?",
        "opciones": {"Gryffindor":"Superar obstáculos físicos y demostrar tu valentía", "Slytherin":"Alcanzar objetivos ambiciosos y destacarte entre los demás", "Hufflepuff":"Resolver acertijos y enigmas complicados utilizando tu ingenio", "Ravenclaw":"Apoyar a tus amigos y seres queridos en momentos difíciles"}
    },
    {
        "pregunta": "¿Qué cualidad valoras más en un líder?",
        "opciones": {"Gryffindor":"Audacia y determinación para enfrentar cualquier desafío", "Slytherin":"Ambición y visión para alcanzar grandes metas", "Hufflepuff":"Inteligencia y sabiduría para tomar decisiones informadas", "Ravenclaw":"Lealtad y empatía para cuidar de quienes te rodean"}
    },
    {
        "pregunta": "Si tuvieras que elegir una palabra para definirte a ti mismo/a, ¿cuál sería?",
        "opciones": {"Gryffindor":"Audaz", "Slytherin":"Astuto/a", "Hufflepuff":"Sabio/a", "Ravenclaw":"Leal"}
    }
]



class SombreroSeleccionador:

    def __init__(self, preguntas):
        self.preguntas = preguntas
        self.resultado = []

    @staticmethod
    def obtener_clave(diccionario,valor):

        for key,value in diccionario.items():

            if valor == value:
                return key

    @staticmethod
    def obtener_clave_resultado(diccionario,valor):

        clave = []

        for key,value in diccionario.items():

            if valor == value:
                 clave.append(key)

        if len(clave) > 1:
            return clave[random.randint(0,len(clave)-1)] 
        else:
            return clave[0]

    def asignar_casa(self):
            
        casas_Hogwarts = ['Gryffindor','Slytherin', 'Hufflepuff', 'Ravenclaw']
        casa_resultado = {}
        
        for r in self.resultado:
            for casa in casas_Hogwarts:
               count = self.resultado.count(casa)
               casa_resultado.update({casa:count})

        valor_max = max(casa_resultado.values())

        return self.obtener_clave_resultado(casa_resultado,valor_max)

    def hacer_preguntas(self):
        respuesta = 0

        for p in self.preguntas:
            i = 0
            op_list = []

            while True:

                print(f'\n[+] {p["pregunta"]}\n')

                for op in p['opciones'].values():
                    i+=1
                    op_list.append(op)
                    print(f'{i} - {op}')

                try:               
                    respuesta = int(input("\n[i] Digite el número de la respuesta: ")) - 1
                    llave = self.obtener_clave(p['opciones'],op_list[respuesta])
                    self.resultado.append(llave)
                    break
                except IndexError:
                    print('\n[Error!] Ingrese un valor entre 1 al 4')
                    i = 0
                except ValueError:
                    print('\n[Error!] Solo se aceptan valores numéricos de entre el 1 al 4')
                    i = 0

        casa = self.asignar_casa()

        print('\n' + '='*90 + f'\n[+] FELICITACIONES PERTENECES A LA CASA DE !{casa}¡\n' + '='*90 )


    @property
    def get_resultado(self):
        return self.resultado

        
  

sombrero = SombreroSeleccionador(preguntas)
sombrero.hacer_preguntas()
