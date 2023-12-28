import random
import requests

class JuegoAdivinarPalabras:
    def __init__(self):
        url = "https://www.randomlists.com/data/words.json"
        response = requests.get(url)
        data = response.json()
        self.palabras = data["data"]
        self.palabra_a_adivinar = self.generar_palabra_a_adivinar()
        self.palabra_mostrada = self.generar_palabra_mostrada()

    def generar_palabra_a_adivinar(self):
        return random.choice(self.palabras)

    def generar_palabra_mostrada(self):
        longitud_palabra = len(self.palabra_a_adivinar)
        porcentaje_oculto = random.randint(40, 60)
        letras_a_ocultar = int(longitud_palabra * (porcentaje_oculto / 100))
        indices_a_ocultar = random.sample(range(longitud_palabra), letras_a_ocultar)
        palabra_mostrada = list(self.palabra_a_adivinar)
        for indice in indices_a_ocultar:
            palabra_mostrada[indice] = "_"
        return "".join(palabra_mostrada)

    def jugar(self):
        intentos_restantes = 6
        while intentos_restantes > 0:
            print(f"Palabra: {self.palabra_mostrada}")
            print(f"Intentos restantes: {intentos_restantes}")
            respuesta = input("Ingresa una letra o la palabra completa: ")
            if len(respuesta) == len(self.palabra_a_adivinar):
                if respuesta == self.palabra_a_adivinar:
                    print("¡Felicidades! Has adivinado la palabra.")
                    return
                else:
                    print("Respuesta incorrecta.")
                    intentos_restantes -= 1
            elif len(respuesta) == 1:
                if respuesta in self.palabra_a_adivinar:
                    print("¡Bien hecho! La letra está en la palabra.")
                    palabra_mostrada_lista = list(self.palabra_mostrada)
                    for i, letra in enumerate(self.palabra_a_adivinar):
                        if letra == respuesta:
                            palabra_mostrada_lista[i] = letra
                    self.palabra_mostrada = "".join(palabra_mostrada_lista)
                    if self.palabra_a_adivinar == self.palabra_mostrada:
                        print("¡Felicidades! Has adivinado la palabra.")
                        return
                else:
                    print("Respuesta incorrecta.")
                    intentos_restantes -= 1
            else:
                print("Respuesta no válida.")
        print(f"Lo siento, has perdido. La palabra era {self.palabra_a_adivinar}.")

juego = JuegoAdivinarPalabras()
juego.jugar()
