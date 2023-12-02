""" Reto 0 Realizado por Emiro Atencio 
    Saludos desde Venezuela"""



def FizzBuzz ():
    i = 1
    for i in range(100):
        aux = i + 1
        if aux % 3 == 0 and aux % 5 == 0:
            print('FizzBuzz')
        elif aux % 3 == 0:
            print('Fizz')
        elif aux % 5 == 0:
            print("Buzz")
        else:
            print(aux)


FizzBuzz();