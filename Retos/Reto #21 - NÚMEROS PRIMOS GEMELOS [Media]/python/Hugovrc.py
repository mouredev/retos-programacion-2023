def es_primo(num: int) -> bool:
    if num <= 1:
        return False
    
    for indice in range(2, num):
        if num % indice == 0:
            return False
    
    return True

def primo_gemelo(num: int):
    gemelos = ""
    for indice in range(2, num):
        if indice + 2 < num and es_primo(indice) and es_primo(indice + 2):
            gemelos += f"({indice}, {indice + 2})"
            
    print(gemelos)

primo_gemelo(25)
primo_gemelo(90)
