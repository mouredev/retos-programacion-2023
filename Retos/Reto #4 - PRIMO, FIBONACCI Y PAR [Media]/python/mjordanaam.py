"""
/*
 * Escribe un programa que, dado un número, compruebe y muestre si es primo, fibonacci y par.
 * Ejemplos:
 * - Con el número 2, nos dirá: "2 es primo, fibonacci y es par"
 * - Con el número 7, nos dirá: "7 es primo, no es fibonacci y es impar"
 */
"""


def fibonacci(number: int) -> int:
	if number == 0:
		return 0
	elif number == 1:
		return 1
	else:
		return fibonacci(number-1) + fibonacci(number-2)


def is_fibonacci(number: int) -> bool:
	sequence = [fibonacci(0)]
	counter = 0

	while sequence[counter] < number:
		counter += 1
		sequence.append(fibonacci(counter))

	if sequence[counter] == number:
		return True

	return False


def is_prime(number: int) -> bool:
	if number > 1:
		for i in range(2, number):
			if number % i == 0:
				return False
		return True
	else:
		return False


def is_even(number: int) -> bool:
	if number % 2 == 0:
		return True

	return False


def check_number(number: int) -> str:
	if number > -1:
		text = str(number) + " is "

		if not is_prime(number):
			text += "not "

		text += "prime, "

		if not is_fibonacci(number):
			text += "is not "
		text += "fibonacci and is "

		if is_even(number):
			text += "even"
		else:
			text += "odd"
	else:
		text = "Negative number"

	return text


print(check_number(2))
print(check_number(7))
print(check_number(8))
print(check_number(16))
print(check_number(17))
print(check_number(0))
print(check_number(89))
print(check_number(97))
print(check_number(100))
print(check_number(1))
print(check_number(-1))
