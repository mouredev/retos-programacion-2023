#fizzBuzz my @I.esteban
for este in range(1,101):
    if este%3==0 and i%5==0:
        print("FizzBuzz")
    elif este%3==0:
        print("Fizz")
    elif este%5==0:
        print("Buzz")
    else:
       print(este)
        
#fizzBuzz AI
resultado = []
for i in range(1, 101):
    resultado.append("fizz"*(i%3==0) + "buzz"*(i%5==0) or str(i))
print("\n".join(resultado))
