def primo(x):
    cont = 0
    if x<=1:
        return "No es primo, "
    for i in range(2,x):
        if x % i == 0:
            cont+=1
        elif cont>0:
            break
    if cont == 0:
        return str(x) + " Es primo, "
    else:
        return str(x) + " No es primo, "
def fibonacci(x):
    num1 = 0
    num2 = 1
    actual = num2

    while actual < x :
        actual = num1 + num2
        num1 = num2
        num2 = actual

    if actual == x:
        return "es fibonacci, "
    else:
        return "No es fibonacci, "
    
def par(x):
    if x % 2 == 0:
        return "es par"
    else:
        return "es impar"
print(primo(8) + fibonacci(8) + par(8))
print(primo(5) + fibonacci(5) + par(5))