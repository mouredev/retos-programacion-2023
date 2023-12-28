'''
	Reto #4: PRIMO, FIBONACCI Y PAR
/*
 * Escribe un programa que, dado un número, compruebe y muestre si es primo, fibonacci y par.
 * Ejemplos:
 * - Con el número 2, nos dirá: "2 es primo, fibonacci y es par"
 * - Con el número 7, nos dirá: "7 es primo, no es fibonacci y es impar"
 */
 '''

# Funcio que verifica si es primo
def primo(number,div=2):
	if div == number: return 'es primo'
	return 'no es primo' if (number%div == 0) else primo(number,div+1) 

# Verifica si es fibonacci
def fibonacci(number):
	fib_1 = 0
	fib_2 = 1
	while fib_2 != number:
		fib_3 = fib_1 + fib_2 
		if fib_3 > number:
			return 'no es fibonacci'

		fib_1,fib_2 = fib_2,fib_3

	return 'es fibonacci'

# Verifica si es par
def par(number):
	return 'es par' if (number%2 == 0) else 'es impar'

def pri_fib_par(number: int):
	return f'{number} {primo(number)}, {fibonacci(number)} y {par(number)}'

try:
	number = int(input('Introduzca un numero: '))
	print(pri_fib_par(number))

except ValueError as error:
	print(f'\nEl numero no es entero.\nValueError: {error}')