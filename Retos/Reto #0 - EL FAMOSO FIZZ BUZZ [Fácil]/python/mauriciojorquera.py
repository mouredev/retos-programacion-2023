
def buzzfizz(num: int) -> str:
    resultado = ''
    if num % 3 == 0:
        resultado += 'fizz'
        
    if num % 5 == 0:
        resultado += 'buzz'
        
    if len(resultado) ==0:
        resultado = str(num)

    return resultado


for i in range(101):
    print(buzzfizz(i))
