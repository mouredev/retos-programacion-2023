num = int(input("Introduce un número: "))

# Comprobar si es primo
es_primo = True
for i in range(2, num):
    if num % i == 0:
        es_primo = False
        break

# Comprobar si es par
es_par = num % 2 == 0

# Comprobar si es un número de Fibonacci
a, b = 0, 1
while b < num:
    a, b = b, a + b
es_fibonacci = b == num

# Mostrar los resultados
if es_primo:
    print(f"{num} es primo,", end=" ")
else:
    print(f"{num} no es primo,", end=" ")

if es_par:
    print("par,", end=" ")
else:
    print("impar,", end=" ")

if es_fibonacci:
    print("y es un número de Fibonacci.")
else:
    print("y no es un número de Fibonacci.")
