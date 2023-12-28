PROMPT_VALENTIA = """
Valentía:
Te encuentras en el bosque prohibido y escuchas gritos de auxilio provenientes de una zona oscura y peligrosa. ¿Qué haces?
1. Te acercas sin dudar para ayudar, enfrentando cualquier peligro que pueda surgir.
2. Te preparas mentalmente y decides ir a investigar, pero pidiendo ayuda a un amigo antes de adentrarte.
3. Decides pedir ayuda a un profesor o adulto antes de enfrentar la situación.
4. Evitas acercarte y regresas al castillo buscando a un adulto para que maneje la situación.
Opción:
"""

PROMPT_INTELIGENCIA = """
Inteligencia:
El profesor Snape te ha asignado una poción complicada que requiere de una gran precisión. ¿Qué enfoque tomas?
1. Te enfrentas al reto con confianza y resuelves la poción usando tus conocimientos mágicos.
2. Buscas en la biblioteca información adicional sobre la poción antes de proceder con la tarea.
3. Consultas con tus compañeros de clase para obtener consejos y orientación.
4. Te sientes abrumado y tienes dificultades para entender la complejidad de la poción.
Opción:
"""

PROMPT_LIDERAZGO = """
Liderazgo:
En el club de duelo, te han nombrado líder del equipo en un importante torneo. ¿Cómo lideras al equipo?
1. Tomas la iniciativa, das instrucciones claras y motivas a tus compañeros para lograr la victoria.
2. Escuchas las ideas y estrategias de tus compañeros, tomando decisiones en consenso. 
3. Prefieres dejar que otro compañero tome el liderazgo y sigues sus instrucciones.
4. Intentas tomar el control, pero tus decisiones generan desacuerdos y confusión en el equipo.
Opción:
"""

PROMPT_HONESTIDAD = """
Honestidad:
Entras a la sala común y encuentras una cartera olvidada con una gran cantidad de galeones. ¿Qué haces?
1. Confiesas inmediatamente que encontraste la cartera y la entregas al jefe de tu casa.
2. Decides buscar al dueño de la cartera, pero antes sacas solo una pequeña cantidad de galeones para ti.
3. Decides quedarte con la cartera y no decir nada, justificándolo como un premio inesperado.
4. Guardas la cartera en tu mochila sin mencionar nada a nadie.
"""

PROMPT_CONFIANZA = """
Confianza:
1. Tienes confianza en tus habilidades mágicas y crees que puedes enfrentar cualquier desafío.
2. Te sientes seguro en la mayoría de las situaciones, pero a veces tienes dudas sobre ti mismo.
3. Tienes inseguridades y te cuesta confiar en tus propias habilidades.
4. Te sientes constantemente inseguro y sin confianza en tus capacidades mágicas.
Opción:
"""

if __name__ == '__main__':
    # Pedir al usuario que puntúe cada cualidad en una escala del 1 al 4
    print("¡Bienvenido al sombrero seleccionador!")
    print("Para determinar tu casa de Hogwarts, necesito que me ayudes a calificar algunas situaciones.")
    print("Recuerda que debes calificar cada situación con un número del 1 al 4.")
    valentia = int(input(PROMPT_VALENTIA))
    inteligencia = int(input(PROMPT_INTELIGENCIA))
    liderazgo = int(input(PROMPT_LIDERAZGO))
    honestidad = int(input(PROMPT_HONESTIDAD))
    confianza = int(input(PROMPT_CONFIANZA))

    puntaje_total = valentia + inteligencia + liderazgo + honestidad + confianza
    print("¡Resultados!")
    print(f"Puntaje total: {puntaje_total}")

    # Determinar la casa de Hogwarts
    if puntaje_total >= 15:
        print("¡Eres un Gryffindor!")
    elif puntaje_total >= 11:
        print("¡Eres un Ravenclaw!")
    elif puntaje_total >= 8:
        print("¡Eres un Hufflepuff!")
    else:
        print("¡Eres un Slytherin!")
