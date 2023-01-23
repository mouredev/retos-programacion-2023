"""
/*
 * Escribe un programa que sea capaz de generar contraseñas de forma aleatoria.
 * Podrás configurar generar contraseñas con los siguientes parámetros:
 * - Longitud: Entre 8 y 16.
 * - Con o sin letras mayúsculas.
 * - Con o sin números.
 * - Con o sin símbolos.
 * (Pudiendo combinar todos estos parámetros entre ellos)
 */
"""
import random
import string

UPPERCASE = string.ascii_uppercase
LOWERCASE = string.ascii_lowercase
NUMBERS = "0123456789"
SPECIAL = "*@$%_:./^~>#()<"


def generate_password(length: int, uppercase: bool, lowercase: bool, numbers: bool, special: bool) -> str:
	password = ""
	characters = ""
	counter = 0
	compulsory = []

	if uppercase:
		characters += UPPERCASE
		counter += 1
		compulsory.append(random.choice(UPPERCASE))

	if lowercase:
		characters += LOWERCASE
		counter += 1
		compulsory.append(random.choice(LOWERCASE))

	if numbers:
		characters += NUMBERS
		counter += 1
		compulsory.append(random.choice(NUMBERS))

	if special:
		characters += SPECIAL
		counter += 1
		compulsory.append(random.choice(SPECIAL))

	if characters != "":
		random.shuffle(compulsory)

		for character in compulsory:
			password += character

		for i in range(0, length - counter):
			password += random.choice(characters)

		final = list(password)
		random.shuffle(final)

		password = ""

		for e in final:
			password += e

	return password


def main():
	length = "d"
	uppercase = "d"
	lowercase = "d"
	numbers = "d"
	special = "d"

	while not length.isnumeric() or int(length) < 8 or int(length) > 16:
		length = input("Please enter length between 8 and 16\n")

	while uppercase != "y" and uppercase != "n":
		uppercase = input("UPPERCASE letters ? (y/n)\n")

	while lowercase != "y" and lowercase != "n":
		lowercase = input("lowercase letters ? (y/n)\n")

	while numbers != "y" and numbers != "n":
		numbers = input("Numbers ? (y/n)\n")

	while special != "y" and special != "n":
		special = input("Special characters ? (y/n)\n")

	if uppercase == 'y':
		uppercase = True
	else:
		uppercase = False

	if lowercase == 'y':
		lowercase = True
	else:
		lowercase = False

	if numbers == 'y':
		numbers = True
	else:
		numbers = False

	if special == 'y':
		special = True
	else:
		special = False

	password = generate_password(int(length), uppercase, lowercase, numbers, special)

	if password != "":
		print("Your password is: ", password)
	else:
		print("Please choose any option")


if __name__ == '__main__':
	main()
