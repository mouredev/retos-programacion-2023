import random

def ocultar_letras(palabra):
    """
    Oculta aleatoriamente algunas letras de la palabra.
    No oculta más del 60% de las letras y siempre deja la primera letra visible.
    """
    letras_ocultas = list(palabra[1:])
    random.shuffle(letras_ocultas)
    num_letras_ocultas = max(1, int(0.6 * len(letras_ocultas)))
    letras_ocultas = letras_ocultas[:num_letras_ocultas]
    
    palabra_oculta = [palabra[0]] + ['_' if letra in letras_ocultas else letra for letra in palabra[1:]]
    
    return ''.join(palabra_oculta)

def jugar_adivinanza(palabra, intentos_maximos=6):
    palabra_oculta = ocultar_letras(palabra)
    intentos_restantes = intentos_maximos

    print(f"Bienvenido al juego de adivinanza. Palabra a adivinar: {palabra_oculta}")

    while intentos_restantes > 0 and '_' in palabra_oculta:
        entrada_usuario = input(f"\nIntentos restantes: {intentos_restantes}. Ingresa una letra o la palabra completa: ").lower()

        if len(entrada_usuario) == 1 and entrada_usuario.isalpha():
            if entrada_usuario in palabra[1:]:
                print("¡Correcto! La letra está en la palabra.")
                palabra_oculta = ''.join([letra if letra == entrada_usuario or palabra_oculta[i] != '_' else '_' for i, letra in enumerate(palabra)])
            else:
                print("Incorrecto. La letra no está en la palabra.")
                intentos_restantes -= 1
        elif len(entrada_usuario) == len(palabra) and entrada_usuario.isalpha():
            if entrada_usuario == palabra:
                print("¡Felicidades! Has adivinado la palabra correctamente.")
                break
            else:
                print("Incorrecto. La palabra no es la correcta.")
                intentos_restantes -= 1
        else:
            print("Entrada inválida. Ingresa una letra o la palabra completa de la longitud correcta.")

        print(f"Palabra actual: {palabra_oculta}")

    if '_' not in palabra_oculta:
        print("\n¡Felicidades! Has adivinado la palabra correctamente.")
    else:
        print(f"\n¡Lo siento! Has agotado todos tus intentos. La palabra correcta era: {palabra}")

# Ejemplo de uso
palabra_a_adivinar = "RicardoMesaGallego"
jugar_adivinanza(palabra_a_adivinar)
