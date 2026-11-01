"""FIZZ BUZZ"""

for i in range(1, 101):
    resultado = ""
    if i % 3 == 0:
        resultado += "fizz"
    if i % 5 == 0:
        resultado += "buzz"
    print(resultado or i)
