import random

INTENTOS = 5

def adivina(palabra_oculta: str, palabra: str, intentos: int) -> str:
    print(f"La palabra a adivinar es {palabra_oculta}")
    while intentos > 0:
        letra = input("Introduce una letra: ")
        if len(letra) > 1:
            if palabra == letra:
                return "Acertastes enhorabuena!!!"
            else:
                intentos -= 1
                print(f"Intentalo de nuevo, te quedan {intentos} intentos")

        if len(letra) == 1:
            if letra in palabra:
                pos_letra = [i for i, _ in enumerate(palabra) if _ == letra]
                for pos in pos_letra:
                    palabra_oculta[pos] = letra
                print(f"Acertastes, ahora la palabra es {palabra_oculta}")
            else:
                intentos -= 1
                print(f"Intentalo de nuevo, te quedan {intentos} intentos")

        if "_" not in palabra_oculta:
            return "Felicidades!!!"
    
    return f"Perdistes, la palabra era {palabra}"

if __name__ == "__main__":
    palabra_acertar = "mayonesa"
    # ocultar el 0.6 de las letras con _
    palabra_oculta = ["_" if random.random() > 0.6 else letra for letra in palabra_acertar]
    print(adivina(palabra_oculta, palabra_acertar, INTENTOS))

