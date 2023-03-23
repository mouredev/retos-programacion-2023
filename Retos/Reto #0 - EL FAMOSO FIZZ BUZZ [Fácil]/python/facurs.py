
for i in range(1, 101):  # range recorre lo que haya en el (start, stop)
  if i % 3 == 0 and i % 5 == 0:  # % devuelve el resto, si el resto es 0 significa que es divisible entre 3 y 5
    print("fizzbuzz")
  elif i % 3 == 0:  # Si es múltiplo de 3
    print("fizz")
  elif i % 5 == 0:  # Si es múltiplo de 5
    print("buzz")
  else:  # Si no es múltiplo ni de 3 ni de 5
    print(i)  # Mostramos el número
