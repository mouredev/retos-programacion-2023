# Escribe un programa que muestre por consola (con un print) los 
# números de 1 a 100 (ambos incluidos y con un salto de línea entre 
# cada impresión), sustituyendo los siguientes: 
#     - Múltiplos de 3 por la palabra "fizz". 
#     - Múltiplos de 5 por la palabra "buzz". 
#     - Múltiplos de 3 y de 5 a la vez por la palabra "fizzbuzz". 


def fizzBuzz ():
    i = 0
    while i < 100:
        output = ''
        if i % 3 == 0:
            output += 'Fizz'
        if i % 5 == 0:
            output += 'Buzz'
        if i % 3 != 0 and i % 5 != 0:
            output = i

        i += 1
        
        print(output)

fizzBuzz()

# OpenAI
# 
# def fizzBuzz():
#     for i in range(1, 101):
#         output = ''
#         if i % 3 == 0:
#             output += 'Fizz'
#         if i % 5 == 0:
#             output += 'Buzz'
#         if not output:
#             output = str(i)
#         print(output)
# 
# fizzBuzz()
# 
# Otra forma:
# 
# for i in range(1, 101):
#     if i % 3 == 0 and i % 5 == 0:
#         print("fizzbuzz")
#     elif i % 3 == 0:
#         print("fizz")
#     elif i % 5 == 0:
#         print("buzz")
#     else:
#         print(i)

