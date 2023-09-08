def es_primo(num: int) -> bool:
    if num == 2:
        return True
    if (num < 1) or (num % 2 == 0):
        return False
    for x in range(3, num, 2):
        if num % x == 0:
            return False
    return True


def primos_gemelos(num : int):
    numeros_primos = [x for x in range(num) if es_primo(x)]
    primos_gemelos = []
    for fst, snd in zip(numeros_primos[:-1], numeros_primos[1:]):
        if snd - fst == 2:
            primos_gemelos.append(f"({fst}, {snd})")
    print(", ".join(primos_gemelos))


primos_gemelos(20)
