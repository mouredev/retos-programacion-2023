numero = 1

while numero <= 100:
    
    if numero% 3 == 0 and numero % 5 == 0:  #Si esto se cumple quiere decir que esto es mltiplo de 3 y de 5
        print("fizzbuzz")
    elif numero % 3 == 0:  #Si esto se cumple quiere decir que esto es mltiplo de 3
        print("fizz") 
    elif numero % 5 == 0: #Si esto se cumple quiere decir que esto es mltiplo de 5
        print("buzz")
    else:
        print(numero)
    numero += 1

print('*' * 30)

print("Resolución con 'for'")

for number in range(1,101):
    if number % 3 == 0 and number % 5 ==0:
        print("fizzbuzz")
    elif number % 3 == 0:
        print("fizz")
    elif number % 5 == 0:
        print("buzz")
    else:
        print(number)
