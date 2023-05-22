def es_primo(n):
    if n <= 1:
        return False
    for i in range(2, int(n**0.5)+1):
        if n % i == 0:
            return False
    return True

if __name__ == '__main__':
    rango = int(input()) - 2
    solucion = ""    
    for item in range(1, rango):
      if es_primo(item) == True and es_primo(item +2) == True:
          solucion += "(" + str(item) + "," + str(item + 2) + ") "
    print(solucion)
