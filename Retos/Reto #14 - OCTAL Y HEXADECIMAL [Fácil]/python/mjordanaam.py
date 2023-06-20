"""
/*
 * Crea una función que reciba un número decimal y lo trasforme a Octal
 * y Hexadecimal.
 * - No está permitido usar funciones propias del lenguaje de programación que
 * realicen esas operaciones directamente.
 */
"""
hexadecimal = {
	"0": "0",
	"1": "1",
	"2": "2",
	"3": "3",
	"4": "4",
	"5": "5",
	"6": "6",
	"7": "7",
	"8": "8",
	"9": "9",
	"10": "A",
	"11": "B",
	"12": "C",
	"13": "D",
	"14": "E",
	"15": "F"
}


def from_decimal_to(number: int, base: int) -> str:
	converted = ""
	converted_aux = []

	while number >= base:
		module = int(number % base)
		number = int(number / base)
		if base == 16:
			converted_aux.append(hexadecimal[str(module)])
		else:
			converted_aux.append(module)

	if base == 16:
		converted_aux.append(hexadecimal[str(number)])
	else:
		converted_aux.append(int(number))

	converted_aux.reverse()

	for n in converted_aux:
		converted += str(n)

	if converted[0] == '0':
		converted = converted[1:]

	return converted


def convert(number: int):
	octal = from_decimal_to(number, 8)
	hexa = from_decimal_to(number, 16)
	# binary = from_decimal_to(number, 2)
	# value = from_decimal_to(number, 3)

	return octal, hexa


print(convert(1))  # 1, 1
print(convert(2))  # 2, 2
print(convert(7))  # 7, 7
print(convert(8))  # 10, 8
print(convert(10))  # 12, A
print(convert(16))  # 20, 10
print(convert(32))  # 40, 20
print(convert(64))  # 100, 40
print(convert(63))  # 77, 3F
print(convert(255))  # 377, FF
print(convert(1000))  # 1750, 3E8
print(convert(4248))  # 10230, 1098
print(convert(5137))  # 12021, 1411