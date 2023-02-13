import string, random, argparse

parser = argparse.ArgumentParser()
parser.add_argument('-l', '--length', type=int, help='password length', required=True)
parser.add_argument('-lc', '--lowercase', type=bool, help='has lowercase', nargs='?', const=True, default=False)
parser.add_argument('-uc', '--uppercase', type=bool, help='has uppercase', nargs='?', const=True, default=False)
parser.add_argument('-n', '--numbers', type=bool, help='has numbers', nargs='?', const=True, default=False)
parser.add_argument('-s', '--symbols', type=bool, help='has symbols', nargs='?', const=True, default=False)

args: argparse = parser.parse_args()

def generator(length: int, has_lowercase:bool, has_uppercase: bool, has_numbers: bool, has_symbols: bool) -> string:
    characters: string = ''

    if has_lowercase: characters += string.ascii_lowercase
    if has_uppercase: characters += string.ascii_uppercase
    if has_numbers: characters += string.digits
    if has_symbols: characters += string.punctuation

    return ''.join(random.choice(characters) for _ in range(length))

def main():
    arguments: tuple[bool] = (args.lowercase, args.uppercase, args.numbers, args.symbols)

    if any(arg == True for arg in arguments):
        password = generator(length=args.length, has_lowercase=args.lowercase, has_uppercase=args.uppercase, has_numbers=args.numbers, has_symbols=args.symbols) if args.length >= 8 and args.length <= 16  else 'La longitud debe ser entre 8 a 16'

        print(password)
    else:
        print('Define lo que debe contener tu contraseña')

if __name__ == '__main__':
    main()

    # Genera una contraseña con minúsculas, mayúsculas, números y símbolos
    # py .\password_generator.py --length 11 --lowercase --uppercase --numbers --symbols

    # Genera una contraseña con minúsculas y números
    # py .\password_generator.py --length 16 --lowercase --numbers