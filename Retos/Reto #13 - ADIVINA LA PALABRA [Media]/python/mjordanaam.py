"""
/*
 * Crea un pequeño juego que consista en adivinar palabras en un número máximo de intentos:
 * - El juego comienza proponiendo una palabra aleatoria incompleta
 *   - Por ejemplo "m_ur_d_v", y el número de intentos que le quedan
 * - El usuario puede introducir únicamente una letra o una palabra (de la misma longitud que
 *   la palabra a adivinar)
 *   - Si escribe una letra y acierta, se muestra esa letra en la palabra. Si falla, se resta
 *     uno al número de intentos
 *   - Si escribe una resolución y acierta, finaliza el juego, en caso contrario, se resta uno
 *     al número de intentos
 *   - Si el contador de intentos llega a 0, el jugador pierde
 * - La palabra debe ocultar de forma aleatoria letras, y nunca puede comenzar ocultando más del 60%
 * - Puedes utilizar las palabras que quieras y el número de intentos que consideres
 */
"""
import random
import re

WORDS = ['mouredev', 'python', 'hello', 'javascript', 'engineering', 'visualbasic', 'docker']


def join_list(characters: list) -> None:
	word = ""

	for c in characters:
		word += c

	print(word)


def letter_recursive(word: str, deleted: list, master: list, hidden: str, hidden_list: list):
	letter: str = input("Enter letter \n")

	while not re.search("[a-zA-Z]", letter) or len(list(letter)) > 1:
		letter: str = input("Enter letter \n")

	if letter in deleted:

		counter = 0

		while letter != master[hidden_list.index('_')] and counter < hidden_list.count('_'):
			counter += 1

		hidden_list[master.index(letter)] = letter
		join_list(hidden_list)

	return hidden_list, hidden, word


def game(attempts: int, word: str, deleted: list, master: list, hidden: str, hidden_list: list) -> None:
	while hidden_list.count('_') > 0 and attempts > 0:
		option = ask_option()

		if option:
			hidden_list = ask_word(master, hidden_list, word)
		else:
			hidden_list, hidden, word = letter_recursive(word, deleted, master, hidden, hidden_list)

		attempts -= 1
		print("Attempts: ", attempts)

	if hidden_list.count('_') == 0:
		print(word)
		print("Congratulations!!")
	else:
		print(word)
		print(":-( GAME OVER")


def ask_word(master:list, hidden_list: list, word: str) -> list:
	entered_word: str = input("Enter word \n")

	while not re.search("[a-zA-Z]", entered_word):
		entered_word: str = input("Enter letter \n")

	if entered_word == word:
		return master

	return hidden_list


def ask_option() -> bool:
	option: str = input("Enter letter or word (l/w)\n")

	if option == 'w':
		return True
	else:
		return False


def get_word():
	attempts = 3
	deleted = []
	word = random.choice(WORDS)
	aux: list = list(word)
	length = round((32*len(aux))/64)

	for i in range(0, length):
		character = random.choice(aux)
		pos = aux.index(character)
		aux[pos] = '_'

		if character == '_':
			character = random.choice(aux)
			while character == '_':
				character = random.choice(aux)
				pos = aux.index(character)
			aux[pos] = '_'

		deleted.append(character)

	hidden_word = ""

	for w in aux:
		hidden_word += w

	if length - 1 >= 3:
		attempts = length - 1

	return word, hidden_word, attempts, deleted


def main():
	word, hidden_word, attempts, deleted = get_word()

	print(hidden_word)
	print("Attempts: ", attempts)
	aux: list = list(hidden_word)
	master: list = list(word)

	game(attempts, word, deleted, master, hidden_word, aux)


if __name__ == "__main__":
	main()
