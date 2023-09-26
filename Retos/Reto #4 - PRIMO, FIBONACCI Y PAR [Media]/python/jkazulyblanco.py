# titulo
print('*'.center(70,'*'))
print('PRIMO, FIBONACCI Y PAR'.center(70,'-'))
print('*'.center(70,'*'))

# numero = 200000089 LIMITE PYTHON CICLO PRIMOS - SE DEMORA VARIOS SEGUNDOS
numero = int(input('\nBienvenido\nDigita un numero para saber si es primo, fibonacci o par:    '))

# crear lista con numeros fibonacci
num1, num2 = 0, 1
fibonacci = []
while num2 <= 300000000:
	fibonacci.append(num1)
	fibonacci.append(num2)
	num1 = num1 + num2
	num2 = num1 + num2


def primo(num): # esta funcion devuelve si un numero es primo o no
    if num < 2: False # si el numero es menor a 2
    else:
        for divisor in range(2, num): # el rango es el mismo numero --> por rendimiento       
            if num % divisor == 0:
                return False
        return True

text = list('primo,fibonacci,par'.split(',')) # lista con texto para mostrar

# da los resultados, si las condiciones son verdaderas o falsas
a = f'\n{numero} es {text[0]},' if primo(numero) else f'\n{numero} no es {text[0]},' # primo
                                       
b = f'es {text[1]}' if numero in fibonacci else f'no es {text[1]}' # fibonacci

c = f'y es {text[2]}.\n' if numero % 2 == 0 else f'y no es {text[2]}.\n' # par

print(a, b, c) # muestra en pantalla los resultados



