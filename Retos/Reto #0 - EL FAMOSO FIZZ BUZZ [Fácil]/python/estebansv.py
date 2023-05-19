
#fizzBuzz my @I.esteban
for x in range(1,101):
    if x%3==0 and x%5==0:
        print("FizzBuzz")
    elif x%3==0:
            print("Fizz")
    elif x%5==0:
                print("Buzz")
    else:
                    print(x)
#fizzBuzz AI
resultado = []
for i in range(1, 101):
    resultado.append("fizz"*(i%3==0) + "buzz"*(i%5==0) or str(i))
print("\n".join(resultado))