# /*
#  * Crea un pequeño juego que consista en adivinar palabras en un número máximo de intentos:
#  * - El juego comienza proponiendo una palabra aleatoria incompleta
#  *   - Por ejemplo "m_ur_d_v", y el número de intentos que le quedan
#  * - El usuario puede introducir únicamente una letra o una palabra (de la misma longitud que
#  *   la palabra a adivinar)
#  *   - Si escribe una letra y acierta, se muestra esa letra en la palabra. Si falla, se resta
#  *     uno al número de intentos
#  *   - Si escribe una resolución y acierta, finaliza el juego, en caso contrario, se resta uno
#  *     al número de intentos
#  *   - Si el contador de intentos llega a 0, el jugador pierde
#  * - La palabra debe ocultar de forma aleatoria letras, y nunca puede comenzar ocultando más del 60%
#  * - Puedes utilizar las palabras que quieras y el número de intentos que consideres
#  */

from random import randint, sample

PALABRAS = [
    "mouredev",
    "arena",
    "cafe",
    "manzana",
    "hamburguesa",
    "teclado",
    "programador",
    "python",
    "javascript",
    "algoritmo",
    "solucion",
    "repositorio",
    "programacion",
    "matematica",
    "futuro",
    "ciencia",
    "escritura",
    "educacion",
    "computadora",
    "algoritmos",
    "inteligencia",
    "inovacion",
    "redes",
    "tecnologia",
    "aprendizaje",
    "desarrollador",
    "internet",
    "codigo",
    "creativo",
    "navegacion",
    "sistema",
    "aplicacion",
    "videojuego",
    "framework",
    "backend",
    "frontend",
    "desarrollo",
    "programador",
    "usuario",
    "seguridad",
    "criptografia",
    "robotica",
    "transformacion",
    "pythonista",
    "analisis",
    "automatizacion",
    "matriz",
    "optimización",
    "estructura",
    "teorema",
    "paradigma",
    "ingenieria",
    "software",
    "hardware",
    "sostenibilidad",
    "biodiversidad",
    "conocimiento",
    "comunicacion",
    "diseño",
    "teoria",
    "proyecto",
    "portafolio"
]

def juego_de_palabras():
    num_palabras = len(PALABRAS)
    intentos = 5
    palabra_random = randint(0, num_palabras-1)
    palabra = PALABRAS[palabra_random]
    palabra_oculta = list(palabra)
    letras_adivinadas = set()

    # Calcular cuántas letras ocultar: máximo 60% de la palabra y al menos 1 letra
    max_ocultas = max(1, int(len(palabra) * 0.6))
    indices_ocultar = sample(range(len(palabra)), max_ocultas) 

    for i in indices_ocultar:
        palabra_oculta[i] = '_'


    print("Bienvenido al juego 'Adivina La Palabra':\n")

    while(True):
        print(f"\nIntentos restantes: {intentos}")
        
        if intentos == 0:
            print(f"¡Has perdido! La palabra era: {palabra}")
            break
            
        print(" ".join(palabra_oculta))
        respuesta = input(f"\n¿Cual es esta palabra? Inserta una letra o la palabra: ").lower()

        if (len(respuesta) == len(palabra)):
            if (respuesta == palabra):
                print("\nAcertaste!!! Juego Terminado")
                break
            else:
                intentos -= 1
                print("\nRespuesta incorrecta, intentalo de nuevo.")
        elif (len(respuesta) == 1):
            if respuesta in letras_adivinadas:
                print("Ya has adivinado esa letra antes.")
            elif respuesta in palabra:
                letras_adivinadas.add(respuesta)

                for i in range(len(palabra)):
                    if palabra[i] == respuesta:
                        palabra_oculta[i] = respuesta
                print("¡Acertaste una letra!")

                if "_" not in palabra_oculta:
                    print(" ".join(palabra_oculta))
                    print("¡Has adivinado todas las letras! Juego Terminado")
                    break
            else:
                intentos -= 1
                print("Respuesta incorrecta, intentalo de nuevo")
        else:
            intentos -= 1
            print("La respuesta debe ser una letra o contener la misma cantidad de letras que la palabra.\n")

juego_de_palabras()
