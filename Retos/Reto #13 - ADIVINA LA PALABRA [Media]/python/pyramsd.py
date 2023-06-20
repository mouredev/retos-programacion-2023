import random

# Palabras a adivinar
palabras = ['gato', 'perro', 'elefante', 'jirafa', 'leon', 'tigre', 'rinoceronte', 'hipopotamo']

palabra_a_adivinar = random.choice(palabras)
letras_ocultas = list(palabra_a_adivinar)
num_letras_ocultas = int(len(letras_ocultas) * 0.6)
indices_ocultos = random.sample(range(len(letras_ocultas)), num_letras_ocultas)
for i in indices_ocultos:
    letras_ocultas[i] = '_'
palabra_oculta = ''.join(letras_ocultas)

intentos_maximos = 5
intentos_restantes = intentos_maximos

print(f'¡Bienvenido al juego de adivinanza de palabras! La palabra a adivinar es: {palabra_oculta}')
while intentos_restantes > 0:
    print(f'Tienes {intentos_restantes} intentos restantes.')
    respuesta = input('Ingresa una letra o una palabra: ').lower()
    if len(respuesta) == 1:
        if respuesta in palabra_a_adivinar:
            print(f'¡Correcto! La letra {respuesta} está en la palabra.')
            letras_ocultas = list(palabra_oculta)
            for i, letra in enumerate(palabra_a_adivinar):
                if letra == respuesta:
                    letras_ocultas[i] = letra
            palabra_oculta = ''.join(letras_ocultas)
            print(f'La palabra a adivinar ahora es: {palabra_oculta}')
            if palabra_oculta == palabra_a_adivinar:
                print('¡Felicidades! Has adivinado la palabra.')
                break
        else:
            print(f'Lo siento, la letra {respuesta} no está en la palabra.')
            intentos_restantes -= 1
    else:
        if respuesta == palabra_a_adivinar:
            print('¡Felicidades! Has adivinado la palabra.')
            break
        else:
            print('Lo siento, esa no es la palabra a adivinar.')
            intentos_restantes -= 1

if intentos_restantes == 0:
    print(f'Lo siento, has perdido. La palabra a adivinar era {palabra_a_adivinar}.')
