

# Inicializamo el range en uno ya que el 0 no esta incluído
for i in range(1, 101):
    # Para cada i, solo entrará en una de estas condiciones
    if i % 3 == 0 and i % 5 == 0:
        print("fizzbuzz")
    elif i % 5 == 0:
        print("buzz")
    elif i % 3 == 0:
        print("fizz")
    else:
        print(i)